import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from memium.source.document import Document
from memium.source.prompts.prompt import BasePrompt

from ..prompts.prompt_qa import QAPrompt
from .extractor import BasePromptExtractor


@dataclass(frozen=True)
class ParsedTable:
    rows: list[dict[str, str]]
    mode: Literal["Ascending", "Descending", "Rowwise"]
    front: str
    back: str


class TableExtractor(BasePromptExtractor):
    def _parse_table(self, input_str: str) -> Sequence[ParsedTable]:
        if not input_str.startswith("|"):
            return []

        rows: list[dict[str, str]] = []
        parsed_tables: Sequence[ParsedTable] = []
        for n, line in enumerate(input_str[1:-1].split("\n")):
            data: dict[str, str] = {}
            if n == 0:
                header = [
                    cell.strip() for cell in line.strip().split("|") if cell
                ]
            if n > 1:
                # Is a row
                if line.startswith("|"):
                    values = [cell.strip() for cell in line.split("|") if cell]
                    for col, value in zip(header, values, strict=False):  # type: ignore
                        data[col] = value
                    rows.append(data)
                # Is description
                elif "//" in line:
                    metadata = line.split("//")
                    parsed_tables.append(
                        ParsedTable(
                            rows=rows,
                            mode=metadata[0].strip(),  # type: ignore
                            front=metadata[1].strip(),  # type: ignore
                            back=metadata[2].strip(),  # type: ignore
                        )
                    )
        return parsed_tables

    def parsed_table_to_prompt(
        self, parsed_table: ParsedTable
    ) -> Sequence[QAPrompt]:
        prompts: Sequence[QAPrompt] = []
        for i in range(len(parsed_table.rows)):
            match parsed_table.mode:
                case "Ascending":
                    front_row = parsed_table.rows[-1 - i]
                    back_row = parsed_table.rows[-2 - i]
                    break_index = len(parsed_table.rows) - 2
                case "Descending":
                    front_row = parsed_table.rows[i]
                    back_row = parsed_table.rows[i + 1]
                    break_index = len(parsed_table.rows) - 2
                case "Rowwise":
                    front_row = parsed_table.rows[i]
                    back_row = parsed_table.rows[i]
                    break_index = len(parsed_table.rows) - 1

            front_placeholders = re.findall(r"\|(.+?)\|", parsed_table.front)
            back_placeholders = re.findall(r"\|(.+?)\|", parsed_table.back)
            front = parsed_table.front
            back = parsed_table.back

            for placeholder in [*front_placeholders, *back_placeholders]:
                front = front.replace(
                    f"|{placeholder}|", front_row[placeholder]
                )
                back = back.replace(f"|{placeholder}|", back_row[placeholder])
            prompts.append(QAPrompt(question=front, answer=back))
            if i == break_index:
                break
        return prompts

    def extract_prompts(self, document: Document) -> Sequence[BasePrompt]:
        blocks = document.content.split("\n\n")
        parsed_tables = [self._parse_table(block) for block in blocks]
        flattened_parsed_tables = [
            parsed_table
            for sublist in parsed_tables
            for parsed_table in sublist
        ]
        prompts = [
            self.parsed_table_to_prompt(parsed_table)
            for parsed_table in flattened_parsed_tables
        ]
        flattened_prompts = [
            prompt for sublist in prompts for prompt in sublist
        ]
        return flattened_prompts
