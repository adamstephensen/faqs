



# azd cli scripts

azd auth login

> https://github.com/Azure-Samples/todo-java-mongo-aca
azd init --template todo-java-mongo-aca

https://techcommunity.microsoft.com/t5/ai-applied-ai-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w/ba-p/3762087
https://github.com/Azure-Samples/azure-search-openai-demo/
azd init -t azure-search-openai-demo

azd up
azd pipeline config
azd monitor --overview
azd monitor --live
azd monitor --logs

# CoPilot Demo Scripts

using comments
// write a function to validate an email address
repeat using the method declaration
genearte the unit test

vulnerability
is there an error in this code ? 
is this code secure ? 
wrap this code in a method

cobol
what does this code do
convert this code to java.


## https://github.com/gh-productivity-workshops/PetSpotR


## https://github.com/nolecram/HelpMeCopilot

experiment1.js
- select all code
- 'document this code'
- build tests for the code

example.cobol
- select all code
- 'document the code'
- 'translate to python'

vulnerable.php
- select all code
- 'is this code secure?'
- 'how do i exploit this vulnerability'
- 'fix it'



#-----------C# 
## install .net 7: command prompt as adminsitrator
# note: didn't work in devbox. gave an error
winget install Microsoft.DotNet.SDK.7

## check installed versions
dotnet --list-sdks

## new csx applications
dotnet script rockpaperscissors.csx

## new console applications
dotnet new console --framework net7.0


public bool ValidatePhoneNumber(string phoneNumber)
        {
             string MatchPhoneNumberPattern = @"^(\+[0-9]{9})$";
             string MatchAustralianPhoneNumberPattern = @"^(\+61[0-9]{9})$";
             string matchUSPhoneNumberPattern = @"^(\+1[0-9]{9})$";
            return Regex.IsMatch(phoneNumber, MatchPhoneNumberPattern);            
        }


#----------- main.py
# Write a rock, paper, scissors game
# import random module
# define main function that handles all the logic
# call main function
>python3 main.py




#-------------- javascript suggestion  (in a .js file)
function calculateDaysBetweenDates(begin, end) {

// find all images without alternate text
// and give them a red border
function process() {

// Express server on port 3000

// Return the current time



## From Catalin Pit
https://www.youtube.com/watch?v=edSZh-tpTIk

```
//find all images
// and add a green border around them
// and add a class "githubCopilot" to them
function go() {}

//create Express server
var app = express();

// set up port

// set up environment 
```


## Visual Studio Code Youtube channel 
https://www.youtube.com/watch?v=o3qURBllpGM

item.cs

```
using Microsoft.EntityFrameworkCore;

public interface  IApplicationDbContext {
    DbSet<TodoList> TodoLists { get; set; }
    DbSet<TodoItem> TodoItems { get; set; }

    Task<int> SaveChangesAsync(CancellationToken cancellationToken);
}

public class ApplicationDbContext : DbContext, IApplicationDbContext {
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }

    public DbSet<TodoList> TodoLists { get; set; }
    public DbSet<TodoItem> TodoItems { get; set; }

    public async Task<int> SaveChangesAsync(CancellationToken cancellationToken) {
        return await base.SaveChangesAsync(cancellationToken);
    }
}


```



item.js

``` 
const express = require('express');
const app = express();
const port = 3000;

app.post("/items", (req, res) => {
   //how to get the item from the req
   let item = req.body.item;
   req.send("Item added");
//    
});

// how to get rid of bullets in the list

```

item.html

```
<link rel="stylesheet" type="text/css" href="style.css" />

<body>

    <h1>My Website</h1>
    <div>
        <ul>
            <li>Home</li>
            <li>About</li>
            <li>Contact</li>
    </div>
    </ul>
</body>
```

style.css

```
/* highlight a list item green when a user mouses over it  */
li:hover {
    background-color: green;

}

/* how to get rid of the bullest in the list */
ul {
    list-style-type: none;
}

/* horizontally and vertically center the text in the body */
body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}
```
