import re
from typing import Any

import misaka


def field_to_html(field: Any) -> str:
    # Math processing
    """
    Need to extract the math in brackets so that it doesn't get markdowned.
    If math is separated with dollar sign it is converted to brackets.
    """
    for bracket in ["(", ")", "[", "]"]:
        field = field.replace(rf"\{bracket}", rf"\\{bracket}")
        # backslashes, man.

    for token in ["*", "/"]:
        if token == "/":
            replacement = "*"
        elif token == "*":
            replacement = "**"

        pattern = f"\\{token}[^<>\\-\n]+\\{token}"

        token_instances = re.findall(pattern, field)

        for instance in token_instances:
            field = field.replace(
                instance,
                replacement + instance[1:-1] + replacement,  # type: ignore
            )  # type: ignore

    # Make sure every \n converts into a newline
    field = field.replace("\n", "  \n")

    return misaka.html(field, extensions=("fenced-code", "math"))  # type: ignore


def compile_field(fieldtext: str) -> str:
    """Turn source markdown into an HTML field suitable for Anki."""
    fieldtext_sans_wiki = fieldtext.replace("[[", "<u>").replace(
        "]]", "</u>"
    )
    fieldtext_sans_comments = re.sub(
        r"<!--.+-->", "", fieldtext_sans_wiki
    )

    return field_to_html(fieldtext_sans_comments)
