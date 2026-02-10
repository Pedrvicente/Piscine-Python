from typing import Protocol, Any, List
from abc import ABC, abstractmethod


class NotificationChannel(Protocol):
    def send(self, message: str) -> str:
        ...


class EmailChannel:
    def send(self, message: str) -> str:
        return f"[EMAIL] {message}"


class SmsChannel:
    def send(self, message: str) -> str:
        return f"[SMS] {message}"


class PushChannel:
    def send(self, message: str) -> str:
        return f"[PUSH] {message}"


class NotificationPipeline(ABC):
    def __init__(self):
        self.channels: List[NotificationChannel] = []

    def add_channel(self, channel: NotificationChannel) -> 'NotificationPipeline':
        self.channels.append(channel)
        return self
    
    @abstractmethod
    def process(self, message: str) -> str:
        pass

    def send_to_all(self, message: str) -> List[str]:
        processed = self.process(message)
        results = [channel.send(processed) for channel in self.channels]
        return results


class UrgentNotification(NotificationPipeline):
    def __init__(self, priority: str):
        super().__init__()
        self.priority = priority

    def process(self, message: str) -> str:
        return f"[URGENT] {message}"


class NormalNotification(NotificationPipeline):
    def __init__(self, priority: str):
        super().__init__()
        self.priority = priority

    def process(self, message: str) -> str:
        return f"[NORMAL] {message}"
    

class NotificationManager:
    def __init__(self):
        self.pipelines: List[NotificationPipeline] = []

    def add_pipeline(self, pipeline: NotificationPipeline) -> 'NotificationManager':
        self.pipelines.append(pipeline)
        return self

    def broadcast(self, message: str) -> List[List[str]]:
        return [pipeline.send_to_all(message) for pipeline in self.pipelines]

if __name__ == '__main__':

    pipeline = (UrgentNotification("high").add_channel(EmailChannel()).add_channel(SmsChannel()).add_channel(PushChannel()))
    
    result = pipeline.send_to_all("server down")
    for r in result:
        print(r)

