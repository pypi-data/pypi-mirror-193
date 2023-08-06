## Description
This package contains a custom client for Salesforce API. This client allows developers
to publish custom events to any SFDC instance.

## Usage
- First, initialize the SalesforceClient by calling `SalesforceClient.initialize`.
- `createSalesforceEvent` will generate a new event.
- `updateSalesforceEvent` will update an existing event or throw an error if the event does not exist.
- `upsertSalesforceEvent` will update an event with the same subject, meeting date, owner, and attendee. If there are multiple events
matching these criteria, override the event that is closest to the request time. If there is no event matching these criteria, create
a new event.
```
    salesforceClient = SalesforceClient.intialize(
        salesforceDomain: 'https://cohesive2-dev-ed.develop.my.salesforce.com',
    );
    eventId = await salesforceClient.createSalesforceEvent(
        accessToken='YOUR_ACCESS_TOKEN',
        data={
            AccountId: 'YOUR_ACCOUNT_ID',
            MeetingName: 'Test Meeting',
            MeetingUrl: 'test.xyz',
            MeetingDate: new Date().toISOString(),
            MeetingSummary: 'Test Summary',
            MeetingAttendee: null,
            Sentiment: 'Positive',
            DurationInMinutes: 30,
        },
        mapping={
            AccountId: 'OwnerId',
            MeetingName: 'Subject',
            MeetingUrl: 'Description',
            MeetingDate: 'ActivityDateTime',
            MeetingSummary: 'Description',
            MeetingAttendee: 'WhoId',
            Sentiment: 'Description',
        },
    );
```