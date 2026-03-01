from abc import ABC, abstractmethod
from typing import Any, Union, Protocol, Dict, List


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage():
    def process(self, data: Any) -> Dict:
        pass


class TransformStage():
    def process(self, data: Any) -> Dict:
        pass


class OutputStage():
    def process(self, data: Any) -> str:
        pass


class ProcessingPipeline(ABC):
    def __init__(self, stages: List[ProcessingStage]) -> None:
        self.stages = stages

    def add_stage():
        pass

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter():
    def __init__(self, pipeline_id):
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        pass


class CSVAdapter():
    def __init__(self, pipeline_id):
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        pass


class StreamAdapter():
    def __init__(self, pipeline_id):
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        pass


class NexusManager():
    def __init__(self, pipelines: List[ProcessingPipeline]) -> None:
        self.pipelines = pipelines

    def add_pipeline():
        pass

    def process(self, data: Any) -> Union[str, Any]:
        pass


if __name__ == '__main__':
    pass
