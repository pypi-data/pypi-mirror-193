import json

def handleSalesforceApiError(res):
  errors = json.loads(res.text)
  error = errors[0]
  if (error is None):
    return
  else:
    if (error['errorCode'] == 'INVALID_SESSION_ID'):
      raise Exception('Invalid Salesforce session ID - ensure that your access token is valid and active.')
    elif (error['errorCode'] == 'NOT_FOUND'):
      raise Exception('Could not find the Salesforce resource - ensure that the resource exists and that you have access to it.')
    else:
      raise Exception(f'Salesforce API error: {error["errorCode"]}: {error["message"]}')

def buildSalesforceQuery(query, isDateTimeType, parameter, argument=None):
  if (argument is None):
    return query
  if (query == ""):
    return f"{query} WHERE {parameter} = '{argument}'" if not isDateTimeType else f"{query} WHERE {parameter} = {argument}"
  else:
    return f"{query} AND {parameter} = '{argument}'" if not isDateTimeType else f"{query} AND {parameter} = {argument}"