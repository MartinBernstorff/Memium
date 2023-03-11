import datetime
import re
from pathlib import Path
from typing import List


class Document:
    def __init__(
        self,
        title: str,
        content: str,
        uuid: str,
        source_path: Path,
    ):
        self.title = title
        self.uuid = uuid
        self.content = content
        self.source_path = source_path

        import_time_formatted = datetime.datetime.now().strftime("%Y-%m-%d")

        self.tags = self.get_tags(self.content, import_time=import_time_formatted)

    def get_tags(self, input_str: str, import_time: str) -> List[str]:
        file_tags = [import_time]

        if self.has_supplementary_tags(input_str):
            for tag in re.findall(r"#anki\/tag\/\S+", input_str):
                file_tags.append(tag[10:])

        return file_tags

    @staticmethod
    def has_supplementary_tags(input_str: str) -> bool:
        return len(re.findall(r"#anki\/tag\/\S+", input_str)) != 0
