import invoke as inv

from .github import GithubIssue, sanitise_issue_title


@inv.task(aliases=("submit",))  # type: ignore
def submit_pr(c: inv.Context):
    c.run("gt sync --delete --force")
    c.run("gt submit --stack --restack -m --no-edit")
    c.run("gt log -s")


def create_branch_from_issue(c: inv.Context, selected_issue: GithubIssue):
    sanitised_title = sanitise_issue_title(selected_issue.title)
    branch_title = f"{selected_issue.number}-{sanitised_title}"
    c.run(f"gt create {branch_title}")
    c.run(f"git commit --allow-empty -m '{selected_issue.title}'")
    c.run(f"git commit --allow-empty -m 'Fixes #{selected_issue.number}'")
