import invoke as inv

from ..tasks import (
    create_branch_from_issue,
    get_issues_assigned_to_me,
    issue_dialog,
)


@inv.task(aliases=("new",))  # type: ignore
def new_branch_from_issue(c: inv.Context):
    my_issues = get_issues_assigned_to_me(c)

    if my_issues is None:
        print("No issues found")
        return

    selected_issue_index = issue_dialog(my_issues)
    c.run("git checkout main")
    c.run("git pull")
    create_branch_from_issue(
        c=c, selected_issue=my_issues[selected_issue_index]
    )
