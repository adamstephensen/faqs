# Simple bot V4 SDK Phase 1

1.	You can navigate to this repo and get more information about the bot https://github.com/Microsoft/BotBuilder and versions.
2.	Navigate to Bot Framework Emulator as it is the one we will be doing to test the bot

3.	Download .net core sdk from .net core sdk page
4.	Navigate to Command prompt 
5.	> dotnet new webapi --name demo1
6.	>cd demo1
7.	Got to nuget and check for Microsoft.Bot.Builder.Integration.AspNet.Core
8.	>dotnet add package Microsoft.Bot.Builder.Integration.AspNet.Core -v 4.1.5
9.	Open project in Visual Studio 
10.	Create new folder Bot and under the folder create new class SimpleBot.cs
11.	Add nuget package using Microsoft.Bot.Builder; and using Microsoft.Bot.Schema;
12.	Simple bot needs to implement IBot
    public class SimpleBot: IBot
    
```    
    {}
```    
    
13.	Add implementation for IBot and add async 

```
    public class SimpleBot : IBot
    {
        public async Task OnTurnAsync(ITurnContext turnContext, CancellationToken cancellationToken = default(CancellationToken))
        {
            throw new NotImplementedException();
        }
 }
```

14.	Add logic 

```
    public class SimpleBot : IBot
    {
        public async Task OnTurnAsync(ITurnContext turnContext, CancellationToken cancellationToken = default(CancellationToken))
        {
            if (turnContext.Activity.Type is ActivityTypes.Message)
            {
                string input = turnContext.Activity.Text;
                await turnContext.SendActivityAsync($"SimpleBot: (input)");

            }
        }
}
```

15.	Navigate to Startup.cs file which basically runs on start up and add the following code and assemblies 
using demo1.Bot;
using Microsoft.Bot.Builder.Integration.AspNet.Core;
using Microsoft.Bot.Builder.BotFramework;

```
        public Startup(IHostingEnvironment env)
        {
            // Set the root path
            ContentRootPath = env.ContentRootPath;
        }

        // Track the root path so that it can be used to setup the app configuration
        public string ContentRootPath { get; private set; }

        public void ConfigureServices(IServiceCollection services)
        {
            // Set up the service configuration
            var builder = new ConfigurationBuilder()
                .SetBasePath(ContentRootPath)
                .AddJsonFile("appsettings.json")
                .AddEnvironmentVariables();
            var configuration = builder.Build();
            services.AddSingleton(configuration);

            // Add your SimpleBot to your application
            services.AddBot<SimpleBot>(options =>
            {
                options.CredentialProvider = new ConfigurationCredentialProvider(configuration);
            });
        }

        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            app.UseStaticFiles();

            // Tell your application to use Bot Framework
            app.UseBotFramework();
        }
```        
        
16.	Now that we have done all the changes to run a simple bot navigate to Solution Explorer -> project -> properties -> debug and untick “Launch Browser” and “Enable SSL”
17.	Copy the link url -> save and run 
18.	Open emulator and add https://localhost:44317/api/messages
19.	TADAAAA it should work! Hopefully 😊


## Simple bot V4 SDK Phase 2 - Middleware Pipeline
If you want to add functionality to your bot you can look at middle ware. Typically, middle ware is general functionality which you want to apply to your bots. For example
1.	Conversation logging – logging every single message that comes in instead of logging every message in the bot itself;
2.	Error handling;
3.	Natural language recognition;

 

figre: Middle ware pipeline 

4.	Add a folder called Middleware and add two classes SimpleMiddleware1.cs and SimpleMiddlewarw2.cs as following:


SimpleMiddleware1.cs

```
public class SimpleMiddleware1 : IMiddleware
    {
        public async Task OnTurnAsync(ITurnContext context, NextDelegate next, CancellationToken cancellationToken = default(CancellationToken))
        {
            await context.SendActivityAsync($"[SimpleMiddleware1] {context.Activity.Type}/OnTurn/Before");

            await next(cancellationToken);

            await context.SendActivityAsync($"[SimpleMiddleware1] {context.Activity.Type}/OnTurn/After");
        }
    }
```

SimpleMiddlewarw2.cs

