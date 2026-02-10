from typing import Protocol, Any, List
from abc import ABC, abstractmethod


class Transformer(Protocol):
    def transform(self, content: str) -> str:
        ...


class UppercaseTransformer:
    def transform(self, content: str) -> str:
        upperc = content.upper()
        return upperc


class LowercaseTransformer:
    def transform(self, content: str) -> str:
        lowerc = content.lower()
        return lowerc


class ReverseTransformer:
    def transform(self, content: str) -> str:
        rev = content[::-1]
        return rev


class TransformationPipeline(ABC):
    def __init__(self):
        self.transformers: List[Transformer] = []

    def add_transformer(self, data: Transformer) -> 'TransformationPipeline':
        self.transformers.append(data)
        return self

    @abstractmethod
    def process(self, content: str) -> str:
        pass

    def execute(self, content: str) -> str:
        result = content
        for trans in self.transformers:
            result = trans.transform(result)
        return self.process(result)


class MarkdownPipeline(TransformationPipeline):
    def __init__(self):
        super().__init__()

    def process(self, content: str) -> str:
        return f"# Markdown: {content}"


class HTMLPipeline(TransformationPipeline):
    def __init__(self):
        super().__init__()

    def process(self, content: str) -> str:
        return f"<html>{content}</html>"


class PipelineManager:
    def __init__(self):
        self.pipelines: List[TransformationPipeline] = []

    def add_pipeline(self, data: TransformationPipeline) -> 'PipelineManager':
        self.pipelines.append(data)
        return self

    def process_all(self, content: str) -> List[str]:
        results = []
        for pipes in self.pipelines:
            result = pipes.execute(content)
            results.append(result)
        return results


if __name__ == '__main__':

    mark = (MarkdownPipeline()
            .add_transformer(UppercaseTransformer()))
    htm = (HTMLPipeline().add_transformer(LowercaseTransformer()))

    pipeline = (PipelineManager()
                .add_pipeline(mark)
                .add_pipeline(htm))

    result = pipeline.process_all("HELLO")
    print(result)

