from collections.abc import AsyncIterable
from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorCollection

from hyprxa.events.models import EventDocument, ValidatedEventDocument



async def get_events(
    collection: AsyncIOMotorCollection,
    topic: str,
    start_time: datetime,
    end_time: datetime | None = None,
    routing_key: str | None = None,
) -> AsyncIterable[EventDocument]:
    """Stream events matching both topic and routing key in a time range.
    
    Args:
        collection: The motor collection.
        topic: The event topic to search.
        start_time: Start time of query. This is inclusive.
        end_time: End time of query. This is inclusive.
        routing_key: The routing key for events to query.

    Yields:
        document: An `EventDocument`

    Raises:
        ValueError: If 'start_time' >= 'end_time'.
        PyMongoError: Error in motor client.
    """
    end_time = end_time or datetime.utcnow().replace(tzinfo=None)
    if start_time >= end_time:
        raise ValueError("'start_time' cannot be greater than or equal to 'end_time'")

    query = {"topic": topic, "timestamp": {"$gte": start_time, "$lte": end_time}}
    if routing_key:
        query.update({"events.routing_key": routing_key})
    async for events in collection.find(
        query,
        projection={"events": 1, "_id": 0}
    ).sort("timestamp", 1):
        if events:
            documents = [ValidatedEventDocument(**event) for event in events["events"]]
            if routing_key:
                documents = [document for document in documents if document.routing_key == routing_key]
            if documents:
                index = sorted([(document.timestamp, i) for i, document in enumerate(documents)])
                for _, i in index:
                    if documents[i].timestamp >= start_time and documents[i].timestamp <= end_time:
                        document = documents[i]
                        row = (
                            document.timestamp,
                            document.posted_by,
                            document.topic,
                            document.routing_key,
                            document.payload
                        )
                        yield row