```
    public class SimpleMiddleware2 : IMiddleware
    {
        public async Task OnTurnAsync(ITurnContext context, NextDelegate next, CancellationToken cancellationToken = default(CancellationToken))
        {
            await context.SendActivityAsync($"[SimpleMiddleware2] {context.Activity.Type}/OnTurn/Before");

            if (context.Activity.Type == ActivityTypes.Message && context.Activity.Text == "secret password")
            {
                // calling next() is totally optional. if the middleware does not call next then the
                // next middleware in the pipeline will not be called, AND the bot will not receive the message.
                //
                // in this instance, we are only handing the message to downstream bots if the user says "secret password"
                await next(cancellationToken);
            }

            await context.SendActivityAsync($"[SimpleMiddleware2] {context.Activity.Type}/OnTurn/After");
        }
    }
```

5.	Navigate back to Startup.cs  and add calls to Middleware 

```
options.Middleware.Add(new SimpleMiddleware1());
options.Middleware.Add(new SimpleMiddleware2());
```

## Simple bot V4 SDK Phase 3 – State Middleware
1.	This is to be able to use middleware to keep the state. For example, store name. 
Create a state class called DemoState.cs. Which is a plan C# object that has a single property on there. 

You can declare a few different states 
1.	User State (to store information like name, surname etc)
2.	Conversation State (Whether the bot asked the user a question, and which question that was)

Links: https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-state?view=azure-bot-service-4.0
https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-v4-state?view=azure-bot-service-4.0&tabs=csharp
https://github.com/Microsoft/BotFramework-Samples/blob/master/SDKV4-Samples/dotnet_core/StateBot/StateBot.cs


2.	Navigate to Startup.cs and add the following to ConfigureServices().Note in this case we are using MemoryStorage(). Its OK for the development, however if you want to use it in production consider using a different storage system. 

Define the storage and create state management objects:

```
                var conversationState = new ConversationState(new MemoryStorage());
                options.State.Add(conversationState);
```

3.	Defines a state property used to track conversation data. Create class BankingBotState.cs 

```
    public class BankingBotState
    {
        public string Recipient { get; set; }
        public int Amount { get; set; }
    }
```

4.	Next, we define a class that contains the state management information we'll need to configure our bot instance. Create class BotAccessors.cs 

```
        public class BotAccessors
        {
            public BotAccessors(ConversationState conversationState)
            {
                ConversationState = conversationState ?? throw new ArgumentNullException(nameof(conversationState));
            }

        public static string BankingBotStateAccessorName { get; } = $"{nameof(BotAccessors)}.BankingBotState";
        public IStatePropertyAccessor<DialogState> DialogStateAccessor { get; internal set; }
        public ConversationState ConversationState { get; }


    }
```

5.	Now we're ready to define the state property accessors and configure our bot. We'll use the conversation state management object for the conversation flow state property accessor. In Startup.cs, we configure ASP.NET to provide the bundled state property and management objects.

```
            services.AddSingleton(serviceProvider =>
            {
                var options = serviceProvider.GetRequiredService<IOptions<BotFrameworkOptions>>().Value;
                var conversationState = options.State.OfType<ConversationState>().FirstOrDefault();

                var accessors = new BotAccessors(conversationState)
                {
                    BankingBotStateStateAccessor = conversationState.CreateProperty<BankingBotState>(BotAccessors.BankingBotStateAccessorName)
                };

                return accessors;
            });
```            
            
6.	Before we use our state properties, we use each accessor to load the property from storage and get it from the state cache.So in BankingBot.cs add 

```        
        private DialogSet dialogs;

        public BankingBot(BotAccessors botAccessors)
        {
            BotAccessors = botAccessors;
        }

        public BotAccessors BotAccessors { get; }
```

7.	And for onTurnAsync add the following code:

```
        public async Task OnTurnAsync(ITurnContext turnContext, CancellationToken cancellationToken = default(CancellationToken))
        {

            if (turnContext.Activity.Type == ActivityTypes.Message)
            {
                // initialize state if necessary
                var state = await BotAccessors.BankingBotStateStateAccessor.GetAsync(turnContext, () => new BankingBotState(), cancellationToken);

                turnContext.TurnState.Add("BotAccessors", BotAccessors);

                state.Amount ++;

                await turnContext.SendActivityAsync($"You said {turnContext.Activity.Text}, and you have made {state.Amount} requests.");

                await BotAccessors.ConversationState.SaveChangesAsync(turnContext, false, cancellationToken);
            }

        
}
```


## Simple bot V4 SDK Phase 4 – Dialog

### General
In Bot framework dialogs there are Dialogs Sets (prompts, waterfalls) and Dialog context contains information pertaining to the dialog,and is used to interact with a dialog set from within your bot's turn handler. 

