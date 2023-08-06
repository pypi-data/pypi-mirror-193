'''
import { HttpMethods, applyQueryParams, parseSchema } from '../utils';
import fetch from 'isomorphic-unfetch';
import {
    salesforceCreateEventResponseSchema,
    salesforceGetContactResponseSchema,
    salesforceGetEventResponseSchema,
    salesforceGetUserResponseSchema,
    salesforceVersionsSchema,
} from './schemas';
import lodash from 'lodash';
import { buildSalesforceQuery, handleSalesforceApiError } from './utils';

class SalesforceClient {
    private hostUrl: string;

    private constructor(hostUrl: string) {
        this.hostUrl = hostUrl;
    }

    public static async initialize(params: { salesforceDomain: string; apiVersion?: string }) {
        const { salesforceDomain, apiVersion } = params;
        const res = await fetch(`${salesforceDomain}/services/data`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        if (res.ok) {
            const rawData = await res.json();
            const versions = parseSchema(salesforceVersionsSchema, rawData);
            const latestVersion = lodash.last(versions);
            if (!latestVersion) {
                throw new Error(
                    `Could not find any version of Salesforce API - make sure the Salesforce domain ${salesforceDomain} has API access.`
                );
            }
            return new SalesforceClient(
                `${salesforceDomain}/${apiVersion ? `/services/data/v${apiVersion}` : latestVersion.url}`
            );
        } else {
            throw new Error(`Could not initialize Salesforce client - ${res.statusText}`);
        }
    }

    private async querySalesforce(params: {
        endpoint: string;
        method: HttpMethods;
        headers?: any;
        queryParams?: Record<string, any>;
        body?: any;
    }): Promise<Response> {
        const { endpoint, queryParams, headers, body, method } = params;
        const endpointWithQueryParams = applyQueryParams({ endpoint, queryParams });
        const url = `${this.hostUrl}${endpointWithQueryParams}`;
        return fetch(url, {
            method,
            headers,
            body: JSON.stringify(body),
        });
    }

    public async getSalesforceUserFromEmail(params: { accessToken: string; email?: string }) {
      const { accessToken, email } = params;
      let query = "";
      query = buildSalesforceQuery({ query, isDateTimeType: false, parameter: 'Email', argument: email });
      const queryParams = `SELECT FIELDS(ALL) FROM User${query !== ""? query : ""} LIMIT 200`;
      const res = await this.querySalesforce({
        endpoint: '/query',
        method: 'GET',
        headers: {
          Authorization: `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
        queryParams: {
          q: queryParams,
        },
      });
      if (res.ok) {
        const rawData = await res.json();
        const { records } = parseSchema(salesforceGetUserResponseSchema, rawData);
        return records;
      } else {
        await handleSalesforceApiError(res);
      }
    }

    public async getSalesforceContactFromEmail(params: { accessToken: string; email?: string }) {
      const { accessToken, email } = params;
      let query = "";
      query = buildSalesforceQuery({ query, isDateTimeType: false, parameter: 'Email', argument: email });
      const queryParams = `SELECT FIELDS(ALL) FROM Contact${query !== ""? query : ""} LIMIT 200`;
      const res = await this.querySalesforce({
        endpoint: '/query',
        method: 'GET',
        headers: {
          Authorization: `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
        queryParams: {
          q: queryParams,
        },
      });
      if (res.ok) {
        const rawData = await res.json();
        const { records } = parseSchema(salesforceGetContactResponseSchema, rawData);
        return records;
      } else {
        await handleSalesforceApiError(res);
      }
    }

    public async getSalesforceEvent(params: {
        accessToken: string;
        owner?: string;
        attendee?: string;
        subject?: string;
        date?: string;
    }) {
        const { accessToken, owner, attendee, subject, date } = params;
        let query = "";
        query = buildSalesforceQuery({ query, isDateTimeType: false, parameter: 'OwnerId', argument: owner });
        query = buildSalesforceQuery({ query, isDateTimeType: false, parameter: 'WhoId', argument: attendee });
        query = buildSalesforceQuery({ query, isDateTimeType: false, parameter: 'Subject', argument: subject });
        query = buildSalesforceQuery({ query, isDateTimeType: true, parameter: 'ActivityDateTime', argument: date });
        const queryParam = `SELECT FIELDS(ALL) FROM Event${query !== ""? query : ""} LIMIT 200`;

        const res = await this.querySalesforce({
            endpoint: '/query',
            method: 'GET',
            headers: {
                Authorization: `Bearer ${accessToken}`,
                'Content-Type': 'application/json',
            },
            queryParams: {
                q: queryParam,
            },
        });
        if (res.ok) {
            const rawData = await res.json();
            const { records } = parseSchema(salesforceGetEventResponseSchema, rawData);
            if (records.length > 0) {
                const eventsByTimestamp = lodash.orderBy(
                    records,
                    (record) => {
                        const timeStr = record.EndDateTime ?? record.StartDateTime ?? Date.now().toString();
                        return new Date(timeStr).valueOf();
                    },
                    'desc'
                );
                return eventsByTimestamp[0];
            }
        } else {
            await handleSalesforceApiError(res);
        }
    }

    public async createSalesforceEvent(params: { accessToken: string; data: any; mapping?: Record<string, string> }) {
        const { accessToken, data, mapping } = params;
        let body: Record<string, any> = {};
        if (mapping) {
            for (const key of Object.keys(data)) {
                if (mapping[key]) {
                  body[mapping[key]] = body[mapping[key]]? `${body[mapping[key]]}\n\n${data[key]}` : data[key];
                } else {
                  body[key] = data[key];
                }
            }
        }
        const res = await this.querySalesforce({
            endpoint: '/sobjects/Event',
            method: 'POST',
            headers: {
                Authorization: `Bearer ${accessToken}`,
                'Content-Type': 'application/json',
            },
            body,
        });
        if (res.ok) {
            const rawData = await res.json();
            const { id } = parseSchema(salesforceCreateEventResponseSchema, rawData);
            return id;
        } else {
            await handleSalesforceApiError(res);
        }
    }

    public async updateSalesforceEvent(params: {
        accessToken: string;
        eventId: string;
        data: any;
        mapping?: Record<string, string>;
    }) {
        const { accessToken, eventId, data, mapping } = params;
        let body: Record<string, any> = {};
        if (mapping) {
            for (const key of Object.keys(data)) {
                if (mapping[key]) {
                  body[mapping[key]] = body[mapping[key]]? `${body[mapping[key]]}\n\n${data[key]}` : data[key];
                } else {
                  body[key] = data[key];
                }
            }
        }
        const res = await this.querySalesforce({
            endpoint: `/sobjects/Event/${eventId}`,
            method: 'PATCH',
            headers: {
              Authorization: `Bearer ${accessToken}`,
              'Content-Type': 'application/json',
            },
            body
        });
        if (res.ok) {
            return eventId;
        } else {
            await handleSalesforceApiError(res);
        }
    }

    public async upsertSalesforceEvent(params: {
        accessToken: string;
        data: any;
        mapping?: Record<string, string>;
    }) {
        const { accessToken, data, mapping } = params;
        let body: Record<string, any> = {};
        if (mapping) {
            for (const key of Object.keys(data)) {
                if (mapping[key]) {
                  body[mapping[key]] = body[mapping[key]]? `${body[mapping[key]]}\n\n${data[key]}` : data[key];
                } else {
                  body[key] = data[key];
                }
            }
        }
        const salesforceEvent = await this.getSalesforceEvent({
            accessToken,
            owner: body['OwnerId'],
            attendee: body['WhoId'],
            subject: body['Subject'],
            date: body['ActivityDateTime'],
        });
        if (salesforceEvent) {
          return await this.updateSalesforceEvent({
            accessToken,
            eventId: salesforceEvent.Id,
            data,
            mapping: params.mapping,
          });
        } else {
          return await this.createSalesforceEvent(params);
        }
    };

    public async upsertSalesforceEventForEmails(params: {
      ownerEmail: string;
      attendeeEmails: string[];
      accessToken: string;
      data: any;
      mapping?: Record<string, string>;
    }) {
      const { accessToken, ownerEmail, attendeeEmails, data, mapping } = params;
      const salesforceClient = await SalesforceClient.initialize({
        salesforceDomain: 'https://cohesive2-dev-ed.develop.my.salesforce.com'
      });

      // Determine what the keys for accountId and contactId in our original data.
      const accountIdKey = mapping? Object.keys(data).find(key => mapping[key] === "WhatId") ?? "WhatId" : "WhatId";
      const contactIdKey = mapping? Object.keys(data).find(key => mapping[key] === "WhoId") ?? "WhoId" : "WhoId";

      // Get the event owner
      const owners = await salesforceClient.getSalesforceUserFromEmail({
        accessToken,
        email: ownerEmail
      });
      const owner = owners? lodash.head(owners) : null;
      if (!owner) {
        throw new Error('Could not find Salesforce user with email ${email}');
      }
      // Get the event attendees' contacts
      const contacts = await salesforceClient.getSalesforceContactFromEmail({
        accessToken,
      });
      const attendeeContacts = contacts
      ? lodash.uniqBy(
        contacts.filter(contact => contact.Email && attendeeEmails.includes(contact.Email)),
        contact => contact.AccountId
      )
      : [];
      const eventIds = lodash.compact(
        await Promise.all(
          attendeeContacts.map(async (contact) => {
            if (contact.AccountId) {
              return salesforceClient.upsertSalesforceEvent({
                accessToken,
                data: {
                  ...data,
                  [accountIdKey]: contact.AccountId,
                  [contactIdKey]: contact.Id
                },
                mapping
              });
            } else {
              return null;
            }
          })
        )
      );
      return eventIds;
    }
}

export default SalesforceClient;
'''
