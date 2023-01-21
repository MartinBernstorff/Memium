import datetime
import re
from typing import List


class Note:
    def __init__(self, title: str, content: str, uuid: str):
        self.title = title
        self.uuid = uuid
        self.content = content

        if self.has_subdeck_tag(self.content):
            self.subdeck = self.get_subdeck_name(self.content)
        else:
            self.subdeck = "Default"

        import_time_formatted = datetime.datetime.now().strftime("%Y-%m-%d")

        self.tags = self.get_tags(self.content, import_time=import_time_formatted)

    @staticmethod
    def has_subdeck_tag(input_str) -> bool:
        return len(re.findall(r"#anki\/deck\/\S+", input_str)) != 0

    @staticmethod
    def get_subdeck_name(input_str) -> str:
        return (
            re.findall(r"#anki\/deck\/\S+", input_str)[0][11:]
            .replace("/", "::")
            .replace("#", "")
        )

    def get_tags(self, input_str, import_time) -> List[str]:
        file_tags = [import_time]

        if self.has_supplementary_tags(input_str):
            for tag in re.findall(r"#anki\/tag\/\S+", input_str):
                file_tags.append(tag[10:])

        return file_tags

    @staticmethod
    def has_supplementary_tags(input_str: str) -> bool:
        return len(re.findall(r"#anki\/tag\/\S+", input_str)) != 0