Your bot needs to define top -level dialogs in a DialogSet using either:
1.	Prompts 
Use DialogSet.Add(string dialogID, IDialog dialog) with * Prompt to add functions that prompt the user for input and process the response. Prompt for date or mobile number.
2.	Waterfall Steps
Use Dialog.Add (string dialogId, WaterfallStep[] steps) to add WaterfallSteps which allow the Dialog to flow from one interaction to the next
The Bot framework SDK version 4 has a dialog library 

 
Dialog sets are, in the simplest terms, a collection of dialogs, which can be prompt, waterfall and component. Each dialog will have a dialog ID.

Dialog context contains information pertaining to the dialog, and is used to interact with a dialog set from within your bot's turn handler. The dialog context includes the current turn context, the parent dialog, and the dialog state, which provides a method for preserving information within the dialog. The dialog context allows you to start a dialog with it's string ID or continue the current dialog (such as a waterfall dialog that has multiple steps).

Good dialog overview: https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-dialog?view=azure-bot-service-4.0



## How to use Dialogs
You can use the dialog context to begin, continue, replace, or end a dialog. You can also cancel all dialogs on the dialog stack.

1.	Create new folder called Dialogs 
2.	Add new class MainDialog.cs and add new nuget package Mic rosoft.Bot.Builder.Dialogs;
3.	It should inherest from waterfall dialogs WaterfallDialog
4.	Navigate back to BotAccessors and add:

```
        public static string DialogStateAccessorName { get; } = $"{nameof(BotAccessors)}.DialogState";
        public IStatePropertyAccessor<DialogState> DialogStateAccessor { get; internal set; }
```         
5.	Navigate to Startup.cs and add another accessor 

```
                    DialogStateAccessor = conversationState.CreateProperty<DialogState>(BotAccessors.DialogStateAccessorName),
```                    

6.	Navigate to Banking.Bot and add the following to BankingBot(BotAccessros botAccessors)

```
     var dialogState = botAccessors.DialogStateAccessor;
          //compose dialogs
       dialogs = new DialogSet(dialogState);
            dialogs.Add(MainDialog.Instance);
        dialogs.Add(new ChoicePrompt("choicePrompt"));
        dialogs.Add(new TextPrompt("textPrompt"));
         dialogs.Add(new NumberPrompt<int>("numberPrompt"));
            BotAccessors = botAccessors;
```

7.	Navigate to BankingBot.cs and add the following to onTurnAsync()

```
                var dialogCtx = await dialogs.CreateContextAsync(turnContext, cancellationToken);

                if (dialogCtx.ActiveDialog == null)
                {
                    await dialogCtx.BeginDialogAsync(MainDialog.Id, cancellationToken);
                }
                else
                {
                    await dialogCtx.ContinueDialogAsync(cancellationToken);
                }
```

8.	Navigate to MainDialog.cs and add:

```
    public MainDialog(string dialogId, IEnumerable<WaterfallStep> steps = null) : base(dialogId, steps)
        {

            AddStep(async (stepContext, cancellationToken) =>
            {
                return await stepContext.PromptAsync("choicePrompt",
                    new PromptOptions
                    {
                        Prompt = stepContext.Context.Activity.CreateReply("[Maindialog] Hi user, what would you like me to say"),
                        Choices = new[] { new Choice { Value = "Great demo" }, new Choice { Value = "Amazing Weather" } }.ToList()
                    });
            });
            AddStep(async (stepContext, cancellationToken) =>
            {
                var response = (stepContext.Result as FoundChoice)?.Value;

                if (response == "Great demo")
                {
                    await stepContext.Context.SendActivityAsync("Great Demo");
                }

                if (response == "Amazing Weather")
                {
                    await stepContext.Context.SendActivityAsync("Amazing Weather");
                }

                return await stepContext.NextAsync();
            });

            AddStep(async (stepContext, cancellationToken) => { return await stepContext.ReplaceDialogAsync(Id); });
        }

        public static string Id => "mainDialog";

        public static MainDialog Instance { get; } = new MainDialog(Id);

    }
```
 
Adding more to Dialog stack
1.	Under Dialogs folder create two more folders such as Balance and Payment folder. 
2.	Under Balance folder create CheckBalanceDialog.cs

```
        public CheckBalanceDialog(string dialogId, IEnumerable<WaterfallStep> steps = null) : base(dialogId, steps)
        {
            AddStep(async (stepContext, cancellationToken) =>
            {
                return await stepContext.PromptAsync("choicePrompt",
                    new PromptOptions
                    {
                        Prompt = stepContext.Context.Activity.CreateReply($"[CheckBalanceDialog] Which account?"),
                        Choices = new[] { new Choice { Value = "Current" }, new Choice { Value = "Savings" } }.ToList()
                    });
            });

            AddStep(async (stepContext, cancellationToken) =>
            {
                var response = stepContext.Result as FoundChoice;

                if (response.Value == "Current")
                {
                }

                if (response.Value == "Savings")
                {
                }

                return await stepContext.EndDialogAsync();
            });
        }

        public static string Id => "checkBalanceDialog";
        public static CheckBalanceDialog Instance { get; } = new CheckBalanceDialog(Id);
```        
        
