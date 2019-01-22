## What is a bot ? 
A bot is an app that users interact with in a conversational way. Bots can communicate conversationally with text, cards, or speech.
For more info check out https://docs.microsoft.com/en-us/azure/bot-service/bot-service-overview-introduction 

## Can I see some good demos ? 
Sure can. Check out the following: 
1. The Microsoft Health Bot http://aka.ms/ai/healthbot
2. 'Sam' - a public-facing chatbot for DHS https://www.humanservices.gov.au/individuals/students-and-trainees
3. Contoso Scuba - http://contososcubademo.azurewebsites.net

## Where can I find documentation ?
There is lots of great documentation on bots.
- QnA Maker https://qnamaker.ai
- LUIS https://www.luis.ai/
- Azure Bot Service Documentation https://docs.microsoft.com/en-us/azure/bot-service/
- The bot framework developer portal https://dev.botframework.com/
- Bot Builder SDK for .NET https://docs.microsoft.com/en-us/azure/bot-service/dotnet/bot-builder-dotnet-overview

## Where can I get sample applications ? 
There are heaps of awesome samples for the Azure Bot Service here https://github.com/Microsoft/BotBuilder-Samples

There are lots of great open source projects for example

Learn AI Bootcamp bot (Bot Framework v4)
[Doco](https://azure.github.io/LearnAI-Bootcamp/emergingaidev_bootcamp) and [Repo](https://github.com/Azure/LearnAI-Bootcamp/tree/master/lab02.2-building_bots)

Password reset bot (Bot Framework v4)
[Blog Post](https://blogs.msdn.microsoft.com/buckwoody/2018/09/25/applied-ai-using-a-bot-for-password-reset/)
 | 
[Source code](https://github.com/pragmatismo-io/AzureADPasswordReset.gbapp/)

Accounts Payable bot using Service Now (Bot Framework v3.. looking for help to upgrade)
https://github.com/jomit/ap-bot (Created by Jomit - a Microsoft CSA in Seattle)


Also, the code for @adamstephensen's bot about bots is here https://github.com/adamstephensen/my-bot-bot
It demonstrates some functionality not in the official bot samples, including how to build a bot on Azure Functions.



## What templates are available for building bots.
There are 5 templates out of the box.
1. Basic bot
2. Form bot
3. Language Understanding bot
4. Question and Answer bot
5. Proactive bot
https://docs.microsoft.com/en-gb/azure/bot-service/bot-service-concept-templates

The important point to make here is that these are out of the box tempates that each demonstrate a single piece of functionality. It is very common to incorporate all of these features in one bot.

## What are the pros and cons of function bots over web bots
What are the benefits of going for a Web Bot
1. Web bot is always on - No Warm up time
Function bot can take a few seconds to warm up if it hasn't been hit for a while
2. More control over how the bot scales / Predictable costing
What a web bot you control how much the bot scales.

Here are the benefits of going for a Function Bot
1. Pay as you use - per second billing
If no-one is using your bot, you will not pay for it
2. Infitinte scale without any need to configure scaling rules.
Scaling just comes in with the platform
3. Easy integration with other Azure services.
Function bots easy integrate with other Azure services like Logic Apps, Service Bus, Cosmos DB, Table Storage, Storage Queues.
4. Simplification of Development
You don't need to host your application on the MVC framework.
You have your run.csx.. and it executes your bot.

## How do I get app settings into my bot?
The trick is to put them into local.settings.json on your dev machine and then to read them from App Settings in Azure.
Check out https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-csharp#environment-variables for more info. 

## Can I use LUIS and QnAMaker together?
Luis and QnA maker love hanging out together.
Check this out http://www.garypretty.co.uk/2017/03/26/forwarding-activities-messages-to-other-dialogs-in-microsoft-bot-framework/

## How do I create a LUIS endpoint key ?
Easy. Check this out https://docs.microsoft.com/en-us/azure/cognitive-services/luis/azureibizasubscription

## Should my dialogues hand off from LUIS to Qna or from Qna To LUIS
It depends.
Some people like to make LUIS the master and if no LUIS intent is identified hand off to QnA maker to return a QnA match.
Others prefer to capture as much as possible in QnA and then pass to LUIS.
One consideration is that calls to QnA Maker are currently Free (as at 24 April 2018) where you pay a very small amount for every LUIS request. 

## Can I add a message when the bot loads ? 
Even though no-one shows you how to do it... of course you can add a message when the bot loads. 
Here are some instructions. https://www.davidezordan.net/blog/?p=8119

## Can I leverage AI ?
To learn about leveraging AI with bots check out https://docs.microsoft.com/en-us/azure/bot-service/bot-service-concept-intelligence

## Is there a commerce demo ? 
For a commerce demo check out https://docs.microsoft.com/en-us/azure/bot-service/bot-service-scenario-commerce

## How do I do a password reset bot?
To build a password reset bot check out https://docs.microsoft.com/en-us/azure/bot-service/bot-service-design-pattern-task-automation

## Can I do Human hand off ?
You can configure your bot to connect a user with a real person using the human hand off pattern. Check out https://docs.microsoft.com/en-us/azure/bot-service/bot-service-design-pattern-handoff-human
https://blogs.msdn.microsoft.com/jamiedalton/2017/08/10/microsoft-bot-framework-handing-off-to-a-human-for-agentssupervisors-with-c-and-the-botbuilder-sdk/

## How do I go to Kudu for by bot ? 
Just go to https://(your-bot-name).scm.azurewebsites.net

## How do I handle global messages ?
You implement global messages like this https://docs.microsoft.com/en-us/azure/bot-service/dotnet/bot-builder-dotnet-global-handlers

## How can I get app settings into my bot?
The trick is to put them into local.settings.json on your dev machine and then to read them from App Settings in Azure.
Check out https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-csharp#environment-variables for more info. 

## Where can I find training about bots ? 
This course is a few years old... but covers all the basics in detail. 
https://mva.microsoft.com/en-us/training-courses/developing-intelligent-bots-from-zero-to-hero-17797
It is well worth a watch.

## How can I learn about async await for asynchronous programming ? 
Check out this reference for async / await https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/await?

## Where can I learn about navigation ? 
Navigation is easy once you understand using dialogs. Check this out... 
https://github.com/Microsoft/BotBuilder-Samples/blob/master/CSharp/core-MultiDialogs/README.md

## Can I have more than 1 QnA in a single bot ? 
Absolutely!
It is often better to have multiple smaller QnA makers than one monster one. 
Consider a bot for a bank.
It may be better for a bank to ask 
"Do you want to discuss Banking, Insurance or Loans ? "
Then the user navigates to a specific QnA maker dialog for either Banking, Insurance or Loans.
Now then the user types 'How do I apply?' the bot can apply in context.

You can set this up by either:
1. have a separate QnA dialogue for each QnA maker
2. have one generic QnA maker dialogue that you pass the keys into and re-use depending on where you are navigating to it from.

## Can you help me understand the dialog lifecycle and navigating dialogs ?
You might need to read this a few times.. but it's important.
- When a dialog is invoked, it takes control of the conversation flow. Every new message will be subject to processing by that dialog until it either closes or redirects to another dialog.
- In C#, you can use context.Wait() to specify the callback to invoke the next time the user sends a message. To close a dialog and remove it from the stack (thereby sending the user back to the prior dialog in the stack), use context.Done(). You must end every dialog method with context.Wait(), context.Fail(), context.Done(), or some redirection directive such as context.Forward() or context.Call(). A dialog method that does not end with one of these will result in an error (because the framework does not know what action to take the next time the user sends a message).
- From https://docs.microsoft.com/en-us/azure/bot-service/dotnet/bot-builder-dotnet-manage-conversation-flow
For more info

There are a few key methods. For a sample application that demonstrates this well check out
https://github.com/Microsoft/BotBuilder-Samples/blob/master/CSharp/core-MultiDialogs/README.md
Look for the implementations of 
- context.Call and context.Done  
- context.Forward 
- context.Wait
- context.Fail

Check out the following links about navigating and building dialogues: 
- https://docs.microsoft.com/en-gb/bot-framework/bot-service-design-conversation-flow
- https://blog.botframework.com/2017/11/10/dialog-management-qna-luis-scorables/
- http://www.garypretty.co.uk/2017/03/26/forwarding-activities-messages-to-other-dialogs-in-microsoft-bot-framework/

Watch out for some pitfalls with bot design navigation
- https://docs.microsoft.com/en-gb/bot-framework/bot-service-design-navigation

## What are the common mistakes ? 
There are a lot of common mistakes made with bots.
1. Bad navigation https://docs.microsoft.com/en-gb/bot-framework/bot-service-design-navigation
2. Having a bot that tries to do too much. You are better off having several small bots that do a specific task very well.
3. Trying to make your bot too 'smart'. The best bots aren't the smartest bots. The best bots are the ones that solve an issue that users have. A simple bot that guides a user to a solution will be well utilised. A 'smart' bot that is hard to use will not.

## Can I get a list of all the questions or FAQs ?
All the FAQs in this bot can be found here https://github.com/adamstephensen/my-bot-bot/blob/master/MyBotBot.BotAssets/FAQs/BotFAQs.md

## How do I setup my machine for bot development ? 
I'm still working on this… check back soon.

## What are the options for deploying my bot using ci/cd and devops ? 
I'm still working on this… check back soon.

## How do I build a multi-lingual bot ? 
Check out this link https://desflanagan.wordpress.com/2016/10/25/build-a-multi-language-bot/ 

## Where does Microsoft have Azure Datacentres ? 

Azure has data centres all over the world. Check out this awesome map http://azuredatacentermap.azurewebsites.net/ 

## Where is the data for my bot? 
Great question.

The list of services and the regions they are available in can be found here: https://azure.microsoft.com/en-au/regions/services/ 

It is particularly important for customers who operate in highly regulated industries, or in countries with data protection laws, to know the geographic location of the data that they have entrusted to a Microsoft cloud service. Microsoft also understands that some customers must maintain their data in a specific geographic location, such as within the European Union (EU). To that end, Microsoft maintains an ever-expanding network of datacenters around the globe, and verifies that each datacenter meets stringent security requirements.

The key to this answer is found on two pages
1. https://www.microsoft.com/en-us/trustcenter/privacy/where-your-data-is-located
2. http://azuredatacentermap.azurewebsites.net/ (Make sure to scroll down to under the map)

It is also worth checking out 
1. The privacy statement https://privacy.microsoft.com/en-us/privacystatement 
2. Cog Services T&Cs https://azure.microsoft.com/en-us/support/legal/cognitive-services-terms/ 

## What are adaptive cards?
Adaptive Cards are a new way for developers to exchange card content in a common and consistent way.
See the official page at http://adaptivecards.io/ for more.
Here is the video introduction from the Build conference https://www.youtube.com/watch?v=VjIhd_9Az9w
Check out adaptive cards designer here https://acdesignerbeta.azurewebsites.net/

## Where can I find out information about the Bot Framework v4? 

v4 is the next version of the Bot Framework. It's still in preview.

Bot Framework v4 can be found on GitHub 
- DotNet is here https://github.com/Microsoft/botbuilder-dotnet
- Node is here https://github.com/Microsoft/botbuilder-js

The doco is here https://docs.microsoft.com/en-us/azure/bot-service/?view=azure-bot-service-4.0

Here is Hello World in Bot Framework v4. https://blog.botframework.com/2018/05/07/build-a-microsoft-bot-framework-bot-with-the-bot-builder-sdk-v4/

Also, check out this video https://www.youtube.com/watch?v=SL077rQQQMg and this article 
Also check out https://blogs.msdn.microsoft.com/martinkearn/2018/07/17/bot-framework-v4-what-i-learnt-in-4-days-in-july-2018/


## What is Chatdown?
Chatdown allows you to 
- export a conversation with a bot as a transcript that can be re-loaded into the emulator at a later point for feedback / analysis
- create chat transcripts and load them into the bot emulator for mocking up bots 
Check out this video for more https://www.youtube.com/playlist?list=PLz6hh7iUxR21lAh7a3yjcRwZN6FnDUxpr

## How should I architect my bot ? 

There are many right ways to architect a bot.

Here are some pattherns and references I find useful: 

[The Scalable Web App reference architecture]
(https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/scalable-web-app)

[A list of common cloud architecture patterns]
(https://docs.microsoft.com/en-us/azure/architecture/patterns/)

Creating a hybrid network (connecting to on-prem resources) either using [Hybrid network with Express Route](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/expressroute)
 or a [Hybrid network using a VPN](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/vpn)
 
 How to use [Azure API Management to connect to internal resources](https://docs.microsoft.com/en-us/azure/api-management/api-management-using-with-internal-vnet)
 
## How do I resolve 401 errors ? 
Check this out https://blogs.msdn.microsoft.com/kwill/2017/05/17/http-401-access-denied-when-calling-azure-cognitive-services-apis/

## There are so many different keys. Help me. 
OK. https://docs.microsoft.com/en-gb/azure/cognitive-services/LUIS/luis-concept-keys
https://blogs.msdn.microsoft.com/kwill/2017/05/17/http-401-access-denied-when-calling-azure-cognitive-services-apis/
https://docs.microsoft.com/en-us/azure/cognitive-services/LUIS/luis-reference-regions#publishing-regions


## How do I build a bot to work on Microsoft Teams ? 
https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/bots/bots-create
https://github.com/OfficeDev/BotBuilder-MicrosoftTeams/tree/master/CSharp/Samples/Microsoft.Bot.Connector.Teams.SampleBot
How to side load a bot into teams in 10 seconds https://docs.microsoft.com/en-us/microsoftteams/add-bots#side-load-your-own-bot-for-private-chat

## How do I store state in Bot Framework v4 ? 
Here is an article http://aihelpwebsite.com/Blog/EntryId/1031/Saving-User-and-Conversation-Data-MS-Bot-Framework-V4-Preview-Edition
As per this link you need to use Cosmos, not table or blob storage. https://github.com/Microsoft/botbuilder-dotnet/issues/736

## Where can I get the v4 Roadmap ? 
You can see the plan for Bot Framework v4 here https://github.com/Microsoft/botbuilder-dotnet/wiki/Roadmap

## How do I do authication for a bot in teams ? 
Here are some links to help you do auth for a bot in teams
https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/authentication/auth-oauth-card
https://github.com/OfficeDev/microsoft-teams-sample-auth-node
https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/authentication/auth-bot-aad
https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/authentication/auth-configure
https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-tutorial-authentication?view=azure-bot-service-3.0#notes-on-the-token-retrieval-flow
https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-tutorial-authentication?view=azure-bot-service-3.0

## Where can I find a v4 hands on lab ? 
There is a great hands on lab here 
https://github.com/Azure/LearnAI-Bootcamp/tree/master/lab02.2-building_bots

## How do I integrate my bot with Alexa ? 
To build an Alexa skill with the bot framework check this out https://github.com/CatalystCode/alexa-bridge 

## How do I do logging ? 
- [Microsoft Lab for logging ](https://github.com/Azure/learnAnalytics-AdvancedFeaturesforMicrosoftBotFramework)
- [ibex dashboard](https://github.com/Azure/ibex-dashboard)
- [instrumentation library](https://github.com/Azure/botbuilder-instrumentation)
