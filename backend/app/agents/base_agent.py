from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseAgent(ABC):
    name: str


    
    @abstractmethod
    def execute(self, context: Dict[str, Any]):
        pass
