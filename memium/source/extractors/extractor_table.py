import enum
import re
from collections.abc import Sequence
from dataclasses import dataclass

from memium.source.document import Document
from memium.source.extractors.to_line_blocks import LineBlock, to_line_blocks

from ..prompt import QAPrompt, QAWithDoc
from .extractor import BasePromptExtractor


class TableParseMode(enum.Enum):
    ASCENDING = "Ascending"
    DESCENDING = "Descending"
    ROWWISE = "Rowwise"
    ROWWISE_ALL = "Rowwise-all"

    @staticmethod
    def sanitize_mode_string(mode_string: str) -> str:
        return mode_string.lower().replace("-", "").strip()

    @staticmethod
    def from_str(val: str) -> "TableParseMode":
        for mode in TableParseMode:
            if TableParseMode.sanitize_mode_string(
                mode.value
            ) == TableParseMode.sanitize_mode_string(val):
                return mode
        raise ValueError(f"Invalid TableParseMode value: {val}")


@dataclass(frozen=True)
class ParsedTable:
    rows: list[dict[str, str]]
    mode: TableParseMode
    front_template: str
    back_template: str
    end_line_nr: int


@dataclass(frozen=True)
class RowPair:
    front: dict[str, str]
    back: dict[str, str]


@dataclass(frozen=True)
class FrontBack:
    front: str
    back: str


def rowwise_all_prompts(parsed_table: ParsedTable, doc: Document) -> Sequence[QAWithDoc]:
    values = [
        TableExtractor.replace_placeholders(parsed_table, RowPair(row, row))
        for row in parsed_table.rows
    ]

    if len(values) == 0:
        return []

    # If there is at least one value, then we can be sure that the first one is not None
    question: str = values[0].front  # pyright: ignore[reportOptionalMemberAccess] # ty:ignore[possibly-missing-attribute]

    front = question + "\n\n" + "\n".join(f"{i + 1}. ?" for i, vb in enumerate(values) if vb)
    back = "\n".join(f"{i + 1}. {vb.back}" for i, vb in enumerate(values) if vb)
    return [
        QAWithDoc(
            prompt=QAPrompt(question=front, answer=back),
            parent_doc=doc,
            line_nr=parsed_table.end_line_nr,
        )
    ]


class TableExtractor(BasePromptExtractor):
    def _parse_table(self, block: LineBlock) -> Sequence[ParsedTable]:
        if not block.content.startswith("|"):
            return []

        rows: list[dict[str, str]] = []
        parsed_tables: Sequence[ParsedTable] = []
        for n, line in enumerate(block.content.strip().split("\n")):
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

                    parsed_tables.append(
                        ParsedTable(
                            rows=rows,
                            mode=TableParseMode.from_str(metadata[0]),
                            front_template=metadata[1].strip(),
                            back_template=metadata[2].strip(),
                            end_line_nr=block.end_line,
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
            case TableParseMode.ROWWISE_ALL:
                raise ValueError("ROWWISE_ALL mode should be handled separately.")

        return RowPair(front_row, back_row)

    @staticmethod
    def replace_placeholders(parsed_table: ParsedTable, row_pair: RowPair) -> FrontBack | None:
        def replace_template(template: str, data: dict[str, str]) -> str | None:
            """Replace placeholders in a template string using provided data."""
            result = template
            placeholders = re.findall(r"\|(.+?)\|", template)

            for placeholder in placeholders:
                replacement = data.get(placeholder, "")
                if not replacement:
                    return None
                result = result.replace(f"|{placeholder}|", replacement)

            return result

        # Process front and back sides
        processed_front = replace_template(parsed_table.front_template, row_pair.front)
        if processed_front is None:
            return None

        processed_back = replace_template(parsed_table.back_template, row_pair.back)
        if processed_back is None:
            return None

        return FrontBack(front=processed_front, back=processed_back)

    def _parsed_table_to_prompt(
        self, parsed_table: ParsedTable, doc: Document
    ) -> Sequence[QAWithDoc]:
        prompts: Sequence[QAWithDoc] = []
        match parsed_table.mode:
            case TableParseMode.ASCENDING | TableParseMode.DESCENDING:
                break_index = len(parsed_table.rows) - 2
            case TableParseMode.ROWWISE:
                break_index = len(parsed_table.rows) - 1
            case TableParseMode.ROWWISE_ALL:
                return rowwise_all_prompts(parsed_table, doc)

        for i in range(len(parsed_table.rows)):
            row_pair = self._get_row_pair(parsed_table, i)

            card = TableExtractor.replace_placeholders(parsed_table, row_pair)

            # Skip rows with empty fronts or backs
            if card:
                prompts.append(
                    QAWithDoc(
                        prompt=QAPrompt(question=card.front, answer=card.back),
                        parent_doc=doc,
                        line_nr=parsed_table.end_line_nr,
                    )
                )
            if i == break_index:
                break
        return prompts

    def extract_prompts(self, document: Document) -> Sequence[QAWithDoc]:
        blocks = to_line_blocks(document.content)

        parsed_tables = [self._parse_table(block) for block in blocks]
        flattened_parsed_tables = [
            parsed_table for sublist in parsed_tables for parsed_table in sublist
        ]
        prompts = [
            self._parsed_table_to_prompt(parsed_table, document)
            for parsed_table in flattened_parsed_tables
        ]
        flattened_prompts = [prompt for sublist in prompts for prompt in sublist]
        return flattened_prompts
