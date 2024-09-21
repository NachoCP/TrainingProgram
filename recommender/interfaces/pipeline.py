from abc import ABC, abstractmethod
from typing import Any


class IPipeline(ABC):
    """
    Abstract base class for a data pipeline with extract, transform, load, and run steps.
    """

    @abstractmethod
    def extract(self, path, **kwargs) -> Any:
        """
        Extract data from a source.
        :return: The extracted data.
        """
        pass

    @abstractmethod
    def transform(self, data: Any, **kwargs) -> Any:
        """
        Transform the extracted data.
        :param data: The data to be transformed.
        :return: The transformed data.
        """
        pass

    @abstractmethod
    def load(self, data: Any, **kwargs) -> None:
        """
        Load the transformed data into a destination.
        :param data: The data to be loaded.
        """
        pass

    def run(self, **kwargs) -> None:
        """
        Run the pipeline by orchestrating the extract, transform, and load steps.
        """

        data = self.extract(**kwargs)
        transformed_data = self.transform(data, **kwargs)
        self.load(transformed_data, **kwargs)
