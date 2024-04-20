from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class LineBlock:
    starting_line: int
    lines: Sequence[str]

    @property
    def content(self) -> str:
        return "\n".join(self.lines)

    @property
    def end_line(self) -> int:
        return self.starting_line + len(self.lines) - 1


def to_line_blocks(content: str) -> Sequence[LineBlock]:
    lines = content.split("\n")

    line_blocks: list[LineBlock] = []
    cur_lines: Sequence[str] = []

    cur_starting_line = 0
    for i, line in enumerate(lines):
        cur_is_newline = line == ""  # Since we split on \n, we can check for empty lines
        if cur_is_newline:
            line_blocks.append(LineBlock(starting_line=cur_starting_line, lines=cur_lines))
            cur_starting_line = i + 1
            cur_lines = []
        else:
            cur_lines.append(line)

        final_line = i == len(lines) - 1
        if final_line:
            line_blocks.append(LineBlock(starting_line=cur_starting_line, lines=cur_lines))

    return line_blocks
