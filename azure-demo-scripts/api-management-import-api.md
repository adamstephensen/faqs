# Import and publish your first API

note: this is a brief summary of the following docs
- [The official import and publish API tutorial](https://docs.microsoft.com/en-us/azure/api-management/import-and-publish)
- [Create and publish a product](https://docs.microsoft.com/en-us/azure/api-management/api-management-howto-add-products)
- [Transform and protect your API](https://docs.microsoft.com/en-us/azure/api-management/transform-api)

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

## Create and publish a product

1. Under **Products** choose **Add**
2. Use the following settings
- Display name: Contoso product *(Used for developer portal)*
- Id: contoso-product
- Description: test product
- State: published *(unpublished by default - only visible to administrators)*
- Requires subscription: if a user requires a subscription key to access method
- Requires approval: false *(if you want an admin to review and accept/reject subscription attempts. false=auto approval)*
- APIs: the apis in the product
3. Click Create
4. Continue configuring in the **Settings** tab
5. View / Add subscribers in the **Subscriptions** tab
6. Set visibility of a product for developers or guest from the **Access control** tab

## Transform an API to strip response headers

We are going to remove the 'X-Powered-By' and 'X-AspNet-Version' Http headers from the Http Response

### Test the original reponose
1. Under **APIs** choose **Demo Conference API | Test | GetSpeakers | Send**
2. Note that the message includes the 'X-Powered-By' and 'X-AspNet-Version' Http headers

### Set the transformation policy
1. Select **Demo Conference API | Design | All Operations | Outbound Processing 'Policies' editor**
2. Position the cursor inside the **outbound** element (before **base**)
3. In the right window, under Transformation policies, click + Set HTTP header twice (to insert two policy snippets).
4. Modify the code to look like this: 

```
 <set-header name="X-Powered-By" exists-action="delete" />
 <set-header name="X-AspNet-Version" exists-action="delete" />  
```
5. Click **Save** and test the result
6. Bonus: Add a find and replace policy

```
  <find-and-replace from="://conferenceapi.azurewebsites.net" to="://apiphany.azure-api.net/conference"/>
```

### Protect an API by adding rate limit policy (throttling)

Set the rate limit to 3 calls per 15 seconds for each subscription Id. After 15 seconds, a developer can retry calling the API.

1. Select **Demo Conference API | Design | All Operations | Inbound Processing 'Policies' editor**
2. Position the cursor inside the **inbound** element (before **base**)
3. In the right window, under **Access restriction policies**, click ** + Limit call rate per key**.
4. Modify the code to look like this: 

```
 <rate-limit-by-key calls="3" renewal-period="15" counter-key="@(context.Subscription.Id)" />
```
5. Click **Save** 
6. Go to the test screen and click **Send** three times in a row -> '429 Too many requests' response
7. Wait 15 seconds and try again -> 200 Response


