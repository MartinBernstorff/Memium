import invoke as inv

from .github import GithubIssue, sanitise_issue_title


@inv.task(aliases=("submit",))  # type: ignore
def submit_pr(c: inv.Context):
    c.run("gt submit --restack --stack --no-edit --publish --merge-when-ready")
    c.run("gt log short")


def create_branch_from_issue(c: inv.Context, selected_issue: GithubIssue):
    sanitised_title = sanitise_issue_title(selected_issue.title)
    branch_title = f"{selected_issue.number}-{sanitised_title}"
    first_commit_str = f"$'{selected_issue.title}\n\nFixes #{selected_issue.number}'"
    c.run(f"gt create {branch_title} --all -m {first_commit_str}")
    c.run(f"git commit --allow-empty -m {first_commit_str}")
