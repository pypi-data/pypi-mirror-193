<p align="center">
	<img src="https://github.com/newvicx/hyprxa/blob/master/docs/img/logo.png?raw=true)" width="465" height="345" alt='Hyprxa'>
</p>

<p align="center"><strong>Hyprxa</strong> <em> (hyper-ex-ay)</em></p>

<p align="center"><em>An asynchronous data integration framework and event hub built on
    </em><a href="https://fastapi.tiangolo.com/"> FastAPI</a>
</p>

## Installation

Install hyprxa using pip:

`pip install hyprxa`

You will also need [MongoDB](https://www.mongodb.com/), [RabbitMQ](https://www.rabbitmq.com/), and [Memcached](https://memcached.org/). To get going quickly, clone the repository and run `docker compose up`

## Introduction

Hyprxa is designed to help developers build secure, scalable, and robust event driven applications. Hyprxa scales with your needs using some of the leading brands in distributed database and messaging technologies.

Hyprxa relies heavily on [pydantic](https://docs.pydantic.dev/) for data validation and ensures data integrations adhere to the target schema set out by the framework.

### Event Hub

Hyprxa ships with a ready-to-use event hub that can be added as a component to new applications. The core model for the event hub is the **Topic**. A topic has a name and a JSON schema that defines the structure for any events associated to that topic. When an event is published to the API, hyprxa validates the event payload against the topic schema. If the validation succeeds, the event is published to the service. Any subscribers listening for the topic (or a sub-topic routing key) will receive the posted event. Additionally, the event is persisted to the database for long term storage. Events can be recalled from the database for auditing and event tracing.

### Data Integrations

The goal of the hyrpxa data integration framework is to provide developers the tools to create a unified timeseries data stream across different data sources. Resources in a data source are uniquely identified through a **subscription**.  A subscription contains all the information required for a data integration to connect to and stream data for a resource. Hyprxa does not ship with any data integrations, it is up to developers to write the integrations. Hyprxa does not care about the underlying protocol, a data integration could be a file watcher to a folder containing CSV files or it could be a websocket connection to a REST API. Hyprxa only requires that the messages from the integration be in a standard format. It will not forward messages to subscribers if the message does not adhere to the schema.

Hyprxa provides a means of grouping subscriptions through a **unitop**. A unitop is a logical grouping of one or more subscriptions to one or more data sources indexed by a common name. Unitops typically represent a physical asset and the subscriptions are sensors on the asset, work orders associated to the asset, transcations related to the asset, etc. However, a unitop can be any logical grouping. For example, we could have a Massachusetts unitop that streams metrics such as average housing price, crime rate, interest rate, etc.

## Documentation

We are working on writing the documentation for Hyprxa. Stay tuned!

## Development

Hyprxa is under active development but, the API is more or less finalized. Hyprxa will remain as an alpha release until proper code coverage testing and documentation is complete. Please report any bugs.
