from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):

    def __init__(self, id: str) -> None:
        self.id = id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        else:
            new_data = [i for i in data_batch if criteria in str(i)]
            return new_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "items_processed": self.processed_count,
            "status": "active"
        }


class SensorStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        temperatures = []
        for item in data_batch:
            if 'temp' in item:
                temperatures.append(item['temp'])

        count = len(data_batch)
        average = sum(temperatures) / len(temperatures)
        return f"{count} readings processed, avg temp: {average}°C"

    def simple_summary(self, data_batch: List[Any]) -> str:
        count = len(data_batch)
        return f"{count} readings processed"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high-priority":
            return [item for item in data_batch
                    if isinstance(item, dict)
                    and item.get('status') == 'high-priority']
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        buys = []
        sells = []
        for item in data_batch:
            if 'buy' in item:
                buys.append(item['buy'])
            elif 'sell' in item:
                sells.append(item['sell'])
        count = len(data_batch)
        buys_total = sum(buys)
        sells_total = sum(sells)

        net_total = buys_total - sells_total
        if net_total > 0:
            return f"{count} operations, net flow: +{net_total} units"
        else:
            return f"{count} operations, net flow: {net_total} units"

    def simple_summary(self, data_batch: List[Any]) -> str:
        count = len(data_batch)
        return f"{count} operations processed"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large":
            large_limit = 100
            return [
                item for item in data_batch
                if isinstance(item, dict)
                and (item.get('buy', 0) > large_limit
                     or item.get('sell', 0) > large_limit)
            ]
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        count = len(data_batch)
        error = [e for e in data_batch if e == 'error']

        return f"Event analysis: {count} events, {len(error)} error detected"

    def simple_summary(self, data_batch: List[Any]) -> str:
        count = len(data_batch)
        return f"{count} events processed"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high-priority":
            return [e for e in data_batch if 'error' in str(e).lower()]
        return super().filter_data(data_batch, criteria)


if __name__ == '__main__':
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    data = [{'temp': 22.5}, {'humidity': 65}, {'pressure': 1013}]
    format = [f"{key}:{value}" for item in data for key, value in item.items()]
    output = ", ".join(format)

    print(f"Stream ID: {sensor.id}, Type: Environmental Data")
    print(f"Processing sensor batch: [{output}]")

    result = sensor.process_batch(data)
    print(f"Sensor analysis: {result}")

    print()

    print("Initializing Transaction Stream...")

    trans = TransactionStream("TRANS_001")
    data = [{'buy': 100}, {'sell': 150}, {'buy': 75}]
    format = [f"{key}:{value}" for item in data for key, value in item.items()]
    output = ", ".join(format)

    print(f"Stream ID: {trans.id}, Type: Financial Data")
    print(f"Processing transaction batch: [{output}]")

    result = trans.process_batch(data)
    print(f"Transaction analysis: {result}")

    print()

    print("Initializing Event Stream...")

    even = EventStream("EVENT_001")
    data = ['login', 'error', 'logout']
    format = [f"{key}" for key in data]
    output = ", ".join(format)

    print(f"Stream ID: {even.id}, Type: System Events")
    print(f"Processing event batch: [{output}]")

    result = even.process_batch(data)
    print(f"Event analysis: {result}")

    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    print("Batch 1 Results:")
    streams = [
        (SensorStream("Sensor001"),
         [{'temp': 22.5}, {'humidity': 65}], "Sensor"),
        (TransactionStream("Trans001"),
         [{'buy': 100}, {'sell': 150}, {'buy': 75}, {'buy': 45}],
         "Transaction"),
        (EventStream("Even001"), ['login', 'error', 'logout'], "Event")
    ]

    for stream, data, name in streams:
        result = stream.simple_summary(data)
        print(f"- {name} data: {result}")

    print("\nStream filtering active: High-priority data only")

    sensor_data = [{'temp': 45.0, 'status': 'high-priority'},
                   {'temp': 31.0},
                   {'temp': 38.5, 'status': 'high-priority'}]

    trans_data = [{'buy': 110}, {'buy': 10}, {'sell': 5}]

    filtered_sensors = SensorStream("S1").filter_data(
        sensor_data, criteria="high-priority"
        )

    filtered_trans = TransactionStream("T1").filter_data(trans_data, "large")

    print(f"Filtered results: {len(filtered_sensors)} critical sensor "
          f"alerts, {len(filtered_trans)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