3.	Under Payment Folder create MakePaymentDialog.cs

```
public MakePaymentDialog(string dialogId, IEnumerable<WaterfallStep> steps = null) : base(dialogId, steps)
        {
            AddStep(async (stepContext, cancellationToken) =>
            {
                return await stepContext.PromptAsync("textPrompt",
                    new PromptOptions
                    {
                        Prompt = stepContext.Context.Activity.CreateReply("Who would you like to pay?")
                    });
            });

            AddStep(async (stepContext, cancellationToken) =>
            {
                var state = await (stepContext.Context.TurnState["BotAccessors"] as BotAccessors).BankingBotStateStateAccessor.GetAsync(stepContext.Context);
                state.Recipient = stepContext.Result.ToString();

                return await stepContext.PromptAsync("numberPrompt",
                    new PromptOptions
                    {
                        Prompt = stepContext.Context.Activity.CreateReply($"{state.Recipient}, got it{Environment.NewLine}How much should I pay?"),
                        RetryPrompt = stepContext.Context.Activity.CreateReply("Sorry, please give me a number.")
                    });
            });

            AddStep(async (stepContext, cancellationToken) =>
            {
                var state = await (stepContext.Context.TurnState["BotAccessors"] as BotAccessors).BankingBotStateStateAccessor.GetAsync(stepContext.Context);
                state.Amount = int.Parse(stepContext.Result.ToString());

                await stepContext.Context.SendActivityAsync($"Thank you, I've paid {state.Amount} to {state.Recipient} 💸");
                return await stepContext.EndDialogAsync();
            });
        }

        public static string Id => "makePaymentDialog";
        public static MakePaymentDialog Instance { get; } = new MakePaymentDialog(Id);
```        
        
4.	They both should inherent WaterfallDialog
5.	Add instance of each dialog in BankingBot.cs 

```
dialogs.Add(MakePaymentDialog.Instance);
dialogs.Add(CheckBalanceDialog.Instance);
```

6.	Return back to Maindialog and under each category declair the start dialog:

```
 return await stepContext.BeginDialogAsync(CheckBalanceDialog.Id);
return await stepContext.BeginDialogAsync(MakePaymentDialog.Id);
```

7.	Also change the buttons to payment and balance.
 

8.	Lest add a few child dialogs to our CheckBalanceDialog.cs
9.	Create a new folder in Balance called CurrentAccount and SavingsAccount
10.	Under CurrentAccount create new dialog CheckCurrentAccountBalanceDialog.cs

```
        public CheckCurrentAccountBalanceDialog(string dialogId, IEnumerable<WaterfallStep> steps = null) : base(dialogId, steps)
        {
            AddStep(async (stepContext, cancellationToken) =>
            {
                await stepContext.Context.SendActivityAsync($"Your current balance is...");
                return await stepContext.EndDialogAsync();
            });
        }

        public static string Id => "checkCurrentAccountBalanceDialog";
        public static CheckCurrentAccountBalanceDialog Instance { get; } = new CheckCurrentAccountBalanceDialog(Id);
```        
        
        
11.	Under SavingsAccount create new dialog called CheckSavingsAccountBalanceDialog.cs

```
        public CheckSavingsAccountBalanceDialog(string dialogId, IEnumerable<WaterfallStep> steps = null) : base(dialogId, steps)
        {
            this.AddStep(async (stepContext, cancellationToken) =>
            {
                await stepContext.Context.SendActivityAsync($"Your savings balance is...");
                return await stepContext.EndDialogAsync();
            });
        }

        public static string Id => "checkSavingsAccountBalanceDialog";
        public static CheckSavingsAccountBalanceDialog Instance { get; } = new CheckSavingsAccountBalanceDialog(Id);
```

12.	Navigate Back to CheckBalanceDialog.cs and add a starter declaration for every single dialog for current and savings 

```
                    return await stepContext.BeginDialogAsync(CheckCurrentAccountBalanceDialog.Id);
                    return await stepContext.BeginDialogAsync(CheckSavingsAccountBalanceDialog.Id);

+                 return await stepContext.NextAsync();

```

