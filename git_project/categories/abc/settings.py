import json
from typing import Tuple, List, Dict
from dataclasses import dataclass, asdict


@dataclass
class Settings:
    def __init__(self, **data: Dict[str, str]) -> None:
        for k, v in data.items():
            if v:
                v_data = json.loads(v)
                setattr(self, k, v_data)

    def as_config_section(self) -> List[Tuple[str, str]]:
        return [(k, json.dumps(v)) for k, v in asdict(self).items()]
