import json
from collections.abc import Sequence
from dataclasses import dataclass
from time import sleep

import invoke as inv

from .str_parsing import (
    get_letter_alphabet_position,
    get_letter_from_alphabet_position,
)


@dataclass(frozen=True)
class GithubIssue:
    number: int
    title: str


def get_issues_assigned_to_me(c: inv.Context) -> Sequence[GithubIssue] | None:
    """Get issues assigned to current user on current repo"""
    my_issues = c.run(
        "gh issue list --assignee='@me' --json number,title", hide=True
    )
    if my_issues is None:
        return None

    output = my_issues.stdout
    parsed_output = [GithubIssue(**value) for value in json.loads(output)]
    return parsed_output


def issue_dialog(my_issues: Sequence[GithubIssue]) -> int:
    issue_strings = [
        f"[{get_letter_from_alphabet_position(i+1)}] #{issue.number} {issue.title}"
        for i, issue in enumerate(my_issues)
    ]

    n_issues = len(my_issues)
    if n_issues == 1:
        print(f"Only one issue found, selecting:\n\t{issue_strings[0]}\nin ")
        for i in range(3, 0, -1):
            print(f"{i}...")
            sleep(1)
        return 0

    terminal_output = "\n".join(issue_strings)
    print(f"\n{terminal_output}\n")

    first_issue_letter = get_letter_from_alphabet_position(1)
    last_issue_letter = get_letter_from_alphabet_position(n_issues)
    issue_index = get_letter_alphabet_position(
        input(
            f"Which issue do you want to work on? [{first_issue_letter}-{last_issue_letter}]\n"
        )
    )

    return issue_index


def sanitise_issue_title(issue_title: str) -> str:
    characters_to_replace = [" ", ":", ",", "'", '"', "(", ")", "[", "]", "`"]

    for character in characters_to_replace:
        issue_title = issue_title.replace(character, "-")

    issue_title = issue_title.replace("--", "-")
    return issue_title
