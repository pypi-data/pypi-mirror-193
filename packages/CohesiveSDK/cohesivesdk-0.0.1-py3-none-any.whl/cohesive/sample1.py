'''
import lodash from 'lodash';
import { SalesforceClient } from '../src';

const ACCESS_TOKEN = '00DDn00000BzCTS!AQQAQP6DOpwuj04yOlHOoVrpM6XFtCTuKKp2GK1SSTYbe.uFkB2ZC36kKu2k6OT3U.Mx9Wrk_H6PIc3ref_ynGTs1NCxF.zd';

const MOCKED_DATA = {
  "Owner Id": '005Dn000004oWGNIA2',
  "Meeting Name": 'Test Meeting 2',
  "Meeting Url": 'test.xyz',
  "Meeting Date": new Date().toISOString(),
  "Meeting Summary": 'Test Summary',
  "Sentiment": 'Very Positive',
  "DurationInMinutes": 30,
  "Attendee": null,
  "Account": null
};

const MOCKED_MAPPING = {
  "Owner Id": 'OwnerId',
  "Meeting Name": 'Subject',
  "Meeting Url": 'Description',
  "Meeting Date": 'ActivityDateTime',
  "Meeting Summary": 'Description',
  "Sentiment": 'Description',
  "Attendee": 'WhoId',
  "Account": 'WhatId'
};

const testUpsertEventsForEmails1 = async (params: {
  accessToken: string,
  ownerEmail: string,
  attendeeEmails: string[],
  data: any,
  mapping: Record<string, any>
}) => {
  const { accessToken, ownerEmail, attendeeEmails, data, mapping } = params;
  const salesforceClient = await SalesforceClient.initialize({
    salesforceDomain: 'https://cohesive2-dev-ed.develop.my.salesforce.com'
  });
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
  const attendeeContacts = contacts? contacts.filter(contact => contact.Email && attendeeEmails.includes(contact.Email)) : [];
  
  // Upsert the event for every account ID
  const eventIds = lodash.compact(
    await Promise.all(
      attendeeContacts.map(async (contact) => {
        if (contact.AccountId) {
          return salesforceClient.upsertSalesforceEvent({
            accessToken,
            data: {
              ...data,
              WhoId: contact.Id,
              WhatId: contact.AccountId,
            },
            mapping
          });
        } else {
          return null;
        }
      })
    )
  );
  console.log("TEST 1: ", eventIds);
}

const testUpsertEventsForEmails2 = async (params: {
  accessToken: string,
  accountId: string,
  attendeeEmails: string[],
  data: any,
  mapping: Record<string, any>
}) => {
  const { accessToken, accountId, attendeeEmails, data, mapping } = params;
  const salesforceClient = await SalesforceClient.initialize({
    salesforceDomain: 'https://cohesive2-dev-ed.develop.my.salesforce.com'
  });
  const eventIds = await salesforceClient.upsertSalesforceEventForEmails({
    accessToken,
    ownerEmail: accountId,
    attendeeEmails,
    data,
    mapping
  });
  console.log("TEST 2: ", eventIds);
}

testUpsertEventsForEmails1({
  ownerEmail: '24ntn96@gmail.com',
  attendeeEmails: ['bond_john@grandhotels.com', 'spavlova@uog.com'],
  accessToken: ACCESS_TOKEN,
  data: MOCKED_DATA,
  mapping: MOCKED_MAPPING
});

testUpsertEventsForEmails2({
  accountId: '24ntn96@gmail.com',
  attendeeEmails: ['bond_john@grandhotels.com', 'j.davis@expressl&t.net'],
  accessToken: ACCESS_TOKEN,
  data: MOCKED_DATA,
  mapping: MOCKED_MAPPING
});
'''