from typing import Dict
from itertools import islice

class ConfigHandler:
    config: Dict[str, list[str]] = {}

    def add_to_config(self, dirname: str, extensions: str) -> Dict[str, list[str]]:
        parsed_extensions: list[str] = self._parse_extensions(extensions)
        self.config[dirname] = parsed_extensions
        print(self.config)
        return self.config

    def remove_from_config(self, index: int) -> Dict[str, list[str]]:
        del self.config[next(islice(self.config, index, None))]
        print(self.config)
        return self.config

    def _parse_extensions(self, extensions: str):
        return extensions.split(';')

    @staticmethod
    def read_config() -> None:
        print("dupa")

    @staticmethod
    def save_config() -> None:
        pass