1. Import the Calculator wsdl
```
http://www.dneonline.com/calculator.asmx?wsdl
```
Don't forget to select the products.

2. Test 'Add method'

3. Change url from 'Post' to 'Get'

4. Remove the following from the body
```{
  "add": {
    "intA": 1.0,
    "intB": 1.0
  }
}
```
5. Design and add '<set-method>POST</set-method>' so policy resembles

```
    <inbound>
        <base />
        <rewrite-uri template="/calculator.asmx" copy-unmatched-params="false" />
        <set-method>POST</set-method>
        <set-header name="SOAPAction" exists-action="override">

```


6. Design and update to 
```
Change the inbound policy from

```
				<soap:Body>
					<Add>
						<intA>{{body.add.intA}}</intA>
						<intB>{{body.add.intB}}</intB>
					</Add>
				</soap:Body>


```
to
```
				<soap:Body>
					<Add>
						<intA>{{context.Request.OriginalUrl.Query.intA}}</intA>
						<intB>{{context.Request.OriginalUrl.Query.intB}}</intB>
					</Add>
				</soap:Body>

```
<policies>
    <inbound>
        <base />
        <rewrite-uri template="/calculator.asmx" copy-unmatched-params="false" />
        <set-method>POST</set-method>
        <set-header name="SOAPAction" exists-action="override">
            <value>"http://tempuri.org/Add"</value>
        </set-header>
        <set-body template="liquid">
			<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns="http://tempuri.org/">
				<soap:Body>
					<Add>
						<intA>{{query.intA}}</intA>
						<intB>{{query.intB}}</intB>
					</Add>
				</soap:Body>
			</soap:Envelope>
		</set-body>
        <set-header name="Content-Type" exists-action="override">
            <value>text/xml</value>
        </set-header>
    </inbound>
    <backend>
        <base />
    </backend>
    <outbound>
        <base />
        <choose>
            <when condition="@(context.Response.StatusCode < 400)">
                <set-body template="liquid">
                                                    {
  "addResponse" : 
  {
    "addResult" : {{body.envelope.body.AddResponse.AddResult}}
  }
}

                                        </set-body>
            </when>
            <otherwise>
                <set-variable name="old-body" value="@(context.Response.Body.As<string>(preserveContent: true))" />
                <!-- Error response as per https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md#7102-error-condition-responses -->
                <set-body template="liquid">
                {
                "error": {
                    "code": "{{body.envelope.body.fault.faultcode}}",
                      "message": "{{body.envelope.body.fault.faultstring}}"
                      }
            }
                </set-body>
                <choose>
                    <when condition="@(string.IsNullOrEmpty(context.Response.Body.As<JObject>(preserveContent: true)["error"]["code"].ToString()) && string.IsNullOrEmpty(context.Response.Body.As<JObject>(preserveContent: true)["error"]["message"].ToString()))">
                        <set-body>@{
                            var newResponseBody = new JObject();
                            newResponseBody["error"] = new JObject();
                            newResponseBody["error"]["code"] = "InvalidErrorResponseBody";
                            if (string.IsNullOrEmpty((string)context.Variables["old-body"]))
                            {
                                newResponseBody["error"]["message"] = "The error response body was not a valid SOAP error response. The response body was empty.";
                            }
                            else
                            {
                                newResponseBody["error"]["message"] = "The error response body was not a valid SOAP error response. The response body was: '" + context.Variables["old-body"] + "'.";
                            }
                            return newResponseBody.ToString();
                        }</set-body>
                    </when>
                </choose>
            </otherwise>
        </choose>
        <set-header name="Content-Type" exists-action="override">
            <value>application/json</value>
        </set-header>
    </outbound>
    <on-error>
        <base />
    </on-error>
</policies>
```


### useful links
- [API Management transformation policies](https://docs.microsoft.com/en-us/azure/api-management/api-management-transformation-policies)
- https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/api-management/restify-soap-api.md
- [Soap to rest datetime handling](https://winterdom.com/2017/11/25/api-management-soap-to-rest-datetime)
- [URL template parameters](https://stackoverflow.com/questions/42255094/work-with-url-template-parameter-values-in-policy-templates)
- [set body](https://docs.microsoft.com/en-us/azure/api-management/api-management-transformation-policies#SetBody)
- https://blogs.msdn.microsoft.com/apimanagement/2016/12/14/soap-to-rest/
- https://shopify.github.io/liquid/basics/introduction/

## resource graph
https://azure.microsoft.com/en-in/features/resource-graph/
https://docs.microsoft.com/en-us/azure/governance/resource-graph/overview
