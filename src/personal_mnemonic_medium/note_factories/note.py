import datetime
import re
from pathlib import Path


class Document:
    def __init__(
        self, title: str, content: str, uuid: str, source_path: Path
    ):
        self.title = title
        self.uuid = uuid
        self.content = self.replace_alias_wiki_links(content)
        self.source_path = source_path

        import_time_formatted = datetime.datetime.now().strftime(
            "%Y-%m-%d"
        )

        self.tags = self.get_tags(
            self.content, import_time=import_time_formatted
        )

    @staticmethod
    def replace_alias_wiki_links(text: str) -> str:
        tokens_in_link = r"[\w|\s|\d|\(|\)\-]"
        regex_pattern = (
            rf"\[\[{tokens_in_link}+\|{tokens_in_link}+\]\]"
        )
        pattern_matches = re.findall(
            pattern=regex_pattern, string=text, flags=re.DOTALL
        )

        for match in pattern_matches:
            link_name = (
                re.findall(
                    pattern=rf"\|{tokens_in_link}+\]\]", string=match
                )[0]
                .replace("|", "")
                .replace("]", "")
            )

            replacement_str = f"[[{link_name}]]"
            text = text.replace(match, replacement_str)

        return text

    def get_tags(self, input_str: str, import_time: str) -> list[str]:
        file_tags = [import_time]

        if self.has_supplementary_tags(input_str):
            for tag in re.findall(r"#anki\/tag\/\S+", input_str):
                file_tags.append(tag[10:])

        return file_tags

    @staticmethod
    def has_supplementary_tags(input_str: str) -> bool:
        return len(re.findall(r"#anki\/tag\/\S+", input_str)) != 0
