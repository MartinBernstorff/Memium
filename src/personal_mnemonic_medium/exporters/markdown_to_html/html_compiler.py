import re
from typing import Any

import misaka
from personal_mnemonic_medium.exporters.anki.globals import CONFIG


def field_to_html(field: Any) -> str:
    # Math processing
    """
    Need to extract the math in brackets so that it doesn't get markdowned.
    If math is separated with dollar sign it is converted to brackets.
    """
    if CONFIG["dollar"]:
        for sep, (op, cl) in [
            ("$$", (r"\\[", r"\\]")),
            ("$", (r"\\(", r"\\)")),
        ]:
            escaped_sep = sep.replace(r"$", r"\$")
            # ignore escaped dollar signs when splitting the field
            field = re.split(rf"(?<!\\){escaped_sep}", field)
            # add op(en) and cl(osing) brackets to every second element of the list
            field[1::2] = [op + e + cl for e in field[1::2]]
            field = "".join(field)
    else:
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
