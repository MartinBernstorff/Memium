## Recommened setup for the repository
 ### Github Repository Settings
 These are all GitHub settings we recommend enabling, e.g. go to the repository's `Settings > General > Allow auto-merge`.

 * General
   * Pull Requests
     * Always suggest updating pull request branches 
     * Allow auto-merge
     * Automatically delete head branches

 * Branches
   * Add a branch protection rule for "main"
     * Require a pull request before merging
     * Require status checks to pass before merging
       * Require branches to be up to date before merging
       * Status checks that are required:
         * static_type_checks (type hinting)
         * pre-commit (formatting)
         * pytest (tests)
         * check_for_rej (check for residual cruft updates)
     * Require conversation resolution before merging
<!-- {BearID:6950e351a47a064b1c013f1a5b3a1d9f} -->