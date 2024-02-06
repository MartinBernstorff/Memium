import enum
import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from memium.source.document import Document
from memium.source.prompts.prompt import BasePrompt

from ..prompts.prompt_qa import QAPrompt
from .extractor import BasePromptExtractor


class TableParseMode(enum.Enum):
    ASCENDING = "Ascending"
    DESCENDING = "Descending"
    ROWWISE = "Rowwise"


@dataclass(frozen=True)
class ParsedTable:
    rows: list[dict[str, str]]
    mode: TableParseMode
    front: str
    back: str


@dataclass(frozen=True)
class RowPair:
    front: dict[str, str]
    back: dict[str, str]


class TableExtractor(BasePromptExtractor):
    def _parse_table(self, input_str: str) -> Sequence[ParsedTable]:
        if not input_str.startswith("|"):
            return []

        rows: list[dict[str, str]] = []
        parsed_tables: Sequence[ParsedTable] = []
        for n, line in enumerate(input_str.strip().split("\n")):
            data: dict[str, str] = {}
            if n == 0:
                header = [cell.strip() for cell in line.split("|") if cell]
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
                    mode_string: Literal[
                        "Ascending", "Descending", "Rowwise", "Row-wise"
                    ] = metadata[0].strip()  # type: ignore

                    match mode_string:
                        case "Ascending":
                            mode = TableParseMode.ASCENDING
                        case "Descending":
                            mode = TableParseMode.DESCENDING
                        case "Rowwise" | "Row-wise":
                            mode = TableParseMode.ROWWISE

                    parsed_tables.append(
                        ParsedTable(
                            rows=rows,
                            mode=mode,
                            front=metadata[1].strip(),
                            back=metadata[2].strip(),
                        )
                    )
        return parsed_tables

    def _get_row_pair(self, parsed_table: ParsedTable, i: int) -> RowPair:
        match parsed_table.mode:
            case TableParseMode.ASCENDING:
                front_row = parsed_table.rows[-1 - i]
                back_row = parsed_table.rows[-2 - i]
            case TableParseMode.DESCENDING:
                front_row = parsed_table.rows[i]
                back_row = parsed_table.rows[i + 1]
            case TableParseMode.ROWWISE:
                front_row = parsed_table.rows[i]
                back_row = parsed_table.rows[i]

        return RowPair(front_row, back_row)

    def _replace_placeholders(
        self, parsed_table: ParsedTable, row_pair: RowPair
    ) -> tuple[str, str]:
        front_placeholders = re.findall(r"\|(.+?)\|", parsed_table.front)
        back_placeholders = re.findall(r"\|(.+?)\|", parsed_table.back)
        front = parsed_table.front
        back = parsed_table.back

        for placeholder in [*front_placeholders, *back_placeholders]:
            front = front.replace(f"|{placeholder}|", row_pair.front[placeholder])
            back = back.replace(f"|{placeholder}|", row_pair.back[placeholder])

        return front, back

    def _parsed_table_to_prompt(self, parsed_table: ParsedTable) -> Sequence[QAPrompt]:
        prompts: Sequence[QAPrompt] = []
        match parsed_table.mode:
            case TableParseMode.ASCENDING | TableParseMode.DESCENDING:
                break_index = len(parsed_table.rows) - 2
            case TableParseMode.ROWWISE:
                break_index = len(parsed_table.rows) - 1

        for i in range(len(parsed_table.rows)):
            row_pair = self._get_row_pair(parsed_table, i)

            front, back = self._replace_placeholders(parsed_table, row_pair)

            # Skip rows with empty fronts or backs
            if front and back:
                prompts.append(QAPrompt(question=front, answer=back))
            if i == break_index:
                break
        return prompts

    def extract_prompts(self, document: Document) -> Sequence[BasePrompt]:
        blocks = document.content.split("\n\n")
        parsed_tables = [self._parse_table(block) for block in blocks]
        flattened_parsed_tables = [
            parsed_table for sublist in parsed_tables for parsed_table in sublist
        ]
        prompts = [
            self._parsed_table_to_prompt(parsed_table) for parsed_table in flattened_parsed_tables
        ]
        flattened_prompts = [prompt for sublist in prompts for prompt in sublist]
        return flattened_prompts
