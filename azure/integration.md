#integration

## official docs

- [Azure integration overview video (6 min)](https://www.youtube.com/watch?v=BcpzXwezudI)
- [Azure integration services white paper](https://azure.microsoft.com/mediahandler/files/resourcefiles/azure-integration-services/Azure-Integration-Services-Whitepaper-v1-0.pdf)
- [Azure integration patterns](https://docs.microsoft.com/en-us/azure/architecture/browse/#integration)

- [Azure Data Factory overview](https://azure.microsoft.com/en-au/services/data-factory/)
- [Data Factory introduction](https://docs.microsoft.com/en-au/azure/data-factory/introduction)
- [Data Factory videos](https://channel9.msdn.com/Tags/azure-data-factory)



- [An overview of Azure Integration Services | Azure Friday](https://www.youtube.com/watch?v=sbqhJsWhKAs)

## Messages vs Events

```
If a publisher has a certain expectation of how the published information item ought to be handled, and what audience should receive it, it’s issuing a command, assigning a job, or handing over control of a collaborative activity, either of which is expressed in a message.

Message exchanges
Messages often carry information that pass the baton of handling certain steps in a workflow or a processing chain to a different role inside a system. Those messages, like a purchase order or a monetary account transfer record, may express significant inherent monetary value. That value may be lost and/or very difficult to recover if such a message were somehow lost in transfer. The transfer of such messages may be subject to certain deadlines, might have to occur at certain times, and may have to be processed in a certain order. Messages may also express outright commands to perform a specific action. The publisher may also expect that the receiver(s) of a message report back the outcome of the processing, and will make a path available for those reports to be sent back.

This kind of contractual message handling is quite different from a publisher offering facts to an audience without having any specific expectations of how they ought to be handled. Distribution of such facts is best-called events.
```
https://azure.microsoft.com/en-gb/blog/events-data-points-and-messages-choosing-the-right-azure-messaging-service-for-your-data/
