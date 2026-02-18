from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria is None:
                return data_batch
            new_data = [i for i in data_batch if criteria in str(i)]
            return new_data
        except Exception:
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "items_processed": self.processed_count,
            "status": "active"
        }


class SensorStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temperatures = []
            for item in data_batch:
                if isinstance(item, dict) and 'temp' in item:
                    temperatures.append(item['temp'])

            self.processed_count += len(data_batch)
            count = len(data_batch)

            if temperatures:
                average = sum(temperatures) / len(temperatures)
                return f"{count} readings processed, avg temp: {average}°C"
            return f"{count} readings processed"
        except ZeroDivisionError:
            return "Error: No temperature data"
        except TypeError:
            return "Error: Invalid sensor data format"
        except Exception as e:
            return f"Error: {e}"

    def simple_summary(self, data_batch: List[Any]) -> str:
        count = len(data_batch)
        return f"{count} readings processed"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria == "high-priority":
                return [item for item in data_batch
                        if isinstance(item, dict)
                        and item.get('status') == 'high-priority']
            return super().filter_data(data_batch, criteria)
        except Exception:
            return []


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            buys = []
            sells = []
            for item in data_batch:
                if isinstance(item, dict):
                    if 'buy' in item:
                        buys.append(item['buy'])
                    elif 'sell' in item:
                        sells.append(item['sell'])

            self.processed_count += len(data_batch)
            count = len(data_batch)
            buys_total = sum(buys)
            sells_total = sum(sells)
            net_total = buys_total - sells_total

            if net_total > 0:
                return f"{count} operations, net flow: +{net_total} units"
            return f"{count} operations, net flow: {net_total} units"
        except TypeError:
            return "Error: Invalid data format"
        except Exception as e:
            return f"Error: {e}"

    def simple_summary(self, data_batch: List[Any]) -> str:
        count = len(data_batch)
        return f"{count} operations processed"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria == "large":
                large_limit = 100
                return [
                    item for item in data_batch
                    if isinstance(item, dict)
                    and (item.get('buy', 0) > large_limit
                         or item.get('sell', 0) > large_limit)
                ]
            return super().filter_data(data_batch, criteria)
        except Exception:
            return []


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed_count += len(data_batch)
            count = len(data_batch)
            error = [e for e in data_batch if e == 'error']

            return (f"Event analysis: {count} events, "
                    f"{len(error)} error detected")
        except Exception as e:
            return f"Error: {e}"

    def simple_summary(self, data_batch: List[Any]) -> str:
        count = len(data_batch)
        return f"{count} events processed"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria == "high-priority":
                return [e for e in data_batch if 'error' in str(e).lower()]
            return super().filter_data(data_batch, criteria)
        except Exception:
            return []


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        try:
            if isinstance(stream, DataStream):
                self.streams.append(stream)
        except Exception:
            pass

    def process_all(self, data_map: Dict[str, List[Any]]) -> List[str]:
        results = []
        try:
            for stream in self.streams:
                if stream.stream_id in data_map:
                    result = stream.process_batch(data_map[stream.stream_id])
                    results.append(result)
        except Exception:
            pass
        return results

    def process_summaries(self, data_map: Dict[str, List[Any]]) -> List[str]:
        results = []
        try:
            for stream in self.streams:
                if stream.stream_id in data_map:
                    data = data_map[stream.stream_id]
                    result = stream.simple_summary(data)
                    results.append(result)
        except Exception:
            pass
        return results

    def get_all_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        return [stream.get_stats() for stream in self.streams]


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    sensor_data = [{'temp': 22.5}, {'humidity': 65}, {'pressure': 1013}]
    fmt = [f"{key}:{value}" for item in sensor_data
           for key, value in item.items()]
    output = ", ".join(fmt)

    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    print(f"Processing sensor batch: [{output}]")
    result = sensor.process_batch(sensor_data)
    print(f"Sensor analysis: {result}")

    print()

    print("Initializing Transaction Stream...")

    trans = TransactionStream("TRANS_001")
    trans_data = [{'buy': 100}, {'sell': 150}, {'buy': 75}]
    fmt = [f"{key}:{value}" for item in trans_data
           for key, value in item.items()]
    output = ", ".join(fmt)

    print(f"Stream ID: {trans.stream_id}, Type: Financial Data")
    print(f"Processing transaction batch: [{output}]")
    result = trans.process_batch(trans_data)
    print(f"Transaction analysis: {result}")

    print()

    print("Initializing Event Stream...")

    even = EventStream("EVENT_001")
    even_data = ['login', 'error', 'logout']
    fmt = [f"{key}" for key in even_data]
    output = ", ".join(fmt)

    print(f"Stream ID: {even.stream_id}, Type: System Events")
    print(f"Processing event batch: [{output}]")
    result = even.process_batch(even_data)
    print(f"Event analysis: {result}")

    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_BATCH"))
    processor.add_stream(TransactionStream("TRANS_BATCH"))
    processor.add_stream(EventStream("EVENT_BATCH"))

    batch_data: Dict[str, List[Any]] = {
        "SENSOR_BATCH": [{'temp': 22.5}, {'humidity': 65}],
        "TRANS_BATCH": [{'buy': 100}, {'sell': 150}, {'buy': 75}, {'buy': 45}],
        "EVENT_BATCH": ['login', 'error', 'logout']
    }

    result = processor.process_summaries(batch_data)
    names = ["Sensor", "Transaction", "Event"]

    print("Batch 1 Results:")
    for name, result in zip(names, result):
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


if __name__ == '__main__':
    main()
