#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------

from __future__ import annotations
from requests.models import PreparedRequest
import requests
import json
import time

from cohesive.util import buildSalesforceQuery, handleSalesforceApiError

class SalesforceClient:
  hostUrl = None

  def __init__(self, hostUrl):
    self.hostUrl = hostUrl

  @staticmethod
  def initialize(salesforceDomain, apiVersion=None):
    res = requests.get(
      url=f"{salesforceDomain}/services/data",
      headers={
        "Content-Type": "application/json"
      }
    )
    if (res.ok):
      versions = json.loads(res.text)
      latestVersion = versions[-1]
      if (latestVersion is None):
        raise Exception(f"Could not find any version of Salesforce API - make sure the Salesforce domain {salesforceDomain} has API access.")
      return SalesforceClient(f"{salesforceDomain}/{apiVersion if apiVersion else latestVersion['url']}")
    else:
      raise Exception(f"Could not initialize Salesforce client - {res.text}")

  def querySalesforce(self, endpoint, method, headers=None, queryParams={}, body=None):
    req = PreparedRequest()
    req.prepare_url(self.hostUrl + endpoint, queryParams)
    return requests.request(
      url=req.url,
      method=method,
      headers=headers,
      data=json.dumps(body)
    )

  def getSalesforceUserFromEmail(self, accessToken, email=None):
    query = ""
    query = buildSalesforceQuery(query, False, "Email", email)
    queryParams = "SELECT FIELDS(ALL) FROM User" + query + " LIMIT 200";
    res = self.querySalesforce(
      endpoint='/query',
      method="GET",
      headers={
        "Authorization": "Bearer " + accessToken,
        "Content-Type": "application/json"
      },
      queryParams={
        "q": queryParams
      }
    )
    if (res.ok):
      rawResponse = json.loads(res.text)
      return rawResponse['records']
    else:
      handleSalesforceApiError(res)

  def getSalesforceContactFromEmail(self, accessToken, email=None):
    query = ""
    query = buildSalesforceQuery(query, False, "Email", email)
    queryParams = "SELECT FIELDS(ALL) FROM Contact" + query + " LIMIT 200";
    res = self.querySalesforce(
      endpoint='/query',
      method="GET",
      headers={
        "Authorization": "Bearer " + accessToken,
        "Content-Type": "application/json"
      },
      queryParams={
        "q": queryParams
      }
    )
    if (res.ok):
      rawResponse = json.loads(res.text)
      return rawResponse['records']
    else:
      handleSalesforceApiError(res)

  def getSalesforceEvent(self, accessToken, owner=None, attendee=None, subject=None, date=None):
    query = ""
    query = buildSalesforceQuery(query, False, "OwnerId", owner)
    query = buildSalesforceQuery(query, False, "WhoId", attendee)
    query = buildSalesforceQuery(query, False, "Subject", subject)
    query = buildSalesforceQuery(query, True, "ActivityDateTime", date)
    queryParams = "SELECT FIELDS(ALL) FROM Event" + query + " LIMIT 200";
    res = self.querySalesforce(
      endpoint='/query',
      method="GET",
      headers={
        "Authorization": "Bearer " + accessToken,
        "Content-Type": "application/json"
      },
      queryParams={
        "q": queryParams
      }
    )
    if (res.ok):
      rawResponse = json.loads(res.text)
      return rawResponse['records']
    else:
      handleSalesforceApiError(res)

  def createSalesforceEvent(self, accessToken, data, mapping=None):
    body = {}
    if (mapping):
      for key in data:
        if key in mapping:
          body[mapping[key]] = body[mapping[key]] + "\n\n" + data[key] if body.get(mapping[key]) else data[key]
        else:
          body[key] = data[key]

    res = self.querySalesforce(
      endpoint="/sobjects/Event",
      method="POST",
      headers={
        "Authorization": "Bearer " + accessToken,
        "Content-Type": "application/json"
      },
      queryParams={},
      body=body
    )

    if (res.ok):
      rawResponse = json.loads(res.text)
      return rawResponse['id']
    else:
      handleSalesforceApiError(res)

  def updateSalesforceEvent(self, accessToken, eventId, data, mapping=None):
    body = {}
    if (mapping):
      for key in data:
        if key in mapping:
          body[mapping[key]] = body[mapping[key]] + "\n\n" + data[key] if body.get(mapping[key]) else data[key]
        else:
          body[key] = data[key]

    res = self.querySalesforce(
      endpoint=f"/sobjects/Event/{eventId}",
      method="PATCH",
      headers={
        "Authorization": "Bearer " + accessToken,
        "Content-Type": "application/json"
      },
      queryParams={},
      body=body
    )

    if (res.ok):
      return eventId
    else:
      handleSalesforceApiError(res)

  def upsertSalesforceEvent(self, accessToken, data, mapping=None):
    body = {}
    if (mapping):
      for key in data:
        if key in mapping:
          body[mapping[key]] = body[mapping[key]] + "\n\n" + data[key] if body.get(mapping[key]) else data[key]
        else:
          body[key] = data[key]
    
    salesforceEvent = self.getSalesforceEvent(
      accessToken=accessToken,
      owner=body.get("OwnerId"),
      attendee=body.get("WhoId"),
      subject=body.get("Subject"),
      date=body.get("ActivityDateTime")
    );

    if (salesforceEvent):
      return self.updateSalesforceEvent(
        accessToken=accessToken,
        eventId=salesforceEvent.id,
        data=data,
        mapping=mapping
      )
    else:
      return self.createSalesforceEvent(
        accessToken=accessToken,
        data=data,
        mapping=mapping
      )

  def upsertSalesforceEventForEmails(self, ownerEmail, attendeeEmails, accessToken, data, mapping=None):
    owners = self.getSalesforceUserFromEmail(accessToken=accessToken, email=ownerEmail)
    owner = owners[0] if owners and len(owners) > 0 else None
    if not owner:
      raise Exception(f"Could not find Salesforce user with email {ownerEmail}")
    contacts = self.getSalesforceContactFromEmail(accessToken=accessToken)
    attendeeContacts = [x for x in contacts if 'Email' in x and x['Email'] in attendeeEmails] if contacts else []
    accountIdKeys = [x for x in data.keys() if mapping.get(x) == "WhatId"]
    accountIdKey = accountIdKeys[0] if accountIdKeys and len(accountIdKeys) > 0 else "WhatId"
    contactIdKeys = [x for x in data.keys() if mapping.get(x) == "WhoId"]
    contactIdKey = contactIdKeys[0] if contactIdKeys and len(contactIdKeys) > 0 else "WhoId"
    eventIds = []
    for contact in attendeeContacts:
      if 'AccountId' in contact:
        eventPayload = data
        eventPayload[accountIdKey] = contact.get('AccountId')
        eventPayload[contactIdKey] = contact.get('Id')
        eventIds.append(
          self.upsertSalesforceEvent(
            accessToken=accessToken,
            data=eventPayload,
            mapping=mapping
          )
        )
    return eventIds


  