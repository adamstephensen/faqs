# Import and publish your first API

note: this is a brief summary of [The official import and publish API tutorial](https://docs.microsoft.com/en-us/azure/api-management/import-and-publish).

## Before the demo
1. create the APIM service - it can take 20 mins to spin up

## Demo steps

### Import and publish a backend API

1. Select **APIs** | **OpenAPI Specification** 
2. Use the following settings
- OpenAPI specification: **http://conferenceapi.azurewebsites.net?format=json**
- Display name: Demo Conference API (shown in the developer portal)
- Name: demo-conference-api 
- URL scheme: https
- API URL suffix: conference (appended to base Url to distinguish APIs)
- Products: Unlimited (To get access to the API, developers must first subscribe to a product. When they subscribe, they get a subscription key that is good for any API in that product. )
3. Click **Create**

## Test the new APIM API in the Azure portal

1. Under **All APIs** choose **Demo Conference API | Test | GetSpeakers** (note that subscription key is filled in) | **Send**
2. Click **Send**
Note that **200 ok** is returned along with Data

## Call an operation from the developer portal

1. Under **Developer Portal** choose **Demo Conference API** then **GetSpeakers**
2. Try it: Click **Try It** and then **Send**
3. Get the code to implement it & execute the CURL @ command prompt (get subscription key first)
