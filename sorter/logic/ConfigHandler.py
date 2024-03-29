from typing import Dict
import json
from .BaseComponent import BaseComponent

class ConfigHandler(BaseComponent):
    config: Dict[str, list[str]] = {}

    def get_config(self) -> Dict[str, list[str]]:
        return self.config 
    
    def add_to_config(self, dirname: str, extensions: str) -> Dict[str, list[str]]:
        parsed_extensions: list[str] = self._parse_extensions(extensions)
        self.config[dirname] = parsed_extensions
        return self.config

    def remove_from_config(self, selected_option: str) -> Dict[str, list[str]]:
        selected_item: str = self._parse_directory_name(selected_option)
        self.config.pop(selected_item)
        return self.config

    def read_config(self, path: str) -> Dict[str, list[str]]:
        with open(path) as json_config:
            data = json.load(json_config)
        self.config = data
        return self.config

    def save_config(self, path: str) -> None:
        with open(f"{path}.json", "w") as json_config:
            json.dump(self.config, json_config)

    def _parse_directory_name(self, dir: str) -> str:
        return dir.split(':')[0]
    
    def _parse_extensions(self, extensions: str):
        return extensions.split(';')
    
    def _get_sorting_representation(self) -> Dict[str, str]:
        temp_dict = {}
        for dest, extensions in self.config.items():
            for extension in extensions:
                temp_dict[extension] = dest
        return temp_dict