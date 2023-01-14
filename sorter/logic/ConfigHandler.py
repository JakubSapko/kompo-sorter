from typing import Dict

class ConfigHandler:
    config: Dict[str, list[str]] = {}

    def add_to_config(self, dirname: str, extensions: str) -> None:
        parsed_extensions: list[str] = self._parse_extensions(extensions)
        self.config[dirname] = parsed_extensions
        return self.config
        
    def _parse_extensions(self, extensions: str):
        return extensions.split(';')

    @staticmethod
    def read_config() -> None:
        print("dupa")

    @staticmethod
    def save_config() -> None:
        pass