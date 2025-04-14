# CHANGELOG


## v0.30.1 (2025-04-14)

### Bug Fixes

- **deps**: Update dependency sentry-sdk to v2.26.0
  ([#858](https://github.com/MartinBernstorff/Memium/pull/858),
  [`692af80`](https://github.com/MartinBernstorff/Memium/commit/692af80ce267ac656dcdf8287345eb4378948e03))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [sentry-sdk](https://redirect.github.com/getsentry/sentry-python)
  ([changelog](https://redirect.github.com/getsentry/sentry-python/blob/master/CHANGELOG.md)) |
  `==2.25.1` -> `==2.26.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/sentry-sdk/2.26.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/sentry-sdk/2.26.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/sentry-sdk/2.25.1/2.26.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/sentry-sdk/2.25.1/2.26.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>getsentry/sentry-python (sentry-sdk)</summary>

### [`v2.26.0`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2260)

[Compare Source](https://redirect.github.com/getsentry/sentry-python/compare/2.25.1...2.26.0)

##### Various fixes & improvements

- fix(debug): Do not consider parent loggers for debug logging
  ([#&#8203;4286](https://redirect.github.com/getsentry/sentry-python/issues/4286)) by
  [@&#8203;szokeasaurusrex](https://redirect.github.com/szokeasaurusrex) - test(tracing): Simplify
  static/classmethod tracing tests
  ([#&#8203;4278](https://redirect.github.com/getsentry/sentry-python/issues/4278)) by
  [@&#8203;szokeasaurusrex](https://redirect.github.com/szokeasaurusrex) - feat(transport): Add a
  timeout ([#&#8203;4252](https://redirect.github.com/getsentry/sentry-python/issues/4252)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - meta: Change CODEOWNERS back to
  Python SDK owners
  ([#&#8203;4269](https://redirect.github.com/getsentry/sentry-python/issues/4269)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - feat(logs): Add sdk name and
  version as log attributes
  ([#&#8203;4262](https://redirect.github.com/getsentry/sentry-python/issues/4262)) by
  [@&#8203;AbhiPrasad](https://redirect.github.com/AbhiPrasad) - feat(logs): Add server.address to
  logs ([#&#8203;4257](https://redirect.github.com/getsentry/sentry-python/issues/4257)) by
  [@&#8203;AbhiPrasad](https://redirect.github.com/AbhiPrasad) - chore: Deprecate
  `same_process_as_parent`
  ([#&#8203;4244](https://redirect.github.com/getsentry/sentry-python/issues/4244)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - feat(logs): Add sentry.origin
  attribute for log handler
  ([#&#8203;4250](https://redirect.github.com/getsentry/sentry-python/issues/4250)) by
  [@&#8203;AbhiPrasad](https://redirect.github.com/AbhiPrasad) - feat(tests): Add optional cutoff to
  toxgen ([#&#8203;4243](https://redirect.github.com/getsentry/sentry-python/issues/4243)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - toxgen: Retry & fail if we fail to
  fetch PyPI data ([#&#8203;4251](https://redirect.github.com/getsentry/sentry-python/issues/4251))
  by [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - build(deps): bump
  actions/create-github-app-token from 1.12.0 to 2.0.2
  ([#&#8203;4248](https://redirect.github.com/getsentry/sentry-python/issues/4248)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot) - Trying to prevent the grpc setup
  from being flaky ([#&#8203;4233](https://redirect.github.com/getsentry/sentry-python/issues/4233))
  by [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - feat(breadcrumbs): add `_meta`
  information for truncation of breadcrumbs
  ([#&#8203;4007](https://redirect.github.com/getsentry/sentry-python/issues/4007)) by
  [@&#8203;shellmayr](https://redirect.github.com/shellmayr) - tests: Move django under toxgen
  ([#&#8203;4238](https://redirect.github.com/getsentry/sentry-python/issues/4238)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - fix: Handle JSONDecodeError
  gracefully in StarletteRequestExtractor
  ([#&#8203;4226](https://redirect.github.com/getsentry/sentry-python/issues/4226)) by
  [@&#8203;moodix](https://redirect.github.com/moodix) - fix(asyncio): Remove shutdown handler
  ([#&#8203;4237](https://redirect.github.com/getsentry/sentry-python/issues/4237)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMzguMCIsInVwZGF0ZWRJblZlciI6IjM5LjIzOC4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Documentation

- Update readme.md
  ([`7ad4590`](https://github.com/MartinBernstorff/Memium/commit/7ad45900a597b85c3ba38c7c61c09c3490eca44d))


## v0.30.0 (2025-04-12)

### Chores

- Cleanup unused code
  ([`cad50d4`](https://github.com/MartinBernstorff/Memium/commit/cad50d4691afbd38976d42b628ba5b200e952f06))

### Documentation

- Update readme.md
  ([`4e59b4a`](https://github.com/MartinBernstorff/Memium/commit/4e59b4a9e6bac79efed49a2282a85bbce582c64b))

- Update readme.md
  ([`1b16827`](https://github.com/MartinBernstorff/Memium/commit/1b16827cd7ee4bbb711f9592998bd3beb653e2d0))

### Features

- Specify whether to show parent doc title independently from prompt type
  ([`b0a0217`](https://github.com/MartinBernstorff/Memium/commit/b0a0217e151bfcf2a29d7dba0267ee403e9ff1b6))

### Refactoring

- Inline more of QA
  ([`8b7fd40`](https://github.com/MartinBernstorff/Memium/commit/8b7fd404839545b8fc8380613bfae9bd6aa0c503))

- Inline QAFromDoc
  ([`838aa03`](https://github.com/MartinBernstorff/Memium/commit/838aa03a72bf063d135bea29b6d10c8813edc629))

- Remove cloze
  ([`0c6e524`](https://github.com/MartinBernstorff/Memium/commit/0c6e524a4c673621f4b7c5ca4d12da3e2ee19e2e))


## v0.29.3 (2025-04-11)

### Bug Fixes

- **deps**: Update dependency markdown to v3.8
  ([#857](https://github.com/MartinBernstorff/Memium/pull/857),
  [`63869c8`](https://github.com/MartinBernstorff/Memium/commit/63869c883e5662e65b23a86b17289fed3e20d460))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [markdown](https://redirect.github.com/Python-Markdown/markdown)
  ([changelog](https://python-markdown.github.io/changelog/)) | `==3.7` -> `==3.8` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/markdown/3.8?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/markdown/3.8?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/markdown/3.7/3.8?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/markdown/3.7/3.8?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>Python-Markdown/markdown (markdown)</summary>

### [`v3.8`](https://redirect.github.com/Python-Markdown/markdown/releases/tag/3.8)

[Compare Source](https://redirect.github.com/Python-Markdown/markdown/compare/3.7...3.8)

##### Changed

- DRY fix in `abbr` extension by introducing method `create_element`
  ([#&#8203;1483](https://redirect.github.com/Python-Markdown/markdown/issues/1483)). - Clean up
  test directory by removing some redundant tests and port non-redundant cases to the newer test
  framework. - Improved performance of the raw HTML post-processor
  ([#&#8203;1510](https://redirect.github.com/Python-Markdown/markdown/issues/1510)).

##### Fixed

- Backslash Unescape IDs set via `attr_list` on `toc`
  ([#&#8203;1493](https://redirect.github.com/Python-Markdown/markdown/issues/1493)). - Ensure
  `md_in_html` processes content inside "markdown" blocks as they are parsed outside of "markdown"
  blocks to keep things more consistent for third-party extensions
  ([#&#8203;1503](https://redirect.github.com/Python-Markdown/markdown/issues/1503)). - `md_in_html`
  handle tags within inline code blocks better
  ([#&#8203;1075](https://redirect.github.com/Python-Markdown/markdown/issues/1075)). - `md_in_html`
  fix handling of one-liner block HTML handling
  ([#&#8203;1074](https://redirect.github.com/Python-Markdown/markdown/issues/1074)). - Ensure
  `<center>` is treated like a block-level element
  ([#&#8203;1481](https://redirect.github.com/Python-Markdown/markdown/issues/1481)). - Ensure that
  `abbr` extension respects `AtomicString` and does not process perceived abbreviations in these
  strings ([#&#8203;1512](https://redirect.github.com/Python-Markdown/markdown/issues/1512)). -
  Ensure `smarty` extension correctly renders nested closing quotes
  ([#&#8203;1514](https://redirect.github.com/Python-Markdown/markdown/issues/1514)).

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMzguMCIsInVwZGF0ZWRJblZlciI6IjM5LjIzOC4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Documentation

- Cleanup roadmap
  ([`5600ff6`](https://github.com/MartinBernstorff/Memium/commit/5600ff69875bc13cff8990f684629c645cb97d8e))


## v0.29.2 (2025-04-10)

### Bug Fixes

- Strip ending punctuation
  ([`a8ce2d3`](https://github.com/MartinBernstorff/Memium/commit/a8ce2d317437f17a622ac36b7c78a97d5cba3636))


## v0.29.1 (2025-04-10)

### Bug Fixes

- Skip definition extraction if no def found
  ([`bab8665`](https://github.com/MartinBernstorff/Memium/commit/bab8665d19d7a4bf4677355c5898562b52ce8082))


## v0.29.0 (2025-04-10)

### Chores

- **deps**: Update dependency ruff to v0.11.5
  ([#856](https://github.com/MartinBernstorff/Memium/pull/856),
  [`db3eee4`](https://github.com/MartinBernstorff/Memium/commit/db3eee49262870f94c61ec52e57da286359b44c3))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [ruff](https://docs.astral.sh/ruff) ([source](https://redirect.github.com/astral-sh/ruff),
  [changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md)) | `==0.11.4` ->
  `==0.11.5` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/ruff/0.11.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/ruff/0.11.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/ruff/0.11.4/0.11.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/ruff/0.11.4/0.11.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>astral-sh/ruff (ruff)</summary>

### [`v0.11.5`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#0115)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.11.4...0.11.5)

##### Preview features

- \[`airflow`] Add missing `AIR302` attribute check
  ([#&#8203;17115](https://redirect.github.com/astral-sh/ruff/pull/17115)) - \[`airflow`] Expand
  module path check to individual symbols (`AIR302`)
  ([#&#8203;17278](https://redirect.github.com/astral-sh/ruff/pull/17278)) - \[`airflow`] Extract
  `AIR312` from `AIR302` rules (`AIR302`, `AIR312`)
  ([#&#8203;17152](https://redirect.github.com/astral-sh/ruff/pull/17152)) - \[`airflow`] Update
  oudated `AIR301`, `AIR302` rules
  ([#&#8203;17123](https://redirect.github.com/astral-sh/ruff/pull/17123)) - \[syntax-errors] Async
  comprehension in sync comprehension
  ([#&#8203;17177](https://redirect.github.com/astral-sh/ruff/pull/17177)) - \[syntax-errors] Check
  annotations in annotated assignments
  ([#&#8203;17283](https://redirect.github.com/astral-sh/ruff/pull/17283)) - \[syntax-errors] Extend
  annotation checks to `await`
  ([#&#8203;17282](https://redirect.github.com/astral-sh/ruff/pull/17282))

##### Bug fixes

- \[`flake8-pie`] Avoid false positive for multiple assignment with `auto()` (`PIE796`)
  ([#&#8203;17274](https://redirect.github.com/astral-sh/ruff/pull/17274))

##### Rule changes

- \[`ruff`] Fix `RUF100` to detect unused file-level `noqa` directives with specific codes
  ([#&#8203;17042](https://redirect.github.com/astral-sh/ruff/issues/17042))
  ([#&#8203;17061](https://redirect.github.com/astral-sh/ruff/pull/17061)) -
  \[`flake8-pytest-style`] Avoid false positive for legacy form of `pytest.raises` (`PT011`)
  ([#&#8203;17231](https://redirect.github.com/astral-sh/ruff/pull/17231))

##### Documentation

- Fix formatting of "See Style Guide" link
  ([#&#8203;17272](https://redirect.github.com/astral-sh/ruff/pull/17272))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMzguMCIsInVwZGF0ZWRJblZlciI6IjM5LjIzOC4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Features

- Extract reversed definition prompts
  ([`9a97b9a`](https://github.com/MartinBernstorff/Memium/commit/9a97b9ac64d74f89e0c084d75e02acb1908e14d9))


## v0.28.0 (2025-04-10)

### Features

- Handle subfolders in wikilinks
  ([`ad9898e`](https://github.com/MartinBernstorff/Memium/commit/ad9898e882ee7660843220bfd7a716604bf4e13a))


## v0.27.0 (2025-04-10)

### Bug Fixes

- **deps**: Update dependency pydantic to v2.11.0
  ([#844](https://github.com/MartinBernstorff/Memium/pull/844),
  [`b475ef8`](https://github.com/MartinBernstorff/Memium/commit/b475ef88196394b17354861fc9e34157fbd58492))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pydantic](https://redirect.github.com/pydantic/pydantic)
  ([changelog](https://docs.pydantic.dev/latest/changelog/)) | `==2.10.6` -> `==2.11.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pydantic/2.11.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pydantic/2.11.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pydantic/2.10.6/2.11.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pydantic/2.10.6/2.11.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pydantic/pydantic (pydantic)</summary>

### [`v2.11.0`](https://redirect.github.com/pydantic/pydantic/blob/HEAD/HISTORY.md#v2110-2025-03-27)

[Compare Source](https://redirect.github.com/pydantic/pydantic/compare/v2.10.6...v2.11.0)

[GitHub release](https://redirect.github.com/pydantic/pydantic/releases/tag/v2.11.0)

##### What's Changed

Pydantic v2.11 is a version strongly focused on build time performance of Pydantic models (and core
  schema generation in general). See the [blog
  post](https://pydantic.dev/articles/pydantic-v2-11-release) for more details.

##### Pacaking

- Bump `pydantic-core` to v2.33.0 by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11631](https://redirect.github.com/pydantic/pydantic/pull/11631)

##### New Features

- Add `encoded_string()` method to the URL types by
  [@&#8203;YassinNouh21](https://redirect.github.com/YassinNouh21) in
  [#&#8203;11580](https://redirect.github.com/pydantic/pydantic/pull/11580) - Add support for
  `defer_build` with `@validate_call` decorator by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11584](https://redirect.github.com/pydantic/pydantic/pull/11584) - Allow `@with_config`
  decorator to be used with keyword arguments by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11608](https://redirect.github.com/pydantic/pydantic/pull/11608) - Simplify customization
  of default value inclusion in JSON Schema generation by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11634](https://redirect.github.com/pydantic/pydantic/pull/11634) - Add
  `generate_arguments_schema()` function by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11572](https://redirect.github.com/pydantic/pydantic/pull/11572)

##### Fixes

- Allow generic typed dictionaries to be used for unpacked variadic keyword parameters by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11571](https://redirect.github.com/pydantic/pydantic/pull/11571) - Fix runtime error when
  computing model string representation involving cached properties and self-referenced models by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11579](https://redirect.github.com/pydantic/pydantic/pull/11579) - Preserve other steps
  when using the ellipsis in the pipeline API by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11626](https://redirect.github.com/pydantic/pydantic/pull/11626) - Fix deferred
  discriminator application logic by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11591](https://redirect.github.com/pydantic/pydantic/pull/11591)

##### New Contributors

- [@&#8203;cmenon12](https://redirect.github.com/cmenon12) made their first contribution in
  [#&#8203;11562](https://redirect.github.com/pydantic/pydantic/pull/11562) -
  [@&#8203;Jeukoh](https://redirect.github.com/Jeukoh) made their first contribution in
  [#&#8203;11611](https://redirect.github.com/pydantic/pydantic/pull/11611)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDcuMSIsInVwZGF0ZWRJblZlciI6IjM5LjIwNy4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency pydantic to v2.11.1
  ([#845](https://github.com/MartinBernstorff/Memium/pull/845),
  [`7ae523c`](https://github.com/MartinBernstorff/Memium/commit/7ae523c38b694a14f9952a06e4f5a9c7fe997acb))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pydantic](https://redirect.github.com/pydantic/pydantic)
  ([changelog](https://docs.pydantic.dev/latest/changelog/)) | `==2.11.0` -> `==2.11.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pydantic/2.11.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pydantic/2.11.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pydantic/2.11.0/2.11.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pydantic/2.11.0/2.11.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pydantic/pydantic (pydantic)</summary>

### [`v2.11.1`](https://redirect.github.com/pydantic/pydantic/blob/HEAD/HISTORY.md#v2111-2025-03-28)

[Compare Source](https://redirect.github.com/pydantic/pydantic/compare/v2.11.0...v2.11.1)

[GitHub release](https://redirect.github.com/pydantic/pydantic/releases/tag/v2.11.1)

##### What's Changed

##### Fixes

- Do not override `'definitions-ref'` schemas containing serialization schemas or metadata by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11644](https://redirect.github.com/pydantic/pydantic/pull/11644)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDcuMSIsInVwZGF0ZWRJblZlciI6IjM5LjIwNy4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency pydantic to v2.11.2
  ([#850](https://github.com/MartinBernstorff/Memium/pull/850),
  [`2b8e258`](https://github.com/MartinBernstorff/Memium/commit/2b8e258b0ed2b9709d503b6535d3bbda38ae55b1))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pydantic](https://redirect.github.com/pydantic/pydantic)
  ([changelog](https://docs.pydantic.dev/latest/changelog/)) | `==2.11.1` -> `==2.11.2` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pydantic/2.11.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pydantic/2.11.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pydantic/2.11.1/2.11.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pydantic/2.11.1/2.11.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pydantic/pydantic (pydantic)</summary>

### [`v2.11.2`](https://redirect.github.com/pydantic/pydantic/blob/HEAD/HISTORY.md#v2112-2025-04-03)

[Compare Source](https://redirect.github.com/pydantic/pydantic/compare/v2.11.1...v2.11.2)

[GitHub release](https://redirect.github.com/pydantic/pydantic/releases/tag/v2.11.2)

##### What's Changed

##### Fixes

- Bump `pydantic-core` to v2.33.1 by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11678](https://redirect.github.com/pydantic/pydantic/pull/11678) - Make sure
  `__pydantic_private__` exists before setting private attributes by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11666](https://redirect.github.com/pydantic/pydantic/pull/11666) - Do not override
  `FieldInfo._complete` when using field from parent class by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11668](https://redirect.github.com/pydantic/pydantic/pull/11668) - Provide the available
  definitions when applying discriminated unions by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11670](https://redirect.github.com/pydantic/pydantic/pull/11670) - Do not expand root
  type in the mypy plugin for variables by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11676](https://redirect.github.com/pydantic/pydantic/pull/11676) - Mention the attribute
  name in model fields deprecation message by [@&#8203;Viicos](https://redirect.github.com/Viicos)
  in [#&#8203;11674](https://redirect.github.com/pydantic/pydantic/pull/11674) - Properly validate
  parameterized mappings by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11658](https://redirect.github.com/pydantic/pydantic/pull/11658)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMjcuMyIsInVwZGF0ZWRJblZlciI6IjM5LjIyNy4zIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency pydantic to v2.11.3
  ([#854](https://github.com/MartinBernstorff/Memium/pull/854),
  [`df226ac`](https://github.com/MartinBernstorff/Memium/commit/df226ace96a3e9c34fd836ad0390b82406b7da06))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pydantic](https://redirect.github.com/pydantic/pydantic)
  ([changelog](https://docs.pydantic.dev/latest/changelog/)) | `==2.11.2` -> `==2.11.3` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pydantic/2.11.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pydantic/2.11.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pydantic/2.11.2/2.11.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pydantic/2.11.2/2.11.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pydantic/pydantic (pydantic)</summary>

### [`v2.11.3`](https://redirect.github.com/pydantic/pydantic/blob/HEAD/HISTORY.md#v2113-2025-04-08)

[Compare Source](https://redirect.github.com/pydantic/pydantic/compare/v2.11.2...v2.11.3)

[GitHub release](https://redirect.github.com/pydantic/pydantic/releases/tag/v2.11.3)

##### What's Changed

##### Packaging

- Update V1 copy to v1.10.21 by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11706](https://redirect.github.com/pydantic/pydantic/pull/11706)

##### Fixes

- Preserve field description when rebuilding model fields by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11698](https://redirect.github.com/pydantic/pydantic/pull/11698)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMzUuMiIsInVwZGF0ZWRJblZlciI6IjM5LjIzNS4yIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency sentry-sdk to v2.23.0
  ([#834](https://github.com/MartinBernstorff/Memium/pull/834),
  [`b06f9e9`](https://github.com/MartinBernstorff/Memium/commit/b06f9e92ed61cd3f5e9ac3b673a7ea936161ec07))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [sentry-sdk](https://redirect.github.com/getsentry/sentry-python)
  ([changelog](https://redirect.github.com/getsentry/sentry-python/blob/master/CHANGELOG.md)) |
  `==2.20.0` -> `==2.23.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/sentry-sdk/2.23.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/sentry-sdk/2.23.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/sentry-sdk/2.20.0/2.23.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/sentry-sdk/2.20.0/2.23.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>getsentry/sentry-python (sentry-sdk)</summary>

### [`v2.23.0`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2230)

[Compare Source](https://redirect.github.com/getsentry/sentry-python/compare/2.22.0...2.23.0)

##### Various fixes & improvements

- Feat(profiling): Add new functions to start/stop continuous profiler
  ([#&#8203;4056](https://redirect.github.com/getsentry/sentry-python/issues/4056)) by
  [@&#8203;Zylphrex](https://redirect.github.com/Zylphrex) - Feat(profiling): Export start/stop
  profile session ([#&#8203;4079](https://redirect.github.com/getsentry/sentry-python/issues/4079))
  by [@&#8203;Zylphrex](https://redirect.github.com/Zylphrex) - Feat(tracing): Backfill missing
  `sample_rand` on `PropagationContext`
  ([#&#8203;4038](https://redirect.github.com/getsentry/sentry-python/issues/4038)) by
  [@&#8203;szokeasaurusrex](https://redirect.github.com/szokeasaurusrex) - Feat(logs): Add alpha
  version of Sentry logs
  ([#&#8203;4126](https://redirect.github.com/getsentry/sentry-python/issues/4126)) by
  [@&#8203;colin-sentry](https://redirect.github.com/colin-sentry) - Security(gha): fix potential
  for shell injection
  ([#&#8203;4099](https://redirect.github.com/getsentry/sentry-python/issues/4099)) by
  [@&#8203;mdtro](https://redirect.github.com/mdtro) - Docs: Add `init()` parameters to ApiDocs.
  ([#&#8203;4100](https://redirect.github.com/getsentry/sentry-python/issues/4100)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Docs: Document that caller must
  check `mutable` ([#&#8203;4010](https://redirect.github.com/getsentry/sentry-python/issues/4010))
  by [@&#8203;szokeasaurusrex](https://redirect.github.com/szokeasaurusrex) - Fix(Anthropic): Add
  partial json support to streams
  ([#&#8203;3674](https://redirect.github.com/getsentry/sentry-python/issues/3674)) - Fix(ASGI): Fix
  KeyError if transaction does not exist
  ([#&#8203;4095](https://redirect.github.com/getsentry/sentry-python/issues/4095)) by
  [@&#8203;kevinji](https://redirect.github.com/kevinji) - Fix(asyncio): Improve asyncio integration
  error handling. ([#&#8203;4129](https://redirect.github.com/getsentry/sentry-python/issues/4129))
  by [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Fix(AWS Lambda): Fix capturing
  errors during AWS Lambda INIT phase
  ([#&#8203;3943](https://redirect.github.com/getsentry/sentry-python/issues/3943)) - Fix(Bottle):
  Prevent internal error on 404
  ([#&#8203;4131](https://redirect.github.com/getsentry/sentry-python/issues/4131)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Fix(CI): Fix API doc failure in CI
  ([#&#8203;4075](https://redirect.github.com/getsentry/sentry-python/issues/4075)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Fix(ClickHouse) ClickHouse in test
  suite ([#&#8203;4087](https://redirect.github.com/getsentry/sentry-python/issues/4087)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Fix(cloudresourcecontext): Added
  timeout to HTTP requests in CloudResourceContextIntegration
  ([#&#8203;4120](https://redirect.github.com/getsentry/sentry-python/issues/4120)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Fix(crons): Fixed bug when
  `cron_jobs` is set to `None` in arq integration
  ([#&#8203;4115](https://redirect.github.com/getsentry/sentry-python/issues/4115)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Fix(debug): Take into account
  parent handlers for debug logger
  ([#&#8203;4133](https://redirect.github.com/getsentry/sentry-python/issues/4133)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Fix(FastAPI/Starlette): Fix
  middleware with positional arguments.
  ([#&#8203;4118](https://redirect.github.com/getsentry/sentry-python/issues/4118)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Fix(featureflags): add LRU
  update/dedupe test coverage
  ([#&#8203;4082](https://redirect.github.com/getsentry/sentry-python/issues/4082)) - Fix(logging):
  Coerce None values into strings in logentry params.
  ([#&#8203;4121](https://redirect.github.com/getsentry/sentry-python/issues/4121)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Fix(pyspark): Grab `attemptId`
  more defensively ([#&#8203;4130](https://redirect.github.com/getsentry/sentry-python/issues/4130))
  by [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Fix(Quart): Support
  `quart_flask_patch`
  ([#&#8203;4132](https://redirect.github.com/getsentry/sentry-python/issues/4132)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Fix(tests): A way to locally run
  AWS Lambda functions
  ([#&#8203;4128](https://redirect.github.com/getsentry/sentry-python/issues/4128)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Fix(tests): Add concurrency
  testcase for arq ([#&#8203;4125](https://redirect.github.com/getsentry/sentry-python/issues/4125))
  by [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Fix(tests): Add fail_on_changes
  to toxgen by [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Fix(tests): Run AWS
  Lambda tests locally
  ([#&#8203;3988](https://redirect.github.com/getsentry/sentry-python/issues/3988)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Fix(tests): Test relevant
  prereleases and allow to ignore releases - Fix(tracing): Move `TRANSACTION_SOURCE_*` constants to
  `Enum` ([#&#8203;3889](https://redirect.github.com/getsentry/sentry-python/issues/3889)) by
  [@&#8203;mgaligniana](https://redirect.github.com/mgaligniana) - Fix(typing): Add more typing info
  to Scope.update_from_kwargs's "contexts"
  ([#&#8203;4080](https://redirect.github.com/getsentry/sentry-python/issues/4080)) - Fix(typing):
  Set correct type for `set_context` everywhere
  ([#&#8203;4123](https://redirect.github.com/getsentry/sentry-python/issues/4123)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Chore(tests): Regenerate tox.ini
  ([#&#8203;4108](https://redirect.github.com/getsentry/sentry-python/issues/4108)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Build(deps): bump
  actions/create-github-app-token from 1.11.5 to 1.11.6
  ([#&#8203;4113](https://redirect.github.com/getsentry/sentry-python/issues/4113)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot) - Build(deps): bump
  codecov/codecov-action from 5.3.1 to 5.4.0
  ([#&#8203;4112](https://redirect.github.com/getsentry/sentry-python/issues/4112)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot)

### [`v2.22.0`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2220)

[Compare Source](https://redirect.github.com/getsentry/sentry-python/compare/2.21.0...2.22.0)

- **New integration:** Add [Statsig](https://statsig.com/) integration
  ([#&#8203;4022](https://redirect.github.com/getsentry/sentry-python/issues/4022)) by
  [@&#8203;aliu39](https://redirect.github.com/aliu39)

For more information, see the documentation for the
  [StatsigIntegration](https://docs.sentry.io/platforms/python/integrations/statsig/).

- Profiling: Continuous profiling lifecycle
  ([#&#8203;4017](https://redirect.github.com/getsentry/sentry-python/issues/4017)) by
  [@&#8203;Zylphrex](https://redirect.github.com/Zylphrex)

- Fix: Revert "feat(tracing): Add `propagate_traces` deprecation warning
  ([#&#8203;3899](https://redirect.github.com/getsentry/sentry-python/issues/3899))"
  ([#&#8203;4055](https://redirect.github.com/getsentry/sentry-python/issues/4055)) by
  [@&#8203;cmanallen](https://redirect.github.com/cmanallen)

- Tests: Generate Web 1 group tox entries by toxgen script
  ([#&#8203;3980](https://redirect.github.com/getsentry/sentry-python/issues/3980)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Tests: Generate Web 2 group tox entries by toxgen script
  ([#&#8203;3981](https://redirect.github.com/getsentry/sentry-python/issues/3981)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Tests: Generate Tasks group tox entries by toxgen script
  ([#&#8203;3976](https://redirect.github.com/getsentry/sentry-python/issues/3976)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Tests: Generate AI group tox entries by toxgen script
  ([#&#8203;3977](https://redirect.github.com/getsentry/sentry-python/issues/3977)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Tests: Generate DB group tox entries by toxgen script
  ([#&#8203;3978](https://redirect.github.com/getsentry/sentry-python/issues/3978)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Tests: Generate Misc group tox entries by toxgen script
  ([#&#8203;3982](https://redirect.github.com/getsentry/sentry-python/issues/3982)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Tests: Generate Flags group tox entries by toxgen script
  ([#&#8203;3974](https://redirect.github.com/getsentry/sentry-python/issues/3974)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Tests: Generate gRPC tox entries by toxgen script
  ([#&#8203;3979](https://redirect.github.com/getsentry/sentry-python/issues/3979)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Tests: Remove toxgen cutoff, add statsig
  ([#&#8203;4048](https://redirect.github.com/getsentry/sentry-python/issues/4048)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Tests: Reduce continuous profiling test flakiness
  ([#&#8203;4052](https://redirect.github.com/getsentry/sentry-python/issues/4052)) by
  [@&#8203;Zylphrex](https://redirect.github.com/Zylphrex)

- Tests: Fix Clickhouse test
  ([#&#8203;4053](https://redirect.github.com/getsentry/sentry-python/issues/4053)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Tests: Fix flaky HTTPS test
  ([#&#8203;4057](https://redirect.github.com/getsentry/sentry-python/issues/4057)) by
  [@&#8203;Zylphrex](https://redirect.github.com/Zylphrex)

- Update sample rate in DSC
  ([#&#8203;4018](https://redirect.github.com/getsentry/sentry-python/issues/4018)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Move the GraphQL group over to the tox gen script
  ([#&#8203;3975](https://redirect.github.com/getsentry/sentry-python/issues/3975)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Update changelog with `profile_session_sample_rate`
  ([#&#8203;4046](https://redirect.github.com/getsentry/sentry-python/issues/4046)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

### [`v2.21.0`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2210)

[Compare Source](https://redirect.github.com/getsentry/sentry-python/compare/2.20.0...2.21.0)

- Fix incompatibility with new Strawberry version
  ([#&#8203;4026](https://redirect.github.com/getsentry/sentry-python/issues/4026)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Add `failed_request_status_codes`
  to Litestar ([#&#8203;4021](https://redirect.github.com/getsentry/sentry-python/issues/4021)) by
  [@&#8203;vrslev](https://redirect.github.com/vrslev)

See https://docs.sentry.io/platforms/python/integrations/litestar/ for details. - Deprecate
  `enable_tracing` option
  ([#&#8203;3935](https://redirect.github.com/getsentry/sentry-python/issues/3935)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker)

The `enable_tracing` option is now deprecated. Please use `traces_sample_rate` instead. See
  https://docs.sentry.io/platforms/python/configuration/options/#traces_sample_rate for more
  information. - Explicitly use `None` default when checking metadata
  ([#&#8203;4039](https://redirect.github.com/getsentry/sentry-python/issues/4039)) by
  [@&#8203;mpurnell1](https://redirect.github.com/mpurnell1) - Fix bug where concurrent accesses to
  the flags property could raise a `RuntimeError`
  ([#&#8203;4034](https://redirect.github.com/getsentry/sentry-python/issues/4034)) by
  [@&#8203;cmanallen](https://redirect.github.com/cmanallen) - Add more min versions of frameworks
  ([#&#8203;3973](https://redirect.github.com/getsentry/sentry-python/issues/3973)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Set level based on status code for
  HTTP client breadcrumbs
  ([#&#8203;4004](https://redirect.github.com/getsentry/sentry-python/issues/4004)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Don't set transaction status to
  error on `sys.exit(0)`
  ([#&#8203;4025](https://redirect.github.com/getsentry/sentry-python/issues/4025)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Continuous profiling sample rate
  ([#&#8203;4002](https://redirect.github.com/getsentry/sentry-python/issues/4002)) by
  [@&#8203;Zylphrex](https://redirect.github.com/Zylphrex)

Set `profile_session_sample_rate=1.0` in your `init()` to collect continuous profiles for 100% of
  profile sessions. See
  https://docs.sentry.io/platforms/python/profiling/#enable-continuous-profiling for more
  information. - Track and report spans that were dropped
  ([#&#8203;4005](https://redirect.github.com/getsentry/sentry-python/issues/4005)) by
  [@&#8203;constantinius](https://redirect.github.com/constantinius) - Change continuous profile
  buffer size ([#&#8203;3987](https://redirect.github.com/getsentry/sentry-python/issues/3987)) by
  [@&#8203;Zylphrex](https://redirect.github.com/Zylphrex) - Handle `MultiPartParserError` to avoid
  internal sentry crash
  ([#&#8203;4001](https://redirect.github.com/getsentry/sentry-python/issues/4001)) by
  [@&#8203;orhanhenrik](https://redirect.github.com/orhanhenrik) - Handle `None` lineno in
  `get_source_context`
  ([#&#8203;3925](https://redirect.github.com/getsentry/sentry-python/issues/3925)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Add support for Python 3.12 and
  3.13 to AWS Lambda integration
  ([#&#8203;3965](https://redirect.github.com/getsentry/sentry-python/issues/3965)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Add `propagate_traces`
  deprecation warning
  ([#&#8203;3899](https://redirect.github.com/getsentry/sentry-python/issues/3899)) by
  [@&#8203;mgaligniana](https://redirect.github.com/mgaligniana) - Check that `__module__` is `str`
  ([#&#8203;3942](https://redirect.github.com/getsentry/sentry-python/issues/3942)) by
  [@&#8203;szokeasaurusrex](https://redirect.github.com/szokeasaurusrex) - Add `__repr__` to
  `Baggage` ([#&#8203;4043](https://redirect.github.com/getsentry/sentry-python/issues/4043)) by
  [@&#8203;szokeasaurusrex](https://redirect.github.com/szokeasaurusrex) - Fix a typo
  ([#&#8203;3923](https://redirect.github.com/getsentry/sentry-python/issues/3923)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Fix various CI errors on master
  ([#&#8203;4009](https://redirect.github.com/getsentry/sentry-python/issues/4009)) by
  [@&#8203;Zylphrex](https://redirect.github.com/Zylphrex) - Split gevent tests off
  ([#&#8203;3964](https://redirect.github.com/getsentry/sentry-python/issues/3964)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Add tox generation script, but
  don't use it yet ([#&#8203;3971](https://redirect.github.com/getsentry/sentry-python/issues/3971))
  by [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Use `httpx_mock` in `test_httpx`
  ([#&#8203;3967](https://redirect.github.com/getsentry/sentry-python/issues/3967)) by
  [@&#8203;sl0thentr0py](https://redirect.github.com/sl0thentr0py) - Fix typo in test name
  ([#&#8203;4036](https://redirect.github.com/getsentry/sentry-python/issues/4036)) by
  [@&#8203;szokeasaurusrex](https://redirect.github.com/szokeasaurusrex) - Fix mypy
  ([#&#8203;4019](https://redirect.github.com/getsentry/sentry-python/issues/4019)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Test Celery's latest RC
  ([#&#8203;3938](https://redirect.github.com/getsentry/sentry-python/issues/3938)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Bump
  `actions/create-github-app-token` from `1.11.2` to `1.11.3`
  ([#&#8203;4023](https://redirect.github.com/getsentry/sentry-python/issues/4023)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot) - Bump
  `actions/create-github-app-token` from `1.11.1` to `1.11.2`
  ([#&#8203;4015](https://redirect.github.com/getsentry/sentry-python/issues/4015)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot) - Bump `codecov/codecov-action` from
  `5.1.2` to `5.3.1`
  ([#&#8203;3995](https://redirect.github.com/getsentry/sentry-python/issues/3995)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDAuMCIsInVwZGF0ZWRJblZlciI6IjM5LjIwMC4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency sentry-sdk to v2.23.1
  ([#835](https://github.com/MartinBernstorff/Memium/pull/835),
  [`8d4142d`](https://github.com/MartinBernstorff/Memium/commit/8d4142d88daa708a589ba7bcaf169abda733b0bf))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [sentry-sdk](https://redirect.github.com/getsentry/sentry-python)
  ([changelog](https://redirect.github.com/getsentry/sentry-python/blob/master/CHANGELOG.md)) |
  `==2.23.0` -> `==2.23.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/sentry-sdk/2.23.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/sentry-sdk/2.23.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/sentry-sdk/2.23.0/2.23.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/sentry-sdk/2.23.0/2.23.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>getsentry/sentry-python (sentry-sdk)</summary>

### [`v2.23.1`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2231)

[Compare Source](https://redirect.github.com/getsentry/sentry-python/compare/2.23.0...2.23.1)

##### Various fixes & improvements

- Fix import problem in release 2.23.0
  ([#&#8203;4140](https://redirect.github.com/getsentry/sentry-python/issues/4140)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDcuMSIsInVwZGF0ZWRJblZlciI6IjM5LjIwNy4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency sentry-sdk to v2.24.0
  ([#840](https://github.com/MartinBernstorff/Memium/pull/840),
  [`a9a0dfc`](https://github.com/MartinBernstorff/Memium/commit/a9a0dfc1ad5a23503f634892875bacea51685af0))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [sentry-sdk](https://redirect.github.com/getsentry/sentry-python)
  ([changelog](https://redirect.github.com/getsentry/sentry-python/blob/master/CHANGELOG.md)) |
  `==2.23.1` -> `==2.24.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/sentry-sdk/2.24.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/sentry-sdk/2.24.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/sentry-sdk/2.23.1/2.24.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/sentry-sdk/2.23.1/2.24.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>getsentry/sentry-python (sentry-sdk)</summary>

### [`v2.24.0`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2240)

[Compare Source](https://redirect.github.com/getsentry/sentry-python/compare/2.23.1...2.24.0)

##### Various fixes & improvements

- fix(tracing): Fix `InvalidOperation`
  ([#&#8203;4179](https://redirect.github.com/getsentry/sentry-python/issues/4179)) by
  [@&#8203;szokeasaurusrex](https://redirect.github.com/szokeasaurusrex) - Fix memory leak by not
  piling up breadcrumbs forever in Spark workers.
  ([#&#8203;4167](https://redirect.github.com/getsentry/sentry-python/issues/4167)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Update scripts sources
  ([#&#8203;4166](https://redirect.github.com/getsentry/sentry-python/issues/4166)) by
  [@&#8203;emmanuel-ferdman](https://redirect.github.com/emmanuel-ferdman) - Fixed flaky test
  ([#&#8203;4165](https://redirect.github.com/getsentry/sentry-python/issues/4165)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - chore(profiler): Add deprecation
  warning for session functions
  ([#&#8203;4171](https://redirect.github.com/getsentry/sentry-python/issues/4171)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - feat(profiling): reverse
  profile_session start/stop methods deprecation
  ([#&#8203;4162](https://redirect.github.com/getsentry/sentry-python/issues/4162)) by
  [@&#8203;viglia](https://redirect.github.com/viglia) - Reset `DedupeIntegration`'s `last-seen` if
  `before_send` dropped the event
  ([#&#8203;4142](https://redirect.github.com/getsentry/sentry-python/issues/4142)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - style(integrations): Fix captured
  typo ([#&#8203;4161](https://redirect.github.com/getsentry/sentry-python/issues/4161)) by
  [@&#8203;pimuzzo](https://redirect.github.com/pimuzzo) - Handle loguru msg levels that are not
  supported by Sentry
  ([#&#8203;4147](https://redirect.github.com/getsentry/sentry-python/issues/4147)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - feat(tests): Update tox.ini
  ([#&#8203;4146](https://redirect.github.com/getsentry/sentry-python/issues/4146)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Support Starlette/FastAPI
  `app.host` ([#&#8203;4157](https://redirect.github.com/getsentry/sentry-python/issues/4157)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDcuMSIsInVwZGF0ZWRJblZlciI6IjM5LjIwNy4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency sentry-sdk to v2.24.1
  ([#842](https://github.com/MartinBernstorff/Memium/pull/842),
  [`bfc1ee4`](https://github.com/MartinBernstorff/Memium/commit/bfc1ee4da122067e2a1d15016bfcbe0b57c77d12))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [sentry-sdk](https://redirect.github.com/getsentry/sentry-python)
  ([changelog](https://redirect.github.com/getsentry/sentry-python/blob/master/CHANGELOG.md)) |
  `==2.24.0` -> `==2.24.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/sentry-sdk/2.24.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/sentry-sdk/2.24.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/sentry-sdk/2.24.0/2.24.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/sentry-sdk/2.24.0/2.24.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>getsentry/sentry-python (sentry-sdk)</summary>

### [`v2.24.1`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2241)

##### Various fixes & improvements

- Always set `_spotlight_url`
  ([#&#8203;4186](https://redirect.github.com/getsentry/sentry-python/issues/4186)) by
  [@&#8203;BYK](https://redirect.github.com/BYK) - Broader except in Django `parsed_body`
  ([#&#8203;4189](https://redirect.github.com/getsentry/sentry-python/issues/4189)) by
  [@&#8203;orhanhenrik](https://redirect.github.com/orhanhenrik) - Add platform header to the
  `chunk` item-type in the envelope
  ([#&#8203;4178](https://redirect.github.com/getsentry/sentry-python/issues/4178)) by
  [@&#8203;viglia](https://redirect.github.com/viglia) - Move `mypy` config into `pyproject.toml`
  ([#&#8203;4181](https://redirect.github.com/getsentry/sentry-python/issues/4181)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Move `flake8` config into
  `pyproject.toml` ([#&#8203;4185](https://redirect.github.com/getsentry/sentry-python/issues/4185))
  by [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Move `pytest` config into
  `pyproject.toml` ([#&#8203;4184](https://redirect.github.com/getsentry/sentry-python/issues/4184))
  by [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Bump
  `actions/create-github-app-token` from `1.11.6` to `1.11.7`
  ([#&#8203;4188](https://redirect.github.com/getsentry/sentry-python/issues/4188)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot) - Add `CODEOWNERS`
  ([#&#8203;4182](https://redirect.github.com/getsentry/sentry-python/issues/4182)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDcuMSIsInVwZGF0ZWRJblZlciI6IjM5LjIwNy4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency sentry-sdk to v2.25.0
  ([#846](https://github.com/MartinBernstorff/Memium/pull/846),
  [`b26ad9d`](https://github.com/MartinBernstorff/Memium/commit/b26ad9d64d7033cfdac08363ad88187b860449a4))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [sentry-sdk](https://redirect.github.com/getsentry/sentry-python)
  ([changelog](https://redirect.github.com/getsentry/sentry-python/blob/master/CHANGELOG.md)) |
  `==2.24.1` -> `==2.25.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/sentry-sdk/2.25.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/sentry-sdk/2.25.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/sentry-sdk/2.24.1/2.25.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/sentry-sdk/2.24.1/2.25.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>getsentry/sentry-python (sentry-sdk)</summary>

### [`v2.25.0`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2250)

[Compare Source](https://redirect.github.com/getsentry/sentry-python/compare/2.24.1...2.25.0)

##### Various fixes & improvements

- **New Beta Feature** Enable Sentry logs in `logging` Integration
  ([#&#8203;4143](https://redirect.github.com/getsentry/sentry-python/issues/4143)) by
  [@&#8203;colin-sentry](https://redirect.github.com/colin-sentry)

You can now send existing log messages to the new Sentry Logs feature.

For more information see:
  [https://github.com/getsentry/sentry/discussions/86804](https://redirect.github.com/getsentry/sentry/discussions/86804)

This is how you can use it (Sentry Logs is in beta right now so the API can still change):

```python import sentry_sdk from sentry_sdk.integrations.logging import LoggingIntegration ```

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDcuMSIsInVwZGF0ZWRJblZlciI6IjM5LjIwNy4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency sentry-sdk to v2.25.1
  ([#848](https://github.com/MartinBernstorff/Memium/pull/848),
  [`0226b58`](https://github.com/MartinBernstorff/Memium/commit/0226b586328ecfd0d679b7f74a98cdee948ff211))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [sentry-sdk](https://redirect.github.com/getsentry/sentry-python)
  ([changelog](https://redirect.github.com/getsentry/sentry-python/blob/master/CHANGELOG.md)) |
  `==2.25.0` -> `==2.25.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/sentry-sdk/2.25.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/sentry-sdk/2.25.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/sentry-sdk/2.25.0/2.25.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/sentry-sdk/2.25.0/2.25.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>getsentry/sentry-python (sentry-sdk)</summary>

### [`v2.25.1`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2251)

[Compare Source](https://redirect.github.com/getsentry/sentry-python/compare/2.25.0...2.25.1)

##### Various fixes & improvements

- fix(logs): Add a class which batches groups of logs together.
  ([#&#8203;4229](https://redirect.github.com/getsentry/sentry-python/issues/4229)) by
  [@&#8203;colin-sentry](https://redirect.github.com/colin-sentry) - fix(logs): Use repr instead of
  json for message and arguments
  ([#&#8203;4227](https://redirect.github.com/getsentry/sentry-python/issues/4227)) by
  [@&#8203;colin-sentry](https://redirect.github.com/colin-sentry) - fix(logs): Debug output from
  Sentry logs should always be `debug` level.
  ([#&#8203;4224](https://redirect.github.com/getsentry/sentry-python/issues/4224)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - fix(ai): Do not consume anthropic
  streaming stop ([#&#8203;4232](https://redirect.github.com/getsentry/sentry-python/issues/4232))
  by [@&#8203;colin-sentry](https://redirect.github.com/colin-sentry) - fix(spotlight): Do not spam
  sentry_sdk.warnings logger w/ Spotlight
  ([#&#8203;4219](https://redirect.github.com/getsentry/sentry-python/issues/4219)) by
  [@&#8203;BYK](https://redirect.github.com/BYK) - fix(docs): fixed code snippet
  ([#&#8203;4218](https://redirect.github.com/getsentry/sentry-python/issues/4218)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - build(deps): bump
  actions/create-github-app-token from 1.11.7 to 1.12.0
  ([#&#8203;4214](https://redirect.github.com/getsentry/sentry-python/issues/4214)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMjcuMyIsInVwZGF0ZWRJblZlciI6IjM5LjIyNy4zIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Chores

- **deps**: Update dependency diff-cover to v9.2.4
  ([#827](https://github.com/MartinBernstorff/Memium/pull/827),
  [`adc193f`](https://github.com/MartinBernstorff/Memium/commit/adc193feff90cad0aee66523df118ab83a645e20))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [diff-cover](https://redirect.github.com/Bachmann1234/diff-cover) | `==9.2.2` -> `==9.2.4` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/diff-cover/9.2.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/diff-cover/9.2.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/diff-cover/9.2.2/9.2.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/diff-cover/9.2.2/9.2.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>Bachmann1234/diff-cover (diff-cover)</summary>

### [`v9.2.4`](https://redirect.github.com/Bachmann1234/diff_cover/releases/tag/v9.2.4): Version
  9.2.4

[Compare Source](https://redirect.github.com/Bachmann1234/diff-cover/compare/v9.2.3...v9.2.4)

#### What's Changed

- Fix escaped untracked files by [@&#8203;buermarc](https://redirect.github.com/buermarc) in
  [https://github.com/Bachmann1234/diff_cover/pull/440](https://redirect.github.com/Bachmann1234/diff_cover/pull/440)

#### New Contributors

- [@&#8203;buermarc](https://redirect.github.com/buermarc) made their first contribution in
  [https://github.com/Bachmann1234/diff_cover/pull/440](https://redirect.github.com/Bachmann1234/diff_cover/pull/440)

##### Dependency Bumps

- Bump isort from 5.13.2 to 6.0.1 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in
  [https://github.com/Bachmann1234/diff_cover/pull/443](https://redirect.github.com/Bachmann1234/diff_cover/pull/443)
  - Bump setuptools from 75.8.0 to 75.8.2 by
  [@&#8203;dependabot](https://redirect.github.com/dependabot) in
  [https://github.com/Bachmann1234/diff_cover/pull/442](https://redirect.github.com/Bachmann1234/diff_cover/pull/442)

**Full Changelog**: https://github.com/Bachmann1234/diff_cover/compare/v9.2.3...v9.2.4

### [`v9.2.3`](https://redirect.github.com/Bachmann1234/diff-cover/compare/v9.2.2...v9.2.3)

[Compare Source](https://redirect.github.com/Bachmann1234/diff-cover/compare/v9.2.2...v9.2.3)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xODUuNCIsInVwZGF0ZWRJblZlciI6IjM5LjE4NS40IiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency pre-commit to v4.2.0
  ([#836](https://github.com/MartinBernstorff/Memium/pull/836),
  [`44a8ef5`](https://github.com/MartinBernstorff/Memium/commit/44a8ef5f64a26b09babd1f37d8f323b0fcffc1b7))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pre-commit](https://redirect.github.com/pre-commit/pre-commit) | `==4.1.0` -> `==4.2.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pre-commit/4.2.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pre-commit/4.2.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pre-commit/4.1.0/4.2.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pre-commit/4.1.0/4.2.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pre-commit/pre-commit (pre-commit)</summary>

###
  [`v4.2.0`](https://redirect.github.com/pre-commit/pre-commit/blob/HEAD/CHANGELOG.md#420---2025-03-18)

[Compare Source](https://redirect.github.com/pre-commit/pre-commit/compare/v4.1.0...v4.2.0)

\==================

##### Features

- For `language: python` first attempt a versioned python executable for the default language
  version before consulting a potentially unversioned `sys.executable`. -
  [#&#8203;3430](https://redirect.github.com/pre-commit/pre-commit/issues/3430) PR by
  [@&#8203;asottile](https://redirect.github.com/asottile).

##### Fixes

- Handle error during conflict detection when a file is named "HEAD" -
  [#&#8203;3425](https://redirect.github.com/pre-commit/pre-commit/issues/3425) PR by
  [@&#8203;tusharsadhwani](https://redirect.github.com/tusharsadhwani).

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDcuMSIsInVwZGF0ZWRJblZlciI6IjM5LjIwNy4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency pyright to v1.1.396
  ([#830](https://github.com/MartinBernstorff/Memium/pull/830),
  [`7e2a95e`](https://github.com/MartinBernstorff/Memium/commit/7e2a95e3e60b37937d8091a1bf6aaf729f244078))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pyright](https://redirect.github.com/RobertCraigie/pyright-python) | `==1.1.393` -> `==1.1.396` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pyright/1.1.396?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pyright/1.1.396?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pyright/1.1.393/1.1.396?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pyright/1.1.393/1.1.396?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>RobertCraigie/pyright-python (pyright)</summary>

###
  [`v1.1.396`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.395...v1.1.396)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.395...v1.1.396)

###
  [`v1.1.395`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.394...v1.1.395)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.394...v1.1.395)

###
  [`v1.1.394`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.393...v1.1.394)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.393...v1.1.394)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xODUuNCIsInVwZGF0ZWRJblZlciI6IjM5LjE4NS40IiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency pyright to v1.1.397
  ([#837](https://github.com/MartinBernstorff/Memium/pull/837),
  [`f0ef9ad`](https://github.com/MartinBernstorff/Memium/commit/f0ef9adc020a1b951efd1e50e7579f1f9337f734))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pyright](https://redirect.github.com/RobertCraigie/pyright-python) | `==1.1.396` -> `==1.1.397` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pyright/1.1.397?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pyright/1.1.397?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pyright/1.1.396/1.1.397?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pyright/1.1.396/1.1.397?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>RobertCraigie/pyright-python (pyright)</summary>

###
  [`v1.1.397`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.396...v1.1.397)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.396...v1.1.397)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDcuMSIsInVwZGF0ZWRJblZlciI6IjM5LjIwNy4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency pyright to v1.1.398
  ([#843](https://github.com/MartinBernstorff/Memium/pull/843),
  [`e675865`](https://github.com/MartinBernstorff/Memium/commit/e67586597c3bbd1d761e4c9c848d0881427033f6))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pyright](https://redirect.github.com/RobertCraigie/pyright-python) | `==1.1.397` -> `==1.1.398` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pyright/1.1.398?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pyright/1.1.398?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pyright/1.1.397/1.1.398?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pyright/1.1.397/1.1.398?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>RobertCraigie/pyright-python (pyright)</summary>

###
  [`v1.1.398`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.397...v1.1.398)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.397...v1.1.398)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDcuMSIsInVwZGF0ZWRJblZlciI6IjM5LjIwNy4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency pytest to v8.3.5
  ([#831](https://github.com/MartinBernstorff/Memium/pull/831),
  [`ad78646`](https://github.com/MartinBernstorff/Memium/commit/ad786469d0e5f14292ff781a272809b2fb371c10))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pytest](https://redirect.github.com/pytest-dev/pytest)
  ([changelog](https://docs.pytest.org/en/stable/changelog.html)) | `==8.3.4` -> `==8.3.5` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pytest/8.3.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pytest/8.3.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pytest/8.3.4/8.3.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pytest/8.3.4/8.3.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pytest-dev/pytest (pytest)</summary>

### [`v8.3.5`](https://redirect.github.com/pytest-dev/pytest/releases/tag/8.3.5)

[Compare Source](https://redirect.github.com/pytest-dev/pytest/compare/8.3.4...8.3.5)

### pytest 8.3.5 (2025-03-02)

#### Bug fixes

- [#&#8203;11777](https://redirect.github.com/pytest-dev/pytest/issues/11777): Fixed issue where
  sequences were still being shortened even with `-vv` verbosity. -
  [#&#8203;12888](https://redirect.github.com/pytest-dev/pytest/issues/12888): Fixed broken input
  when using Python 3.13+ and a `libedit` build of Python, such as on macOS or with uv-managed
  Python binaries from the `python-build-standalone` project. This could manifest e.g. by a broken
  prompt when using `Pdb`, or seeing empty inputs with manual usage of `input()` and suspended
  capturing. - [#&#8203;13026](https://redirect.github.com/pytest-dev/pytest/issues/13026): Fixed
  `AttributeError`{.interpreted-text role="class"} crash when using `--import-mode=importlib` when
  top-level directory same name as another module of the standard library. -
  [#&#8203;13053](https://redirect.github.com/pytest-dev/pytest/issues/13053): Fixed a regression in
  pytest 8.3.4 where, when using `--import-mode=importlib`, a directory containing py file with the
  same name would cause an `ImportError` -
  [#&#8203;13083](https://redirect.github.com/pytest-dev/pytest/issues/13083): Fixed issue where
  pytest could crash if one of the collected directories got removed during collection.

#### Improved documentation

- [#&#8203;12842](https://redirect.github.com/pytest-dev/pytest/issues/12842): Added dedicated page
  about using types with pytest.

See `types`{.interpreted-text role="ref"} for detailed usage.

#### Contributor-facing changes

- [#&#8203;13112](https://redirect.github.com/pytest-dev/pytest/issues/13112): Fixed selftest
  failures in `test_terminal.py` with Pygments >= 2.19.0 -
  [#&#8203;13256](https://redirect.github.com/pytest-dev/pytest/issues/13256): Support for Towncrier
  versions released in 2024 has been re-enabled when building Sphinx docs -- by
  `webknjaz`{.interpreted-text role="user"}.

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xODUuNCIsInVwZGF0ZWRJblZlciI6IjM5LjE4NS40IiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency pytest-cov to v6.1.0
  ([#847](https://github.com/MartinBernstorff/Memium/pull/847),
  [`9503e86`](https://github.com/MartinBernstorff/Memium/commit/9503e8608f422d1a3a028dda37e4de130441d90e))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pytest-cov](https://redirect.github.com/pytest-dev/pytest-cov)
  ([changelog](https://pytest-cov.readthedocs.io/en/latest/changelog.html)) | `==6.0.0` -> `==6.1.0`
  |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pytest-cov/6.1.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pytest-cov/6.1.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pytest-cov/6.0.0/6.1.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pytest-cov/6.0.0/6.1.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pytest-dev/pytest-cov (pytest-cov)</summary>

###
  [`v6.1.0`](https://redirect.github.com/pytest-dev/pytest-cov/blob/HEAD/CHANGELOG.rst#610-2025-04-01)

[Compare Source](https://redirect.github.com/pytest-dev/pytest-cov/compare/v6.0.0...v6.1.0)

- Change terminal output to use full width lines for the coverage header. Contributed by Tsvika
  Shapira in `#&#8203;678 <https://github.com/pytest-dev/pytest-cov/pull/678>`\_. - Removed
  unnecessary CovFailUnderWarning. Fixes `#&#8203;675
  <https://github.com/pytest-dev/pytest-cov/issues/675>`\_. - Fixed the term report not using the
  precision specified via `--cov-precision`.

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMjcuMyIsInVwZGF0ZWRJblZlciI6IjM5LjIyNy4zIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency pytest-cov to v6.1.1
  ([#852](https://github.com/MartinBernstorff/Memium/pull/852),
  [`2d7f5f6`](https://github.com/MartinBernstorff/Memium/commit/2d7f5f6abecc1f41b01582bb2cbc8135dacef6c9))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pytest-cov](https://redirect.github.com/pytest-dev/pytest-cov)
  ([changelog](https://pytest-cov.readthedocs.io/en/latest/changelog.html)) | `==6.1.0` -> `==6.1.1`
  |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pytest-cov/6.1.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pytest-cov/6.1.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pytest-cov/6.1.0/6.1.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pytest-cov/6.1.0/6.1.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pytest-dev/pytest-cov (pytest-cov)</summary>

###
  [`v6.1.1`](https://redirect.github.com/pytest-dev/pytest-cov/blob/HEAD/CHANGELOG.rst#611-2025-04-05)

[Compare Source](https://redirect.github.com/pytest-dev/pytest-cov/compare/v6.1.0...v6.1.1)

- Fixed breakage that occurs when `--cov-context` and the `no_cover` marker are used together.

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMjcuMyIsInVwZGF0ZWRJblZlciI6IjM5LjIyNy4zIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency ruff to v0.10.0
  ([#832](https://github.com/MartinBernstorff/Memium/pull/832),
  [`a15b2ff`](https://github.com/MartinBernstorff/Memium/commit/a15b2ff441b325badad857c13cc99fb1c92a35ae))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [ruff](https://docs.astral.sh/ruff) ([source](https://redirect.github.com/astral-sh/ruff),
  [changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md)) | `==0.9.10` ->
  `==0.10.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/ruff/0.10.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/ruff/0.10.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/ruff/0.9.10/0.10.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/ruff/0.9.10/0.10.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>astral-sh/ruff (ruff)</summary>

### [`v0.10.0`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#0100)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.9.10...0.10.0)

Check out the [blog post](https://astral.sh/blog/ruff-v0.10.0) for a migration guide and overview of
  the changes!

##### Breaking changes

See also, the "Remapped rules" section which may result in disabled rules.

- **Changes to how the Python version is inferred when a `target-version` is not specified**
  ([#&#8203;16319](https://redirect.github.com/astral-sh/ruff/pull/16319))

In previous versions of Ruff, you could specify your Python version with:

- The `target-version` option in a `ruff.toml` file or the `[tool.ruff]` section of a pyproject.toml
  file. - The `project.requires-python` field in a `pyproject.toml` file with a `[tool.ruff]`
  section.

These options worked well in most cases, and are still recommended for fine control of the Python
  version. However, because of the way Ruff discovers config files, `pyproject.toml` files without a
  `[tool.ruff]` section would be ignored, including the `requires-python` setting. Ruff would then
  use the default Python version (3.9 as of this writing) instead, which is surprising when you've
  attempted to request another version.

In v0.10, config discovery has been updated to address this issue:

- If Ruff finds a `ruff.toml` file without a `target-version`, it will check for a `pyproject.toml`
  file in the same directory and respect its `requires-python` version, even if it does not contain
  a `[tool.ruff]` section. - If Ruff finds a user-level configuration, the `requires-python` field
  of the closest `pyproject.toml` in a parent directory will take precedence. - If there is no
  config file (`ruff.toml`or `pyproject.toml` with a `[tool.ruff]` section) in the directory of the
  file being checked, Ruff will search for the closest `pyproject.toml` in the parent directories
  and use its `requires-python` setting.

- **Updated `TYPE_CHECKING` behavior**
  ([#&#8203;16669](https://redirect.github.com/astral-sh/ruff/pull/16669))

Previously, Ruff only recognized typechecking blocks that tested the `typing.TYPE_CHECKING` symbol.
  Now, Ruff recognizes any local variable named `TYPE_CHECKING`. This release also removes support
  for the legacy `if 0:` and `if False:` typechecking checks. Use a local `TYPE_CHECKING` variable
  instead.

- **More robust noqa parsing**
  ([#&#8203;16483](https://redirect.github.com/astral-sh/ruff/pull/16483))

The syntax for both file-level and in-line suppression comments has been unified and made more
  robust to certain errors. In most cases, this will result in more suppression comments being read
  by Ruff, but there are a few instances where previously read comments will now log an error to the
  user instead. Please refer to the documentation on [*Error
  suppression*](https://docs.astral.sh/ruff/linter/#error-suppression) for the full specification.

- **Avoid unnecessary parentheses around with statements with a single context manager and a
  trailing comment** ([#&#8203;14005](https://redirect.github.com/astral-sh/ruff/pull/14005))

This change fixes a bug in the formatter where it introduced unnecessary parentheses around with
  statements with a single context manager and a trailing comment. This change may result in a
  change in formatting for some users.

- **Bump alpine default tag to 3.21 for derived Docker images**
  ([#&#8203;16456](https://redirect.github.com/astral-sh/ruff/pull/16456))

Alpine 3.21 was released in Dec 2024 and is used in the official Alpine-based Python images. Now the
  ruff:alpine image will use 3.21 instead of 3.20 and ruff:alpine3.20 will no longer be updated.

##### Deprecated Rules

The following rules have been deprecated:

- [`non-pep604-isinstance`](https://docs.astral.sh/ruff/rules/non-pep604-isinstance/) (`UP038`) -
  [`suspicious-xmle-tree-usage`](https://docs.astral.sh/ruff/rules/suspicious-xmle-tree-usage/)
  (`S320`)

##### Remapped rules

The following rules have been remapped to new rule codes:

- \[`unsafe-markup-use`]: `RUF035` to `S704`

##### Stabilization

The following rules have been stabilized and are no longer in preview:

-
  [`batched-without-explicit-strict`](https://docs.astral.sh/ruff/rules/batched-without-explicit-strict)
  (`B911`) -
  [`unnecessary-dict-comprehension-for-iterable`](https://docs.astral.sh/ruff/rules/unnecessary-dict-comprehension-for-iterable)
  (`C420`) - [`datetime-min-max`](https://docs.astral.sh/ruff/rules/datetime-min-max) (`DTZ901`) -
  [`fast-api-unused-path-parameter`](https://docs.astral.sh/ruff/rules/fast-api-unused-path-parameter)
  (`FAST003`) - [`root-logger-call`](https://docs.astral.sh/ruff/rules/root-logger-call) (`LOG015`)
  - [`len-test`](https://docs.astral.sh/ruff/rules/len-test) (`PLC1802`) -
  [`shallow-copy-environ`](https://docs.astral.sh/ruff/rules/shallow-copy-environ) (`PLW1507`) -
  [`os-listdir`](https://docs.astral.sh/ruff/rules/os-listdir) (`PTH208`) -
  [`invalid-pathlib-with-suffix`](https://docs.astral.sh/ruff/rules/invalid-pathlib-with-suffix)
  (`PTH210`) -
  [`invalid-assert-message-literal-argument`](https://docs.astral.sh/ruff/rules/invalid-assert-message-literal-argument)
  (`RUF040`) -
  [`unnecessary-nested-literal`](https://docs.astral.sh/ruff/rules/unnecessary-nested-literal)
  (`RUF041`) -
  [`unnecessary-cast-to-int`](https://docs.astral.sh/ruff/rules/unnecessary-cast-to-int) (`RUF046`)
  - [`map-int-version-parsing`](https://docs.astral.sh/ruff/rules/map-int-version-parsing)
  (`RUF048`) - [`if-key-in-dict-del`](https://docs.astral.sh/ruff/rules/if-key-in-dict-del)
  (`RUF051`) - [`unsafe-markup-use`](https://docs.astral.sh/ruff/rules/unsafe-markup-use) (`S704`).
  This rule has also been renamed from `RUF035`. -
  [`split-static-string`](https://docs.astral.sh/ruff/rules/split-static-string) (`SIM905`) -
  [`runtime-cast-value`](https://docs.astral.sh/ruff/rules/runtime-cast-value) (`TC006`) -
  [`unquoted-type-alias`](https://docs.astral.sh/ruff/rules/unquoted-type-alias) (`TC007`) -
  [`non-pep646-unpack`](https://docs.astral.sh/ruff/rules/non-pep646-unpack) (`UP044`)

The following behaviors have been stabilized:

- [`bad-staticmethod-argument`](https://docs.astral.sh/ruff/rules/bad-staticmethod-argument/)
  (`PLW0211`)
  [`invalid-first-argument-name-for-class-method`](https://docs.astral.sh/ruff/rules/invalid-first-argument-name-for-class-method/)
  (`N804`): `__new__` methods are now no longer flagged by
  `invalid-first-argument-name-for-class-method` (`N804`) but instead by `bad-staticmethod-argument`
  (`PLW0211`) - [`bad-str-strip-call`](https://docs.astral.sh/ruff/rules/bad-str-strip-call/)
  (`PLE1310`): The rule now applies to objects which are known to have type `str` or `bytes`. -
  [`blanket-noqa`](https://docs.astral.sh/ruff/rules/blanket-noqa/) (`PGH004`): Also detect blanked
  file-level noqa comments (and not just line level comments). -
  [`custom-type-var-for-self`](https://docs.astral.sh/ruff/rules/custom-type-var-for-self/)
  (`PYI019`): More accurate detection of custom `TypeVars` replaceable by `Self`. The range of the
  diagnostic is now the full function header rather than just the return annotation. -
  [`invalid-argument-name`](https://docs.astral.sh/ruff/rules/invalid-argument-name/) (`N803`):
  Ignore argument names of functions decorated with `typing.override` -
  [`invalid-envvar-default`](https://docs.astral.sh/ruff/rules/invalid-envvar-default/) (`PLW1508`):
  Detect default value arguments to `os.environ.get` with invalid type. -
  [`pytest-raises-with-multiple-statements`](https://docs.astral.sh/ruff/rules/pytest-raises-with-multiple-statements/)
  (`PT012`)
  [`pytest-warns-with-multiple-statements`](https://docs.astral.sh/ruff/rules/pytest-warns-with-multiple-statements/)
  (`PT031`): Allow `for` statements with an empty body in `pytest.raises` and `pytest.warns` `with`
  statements. - [`redundant-open-modes`](https://docs.astral.sh/ruff/rules/redundant-open-modes/)
  (`UP015`): The diagnostic range is now the range of the redundant mode argument where it
  previously was the range of the entire open call. You may have to replace your `noqa` comments
  when suppressing `UP015`. -
  [`stdlib-module-shadowing`](https://docs.astral.sh/ruff/rules/stdlib-module-shadowing/) (`A005`):
  Changes the default value of `lint.flake8-builtins.strict-checking` from `true` to `false`. -
  [`type-none-comparison`](https://docs.astral.sh/ruff/rules/type-none-comparison/) (`FURB169`): Now
  also recognizes `type(expr) is type(None)` comparisons where `expr` isn't a name expression.

The following fixes or improvements to fixes have been stabilized:

- [`repeated-equality-comparison`](https://docs.astral.sh/ruff/rules/repeated-equality-comparison/)
  (`PLR1714`) ([#&#8203;16685](https://redirect.github.com/astral-sh/ruff/pull/16685)) -
  [`needless-bool`](https://docs.astral.sh/ruff/rules/needless-bool/) (`SIM103`)
  ([#&#8203;16684](https://redirect.github.com/astral-sh/ruff/pull/16684)) -
  [`unused-private-type-var`](https://docs.astral.sh/ruff/rules/unused-private-type-var/) (`PYI018`)
  ([#&#8203;16682](https://redirect.github.com/astral-sh/ruff/pull/16682))

##### Server

- Remove logging output for `ruff.printDebugInformation`
  ([#&#8203;16617](https://redirect.github.com/astral-sh/ruff/pull/16617))

##### Configuration

- \[`flake8-builtins`] Deprecate the `builtins-` prefixed options in favor of the unprefixed options
  (e.g. `builtins-allowed-modules` is now deprecated in favor of `allowed-modules`)
  ([#&#8203;16092](https://redirect.github.com/astral-sh/ruff/pull/16092))

##### Bug fixes

- \[flake8-bandit] Fix mixed-case hash algorithm names (S324)
  ([#&#8203;16552](https://redirect.github.com/astral-sh/ruff/pull/16552))

##### CLI

- \[ruff] Fix `last_tag`/`commits_since_last_tag` for `version` command
  ([#&#8203;16686](https://redirect.github.com/astral-sh/ruff/pull/16686))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDAuMCIsInVwZGF0ZWRJblZlciI6IjM5LjIwMC4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency ruff to v0.11.0
  ([#833](https://github.com/MartinBernstorff/Memium/pull/833),
  [`7a77fcb`](https://github.com/MartinBernstorff/Memium/commit/7a77fcb7c91b91ba3e954eb0b50866f6d98b6f88))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [ruff](https://docs.astral.sh/ruff) ([source](https://redirect.github.com/astral-sh/ruff),
  [changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md)) | `==0.10.0` ->
  `==0.11.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/ruff/0.11.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/ruff/0.11.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/ruff/0.10.0/0.11.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/ruff/0.10.0/0.11.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>astral-sh/ruff (ruff)</summary>

### [`v0.11.0`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#0110)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.10.0...0.11.0)

This is a follow-up to release 0.10.0. Because of a mistake in the release process, the
  `requires-python` inference changes were not included in that release. Ruff 0.11.0 now includes
  this change as well as the stabilization of the preview behavior for `PGH004`.

##### Breaking changes

- **Changes to how the Python version is inferred when a `target-version` is not specified**
  ([#&#8203;16319](https://redirect.github.com/astral-sh/ruff/pull/16319))

In previous versions of Ruff, you could specify your Python version with:

- The `target-version` option in a `ruff.toml` file or the `[tool.ruff]` section of a pyproject.toml
  file. - The `project.requires-python` field in a `pyproject.toml` file with a `[tool.ruff]`
  section.

These options worked well in most cases, and are still recommended for fine control of the Python
  version. However, because of the way Ruff discovers config files, `pyproject.toml` files without a
  `[tool.ruff]` section would be ignored, including the `requires-python` setting. Ruff would then
  use the default Python version (3.9 as of this writing) instead, which is surprising when you've
  attempted to request another version.

In v0.10, config discovery has been updated to address this issue:

- If Ruff finds a `ruff.toml` file without a `target-version`, it will check for a `pyproject.toml`
  file in the same directory and respect its `requires-python` version, even if it does not contain
  a `[tool.ruff]` section. - If Ruff finds a user-level configuration, the `requires-python` field
  of the closest `pyproject.toml` in a parent directory will take precedence. - If there is no
  config file (`ruff.toml`or `pyproject.toml` with a `[tool.ruff]` section) in the directory of the
  file being checked, Ruff will search for the closest `pyproject.toml` in the parent directories
  and use its `requires-python` setting.

##### Stabilization

The following behaviors have been stabilized:

- [`blanket-noqa`](https://docs.astral.sh/ruff/rules/blanket-noqa/) (`PGH004`): Also detect blanked
  file-level noqa comments (and not just line level comments).

##### Preview features

- \[syntax-errors] Tuple unpacking in `for` statement iterator clause before Python 3.9
  ([#&#8203;16558](https://redirect.github.com/astral-sh/ruff/pull/16558))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDAuMCIsInVwZGF0ZWRJblZlciI6IjM5LjIwMC4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency ruff to v0.11.1
  ([#838](https://github.com/MartinBernstorff/Memium/pull/838),
  [`f686813`](https://github.com/MartinBernstorff/Memium/commit/f686813bfd10df8075fa2a22597c4770b7439f60))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [ruff](https://docs.astral.sh/ruff) ([source](https://redirect.github.com/astral-sh/ruff),
  [changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md)) | `==0.11.0` ->
  `==0.11.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/ruff/0.11.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/ruff/0.11.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/ruff/0.11.0/0.11.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/ruff/0.11.0/0.11.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>astral-sh/ruff (ruff)</summary>

### [`v0.11.1`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#0111)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.11.0...0.11.1)

##### Preview features

- \[`airflow`] Add `chain`, `chain_linear` and `cross_downstream` for `AIR302`
  ([#&#8203;16647](https://redirect.github.com/astral-sh/ruff/pull/16647)) - \[syntax-errors]
  Improve error message and range for pre-PEP-614 decorator syntax errors
  ([#&#8203;16581](https://redirect.github.com/astral-sh/ruff/pull/16581)) - \[syntax-errors] PEP
  701 f-strings before Python 3.12
  ([#&#8203;16543](https://redirect.github.com/astral-sh/ruff/pull/16543)) - \[syntax-errors]
  Parenthesized context managers before Python 3.9
  ([#&#8203;16523](https://redirect.github.com/astral-sh/ruff/pull/16523)) - \[syntax-errors] Star
  annotations before Python 3.11
  ([#&#8203;16545](https://redirect.github.com/astral-sh/ruff/pull/16545)) - \[syntax-errors] Star
  expression in index before Python 3.11
  ([#&#8203;16544](https://redirect.github.com/astral-sh/ruff/pull/16544)) - \[syntax-errors]
  Unparenthesized assignment expressions in sets and indexes
  ([#&#8203;16404](https://redirect.github.com/astral-sh/ruff/pull/16404))

##### Bug fixes

- Server: Allow `FixAll` action in presence of version-specific syntax errors
  ([#&#8203;16848](https://redirect.github.com/astral-sh/ruff/pull/16848)) - \[`flake8-bandit`]
  Allow raw strings in `suspicious-mark-safe-usage` (`S308`)
  [#&#8203;16702](https://redirect.github.com/astral-sh/ruff/issues/16702)
  ([#&#8203;16770](https://redirect.github.com/astral-sh/ruff/pull/16770)) - \[`refurb`] Avoid
  panicking `unwrap` in `verbose-decimal-constructor` (`FURB157`)
  ([#&#8203;16777](https://redirect.github.com/astral-sh/ruff/pull/16777)) - \[`refurb`] Fix starred
  expressions fix (`FURB161`)
  ([#&#8203;16550](https://redirect.github.com/astral-sh/ruff/pull/16550)) - Fix `--statistics`
  reporting for unsafe fixes
  ([#&#8203;16756](https://redirect.github.com/astral-sh/ruff/pull/16756))

##### Rule changes

- \[`flake8-executables`] Allow `uv run` in shebang line for `shebang-missing-python` (`EXE003`)
  ([#&#8203;16849](https://redirect.github.com/astral-sh/ruff/pull/16849),[#&#8203;16855](https://redirect.github.com/astral-sh/ruff/pull/16855))

##### CLI

- Add `--exit-non-zero-on-format`
  ([#&#8203;16009](https://redirect.github.com/astral-sh/ruff/pull/16009))

##### Documentation

- Update Ruff tutorial to avoid non-existent fix in `__init__.py`
  ([#&#8203;16818](https://redirect.github.com/astral-sh/ruff/pull/16818)) - \[`flake8-gettext`]
  Swap `format-` and `printf-in-get-text-func-call` examples (`INT002`, `INT003`)
  ([#&#8203;16769](https://redirect.github.com/astral-sh/ruff/pull/16769))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDcuMSIsInVwZGF0ZWRJblZlciI6IjM5LjIwNy4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency ruff to v0.11.2
  ([#839](https://github.com/MartinBernstorff/Memium/pull/839),
  [`c581595`](https://github.com/MartinBernstorff/Memium/commit/c581595bfaa331087dd90360c59029b59b291edf))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [ruff](https://docs.astral.sh/ruff) ([source](https://redirect.github.com/astral-sh/ruff),
  [changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md)) | `==0.11.1` ->
  `==0.11.2` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/ruff/0.11.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/ruff/0.11.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/ruff/0.11.1/0.11.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/ruff/0.11.1/0.11.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>astral-sh/ruff (ruff)</summary>

### [`v0.11.2`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#0112)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.11.1...0.11.2)

##### Preview features

- \[syntax-errors] Fix false-positive syntax errors emitted for annotations on variadic parameters
  before Python 3.11 ([#&#8203;16878](https://redirect.github.com/astral-sh/ruff/pull/16878))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDcuMSIsInVwZGF0ZWRJblZlciI6IjM5LjIwNy4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency ruff to v0.11.3
  ([#849](https://github.com/MartinBernstorff/Memium/pull/849),
  [`519dfc9`](https://github.com/MartinBernstorff/Memium/commit/519dfc9d9687d59ae0e6e065e997f929754763fc))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [ruff](https://docs.astral.sh/ruff) ([source](https://redirect.github.com/astral-sh/ruff),
  [changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md)) | `==0.11.2` ->
  `==0.11.3` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/ruff/0.11.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/ruff/0.11.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/ruff/0.11.2/0.11.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/ruff/0.11.2/0.11.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>astral-sh/ruff (ruff)</summary>

### [`v0.11.3`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#0113)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.11.2...0.11.3)

##### Preview features

- \[`airflow`] Add more autofixes for `AIR302`
  ([#&#8203;16876](https://redirect.github.com/astral-sh/ruff/pull/16876),
  [#&#8203;16977](https://redirect.github.com/astral-sh/ruff/pull/16977),
  [#&#8203;16976](https://redirect.github.com/astral-sh/ruff/pull/16976),
  [#&#8203;16965](https://redirect.github.com/astral-sh/ruff/pull/16965)) - \[`airflow`] Move
  `AIR301` to `AIR002` ([#&#8203;16978](https://redirect.github.com/astral-sh/ruff/pull/16978)) -
  \[`airflow`] Move `AIR302` to `AIR301` and `AIR303` to `AIR302`
  ([#&#8203;17151](https://redirect.github.com/astral-sh/ruff/pull/17151)) - \[`flake8-bandit`] Mark
  `str` and `list[str]` literals as trusted input (`S603`)
  ([#&#8203;17136](https://redirect.github.com/astral-sh/ruff/pull/17136)) - \[`ruff`] Support
  slices in `RUF005` ([#&#8203;17078](https://redirect.github.com/astral-sh/ruff/pull/17078)) -
  \[syntax-errors] Start detecting compile-time syntax errors
  ([#&#8203;16106](https://redirect.github.com/astral-sh/ruff/pull/16106)) - \[syntax-errors]
  Duplicate type parameter names
  ([#&#8203;16858](https://redirect.github.com/astral-sh/ruff/pull/16858)) - \[syntax-errors]
  Irrefutable `case` pattern before final case
  ([#&#8203;16905](https://redirect.github.com/astral-sh/ruff/pull/16905)) - \[syntax-errors]
  Multiple assignments in `case` pattern
  ([#&#8203;16957](https://redirect.github.com/astral-sh/ruff/pull/16957)) - \[syntax-errors] Single
  starred assignment target ([#&#8203;17024](https://redirect.github.com/astral-sh/ruff/pull/17024))
  - \[syntax-errors] Starred expressions in `return`, `yield`, and `for`
  ([#&#8203;17134](https://redirect.github.com/astral-sh/ruff/pull/17134)) - \[syntax-errors] Store
  to or delete `__debug__` ([#&#8203;16984](https://redirect.github.com/astral-sh/ruff/pull/16984))

##### Bug fixes

- Error instead of `panic!` when running Ruff from a deleted directory
  ([#&#8203;16903](https://redirect.github.com/astral-sh/ruff/issues/16903))
  ([#&#8203;17054](https://redirect.github.com/astral-sh/ruff/pull/17054)) - \[syntax-errors] Fix
  false positive for parenthesized tuple index
  ([#&#8203;16948](https://redirect.github.com/astral-sh/ruff/pull/16948))

##### CLI

- Check `pyproject.toml` correctly when it is passed via stdin
  ([#&#8203;16971](https://redirect.github.com/astral-sh/ruff/pull/16971))

##### Configuration

- \[`flake8-import-conventions`] Add import `numpy.typing as npt` to default
  `flake8-import-conventions.aliases`
  ([#&#8203;17133](https://redirect.github.com/astral-sh/ruff/pull/17133))

##### Documentation

- \[`refurb`] Document why `UserDict`, `UserList`, and `UserString` are preferred over `dict`,
  `list`, and `str` (`FURB189`)
  ([#&#8203;16927](https://redirect.github.com/astral-sh/ruff/pull/16927))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMjcuMyIsInVwZGF0ZWRJblZlciI6IjM5LjIyNy4zIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency ruff to v0.11.4
  ([#851](https://github.com/MartinBernstorff/Memium/pull/851),
  [`906c81b`](https://github.com/MartinBernstorff/Memium/commit/906c81b24abbb447a6a7cf64b6319b33c43d9942))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [ruff](https://docs.astral.sh/ruff) ([source](https://redirect.github.com/astral-sh/ruff),
  [changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md)) | `==0.11.3` ->
  `==0.11.4` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/ruff/0.11.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/ruff/0.11.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/ruff/0.11.3/0.11.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/ruff/0.11.3/0.11.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>astral-sh/ruff (ruff)</summary>

### [`v0.11.4`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#0114)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.11.3...0.11.4)

##### Preview features

- \[`ruff`] Implement `invalid-rule-code` as `RUF102`
  ([#&#8203;17138](https://redirect.github.com/astral-sh/ruff/pull/17138)) - \[syntax-errors] Detect
  duplicate keys in `match` mapping patterns
  ([#&#8203;17129](https://redirect.github.com/astral-sh/ruff/pull/17129)) - \[syntax-errors] Detect
  duplicate attributes in `match` class patterns
  ([#&#8203;17186](https://redirect.github.com/astral-sh/ruff/pull/17186)) - \[syntax-errors] Detect
  invalid syntax in annotations
  ([#&#8203;17101](https://redirect.github.com/astral-sh/ruff/pull/17101))

##### Bug fixes

- \[syntax-errors] Fix multiple assignment error for class fields in `match` patterns
  ([#&#8203;17184](https://redirect.github.com/astral-sh/ruff/pull/17184)) - Don't skip visiting
  non-tuple slice in `typing.Annotated` subscripts
  ([#&#8203;17201](https://redirect.github.com/astral-sh/ruff/pull/17201))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMjcuMyIsInVwZGF0ZWRJblZlciI6IjM5LjIyNy4zIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency ruff to v0.9.10
  ([#825](https://github.com/MartinBernstorff/Memium/pull/825),
  [`d6bf5a2`](https://github.com/MartinBernstorff/Memium/commit/d6bf5a2cec7eeccd658d9c37293665df42b4269f))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [ruff](https://docs.astral.sh/ruff) ([source](https://redirect.github.com/astral-sh/ruff),
  [changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md)) | `==0.4.5` ->
  `==0.9.10` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/ruff/0.9.10?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/ruff/0.9.10?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/ruff/0.4.5/0.9.10?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/ruff/0.4.5/0.9.10?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>astral-sh/ruff (ruff)</summary>

### [`v0.9.10`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#0910)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.9.9...0.9.10)

##### Preview features

- \[`ruff`] Add new rule `RUF059`: Unused unpacked assignment
  ([#&#8203;16449](https://redirect.github.com/astral-sh/ruff/pull/16449)) - \[`syntax-errors`]
  Detect assignment expressions before Python 3.8
  ([#&#8203;16383](https://redirect.github.com/astral-sh/ruff/pull/16383)) - \[`syntax-errors`]
  Named expressions in decorators before Python 3.9
  ([#&#8203;16386](https://redirect.github.com/astral-sh/ruff/pull/16386)) - \[`syntax-errors`]
  Parenthesized keyword argument names after Python 3.8
  ([#&#8203;16482](https://redirect.github.com/astral-sh/ruff/pull/16482)) - \[`syntax-errors`]
  Positional-only parameters before Python 3.8
  ([#&#8203;16481](https://redirect.github.com/astral-sh/ruff/pull/16481)) - \[`syntax-errors`]
  Tuple unpacking in `return` and `yield` before Python 3.8
  ([#&#8203;16485](https://redirect.github.com/astral-sh/ruff/pull/16485)) - \[`syntax-errors`] Type
  parameter defaults before Python 3.13
  ([#&#8203;16447](https://redirect.github.com/astral-sh/ruff/pull/16447)) - \[`syntax-errors`] Type
  parameter lists before Python 3.12
  ([#&#8203;16479](https://redirect.github.com/astral-sh/ruff/pull/16479)) - \[`syntax-errors`]
  `except*` before Python 3.11
  ([#&#8203;16446](https://redirect.github.com/astral-sh/ruff/pull/16446)) - \[`syntax-errors`]
  `type` statements before Python 3.12
  ([#&#8203;16478](https://redirect.github.com/astral-sh/ruff/pull/16478))

##### Bug fixes

- Escape template filenames in glob patterns in configuration
  ([#&#8203;16407](https://redirect.github.com/astral-sh/ruff/pull/16407)) - \[`flake8-simplify`]
  Exempt unittest context methods for `SIM115` rule
  ([#&#8203;16439](https://redirect.github.com/astral-sh/ruff/pull/16439)) - Formatter: Fix syntax
  error location in notebooks
  ([#&#8203;16499](https://redirect.github.com/astral-sh/ruff/pull/16499)) - \[`pyupgrade`] Do not
  offer fix when at least one target is `global`/`nonlocal` (`UP028`)
  ([#&#8203;16451](https://redirect.github.com/astral-sh/ruff/pull/16451)) - \[`flake8-builtins`]
  Ignore variables matching module attribute names (`A001`)
  ([#&#8203;16454](https://redirect.github.com/astral-sh/ruff/pull/16454)) - \[`pylint`] Convert
  `code` keyword argument to a positional argument in fix for (`PLR1722`)
  ([#&#8203;16424](https://redirect.github.com/astral-sh/ruff/pull/16424))

##### CLI

- Move rule code from `description` to `check_name` in GitLab output serializer
  ([#&#8203;16437](https://redirect.github.com/astral-sh/ruff/pull/16437))

##### Documentation

- \[`pydocstyle`] Clarify that `D417` only checks docstrings with an arguments section
  ([#&#8203;16494](https://redirect.github.com/astral-sh/ruff/pull/16494))

### [`v0.9.9`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#099)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.9.8...0.9.9)

- Fix caching of unsupported-syntax errors
  ([#&#8203;16425](https://redirect.github.com/astral-sh/ruff/pull/16425))

- Only show unsupported-syntax errors in editors when preview mode is enabled
  ([#&#8203;16429](https://redirect.github.com/astral-sh/ruff/pull/16429))

### [`v0.9.8`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#098)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.9.7...0.9.8)

- Start detecting version-related syntax errors in the parser
  ([#&#8203;16090](https://redirect.github.com/astral-sh/ruff/pull/16090))

##### Rule changes

- \[`pylint`] Mark fix unsafe (`PLW1507`)
  ([#&#8203;16343](https://redirect.github.com/astral-sh/ruff/pull/16343)) - \[`pylint`] Catch `case
  np.nan`/`case math.nan` in `match` statements (`PLW0177`)
  ([#&#8203;16378](https://redirect.github.com/astral-sh/ruff/pull/16378)) - \[`ruff`] Add more
  Pydantic models variants to the list of default copy semantics (`RUF012`)
  ([#&#8203;16291](https://redirect.github.com/astral-sh/ruff/pull/16291))

##### Server

- Avoid indexing the project if `configurationPreference` is `editorOnly`
  ([#&#8203;16381](https://redirect.github.com/astral-sh/ruff/pull/16381)) - Avoid unnecessary info
  at non-trace server log level
  ([#&#8203;16389](https://redirect.github.com/astral-sh/ruff/pull/16389)) - Expand
  `ruff.configuration` to allow inline config
  ([#&#8203;16296](https://redirect.github.com/astral-sh/ruff/pull/16296)) - Notify users for
  invalid client settings ([#&#8203;16361](https://redirect.github.com/astral-sh/ruff/pull/16361))

##### Configuration

- Add `per-file-target-version` option
  ([#&#8203;16257](https://redirect.github.com/astral-sh/ruff/pull/16257))

- \[`refurb`] Do not consider docstring(s) (`FURB156`)
  ([#&#8203;16391](https://redirect.github.com/astral-sh/ruff/pull/16391)) - \[`flake8-self`] Ignore
  attribute accesses on instance-like variables (`SLF001`)
  ([#&#8203;16149](https://redirect.github.com/astral-sh/ruff/pull/16149)) - \[`pylint`] Fix false
  positives, add missing methods, and support positional-only parameters (`PLE0302`)
  ([#&#8203;16263](https://redirect.github.com/astral-sh/ruff/pull/16263)) - \[`flake8-pyi`] Mark
  `PYI030` fix unsafe when comments are deleted
  ([#&#8203;16322](https://redirect.github.com/astral-sh/ruff/pull/16322))

- Fix example for `S611` ([#&#8203;16316](https://redirect.github.com/astral-sh/ruff/pull/16316)) -
  Normalize inconsistent markdown headings in docstrings
  ([#&#8203;16364](https://redirect.github.com/astral-sh/ruff/pull/16364)) - Document MSRV policy
  ([#&#8203;16384](https://redirect.github.com/astral-sh/ruff/pull/16384))

### [`v0.9.7`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#097)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.9.6...0.9.7)

- Consider `__new__` methods as special function type for enforcing class method or static method
  rules ([#&#8203;13305](https://redirect.github.com/astral-sh/ruff/pull/13305)) - \[`airflow`]
  Improve the internal logic to differentiate deprecated symbols (`AIR303`)
  ([#&#8203;16013](https://redirect.github.com/astral-sh/ruff/pull/16013)) - \[`refurb`] Manual
  timezone monkeypatching (`FURB162`)
  ([#&#8203;16113](https://redirect.github.com/astral-sh/ruff/pull/16113)) - \[`ruff`] Implicit
  class variable in dataclass (`RUF045`)
  ([#&#8203;14349](https://redirect.github.com/astral-sh/ruff/pull/14349)) - \[`ruff`] Skip
  singleton starred expressions for `incorrectly-parenthesized-tuple-in-subscript` (`RUF031`)
  ([#&#8203;16083](https://redirect.github.com/astral-sh/ruff/pull/16083)) - \[`refurb`] Check for
  subclasses includes subscript expressions (`FURB189`)
  ([#&#8203;16155](https://redirect.github.com/astral-sh/ruff/pull/16155))

- \[`flake8-debugger`] Also flag `sys.breakpointhook` and `sys.__breakpointhook__` (`T100`)
  ([#&#8203;16191](https://redirect.github.com/astral-sh/ruff/pull/16191)) - \[`pycodestyle`] Exempt
  `site.addsitedir(...)` calls (`E402`)
  ([#&#8203;16251](https://redirect.github.com/astral-sh/ruff/pull/16251))

##### Formatter

- Fix unstable formatting of trailing end-of-line comments of parenthesized attribute values
  ([#&#8203;16187](https://redirect.github.com/astral-sh/ruff/pull/16187))

- Fix handling of requests received after shutdown message
  ([#&#8203;16262](https://redirect.github.com/astral-sh/ruff/pull/16262)) - Ignore
  `source.organizeImports.ruff` and `source.fixAll.ruff` code actions for a notebook cell
  ([#&#8203;16154](https://redirect.github.com/astral-sh/ruff/pull/16154)) - Include document
  specific debug info for `ruff.printDebugInformation`
  ([#&#8203;16215](https://redirect.github.com/astral-sh/ruff/pull/16215)) - Update server to return
  the debug info as string with `ruff.printDebugInformation`
  ([#&#8203;16214](https://redirect.github.com/astral-sh/ruff/pull/16214))

- Warn on invalid `noqa` even when there are no diagnostics
  ([#&#8203;16178](https://redirect.github.com/astral-sh/ruff/pull/16178)) - Better error messages
  while loading configuration `extend`s
  ([#&#8203;15658](https://redirect.github.com/astral-sh/ruff/pull/15658))

- \[`flake8-comprehensions`] Handle trailing comma in `C403` fix
  ([#&#8203;16110](https://redirect.github.com/astral-sh/ruff/pull/16110)) - \[`flake8-pyi`] Avoid
  flagging `custom-typevar-for-self` on metaclass methods (`PYI019`)
  ([#&#8203;16141](https://redirect.github.com/astral-sh/ruff/pull/16141)) - \[`pydocstyle`] Handle
  arguments with the same names as sections (`D417`)
  ([#&#8203;16011](https://redirect.github.com/astral-sh/ruff/pull/16011)) - \[`pylint`] Correct
  ordering of arguments in fix for `if-stmt-min-max` (`PLR1730`)
  ([#&#8203;16080](https://redirect.github.com/astral-sh/ruff/pull/16080)) - \[`pylint`] Do not
  offer fix for raw strings (`PLE251`)
  ([#&#8203;16132](https://redirect.github.com/astral-sh/ruff/pull/16132)) - \[`pyupgrade`] Do not
  upgrade functional `TypedDicts` with private field names to the class-based syntax (`UP013`)
  ([#&#8203;16219](https://redirect.github.com/astral-sh/ruff/pull/16219)) - \[`pyupgrade`] Handle
  micro version numbers correctly (`UP036`)
  ([#&#8203;16091](https://redirect.github.com/astral-sh/ruff/pull/16091)) - \[`pyupgrade`] Unwrap
  unary expressions correctly (`UP018`)
  ([#&#8203;15919](https://redirect.github.com/astral-sh/ruff/pull/15919)) - \[`refurb`] Correctly
  handle lengths of literal strings in `slice-to-remove-prefix-or-suffix` (`FURB188`)
  ([#&#8203;16237](https://redirect.github.com/astral-sh/ruff/pull/16237)) - \[`ruff`] Skip `RUF001`
  diagnostics when visiting string type definitions
  ([#&#8203;16122](https://redirect.github.com/astral-sh/ruff/pull/16122))

- Add FAQ entry for `source.*` code actions in Notebook
  ([#&#8203;16212](https://redirect.github.com/astral-sh/ruff/pull/16212)) - Add `SECURITY.md`
  ([#&#8203;16224](https://redirect.github.com/astral-sh/ruff/pull/16224))

### [`v0.9.6`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#096)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.9.5...0.9.6)

- \[`airflow`] Add `external_task.{ExternalTaskMarker, ExternalTaskSensor}` for `AIR302`
  ([#&#8203;16014](https://redirect.github.com/astral-sh/ruff/pull/16014)) - \[`flake8-builtins`]
  Make strict module name comparison optional (`A005`)
  ([#&#8203;15951](https://redirect.github.com/astral-sh/ruff/pull/15951)) - \[`flake8-pyi`] Extend
  fix to Python <= 3.9 for `redundant-none-literal` (`PYI061`)
  ([#&#8203;16044](https://redirect.github.com/astral-sh/ruff/pull/16044)) - \[`pylint`] Also report
  when the object isn't a literal (`PLE1310`)
  ([#&#8203;15985](https://redirect.github.com/astral-sh/ruff/pull/15985)) - \[`ruff`] Implement
  `indented-form-feed` (`RUF054`)
  ([#&#8203;16049](https://redirect.github.com/astral-sh/ruff/pull/16049)) - \[`ruff`] Skip type
  definitions for `missing-f-string-syntax` (`RUF027`)
  ([#&#8203;16054](https://redirect.github.com/astral-sh/ruff/pull/16054))

- \[`flake8-annotations`] Correct syntax for `typing.Union` in suggested return type fixes for
  `ANN20x` rules ([#&#8203;16025](https://redirect.github.com/astral-sh/ruff/pull/16025)) -
  \[`flake8-builtins`] Match upstream module name comparison (`A005`)
  ([#&#8203;16006](https://redirect.github.com/astral-sh/ruff/pull/16006)) -
  \[`flake8-comprehensions`] Detect overshadowed `list`/`set`/`dict`, ignore variadics and named
  expressions (`C417`) ([#&#8203;15955](https://redirect.github.com/astral-sh/ruff/pull/15955)) -
  \[`flake8-pie`] Remove following comma correctly when the unpacked dictionary is empty (`PIE800`)
  ([#&#8203;16008](https://redirect.github.com/astral-sh/ruff/pull/16008)) - \[`flake8-simplify`]
  Only trigger `SIM401` on known dictionaries
  ([#&#8203;15995](https://redirect.github.com/astral-sh/ruff/pull/15995)) - \[`pylint`] Do not
  report calls when object type and argument type mismatch, remove custom escape handling logic
  (`PLE1310`) ([#&#8203;15984](https://redirect.github.com/astral-sh/ruff/pull/15984)) -
  \[`pyupgrade`] Comments within parenthesized value ranges should not affect applicability
  (`UP040`) ([#&#8203;16027](https://redirect.github.com/astral-sh/ruff/pull/16027)) -
  \[`pyupgrade`] Don't introduce invalid syntax when upgrading old-style type aliases with
  parenthesized multiline values (`UP040`)
  ([#&#8203;16026](https://redirect.github.com/astral-sh/ruff/pull/16026)) - \[`pyupgrade`] Ensure
  we do not rename two type parameters to the same name (`UP049`)
  ([#&#8203;16038](https://redirect.github.com/astral-sh/ruff/pull/16038)) - \[`pyupgrade`]
  \[`ruff`] Don't apply renamings if the new name is shadowed in a scope of one of the references to
  the binding (`UP049`, `RUF052`)
  ([#&#8203;16032](https://redirect.github.com/astral-sh/ruff/pull/16032)) - \[`ruff`] Update
  `RUF009` to behave similar to `B008` and ignore attributes with immutable types
  ([#&#8203;16048](https://redirect.github.com/astral-sh/ruff/pull/16048))

- Root exclusions in the server to project root
  ([#&#8203;16043](https://redirect.github.com/astral-sh/ruff/pull/16043))

- \[`flake8-datetime`] Ignore `.replace()` calls while looking for `.astimezone`
  ([#&#8203;16050](https://redirect.github.com/astral-sh/ruff/pull/16050)) -
  \[`flake8-type-checking`] Avoid `TC004` false positive where the runtime definition is provided by
  `__getattr__` ([#&#8203;16052](https://redirect.github.com/astral-sh/ruff/pull/16052))

- Improve `ruff-lsp` migration document
  ([#&#8203;16072](https://redirect.github.com/astral-sh/ruff/pull/16072)) - Undeprecate
  `ruff.nativeServer` ([#&#8203;16039](https://redirect.github.com/astral-sh/ruff/pull/16039))

### [`v0.9.5`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#095)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.9.4...0.9.5)

- Recognize all symbols named `TYPE_CHECKING` for `in_type_checking_block`
  ([#&#8203;15719](https://redirect.github.com/astral-sh/ruff/pull/15719)) -
  \[`flake8-comprehensions`] Handle builtins at top of file correctly for
  `unnecessary-dict-comprehension-for-iterable` (`C420`)
  ([#&#8203;15837](https://redirect.github.com/astral-sh/ruff/pull/15837)) - \[`flake8-logging`]
  `.exception()` and `exc_info=` outside exception handlers (`LOG004`, `LOG014`)
  ([#&#8203;15799](https://redirect.github.com/astral-sh/ruff/pull/15799)) - \[`flake8-pyi`] Fix
  incorrect behaviour of `custom-typevar-return-type` preview-mode autofix if `typing` was already
  imported (`PYI019`) ([#&#8203;15853](https://redirect.github.com/astral-sh/ruff/pull/15853)) -
  \[`flake8-pyi`] Fix more complex cases (`PYI019`)
  ([#&#8203;15821](https://redirect.github.com/astral-sh/ruff/pull/15821)) - \[`flake8-pyi`] Make
  `PYI019` autofixable for `.py` files in preview mode as well as stubs
  ([#&#8203;15889](https://redirect.github.com/astral-sh/ruff/pull/15889)) - \[`flake8-pyi`] Remove
  type parameter correctly when it is the last (`PYI019`)
  ([#&#8203;15854](https://redirect.github.com/astral-sh/ruff/pull/15854)) - \[`pylint`] Fix missing
  parens in unsafe fix for `unnecessary-dunder-call` (`PLC2801`)
  ([#&#8203;15762](https://redirect.github.com/astral-sh/ruff/pull/15762)) - \[`pyupgrade`] Better
  messages and diagnostic range (`UP015`)
  ([#&#8203;15872](https://redirect.github.com/astral-sh/ruff/pull/15872)) - \[`pyupgrade`] Rename
  private type parameters in PEP 695 generics (`UP049`)
  ([#&#8203;15862](https://redirect.github.com/astral-sh/ruff/pull/15862)) - \[`refurb`] Also report
  non-name expressions (`FURB169`)
  ([#&#8203;15905](https://redirect.github.com/astral-sh/ruff/pull/15905)) - \[`refurb`] Mark fix as
  unsafe if there are comments (`FURB171`)
  ([#&#8203;15832](https://redirect.github.com/astral-sh/ruff/pull/15832)) - \[`ruff`] Classes with
  mixed type variable style (`RUF053`)
  ([#&#8203;15841](https://redirect.github.com/astral-sh/ruff/pull/15841)) - \[`airflow`]
  `BashOperator` has been moved to `airflow.providers.standard.operators.bash.BashOperator`
  (`AIR302`) ([#&#8203;15922](https://redirect.github.com/astral-sh/ruff/pull/15922)) -
  \[`flake8-pyi`] Add autofix for unused-private-type-var (`PYI018`)
  ([#&#8203;15999](https://redirect.github.com/astral-sh/ruff/pull/15999)) - \[`flake8-pyi`]
  Significantly improve accuracy of `PYI019` if preview mode is enabled
  ([#&#8203;15888](https://redirect.github.com/astral-sh/ruff/pull/15888))

- Preserve triple quotes and prefixes for strings
  ([#&#8203;15818](https://redirect.github.com/astral-sh/ruff/pull/15818)) -
  \[`flake8-comprehensions`] Skip when `TypeError` present from too many (kw)args for `C410`,`C411`,
  and `C418` ([#&#8203;15838](https://redirect.github.com/astral-sh/ruff/pull/15838)) -
  \[`flake8-pyi`] Rename `PYI019` and improve its diagnostic message
  ([#&#8203;15885](https://redirect.github.com/astral-sh/ruff/pull/15885)) - \[`pep8-naming`] Ignore
  `@override` methods (`N803`)
  ([#&#8203;15954](https://redirect.github.com/astral-sh/ruff/pull/15954)) - \[`pyupgrade`] Reuse
  replacement logic from `UP046` and `UP047` to preserve more comments (`UP040`)
  ([#&#8203;15840](https://redirect.github.com/astral-sh/ruff/pull/15840)) - \[`ruff`] Analyze
  deferred annotations before enforcing `mutable-(data)class-default` and
  `function-call-in-dataclass-default-argument` (`RUF008`,`RUF009`,`RUF012`)
  ([#&#8203;15921](https://redirect.github.com/astral-sh/ruff/pull/15921)) - \[`pycodestyle`] Exempt
  `sys.path += ...` calls (`E402`)
  ([#&#8203;15980](https://redirect.github.com/astral-sh/ruff/pull/15980))

- Config error only when `flake8-import-conventions` alias conflicts with `isort.required-imports`
  bound name ([#&#8203;15918](https://redirect.github.com/astral-sh/ruff/pull/15918)) - Workaround
  Even Better TOML crash related to `allOf`
  ([#&#8203;15992](https://redirect.github.com/astral-sh/ruff/pull/15992))

- \[`flake8-comprehensions`] Unnecessary `list` comprehension (rewrite as a `set` comprehension)
  (`C403`) - Handle extraneous parentheses around list comprehension
  ([#&#8203;15877](https://redirect.github.com/astral-sh/ruff/pull/15877)) -
  \[`flake8-comprehensions`] Handle trailing comma in fixes for `unnecessary-generator-list/set`
  (`C400`,`C401`) ([#&#8203;15929](https://redirect.github.com/astral-sh/ruff/pull/15929)) -
  \[`flake8-pyi`] Fix several correctness issues with `custom-type-var-return-type` (`PYI019`)
  ([#&#8203;15851](https://redirect.github.com/astral-sh/ruff/pull/15851)) - \[`pep8-naming`]
  Consider any number of leading underscore for `N801`
  ([#&#8203;15988](https://redirect.github.com/astral-sh/ruff/pull/15988)) - \[`pyflakes`] Visit
  forward annotations in `TypeAliasType` as types (`F401`)
  ([#&#8203;15829](https://redirect.github.com/astral-sh/ruff/pull/15829)) - \[`pylint`] Correct
  min/max auto-fix and suggestion for (`PL1730`)
  ([#&#8203;15930](https://redirect.github.com/astral-sh/ruff/pull/15930)) - \[`refurb`] Handle
  unparenthesized tuples correctly (`FURB122`, `FURB142`)
  ([#&#8203;15953](https://redirect.github.com/astral-sh/ruff/pull/15953)) - \[`refurb`] Avoid `None
  | None` as well as better detection and fix (`FURB168`)
  ([#&#8203;15779](https://redirect.github.com/astral-sh/ruff/pull/15779))

- Add deprecation warning for `ruff-lsp` related settings
  ([#&#8203;15850](https://redirect.github.com/astral-sh/ruff/pull/15850)) - Docs (`linter.md`):
  clarify that Python files are always searched for in subdirectories
  ([#&#8203;15882](https://redirect.github.com/astral-sh/ruff/pull/15882)) - Fix a typo in
  `non_pep695_generic_class.rs`
  ([#&#8203;15946](https://redirect.github.com/astral-sh/ruff/pull/15946)) - Improve Docs: Pylint
  subcategories' codes ([#&#8203;15909](https://redirect.github.com/astral-sh/ruff/pull/15909)) -
  Remove non-existing `lint.extendIgnore` editor setting
  ([#&#8203;15844](https://redirect.github.com/astral-sh/ruff/pull/15844)) - Update black deviations
  ([#&#8203;15928](https://redirect.github.com/astral-sh/ruff/pull/15928)) - Mention `UP049` in
  `UP046` and `UP047`, add `See also` section to `UP040`
  ([#&#8203;15956](https://redirect.github.com/astral-sh/ruff/pull/15956)) - Add instance variable
  examples to `RUF012` ([#&#8203;15982](https://redirect.github.com/astral-sh/ruff/pull/15982)) -
  Explain precedence for `ignore` and `select` config
  ([#&#8203;15883](https://redirect.github.com/astral-sh/ruff/pull/15883))

### [`v0.9.4`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#094)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.9.3...0.9.4)

- \[`airflow`] Extend airflow context parameter check for `BaseOperator.execute` (`AIR302`)
  ([#&#8203;15713](https://redirect.github.com/astral-sh/ruff/pull/15713)) - \[`airflow`] Update
  `AIR302` to check for deprecated context keys
  ([#&#8203;15144](https://redirect.github.com/astral-sh/ruff/pull/15144)) - \[`flake8-bandit`]
  Permit suspicious imports within stub files (`S4`)
  ([#&#8203;15822](https://redirect.github.com/astral-sh/ruff/pull/15822)) - \[`pylint`] Do not
  trigger `PLR6201` on empty collections
  ([#&#8203;15732](https://redirect.github.com/astral-sh/ruff/pull/15732)) - \[`refurb`] Do not emit
  diagnostic when loop variables are used outside loop body (`FURB122`)
  ([#&#8203;15757](https://redirect.github.com/astral-sh/ruff/pull/15757)) - \[`ruff`] Add support
  for more `re` patterns (`RUF055`)
  ([#&#8203;15764](https://redirect.github.com/astral-sh/ruff/pull/15764)) - \[`ruff`] Check for
  shadowed `map` before suggesting fix (`RUF058`)
  ([#&#8203;15790](https://redirect.github.com/astral-sh/ruff/pull/15790)) - \[`ruff`] Do not emit
  diagnostic when all arguments to `zip()` are variadic (`RUF058`)
  ([#&#8203;15744](https://redirect.github.com/astral-sh/ruff/pull/15744)) - \[`ruff`] Parenthesize
  fix when argument spans multiple lines for `unnecessary-round` (`RUF057`)
  ([#&#8203;15703](https://redirect.github.com/astral-sh/ruff/pull/15703))

- Preserve quote style in generated code
  ([#&#8203;15726](https://redirect.github.com/astral-sh/ruff/pull/15726),
  [#&#8203;15778](https://redirect.github.com/astral-sh/ruff/pull/15778),
  [#&#8203;15794](https://redirect.github.com/astral-sh/ruff/pull/15794)) - \[`flake8-bugbear`]
  Exempt `NewType` calls where the original type is immutable (`B008`)
  ([#&#8203;15765](https://redirect.github.com/astral-sh/ruff/pull/15765)) - \[`pylint`] Honor
  banned top-level imports by `TID253` in `PLC0415`.
  ([#&#8203;15628](https://redirect.github.com/astral-sh/ruff/pull/15628)) - \[`pyupgrade`] Ignore
  `is_typeddict` and `TypedDict` for `deprecated-import` (`UP035`)
  ([#&#8203;15800](https://redirect.github.com/astral-sh/ruff/pull/15800))

- Fix formatter warning message for `flake8-quotes` option
  ([#&#8203;15788](https://redirect.github.com/astral-sh/ruff/pull/15788)) - Implement tab
  autocomplete for `ruff config`
  ([#&#8203;15603](https://redirect.github.com/astral-sh/ruff/pull/15603))

- \[`flake8-comprehensions`] Do not emit `unnecessary-map` diagnostic when lambda has different
  arity (`C417`) ([#&#8203;15802](https://redirect.github.com/astral-sh/ruff/pull/15802)) -
  \[`flake8-comprehensions`] Parenthesize `sorted` when needed for `unnecessary-call-around-sorted`
  (`C413`) ([#&#8203;15825](https://redirect.github.com/astral-sh/ruff/pull/15825)) - \[`pyupgrade`]
  Handle end-of-line comments for `quoted-annotation` (`UP037`)
  ([#&#8203;15824](https://redirect.github.com/astral-sh/ruff/pull/15824))

- Add missing config docstrings
  ([#&#8203;15803](https://redirect.github.com/astral-sh/ruff/pull/15803)) - Add references to
  `trio.run_process` and `anyio.run_process`
  ([#&#8203;15761](https://redirect.github.com/astral-sh/ruff/pull/15761)) - Use `uv init --lib` in
  tutorial ([#&#8203;15718](https://redirect.github.com/astral-sh/ruff/pull/15718))

### [`v0.9.3`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#093)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.9.2...0.9.3)

- \[`airflow`] Argument `fail_stop` in DAG has been renamed as `fail_fast` (`AIR302`)
  ([#&#8203;15633](https://redirect.github.com/astral-sh/ruff/pull/15633)) - \[`airflow`] Extend
  `AIR303` with more symbols
  ([#&#8203;15611](https://redirect.github.com/astral-sh/ruff/pull/15611)) - \[`flake8-bandit`]
  Report all references to suspicious functions (`S3`)
  ([#&#8203;15541](https://redirect.github.com/astral-sh/ruff/pull/15541)) -
  \[`flake8-pytest-style`] Do not emit diagnostics for empty `for` loops (`PT012`, `PT031`)
  ([#&#8203;15542](https://redirect.github.com/astral-sh/ruff/pull/15542)) - \[`flake8-simplify`]
  Avoid double negations (`SIM103`)
  ([#&#8203;15562](https://redirect.github.com/astral-sh/ruff/pull/15562)) - \[`pyflakes`] Fix
  infinite loop with unused local import in `__init__.py` (`F401`)
  ([#&#8203;15517](https://redirect.github.com/astral-sh/ruff/pull/15517)) - \[`pylint`] Do not
  report methods with only one `EM101`-compatible `raise` (`PLR6301`)
  ([#&#8203;15507](https://redirect.github.com/astral-sh/ruff/pull/15507)) - \[`pylint`] Implement
  `redefined-slots-in-subclass` (`W0244`)
  ([#&#8203;9640](https://redirect.github.com/astral-sh/ruff/pull/9640)) - \[`pyupgrade`] Add rules
  to use PEP 695 generics in classes and functions (`UP046`, `UP047`)
  ([#&#8203;15565](https://redirect.github.com/astral-sh/ruff/pull/15565),
  [#&#8203;15659](https://redirect.github.com/astral-sh/ruff/pull/15659)) - \[`refurb`] Implement
  `for-loop-writes` (`FURB122`)
  ([#&#8203;10630](https://redirect.github.com/astral-sh/ruff/pull/10630)) - \[`ruff`] Implement
  `needless-else` clause (`RUF047`)
  ([#&#8203;15051](https://redirect.github.com/astral-sh/ruff/pull/15051)) - \[`ruff`] Implement
  `starmap-zip` (`RUF058`) ([#&#8203;15483](https://redirect.github.com/astral-sh/ruff/pull/15483))

- \[`flake8-bugbear`] Do not raise error if keyword argument is present and target-python version is
  less or equals than 3.9 (`B903`)
  ([#&#8203;15549](https://redirect.github.com/astral-sh/ruff/pull/15549)) -
  \[`flake8-comprehensions`] strip parentheses around generators in `unnecessary-generator-set`
  (`C401`) ([#&#8203;15553](https://redirect.github.com/astral-sh/ruff/pull/15553)) -
  \[`flake8-pytest-style`] Rewrite references to `.exception` (`PT027`)
  ([#&#8203;15680](https://redirect.github.com/astral-sh/ruff/pull/15680)) - \[`flake8-simplify`]
  Mark fixes as unsafe (`SIM201`, `SIM202`)
  ([#&#8203;15626](https://redirect.github.com/astral-sh/ruff/pull/15626)) -
  \[`flake8-type-checking`] Fix some safe fixes being labeled unsafe (`TC006`,`TC008`)
  ([#&#8203;15638](https://redirect.github.com/astral-sh/ruff/pull/15638)) - \[`isort`] Omit
  trailing whitespace in `unsorted-imports` (`I001`)
  ([#&#8203;15518](https://redirect.github.com/astral-sh/ruff/pull/15518)) - \[`pydoclint`] Allow
  ignoring one line docstrings for `DOC` rules
  ([#&#8203;13302](https://redirect.github.com/astral-sh/ruff/pull/13302)) - \[`pyflakes`] Apply
  redefinition fixes by source code order (`F811`)
  ([#&#8203;15575](https://redirect.github.com/astral-sh/ruff/pull/15575)) - \[`pyflakes`] Avoid
  removing too many imports in `redefined-while-unused` (`F811`)
  ([#&#8203;15585](https://redirect.github.com/astral-sh/ruff/pull/15585)) - \[`pyflakes`] Group
  redefinition fixes by source statement (`F811`)
  ([#&#8203;15574](https://redirect.github.com/astral-sh/ruff/pull/15574)) - \[`pylint`] Include
  name of base class in message for `redefined-slots-in-subclass` (`W0244`)
  ([#&#8203;15559](https://redirect.github.com/astral-sh/ruff/pull/15559)) - \[`ruff`] Update fix
  for `RUF055` to use `var == value`
  ([#&#8203;15605](https://redirect.github.com/astral-sh/ruff/pull/15605))

- Fix bracket spacing for single-element tuples in f-string expressions
  ([#&#8203;15537](https://redirect.github.com/astral-sh/ruff/pull/15537)) - Fix unstable f-string
  formatting for expressions containing a trailing comma
  ([#&#8203;15545](https://redirect.github.com/astral-sh/ruff/pull/15545))

##### Performance

- Avoid quadratic membership check in import fixes
  ([#&#8203;15576](https://redirect.github.com/astral-sh/ruff/pull/15576))

- Allow `unsafe-fixes` settings for code actions
  ([#&#8203;15666](https://redirect.github.com/astral-sh/ruff/pull/15666))

- \[`flake8-bandit`] Add missing single-line/dotall regex flag (`S608`)
  ([#&#8203;15654](https://redirect.github.com/astral-sh/ruff/pull/15654)) -
  \[`flake8-import-conventions`] Fix infinite loop between `ICN001` and `I002` (`ICN001`)
  ([#&#8203;15480](https://redirect.github.com/astral-sh/ruff/pull/15480)) - \[`flake8-simplify`] Do
  not emit diagnostics for expressions inside string type annotations (`SIM222`, `SIM223`)
  ([#&#8203;15405](https://redirect.github.com/astral-sh/ruff/pull/15405)) - \[`pyflakes`] Treat
  arguments passed to the `default=` parameter of `TypeVar` as type expressions (`F821`)
  ([#&#8203;15679](https://redirect.github.com/astral-sh/ruff/pull/15679)) - \[`pyupgrade`] Avoid
  syntax error when the iterable is a non-parenthesized tuple (`UP028`)
  ([#&#8203;15543](https://redirect.github.com/astral-sh/ruff/pull/15543)) - \[`ruff`] Exempt
  `NewType` calls where the original type is immutable (`RUF009`)
  ([#&#8203;15588](https://redirect.github.com/astral-sh/ruff/pull/15588)) - Preserve raw string
  prefix and escapes in all codegen fixes
  ([#&#8203;15694](https://redirect.github.com/astral-sh/ruff/pull/15694))

- Generate documentation redirects for lowercase rule codes
  ([#&#8203;15564](https://redirect.github.com/astral-sh/ruff/pull/15564)) - `TRY300`: Add some
  extra notes on not catching exceptions you didn't expect
  ([#&#8203;15036](https://redirect.github.com/astral-sh/ruff/pull/15036))

### [`v0.9.2`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#092)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.9.1...0.9.2)

- \[`airflow`] Fix typo "security_managr" to "security_manager" (`AIR303`)
  ([#&#8203;15463](https://redirect.github.com/astral-sh/ruff/pull/15463)) - \[`airflow`] extend and
  fix AIR302 rules ([#&#8203;15525](https://redirect.github.com/astral-sh/ruff/pull/15525)) -
  \[`fastapi`] Handle parameters with `Depends` correctly (`FAST003`)
  ([#&#8203;15364](https://redirect.github.com/astral-sh/ruff/pull/15364)) -
  \[`flake8-pytest-style`] Implement pytest.warns diagnostics (`PT029`, `PT030`, `PT031`)
  ([#&#8203;15444](https://redirect.github.com/astral-sh/ruff/pull/15444)) -
  \[`flake8-pytest-style`] Test function parameters with default arguments (`PT028`)
  ([#&#8203;15449](https://redirect.github.com/astral-sh/ruff/pull/15449)) -
  \[`flake8-type-checking`] Avoid false positives for `|` in `TC008`
  ([#&#8203;15201](https://redirect.github.com/astral-sh/ruff/pull/15201))

- \[`flake8-todos`] Allow VSCode GitHub PR extension style links in `missing-todo-link` (`TD003`)
  ([#&#8203;15519](https://redirect.github.com/astral-sh/ruff/pull/15519)) - \[`pyflakes`] Show
  syntax error message for `F722`
  ([#&#8203;15523](https://redirect.github.com/astral-sh/ruff/pull/15523))

- Fix curly bracket spacing around f-string expressions containing curly braces
  ([#&#8203;15471](https://redirect.github.com/astral-sh/ruff/pull/15471)) - Fix joining of
  f-strings with different quotes when using quote style `Preserve`
  ([#&#8203;15524](https://redirect.github.com/astral-sh/ruff/pull/15524))

- Avoid indexing the same workspace multiple times
  ([#&#8203;15495](https://redirect.github.com/astral-sh/ruff/pull/15495)) - Display context for
  `ruff.configuration` errors
  ([#&#8203;15452](https://redirect.github.com/astral-sh/ruff/pull/15452))

- Remove `flatten` to improve deserialization error messages
  ([#&#8203;15414](https://redirect.github.com/astral-sh/ruff/pull/15414))

- Parse triple-quoted string annotations as if parenthesized
  ([#&#8203;15387](https://redirect.github.com/astral-sh/ruff/pull/15387)) - \[`fastapi`] Update
  `Annotated` fixes (`FAST002`)
  ([#&#8203;15462](https://redirect.github.com/astral-sh/ruff/pull/15462)) - \[`flake8-bandit`]
  Check for `builtins` instead of `builtin` (`S102`, `PTH123`)
  ([#&#8203;15443](https://redirect.github.com/astral-sh/ruff/pull/15443)) - \[`flake8-pathlib`] Fix
  `--select` for `os-path-dirname` (`PTH120`)
  ([#&#8203;15446](https://redirect.github.com/astral-sh/ruff/pull/15446)) - \[`ruff`] Fix false
  positive on global keyword (`RUF052`)
  ([#&#8203;15235](https://redirect.github.com/astral-sh/ruff/pull/15235))

### [`v0.9.1`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#091)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.9.0...0.9.1)

- \[`pycodestyle`] Run `too-many-newlines-at-end-of-file` on each cell in notebooks (`W391`)
  ([#&#8203;15308](https://redirect.github.com/astral-sh/ruff/pull/15308)) - \[`ruff`] Omit
  diagnostic for shadowed private function parameters in `used-dummy-variable` (`RUF052`)
  ([#&#8203;15376](https://redirect.github.com/astral-sh/ruff/pull/15376))

- \[`flake8-bugbear`] Improve `assert-raises-exception` message (`B017`)
  ([#&#8203;15389](https://redirect.github.com/astral-sh/ruff/pull/15389))

- Preserve trailing end-of line comments for the last string literal in implicitly concatenated
  strings ([#&#8203;15378](https://redirect.github.com/astral-sh/ruff/pull/15378))

- Fix a bug where the server and client notebooks were out of sync after reordering cells
  ([#&#8203;15398](https://redirect.github.com/astral-sh/ruff/pull/15398))

- \[`flake8-pie`] Correctly remove wrapping parentheses (`PIE800`)
  ([#&#8203;15394](https://redirect.github.com/astral-sh/ruff/pull/15394)) - \[`pyupgrade`] Handle
  comments and multiline expressions correctly (`UP037`)
  ([#&#8203;15337](https://redirect.github.com/astral-sh/ruff/pull/15337))

### [`v0.9.0`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#090)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.8.6...0.9.0)

Check out the [blog post](https://astral.sh/blog/ruff-v0.9.0) for a migration guide and overview of
  the changes!

##### Breaking changes

Ruff now formats your code according to the 2025 style guide. As a result, your code might now get
  formatted differently. See the formatter section for a detailed list of changes.

This release doesn’t remove or remap any existing stable rules.

##### Stabilization

The following rules have been stabilized and are no longer in preview:

- [`stdlib-module-shadowing`](https://docs.astral.sh/ruff/rules/stdlib-module-shadowing/) (`A005`).
  This rule has also been renamed: previously, it was called `builtin-module-shadowing`. -
  [`builtin-lambda-argument-shadowing`](https://docs.astral.sh/ruff/rules/builtin-lambda-argument-shadowing/)
  (`A006`) -
  [`slice-to-remove-prefix-or-suffix`](https://docs.astral.sh/ruff/rules/slice-to-remove-prefix-or-suffix/)
  (`FURB188`) -
  [`boolean-chained-comparison`](https://docs.astral.sh/ruff/rules/boolean-chained-comparison/)
  (`PLR1716`) -
  [`decimal-from-float-literal`](https://docs.astral.sh/ruff/rules/decimal-from-float-literal/)
  (`RUF032`) - [`post-init-default`](https://docs.astral.sh/ruff/rules/post-init-default/)
  (`RUF033`) - [`useless-if-else`](https://docs.astral.sh/ruff/rules/useless-if-else/) (`RUF034`)

The following behaviors have been stabilized:

-
  [`pytest-parametrize-names-wrong-type`](https://docs.astral.sh/ruff/rules/pytest-parametrize-names-wrong-type/)
  (`PT006`): Detect
  [`pytest.parametrize`](https://docs.pytest.org/en/7.1.x/how-to/parametrize.html#parametrize) calls
  outside decorators and calls with keyword arguments. -
  [`module-import-not-at-top-of-file`](https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file/)
  (`E402`): Ignore
  [`pytest.importorskip`](https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest-importorskip)
  calls between import statements. -
  [`mutable-dataclass-default`](https://docs.astral.sh/ruff/rules/mutable-dataclass-default/)
  (`RUF008`) and
  [`function-call-in-dataclass-default-argument`](https://docs.astral.sh/ruff/rules/function-call-in-dataclass-default-argument/)
  (`RUF009`): Add support for [`attrs`](https://www.attrs.org/en/stable/). -
  [`bad-version-info-comparison`](https://docs.astral.sh/ruff/rules/bad-version-info-comparison/)
  (`PYI006`): Extend the rule to check non-stub files.

The following fixes or improvements to fixes have been stabilized:

- [`redundant-numeric-union`](https://docs.astral.sh/ruff/rules/redundant-numeric-union/) (`PYI041`)
  - [`duplicate-union-members`](https://docs.astral.sh/ruff/rules/duplicate-union-member/)
  (`PYI016`)

This release introduces the new 2025 stable style
  ([#&#8203;13371](https://redirect.github.com/astral-sh/ruff/issues/13371)), stabilizing the
  following changes:

- Format expressions in f-string elements
  ([#&#8203;7594](https://redirect.github.com/astral-sh/ruff/issues/7594)) - Alternate quotes for
  strings inside f-strings ([#&#8203;13860](https://redirect.github.com/astral-sh/ruff/pull/13860))
  - Preserve the casing of hex codes in f-string debug expressions
  ([#&#8203;14766](https://redirect.github.com/astral-sh/ruff/issues/14766)) - Choose the quote
  style for each string literal in an implicitly concatenated f-string rather than for the entire
  string ([#&#8203;13539](https://redirect.github.com/astral-sh/ruff/pull/13539)) - Automatically
  join an implicitly concatenated string into a single string literal if it fits on a single line
  ([#&#8203;9457](https://redirect.github.com/astral-sh/ruff/issues/9457)) - Remove the
  [`ISC001`](https://docs.astral.sh/ruff/rules/single-line-implicit-string-concatenation/)
  incompatibility warning ([#&#8203;15123](https://redirect.github.com/astral-sh/ruff/pull/15123)) -
  Prefer parenthesizing the `assert` message over breaking the assertion expression
  ([#&#8203;9457](https://redirect.github.com/astral-sh/ruff/issues/9457)) - Automatically
  parenthesize over-long `if` guards in `match` `case` clauses
  ([#&#8203;13513](https://redirect.github.com/astral-sh/ruff/pull/13513)) - More consistent
  formatting for `match` `case` patterns
  ([#&#8203;6933](https://redirect.github.com/astral-sh/ruff/issues/6933)) - Avoid unnecessary
  parentheses around return type annotations
  ([#&#8203;13381](https://redirect.github.com/astral-sh/ruff/pull/13381)) - Keep the opening
  parentheses on the same line as the `if` keyword for comprehensions where the condition has a
  leading comment ([#&#8203;12282](https://redirect.github.com/astral-sh/ruff/pull/12282)) - More
  consistent formatting for `with` statements with a single context manager for Python 3.8 or older
  ([#&#8203;10276](https://redirect.github.com/astral-sh/ruff/pull/10276)) - Correctly calculate the
  line-width for code blocks in docstrings when using `max-doc-code-line-length = "dynamic"`
  ([#&#8203;13523](https://redirect.github.com/astral-sh/ruff/pull/13523))

- \[`flake8-bugbear`] Implement `class-as-data-structure` (`B903`)
  ([#&#8203;9601](https://redirect.github.com/astral-sh/ruff/pull/9601)) - \[`flake8-type-checking`]
  Apply `quoted-type-alias` more eagerly in `TYPE_CHECKING` blocks and ignore it in stubs (`TC008`)
  ([#&#8203;15180](https://redirect.github.com/astral-sh/ruff/pull/15180)) - \[`pylint`] Ignore
  `eq-without-hash` in stub files (`PLW1641`)
  ([#&#8203;15310](https://redirect.github.com/astral-sh/ruff/pull/15310)) - \[`pyupgrade`] Split
  `UP007` into two individual rules: `UP007` for `Union` and `UP045` for `Optional` (`UP007`,
  `UP045`) ([#&#8203;15313](https://redirect.github.com/astral-sh/ruff/pull/15313)) - \[`ruff`] New
  rule that detects classes that are both an enum and a `dataclass` (`RUF049`)
  ([#&#8203;15299](https://redirect.github.com/astral-sh/ruff/pull/15299)) - \[`ruff`] Recode
  `RUF025` to `RUF037` (`RUF037`)
  ([#&#8203;15258](https://redirect.github.com/astral-sh/ruff/pull/15258))

- \[`flake8-builtins`] Ignore
  [`stdlib-module-shadowing`](https://docs.astral.sh/ruff/rules/stdlib-module-shadowing/) in stub
  files(`A005`) ([#&#8203;15350](https://redirect.github.com/astral-sh/ruff/pull/15350)) -
  \[`flake8-return`] Add support for functions returning `typing.Never` (`RET503`)
  ([#&#8203;15298](https://redirect.github.com/astral-sh/ruff/pull/15298))

- Improve the observability by removing the need for the ["trace"
  value](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#traceValue)
  to turn on or off logging. The server logging is solely controlled using the [`logLevel` server
  setting](https://docs.astral.sh/ruff/editors/settings/#loglevel) which defaults to `info`. This
  addresses the issue where users were notified about an error and told to consult the log, but it
  didn’t contain any messages.
  ([#&#8203;15232](https://redirect.github.com/astral-sh/ruff/pull/15232)) - Ignore diagnostics from
  other sources for code action requests
  ([#&#8203;15373](https://redirect.github.com/astral-sh/ruff/pull/15373))

- Improve the error message for `--config key=value` when the `key` is for a table and it’s a simple
  `value`

- \[`eradicate`] Ignore metadata blocks directly followed by normal blocks (`ERA001`)
  ([#&#8203;15330](https://redirect.github.com/astral-sh/ruff/pull/15330)) - \[`flake8-django`]
  Recognize other magic methods (`DJ012`)
  ([#&#8203;15365](https://redirect.github.com/astral-sh/ruff/pull/15365)) - \[`pycodestyle`] Avoid
  false positives related to type aliases (`E252`)
  ([#&#8203;15356](https://redirect.github.com/astral-sh/ruff/pull/15356)) - \[`pydocstyle`] Avoid
  treating newline-separated sections as sub-sections (`D405`)
  ([#&#8203;15311](https://redirect.github.com/astral-sh/ruff/pull/15311)) - \[`pyflakes`] Remove
  call when removing final argument from `format` (`F523`)
  ([#&#8203;15309](https://redirect.github.com/astral-sh/ruff/pull/15309)) - \[`refurb`] Mark fix as
  unsafe when the right-hand side is a string (`FURB171`)
  ([#&#8203;15273](https://redirect.github.com/astral-sh/ruff/pull/15273)) - \[`ruff`] Treat `)` as
  a regex metacharacter (`RUF043`, `RUF055`)
  ([#&#8203;15318](https://redirect.github.com/astral-sh/ruff/pull/15318)) - \[`ruff`] Parenthesize
  the `int`-call argument when removing the `int` call would change semantics (`RUF046`)
  ([#&#8203;15277](https://redirect.github.com/astral-sh/ruff/pull/15277))

### [`v0.8.6`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#086)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.8.5...0.8.6)

- \[`format`]: Preserve multiline implicit concatenated strings in docstring positions
  ([#&#8203;15126](https://redirect.github.com/astral-sh/ruff/pull/15126)) - \[`ruff`] Add rule to
  detect empty literal in deque call (`RUF025`)
  ([#&#8203;15104](https://redirect.github.com/astral-sh/ruff/pull/15104)) - \[`ruff`] Avoid
  reporting when `ndigits` is possibly negative (`RUF057`)
  ([#&#8203;15234](https://redirect.github.com/astral-sh/ruff/pull/15234))

- \[`flake8-todos`] remove issue code length restriction (`TD003`)
  ([#&#8203;15175](https://redirect.github.com/astral-sh/ruff/pull/15175)) - \[`pyflakes`] Ignore
  errors in `@no_type_check` string annotations (`F722`, `F821`)
  ([#&#8203;15215](https://redirect.github.com/astral-sh/ruff/pull/15215))

- Show errors for attempted fixes only when passed `--verbose`
  ([#&#8203;15237](https://redirect.github.com/astral-sh/ruff/pull/15237))

- \[`ruff`] Avoid syntax error when removing int over multiple lines (`RUF046`)
  ([#&#8203;15230](https://redirect.github.com/astral-sh/ruff/pull/15230)) - \[`pyupgrade`] Revert
  "Add all PEP-585 names to `UP006` rule"
  ([#&#8203;15250](https://redirect.github.com/astral-sh/ruff/pull/15250))

### [`v0.8.5`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#085)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.8.4...0.8.5)

- \[`airflow`] Extend names moved from core to provider (`AIR303`)
  ([#&#8203;15145](https://redirect.github.com/astral-sh/ruff/pull/15145),
  [#&#8203;15159](https://redirect.github.com/astral-sh/ruff/pull/15159),
  [#&#8203;15196](https://redirect.github.com/astral-sh/ruff/pull/15196),
  [#&#8203;15216](https://redirect.github.com/astral-sh/ruff/pull/15216)) - \[`airflow`] Extend rule
  to check class attributes, methods, arguments (`AIR302`)
  ([#&#8203;15054](https://redirect.github.com/astral-sh/ruff/pull/15054),
  [#&#8203;15083](https://redirect.github.com/astral-sh/ruff/pull/15083)) - \[`fastapi`] Update
  `FAST002` to check keyword-only arguments
  ([#&#8203;15119](https://redirect.github.com/astral-sh/ruff/pull/15119)) -
  \[`flake8-type-checking`] Disable `TC006` and `TC007` in stub files
  ([#&#8203;15179](https://redirect.github.com/astral-sh/ruff/pull/15179)) - \[`pylint`] Detect
  nested methods correctly (`PLW1641`)
  ([#&#8203;15032](https://redirect.github.com/astral-sh/ruff/pull/15032)) - \[`ruff`] Detect more
  strict-integer expressions (`RUF046`)
  ([#&#8203;14833](https://redirect.github.com/astral-sh/ruff/pull/14833)) - \[`ruff`] Implement
  `falsy-dict-get-fallback` (`RUF056`)
  ([#&#8203;15160](https://redirect.github.com/astral-sh/ruff/pull/15160)) - \[`ruff`] Implement
  `unnecessary-round` (`RUF057`)
  ([#&#8203;14828](https://redirect.github.com/astral-sh/ruff/pull/14828))

- Visit PEP 764 inline `TypedDict` keys as non-type-expressions
  ([#&#8203;15073](https://redirect.github.com/astral-sh/ruff/pull/15073)) -
  \[`flake8-comprehensions`] Skip `C416` if comprehension contains unpacking
  ([#&#8203;14909](https://redirect.github.com/astral-sh/ruff/pull/14909)) - \[`flake8-pie`] Allow
  `cast(SomeType, ...)` (`PIE796`)
  ([#&#8203;15141](https://redirect.github.com/astral-sh/ruff/pull/15141)) - \[`flake8-simplify`]
  More precise inference for dictionaries (`SIM300`)
  ([#&#8203;15164](https://redirect.github.com/astral-sh/ruff/pull/15164)) - \[`flake8-use-pathlib`]
  Catch redundant joins in `PTH201` and avoid syntax errors
  ([#&#8203;15177](https://redirect.github.com/astral-sh/ruff/pull/15177)) - \[`pycodestyle`]
  Preserve original value format (`E731`)
  ([#&#8203;15097](https://redirect.github.com/astral-sh/ruff/pull/15097)) - \[`pydocstyle`] Split
  on first whitespace character (`D403`)
  ([#&#8203;15082](https://redirect.github.com/astral-sh/ruff/pull/15082)) - \[`pyupgrade`] Add all
  PEP-585 names to `UP006` rule
  ([#&#8203;5454](https://redirect.github.com/astral-sh/ruff/pull/5454))

- \[`flake8-type-checking`] Improve flexibility of `runtime-evaluated-decorators`
  ([#&#8203;15204](https://redirect.github.com/astral-sh/ruff/pull/15204)) - \[`pydocstyle`] Add
  setting to ignore missing documentation for `*args` and `**kwargs` parameters (`D417`)
  ([#&#8203;15210](https://redirect.github.com/astral-sh/ruff/pull/15210)) - \[`ruff`] Add an
  allowlist for `unsafe-markup-use` (`RUF035`)
  ([#&#8203;15076](https://redirect.github.com/astral-sh/ruff/pull/15076))

- Fix type subscript on older python versions
  ([#&#8203;15090](https://redirect.github.com/astral-sh/ruff/pull/15090)) - Use `TypeChecker` for
  detecting `fastapi` routes
  ([#&#8203;15093](https://redirect.github.com/astral-sh/ruff/pull/15093)) - \[`pycodestyle`] Avoid
  false positives and negatives related to type parameter default syntax (`E225`, `E251`)
  ([#&#8203;15214](https://redirect.github.com/astral-sh/ruff/pull/15214))

- Fix incorrect doc in `shebang-not-executable` (`EXE001`) and add git+windows solution to
  executable bit ([#&#8203;15208](https://redirect.github.com/astral-sh/ruff/pull/15208)) - Rename
  rules currently not conforming to naming convention
  ([#&#8203;15102](https://redirect.github.com/astral-sh/ruff/pull/15102))

### [`v0.8.4`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#084)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.8.3...0.8.4)

- \[`airflow`] Extend `AIR302` with additional functions and classes
  ([#&#8203;15015](https://redirect.github.com/astral-sh/ruff/pull/15015)) - \[`airflow`] Implement
  `moved-to-provider-in-3` for modules that has been moved to Airflow providers (`AIR303`)
  ([#&#8203;14764](https://redirect.github.com/astral-sh/ruff/pull/14764)) - \[`flake8-use-pathlib`]
  Extend check for invalid path suffix to include the case `"."` (`PTH210`)
  ([#&#8203;14902](https://redirect.github.com/astral-sh/ruff/pull/14902)) - \[`perflint`] Fix panic
  in `PERF401` when list variable is after the `for` loop
  ([#&#8203;14971](https://redirect.github.com/astral-sh/ruff/pull/14971)) - \[`perflint`] Simplify
  finding the loop target in `PERF401`
  ([#&#8203;15025](https://redirect.github.com/astral-sh/ruff/pull/15025)) - \[`pylint`] Preserve
  original value format (`PLR6104`)
  ([#&#8203;14978](https://redirect.github.com/astral-sh/ruff/pull/14978)) - \[`ruff`] Avoid false
  positives for `RUF027` for typing context bindings
  ([#&#8203;15037](https://redirect.github.com/astral-sh/ruff/pull/15037)) - \[`ruff`] Check for
  ambiguous pattern passed to `pytest.raises()` (`RUF043`)
  ([#&#8203;14966](https://redirect.github.com/astral-sh/ruff/pull/14966))

- \[`flake8-bandit`] Check `S105` for annotated assignment
  ([#&#8203;15059](https://redirect.github.com/astral-sh/ruff/pull/15059)) - \[`flake8-pyi`] More
  autofixes for `redundant-none-literal` (`PYI061`)
  ([#&#8203;14872](https://redirect.github.com/astral-sh/ruff/pull/14872)) - \[`pydocstyle`] Skip
  leading whitespace for `D403`
  ([#&#8203;14963](https://redirect.github.com/astral-sh/ruff/pull/14963)) - \[`ruff`] Skip
  `SQLModel` base classes for `mutable-class-default` (`RUF012`)
  ([#&#8203;14949](https://redirect.github.com/astral-sh/ruff/pull/14949))

##### Bug

- \[`perflint`] Parenthesize walrus expressions in autofix for `manual-list-comprehension`
  (`PERF401`) ([#&#8203;15050](https://redirect.github.com/astral-sh/ruff/pull/15050))

- Check diagnostic refresh support from client capability which enables dynamic configuration for
  various editors ([#&#8203;15014](https://redirect.github.com/astral-sh/ruff/pull/15014))

### [`v0.8.3`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#083)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.8.2...0.8.3)

- Fix fstring formatting removing overlong implicit concatenated string in expression part
  ([#&#8203;14811](https://redirect.github.com/astral-sh/ruff/pull/14811)) - \[`airflow`] Add fix to
  remove deprecated keyword arguments (`AIR302`)
  ([#&#8203;14887](https://redirect.github.com/astral-sh/ruff/pull/14887)) - \[`airflow`]: Extend
  rule to include deprecated names for Airflow 3.0 (`AIR302`)
  ([#&#8203;14765](https://redirect.github.com/astral-sh/ruff/pull/14765) and
  [#&#8203;14804](https://redirect.github.com/astral-sh/ruff/pull/14804)) - \[`flake8-bugbear`]
  Improve error messages for `except*` (`B025`, `B029`, `B030`, `B904`)
  ([#&#8203;14815](https://redirect.github.com/astral-sh/ruff/pull/14815)) - \[`flake8-bugbear`]
  `itertools.batched()` without explicit `strict` (`B911`)
  ([#&#8203;14408](https://redirect.github.com/astral-sh/ruff/pull/14408)) - \[`flake8-use-pathlib`]
  Dotless suffix passed to `Path.with_suffix()` (`PTH210`)
  ([#&#8203;14779](https://redirect.github.com/astral-sh/ruff/pull/14779)) - \[`pylint`] Include
  parentheses and multiple comparators in check for `boolean-chained-comparison` (`PLR1716`)
  ([#&#8203;14781](https://redirect.github.com/astral-sh/ruff/pull/14781)) - \[`ruff`] Do not
  simplify `round()` calls (`RUF046`)
  ([#&#8203;14832](https://redirect.github.com/astral-sh/ruff/pull/14832)) - \[`ruff`] Don't emit
  `used-dummy-variable` on function parameters (`RUF052`)
  ([#&#8203;14818](https://redirect.github.com/astral-sh/ruff/pull/14818)) - \[`ruff`] Implement
  `if-key-in-dict-del` (`RUF051`)
  ([#&#8203;14553](https://redirect.github.com/astral-sh/ruff/pull/14553)) - \[`ruff`] Mark autofix
  for `RUF052` as always unsafe
  ([#&#8203;14824](https://redirect.github.com/astral-sh/ruff/pull/14824)) - \[`ruff`] Teach autofix
  for `used-dummy-variable` about TypeVars etc. (`RUF052`)
  ([#&#8203;14819](https://redirect.github.com/astral-sh/ruff/pull/14819))

- \[`flake8-bugbear`] Offer unsafe autofix for `no-explicit-stacklevel` (`B028`)
  ([#&#8203;14829](https://redirect.github.com/astral-sh/ruff/pull/14829)) - \[`flake8-pyi`] Skip
  all type definitions in `string-or-bytes-too-long` (`PYI053`)
  ([#&#8203;14797](https://redirect.github.com/astral-sh/ruff/pull/14797)) - \[`pyupgrade`] Do not
  report when a UTF-8 comment is followed by a non-UTF-8 one (`UP009`)
  ([#&#8203;14728](https://redirect.github.com/astral-sh/ruff/pull/14728)) - \[`pyupgrade`] Mark
  fixes for `convert-typed-dict-functional-to-class` and `convert-named-tuple-functional-to-class`
  as unsafe if they will remove comments (`UP013`, `UP014`)
  ([#&#8203;14842](https://redirect.github.com/astral-sh/ruff/pull/14842))

- Raise syntax error for mixing `except` and `except*`
  ([#&#8203;14895](https://redirect.github.com/astral-sh/ruff/pull/14895)) - \[`flake8-bugbear`] Fix
  `B028` to allow `stacklevel` to be explicitly assigned as a positional argument
  ([#&#8203;14868](https://redirect.github.com/astral-sh/ruff/pull/14868)) - \[`flake8-bugbear`]
  Skip `B028` if `warnings.warn` is called with `*args` or `**kwargs`
  ([#&#8203;14870](https://redirect.github.com/astral-sh/ruff/pull/14870)) -
  \[`flake8-comprehensions`] Skip iterables with named expressions in `unnecessary-map` (`C417`)
  ([#&#8203;14827](https://redirect.github.com/astral-sh/ruff/pull/14827)) - \[`flake8-pyi`] Also
  remove `self` and `cls`'s annotation (`PYI034`)
  ([#&#8203;14801](https://redirect.github.com/astral-sh/ruff/pull/14801)) -
  \[`flake8-pytest-style`] Fix `pytest-parametrize-names-wrong-type` (`PT006`) to edit both
  `argnames` and `argvalues` if both of them are single-element tuples/lists
  ([#&#8203;14699](https://redirect.github.com/astral-sh/ruff/pull/14699)) - \[`perflint`] Improve
  autofix for `PERF401` ([#&#8203;14369](https://redirect.github.com/astral-sh/ruff/pull/14369)) -
  \[`pylint`] Fix `PLW1508` false positive for default string created via a mult operation
  ([#&#8203;14841](https://redirect.github.com/astral-sh/ruff/pull/14841))

### [`v0.8.2`](https://redirect.github.com/astral-sh/ruff/blob/HEAD/CHANGELOG.md#082)

[Compare Source](https://redirect.github.com/astral-sh/ruff/compare/0.8.1...0.8.2)

- \[`airflow`] Avoid deprecated values (`AIR302`)
  ([#&#8203;14582](https://redirect.github.com/astral-sh/ruff/pull/14582)) - \[`airflow`] Extend
  removed names for `AIR302`
  ([#&#8203;14734](https://redirect.github.com/astral-sh/ruff/pull/14734)) - \[`ruff`] Extend
  `unnecessary-regular-expression` to non-literal strings (`RUF055`)
  ([#&#8203;14679](https://redirect.github.com/astral-sh/ruff/pull/14679)) - \[`ruff`] Implement
  `used-dummy-variable` (`RUF052`)
  ([#&#8203;14611](https://redirect.github.com/astral-sh/ruff/pull/14611)) - \[`ruff`] Implement
  `unnecessary-cast-to-int` (`RUF046`)
  ([#&#8203;14697](https://redirect.github.com/astral-sh/ruff/pull/14697))

- \[`airflow`] Check `AIR001` from builtin or providers `operators` module
  ([#&#8203;14631](https://redirect.github.com/astral-sh/ruff/pull/14631)) -
  \[`flake8-pytest-style`] Remove `@` in `pytest.mark.parametrize` rule messages
  ([#&#8203;14770](https://redirect.github.com/astral-sh/ruff/pull/14770)) - \[`pandas-vet`] Skip
  rules if the `panda` module hasn't been seen
  ([#&#8203;14671](https://redirect.github.com/astral-sh/ruff/pull/14671)) - \[`pylint`] Fix false
  negatives for `ascii` and `sorted` in `len-as-condition` (`PLC1802`)
  ([#&#8203;14692](https://redirect.github.com/astral-sh/ruff/pull/14692)) - \[`refurb`] Guard
  `hashlib` imports and mark `hashlib-digest-hex` fix as safe (`FURB181`)
  ([#&#8203;14694](https://redirect.github.com/astral-sh/ruff/pull/14694))

- \[`flake8-import-conventions`] Improve syntax check for aliases supplied in configuration for
  `unconventional-import-alias` (`ICN001`)
  ([#&#8203;14745](https://redirect.github.com/astral-sh/ruff/pull/14745))

- Revert: \[pyflakes] Avoid false positives in `@no_type_check` contexts (`F821`, `F722`)
  ([#&#8203;14615](https://redirect.github.com/astral-sh/ruff/issues/14615))
  ([#&#8203;14726](https://redirect.github.com/astral-sh/ruff/pull/14726)) - \[`pep8-naming`] Avoid
  false positive for `class Bar(type(foo))` (`N804`)
  ([#&#8203;14683](https://redirect.github.com/astral-sh/ruff/pull/14683)) - \[`pycodestyle`] Handle
  f-strings properly for `invalid-escape-sequence` (`W605`)
  ([#&#8203;14748](https://redirect.github.com/astral-sh/ruff/pull/14748)) - \[`pylint`] Ignore
  `@overload` in `PLR0904` ([#&#8203;14730](https://redirect.github.com/astral-sh/ruff/pull/14730))
  - \[`refurb`] Handle non-finite decimals in `verbose-decimal-constructor` (`FURB157`)
  ([#&#8203;14596](https://redirect.github.com/astral-sh/ruff/pull/14596)) - \[`ruff`] Avoid
  emitting `assignment-in-assert` when all references to the assigned variable are themse

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xODUuNCIsInVwZGF0ZWRJblZlciI6IjM5LjE4NS40IiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency syrupy to v4.9.0
  ([#826](https://github.com/MartinBernstorff/Memium/pull/826),
  [`5d89cb3`](https://github.com/MartinBernstorff/Memium/commit/5d89cb3cd0b3c2eca0dcc3d4fc78bf9ea423e2fa))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [syrupy](https://redirect.github.com/syrupy-project/syrupy) | `==4.8.1` -> `==4.9.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/syrupy/4.9.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/syrupy/4.9.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/syrupy/4.8.1/4.9.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/syrupy/4.8.1/4.9.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>syrupy-project/syrupy (syrupy)</summary>

###
  [`v4.9.0`](https://redirect.github.com/syrupy-project/syrupy/blob/HEAD/CHANGELOG.md#490-2025-03-08)

[Compare Source](https://redirect.github.com/syrupy-project/syrupy/compare/v4.8.3...v4.9.0)

##### Bug Fixes

- **serializer:** raise TypeError when serializing non-byte like object in binary mode
  ([#&#8203;951](https://redirect.github.com/syrupy-project/syrupy/issues/951))
  ([2bd0f54](https://redirect.github.com/syrupy-project/syrupy/commit/2bd0f54ea0923f4c549209abc40d2eec9b973d65))

##### Features

- add --snapshot-ignore-file-extensions argument to support DVC
  ([#&#8203;943](https://redirect.github.com/syrupy-project/syrupy/issues/943))
  ([056cc6e](https://redirect.github.com/syrupy-project/syrupy/commit/056cc6e1057f6d1c49b4b609aa09be9f507dd55c))
  - add compose_matchers utility for composing 1 or more matchers
  ([#&#8203;952](https://redirect.github.com/syrupy-project/syrupy/issues/952))
  ([157dbec](https://redirect.github.com/syrupy-project/syrupy/commit/157dbecc87fd03ea938c4a7dc194418da43c90a5))
  - add SingleFileAmberSnapshotExtension as a single-file variant of the default amber extension
  ([#&#8203;959](https://redirect.github.com/syrupy-project/syrupy/issues/959))
  ([a753b7a](https://redirect.github.com/syrupy-project/syrupy/commit/a753b7a0aa6763a7489da78291bf27b7b5081b74))
  - include details about created/updated snapshots in detailed report
  ([#&#8203;942](https://redirect.github.com/syrupy-project/syrupy/issues/942))
  ([25d37ef](https://redirect.github.com/syrupy-project/syrupy/commit/25d37ef978cbbd5b034fe394d283e923295b1750))

#### [4.8.3](https://redirect.github.com/syrupy-project/syrupy/compare/v4.8.2...v4.8.3) (2025-03-08)

- snapshots of deselected parametrized tests wrongly marked as unused
  ([#&#8203;965](https://redirect.github.com/syrupy-project/syrupy/issues/965))
  ([52f3bb2](https://redirect.github.com/syrupy-project/syrupy/commit/52f3bb2089f6289ef6502486301d56d7b13fdf28))

#### [4.8.2](https://redirect.github.com/syrupy-project/syrupy/compare/v4.8.1...v4.8.2) (2025-02-20)

- avoid unnecessary env updates to reduce chances of segfault
  ([#&#8203;956](https://redirect.github.com/syrupy-project/syrupy/issues/956))
  ([7fdffd9](https://redirect.github.com/syrupy-project/syrupy/commit/7fdffd906dc851d8ff7aa0327b6a8bdb5d0cbed5))

#### [4.8.1](https://redirect.github.com/syrupy-project/syrupy/compare/v4.8.0...v4.8.1) (2025-01-13)

- check current session's pending-write queue when recalling snapshots (e.g. diffing)
  ([#&#8203;927](https://redirect.github.com/syrupy-project/syrupy/issues/927))
  ([0f6bb55](https://redirect.github.com/syrupy-project/syrupy/commit/0f6bb55000593e5d5198feb2bd9ccbb1376a37fb))

###
  [`v4.8.3`](https://redirect.github.com/syrupy-project/syrupy/blob/HEAD/CHANGELOG.md#483-2025-03-08)

[Compare Source](https://redirect.github.com/syrupy-project/syrupy/compare/v4.8.2...v4.8.3)

###
  [`v4.8.2`](https://redirect.github.com/syrupy-project/syrupy/blob/HEAD/CHANGELOG.md#482-2025-02-20)

[Compare Source](https://redirect.github.com/syrupy-project/syrupy/compare/v4.8.1...v4.8.2)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xODUuNCIsInVwZGF0ZWRJblZlciI6IjM5LjE4NS40IiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency syrupy to v4.9.1
  ([#841](https://github.com/MartinBernstorff/Memium/pull/841),
  [`9658ec5`](https://github.com/MartinBernstorff/Memium/commit/9658ec5caae94f45af26eb9e86ca9150ae880116))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [syrupy](https://redirect.github.com/syrupy-project/syrupy) | `==4.9.0` -> `==4.9.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/syrupy/4.9.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/syrupy/4.9.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/syrupy/4.9.0/4.9.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/syrupy/4.9.0/4.9.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>syrupy-project/syrupy (syrupy)</summary>

###
  [`v4.9.1`](https://redirect.github.com/syrupy-project/syrupy/blob/HEAD/CHANGELOG.md#491-2025-03-24)

[Compare Source](https://redirect.github.com/syrupy-project/syrupy/compare/v4.9.0...v4.9.1)

##### Bug Fixes

- **serializer:** preserve trailing newlines in ambr serialization
  ([#&#8203;950](https://redirect.github.com/syrupy-project/syrupy/issues/950))
  ([5897490](https://redirect.github.com/syrupy-project/syrupy/commit/5897490e9821156327fe56bc5f7695146e2363a5))
  - **serializer:** preserve trailing newlines in ambr serialization
  ([#&#8203;950](https://redirect.github.com/syrupy-project/syrupy/issues/950))
  ([5037477](https://redirect.github.com/syrupy-project/syrupy/commit/5037477ceece0f2cf861aabd356f4dd07a9eeb71))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4yMDcuMSIsInVwZGF0ZWRJblZlciI6IjM5LjIwNy4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Documentation

- Update readme.md
  ([`f2350fa`](https://github.com/MartinBernstorff/Memium/commit/f2350fa153f0e822e354b1def26e3f70a32f8977))

- Update readme.md
  ([`94ebd97`](https://github.com/MartinBernstorff/Memium/commit/94ebd972b948b66bfe47d0339a659ee29a7b6042))

### Features

- **ci**: Migrate to uv ([#824](https://github.com/MartinBernstorff/Memium/pull/824),
  [`d2256cc`](https://github.com/MartinBernstorff/Memium/commit/d2256cc686b23f598f2ca82ab1f5117a73ca588d))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.26.0 (2025-03-06)

### Bug Fixes

- Better identity for QA
  ([`bfa53d9`](https://github.com/MartinBernstorff/Memium/commit/bfa53d9bcfaf9ea2d46f403992bf35feb0217609))

- **deps**: Update dependency pyright to v1.1.396
  ([#816](https://github.com/MartinBernstorff/Memium/pull/816),
  [`7dd103c`](https://github.com/MartinBernstorff/Memium/commit/7dd103c09de79620be417ce75ebe78577c17339f))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pyright](https://redirect.github.com/RobertCraigie/pyright-python) | `==1.1.393` -> `==1.1.396` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pyright/1.1.396?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pyright/1.1.396?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pyright/1.1.393/1.1.396?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pyright/1.1.393/1.1.396?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>RobertCraigie/pyright-python (pyright)</summary>

###
  [`v1.1.396`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.395...v1.1.396)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.395...v1.1.396)

###
  [`v1.1.395`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.394...v1.1.395)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.394...v1.1.395)

###
  [`v1.1.394`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.393...v1.1.394)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.393...v1.1.394)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xNjQuMSIsInVwZGF0ZWRJblZlciI6IjM5LjE3Ni4yIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency pytest to v8.3.5
  ([#823](https://github.com/MartinBernstorff/Memium/pull/823),
  [`32ca4ef`](https://github.com/MartinBernstorff/Memium/commit/32ca4eff181fc6bce310d048c6269148a793af25))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pytest](https://redirect.github.com/pytest-dev/pytest)
  ([changelog](https://docs.pytest.org/en/stable/changelog.html)) | `==8.3.4` -> `==8.3.5` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pytest/8.3.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pytest/8.3.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pytest/8.3.4/8.3.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pytest/8.3.4/8.3.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pytest-dev/pytest (pytest)</summary>

### [`v8.3.5`](https://redirect.github.com/pytest-dev/pytest/releases/tag/8.3.5)

[Compare Source](https://redirect.github.com/pytest-dev/pytest/compare/8.3.4...8.3.5)

### pytest 8.3.5 (2025-03-02)

#### Bug fixes

- [#&#8203;11777](https://redirect.github.com/pytest-dev/pytest/issues/11777): Fixed issue where
  sequences were still being shortened even with `-vv` verbosity. -
  [#&#8203;12888](https://redirect.github.com/pytest-dev/pytest/issues/12888): Fixed broken input
  when using Python 3.13+ and a `libedit` build of Python, such as on macOS or with uv-managed
  Python binaries from the `python-build-standalone` project. This could manifest e.g. by a broken
  prompt when using `Pdb`, or seeing empty inputs with manual usage of `input()` and suspended
  capturing. - [#&#8203;13026](https://redirect.github.com/pytest-dev/pytest/issues/13026): Fixed
  `AttributeError`{.interpreted-text role="class"} crash when using `--import-mode=importlib` when
  top-level directory same name as another module of the standard library. -
  [#&#8203;13053](https://redirect.github.com/pytest-dev/pytest/issues/13053): Fixed a regression in
  pytest 8.3.4 where, when using `--import-mode=importlib`, a directory containing py file with the
  same name would cause an `ImportError` -
  [#&#8203;13083](https://redirect.github.com/pytest-dev/pytest/issues/13083): Fixed issue where
  pytest could crash if one of the collected directories got removed during collection.

#### Improved documentation

- [#&#8203;12842](https://redirect.github.com/pytest-dev/pytest/issues/12842): Added dedicated page
  about using types with pytest.

See `types`{.interpreted-text role="ref"} for detailed usage.

#### Contributor-facing changes

- [#&#8203;13112](https://redirect.github.com/pytest-dev/pytest/issues/13112): Fixed selftest
  failures in `test_terminal.py` with Pygments >= 2.19.0 -
  [#&#8203;13256](https://redirect.github.com/pytest-dev/pytest/issues/13256): Support for Towncier
  versions released in 2024 has been re-enabled when building Sphinx docs -- by
  `webknjaz`{.interpreted-text role="user"}.

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xNzYuMiIsInVwZGF0ZWRJblZlciI6IjM5LjE3Ni4yIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency ruff to v0.9.9
  ([`6fb54ab`](https://github.com/MartinBernstorff/Memium/commit/6fb54ab36d860f01e54a558ba3c052594e94f4d0))

- **deps**: Update dependency syrupy to v4.8.2
  ([#819](https://github.com/MartinBernstorff/Memium/pull/819),
  [`01ea7a2`](https://github.com/MartinBernstorff/Memium/commit/01ea7a2ee7828dbce1f69d9302c259b369f307f9))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [syrupy](https://redirect.github.com/syrupy-project/syrupy) | `==4.8.1` -> `==4.8.2` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/syrupy/4.8.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/syrupy/4.8.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/syrupy/4.8.1/4.8.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/syrupy/4.8.1/4.8.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>syrupy-project/syrupy (syrupy)</summary>

###
  [`v4.8.2`](https://redirect.github.com/syrupy-project/syrupy/blob/HEAD/CHANGELOG.md#482-2025-02-20)

[Compare Source](https://redirect.github.com/syrupy-project/syrupy/compare/v4.8.1...v4.8.2)

##### Bug Fixes

- avoid unnecessary env updates to reduce chances of segfault
  ([#&#8203;956](https://redirect.github.com/syrupy-project/syrupy/issues/956))
  ([7fdffd9](https://redirect.github.com/syrupy-project/syrupy/commit/7fdffd906dc851d8ff7aa0327b6a8bdb5d0cbed5))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xNzYuMiIsInVwZGF0ZWRJblZlciI6IjM5LjE3Ni4yIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency typer to v0.15.2
  ([#820](https://github.com/MartinBernstorff/Memium/pull/820),
  [`fa6e417`](https://github.com/MartinBernstorff/Memium/commit/fa6e41780e1f8ccbba013d3362643b653cbc8803))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [typer](https://redirect.github.com/fastapi/typer)
  ([changelog](https://typer.tiangolo.com/release-notes/)) | `==0.15.1` -> `==0.15.2` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/typer/0.15.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/typer/0.15.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/typer/0.15.1/0.15.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/typer/0.15.1/0.15.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>fastapi/typer (typer)</summary>

### [`v0.15.2`](https://redirect.github.com/fastapi/typer/releases/tag/0.15.2)

[Compare Source](https://redirect.github.com/fastapi/typer/compare/0.15.1...0.15.2)

##### Features

- ✨ Allow custom styles for commands in help output. PR
  [#&#8203;1103](https://redirect.github.com/fastapi/typer/pull/1103) by
  [@&#8203;TheTechromancer](https://redirect.github.com/TheTechromancer). - ✨ Avoid the unnecessary
  import of `typing_extensions` in newer Python versions. PR
  [#&#8203;1048](https://redirect.github.com/fastapi/typer/pull/1048) by
  [@&#8203;horta](https://redirect.github.com/horta).

##### Fixes

- 🐛 Fix shell completions for the fish shell. PR
  [#&#8203;1069](https://redirect.github.com/fastapi/typer/pull/1069) by
  [@&#8203;goraje](https://redirect.github.com/goraje).

##### Refactors

- 🚚 Rename test to corner-cases to make it more explicit. PR
  [#&#8203;1083](https://redirect.github.com/fastapi/typer/pull/1083) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo).

##### Docs

- ✏️ Fix small typos in the tutorial documentation. PR
  [#&#8203;1137](https://redirect.github.com/fastapi/typer/pull/1137) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - 📝 Update optional CLI argument section
  in tutorial with `Annotated`. PR [#&#8203;983](https://redirect.github.com/fastapi/typer/pull/983)
  by [@&#8203;gkeuccsr](https://redirect.github.com/gkeuccsr). - 📝 Clarify the need for `mix_stderr`
  when accessing the output of `stderr` in tests. PR
  [#&#8203;1045](https://redirect.github.com/fastapi/typer/pull/1045) by
  [@&#8203;mrchrisadams](https://redirect.github.com/mrchrisadams).

##### Internal

- 🔧 Add support for Python 3.13, tests in CI and add PyPI trove classifier. PR
  [#&#8203;1091](https://redirect.github.com/fastapi/typer/pull/1091) by
  [@&#8203;edgarrmondragon](https://redirect.github.com/edgarrmondragon). - ⬆ Bump ruff from 0.9.6
  to 0.9.7. PR [#&#8203;1161](https://redirect.github.com/fastapi/typer/pull/1161) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1162](https://redirect.github.com/fastapi/typer/pull/1162) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.9.5 to 0.9.6. PR [#&#8203;1153](https://redirect.github.com/fastapi/typer/pull/1153) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1151](https://redirect.github.com/fastapi/typer/pull/1151) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.9.4 to 0.9.5. PR [#&#8203;1146](https://redirect.github.com/fastapi/typer/pull/1146) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1142](https://redirect.github.com/fastapi/typer/pull/1142) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.9.3 to 0.9.4. PR [#&#8203;1139](https://redirect.github.com/fastapi/typer/pull/1139) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1135](https://redirect.github.com/fastapi/typer/pull/1135) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.9.1 to 0.9.3. PR [#&#8203;1136](https://redirect.github.com/fastapi/typer/pull/1136) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1130](https://redirect.github.com/fastapi/typer/pull/1130) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.8.6 to 0.9.1. PR [#&#8203;1118](https://redirect.github.com/fastapi/typer/pull/1118) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  pypa/gh-action-pypi-publish from 1.12.3 to 1.12.4. PR
  [#&#8203;1132](https://redirect.github.com/fastapi/typer/pull/1132) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump mkdocs-material
  from 9.5.49 to 9.5.50. PR [#&#8203;1129](https://redirect.github.com/fastapi/typer/pull/1129) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - 💚 Fix test matrix for
  Python 3.7. PR [#&#8203;1116](https://redirect.github.com/fastapi/typer/pull/1116) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - ⬆ Bump ruff from 0.8.4 to 0.8.6. PR
  [#&#8203;1107](https://redirect.github.com/fastapi/typer/pull/1107) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1109](https://redirect.github.com/fastapi/typer/pull/1109) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump pillow
  from 11.0.0 to 11.1.0. PR [#&#8203;1104](https://redirect.github.com/fastapi/typer/pull/1104) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1102](https://redirect.github.com/fastapi/typer/pull/1102) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.8.3 to 0.8.4. PR [#&#8203;1097](https://redirect.github.com/fastapi/typer/pull/1097) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  astral-sh/setup-uv from 4 to 5. PR
  [#&#8203;1098](https://redirect.github.com/fastapi/typer/pull/1098) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  markdown-include-variants from 0.0.3 to 0.0.4. PR
  [#&#8203;1100](https://redirect.github.com/fastapi/typer/pull/1100) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump ruff from 0.8.2
  to 0.8.3. PR [#&#8203;1090](https://redirect.github.com/fastapi/typer/pull/1090) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1093](https://redirect.github.com/fastapi/typer/pull/1093) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump
  mkdocs-material from 9.5.48 to 9.5.49. PR
  [#&#8203;1092](https://redirect.github.com/fastapi/typer/pull/1092) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  pypa/gh-action-pypi-publish from 1.12.2 to 1.12.3. PR
  [#&#8203;1088](https://redirect.github.com/fastapi/typer/pull/1088) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1087](https://redirect.github.com/fastapi/typer/pull/1087) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.8.1 to 0.8.2. PR [#&#8203;1084](https://redirect.github.com/fastapi/typer/pull/1084) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump mkdocs-material
  from 9.5.47 to 9.5.48. PR [#&#8203;1086](https://redirect.github.com/fastapi/typer/pull/1086) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot).

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xNzYuMiIsInVwZGF0ZWRJblZlciI6IjM5LjE3Ni4yIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Build System

- Update makefile
  ([`d3c13ce`](https://github.com/MartinBernstorff/Memium/commit/d3c13ceedb8d9677d88b24de17d97cddb0da7e07))

- **deps**: Update test_extractor_table.py, hash_cleaned_str.py, pyproject.toml and tasks.py
  ([`b42a387`](https://github.com/MartinBernstorff/Memium/commit/b42a3878c1731f241cec0f291f90b6f8181acdb9))

### Chores

- Misc.
  ([`a75aa02`](https://github.com/MartinBernstorff/Memium/commit/a75aa029f07f2b5138915fa0d4dd15e5497a9ee0))

- Update launch.json
  ([`e13bca9`](https://github.com/MartinBernstorff/Memium/commit/e13bca95af71d6b07b3def849cf0f7ccdccb55ad))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.21.0
  ([#813](https://github.com/MartinBernstorff/Memium/pull/813),
  [`804345e`](https://github.com/MartinBernstorff/Memium/commit/804345e95d587a5f7bbd1bf691f22055eab03b08))

This PR contains the following updates:

| Package | Type | Update | Change | |---|---|---|---| |
  [python-semantic-release/python-semantic-release](https://redirect.github.com/python-semantic-release/python-semantic-release)
  | action | minor | `v9.17.0` -> `v9.21.0` |

---

### Release Notes

<details> <summary>python-semantic-release/python-semantic-release
  (python-semantic-release/python-semantic-release)</summary>

###
  [`v9.21.0`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.rst#v9210-2025-02-23)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.20.0...v9.21.0)

\====================

## ✨ Features

- Add package name variant, `python-semantic-release`, project script, closes `#1195`\_ (`PR#1199`*,
  `1ac97bc`*)

## 📖 Documentation

- **github-actions**: Update example workflow to handle rapid merges (`PR#1200`*, `1a4116a`*)

..
  \_#1195:[https://github.com/python-semantic-release/python-semantic-release/issues/1195](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1195)5
  .. \_1a4116a:
  https://github.com/python-semantic-release/python-semantic-release/commit/1a4116af4b999144998cf94cf84c9c23ff2e352f
  .. \_1ac97bc:
  https://github.com/python-semantic-release/python-semantic-release/commit/1ac97bc74c69ce61cec98242c19bf8adc1d37fb9
  ..
  \_PR#11[https://github.com/python-semantic-release/python-semantic-release/pull/1199](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1199)1199
  ..
  \_PR#1[https://github.com/python-semantic-release/python-semantic-release/pull/1200](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1200)/1200

.. \_changelog-v9.20.0:

###
  [`v9.20.0`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.rst#v9200-2025-02-17)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.19.1...v9.20.0)

- **cmd-version**: Enable stamping of tag formatted versions into files, closes `#846`\_
  (`PR#1190`*, `8906d8e`*)

- **cmd-version**: Extend `version_variables` to stamp versions with `@` symbol separator, closes
  `#1156`\_ (`PR#1185`*, `23f69b6`*)

- **configuration**: Add usage information for tag format version stamping (`PR#1190`*, `8906d8e`*)

- **configuration**: Clarify `version_variables` config description & `@` separator usage
  (`PR#1185`*, `23f69b6`*)

## ⚙️ Build System

- **deps**: Add `deprecated~=1.2` for deprecation notices & sphinx documentation (`PR#1190`*,
  `8906d8e`*)

..
  \_#1156:[https://github.com/python-semantic-release/python-semantic-release/issues/1156](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1156)6
  ..
  \_#846[https://github.com/python-semantic-release/python-semantic-release/issues/846](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/846)46
  .. \_23f69b6:
  https://github.com/python-semantic-release/python-semantic-release/commit/23f69b6ac206d111b1e566367f9b2f033df5c87a
  .. \_8906d8e:
  https://github.com/python-semantic-release/python-semantic-release/commit/8906d8e70467af1489d797ec8cb09b1f95e5d409
  ..
  \_PR#1[https://github.com/python-semantic-release/python-semantic-release/pull/1185](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1185)/1185
  ..
  \_PR#[https://github.com/python-semantic-release/python-semantic-release/pull/1190](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1190)l/1190

.. \_changelog-v9.19.1:

###
  [`v9.19.1`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.rst#v9191-2025-02-11)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.19.0...v9.19.1)

## 🪲 Bug Fixes

- **changelog**: Standardize heading format for across all version sections (`PR#1182`*, `81f9e80`*)

- **changelog-md**: Standardize heading format for extra release information (`PR#1182`*,
  `81f9e80`*)

- **changelog-rst**: Standardize heading format for extra release information (`PR#1182`*,
  `81f9e80`*)

- **config**: Handle invalid `commit_parser` type gracefully (`PR#1180`*, `903c8ba`*)

- **release-notes**: Standardize heading format for extra release information (`PR#1182`*,
  `81f9e80`*)

- Fix spelling errors & inaccurate descriptions (`55d4a05`\_)

- **automatic-releases**: Declutter the table of contents for automatic release guides (`e8343ee`\_)

- **commit-parsing**: Update reference to section name of additional release info (`PR#1182`*,
  `81f9e80`*)

.. \_55d4a05:
  https://github.com/python-semantic-release/python-semantic-release/commit/55d4a05ff56321cf9874f8f302fbe7e5163ad4f7
  .. \_81f9e80:
  https://github.com/python-semantic-release/python-semantic-release/commit/81f9e80c3df185ef5e553e024b903ce153e14304
  .. \_903c8ba:
  https://github.com/python-semantic-release/python-semantic-release/commit/903c8ba68d797f7cd9e5025c9a3a3ad471c805ae
  .. \_e8343ee:
  https://github.com/python-semantic-release/python-semantic-release/commit/e8343eeb38d3b4e18953ac0f97538df396d22b76
  ..
  \_PR#1[https://github.com/python-semantic-release/python-semantic-release/pull/1180](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1180)/1180
  ..
  \_PR#[https://github.com/python-semantic-release/python-semantic-release/pull/1182](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1182)l/1182

.. \_changelog-v9.19.0:

###
  [`v9.19.0`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.rst#v9190-2025-02-10)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.18.1...v9.19.0)

- **parser-conventional**: Add official `conventional-commits` parser (`PR#1177`*, `27ddf84`*)

- Update references to Angular parser to Conventional Commit Parser (`PR#1177`*, `27ddf84`*)

## 💡 ADDITIONAL RELEASE INFORMATION

- **parser-conventional**: The 'angular' commit parser has been renamed to 'conventional' to match
  the official conventional-commits standard for which the 'angular' parser has evolved into. Please
  update your configurations to specify 'conventional' as the 'commit_parser' value in place of
  'angular'. The 'angular' type will be removed in v11.

.. \_27ddf84:
  https://github.com/python-semantic-release/python-semantic-release/commit/27ddf840f8c812361c60bac9cf0b110d401f33d6
  ..
  \_PR#1177[https://github.com/python-semantic-release/python-semantic-release/pull/1177](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1177)77

.. \_changelog-v9.18.1:

###
  [`v9.18.1`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.rst#v9181-2025-02-08)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.18.0...v9.18.1)

- **config**: Refactors default token resolution to prevent pre-mature insecure URL error, closes
  `#1074`*, `#1169`* (`PR#1173`*, `37db258`*)

..
  \_#1074:[https://github.com/python-semantic-release/python-semantic-release/issues/1074](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1074)4
  ..
  \_#1169[https://github.com/python-semantic-release/python-semantic-release/issues/1169](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1169)69
  .. \_37db258:
  https://github.com/python-semantic-release/python-semantic-release/commit/37db2581620ad02e66716a4b3b365aa28abe65f8
  ..
  \_PR#11[https://github.com/python-semantic-release/python-semantic-release/pull/1173](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1173)1173

.. \_changelog-v9.18.0:

###
  [`v9.18.0`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.rst#v9180-2025-02-06)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.17.0...v9.18.0)

- Add `create_release_url` & `format_w_official_vcs_name` filters (`PR#1161`*, `f853cf0`*)

- **changelog**: Add `create_pypi_url` filter to jinja template render context (`PR#1160`*,
  `45d49c3`*)

- **changelog**: Add additional release info to changeling from commit `NOTICE`'s (`PR#1166`*,
  `834ce32`*)

- **changelog-md**: Add additional release info section to default markdown template, closes
  `#223`\_ (`PR#1166`*, `834ce32`*)

- **changelog-rst**: Add additional release info section to default ReStructuredText template,
  closes `#223`\_ (`PR#1166`*, `834ce32`*)

- **commit-parser**: Enable parsers to identify additional release notices from commit msgs
  (`PR#1166`*, `834ce32`*)

- **parser-angular**: Add a `ignore_merge_commits` option to discard parsing merge commits
  (`PR#1164`*, `463e43b`*)

- **parser-angular**: Add functionality to parse out `NOTICE:` prefixed statements in commits,
  closes `#223`\_ (`PR#1166`*, `834ce32`*)

- **parser-emoji**: Add a `ignore_merge_commits` option to discard parsing merge commits
  (`PR#1164`*, `463e43b`*)

- **parser-emoji**: Add functionality to parse out `NOTICE:` prefixed statements in commits, closes
  `#223`\_ (`PR#1166`*, `834ce32`*)

- **parsers**: Add option `ignore_merge_commits` to discard parsing merge commits (`PR#1164`*,
  `463e43b`*)

- **release-notes**: Add license information to default release notes template, closes `#228`\_
  (`PR#1167`*, `41172c1`*)

- **vcs-bitbucket**: Add `format_w_official_vcs_name` filter function (`PR#1161`*, `f853cf0`*)

- **vcs-gitea**: Add `create_release_url` & `format_w_official_vcs_name` filter functions
  (`PR#1161`*, `f853cf0`*)

- **vcs-github**: Add `create_release_url` & `format_w_official_vcs_name` filter functions
  (`PR#1161`*, `f853cf0`*)

- **vcs-gitlab**: Add `create_release_url` & `format_w_official_vcs_name` filter functions
  (`PR#1161`*, `f853cf0`*)

- Refactor parsing compatibility function to support older custom parsers (`PR#1165`*, `cf340c5`*)

- **changelog**: Fix parsing compatibility w/ custom parsers, closes `#1162`\_ (`PR#1165`*,
  `cf340c5`*)

- **changelog-templates**: Adjust default templates to avoid empty version sections (`PR#1164`*,
  `463e43b`*)

- **parser-angular**: Adjust parser to prevent empty message extractions (`PR#1166`*, `834ce32`*)

- **parser-emoji**: Adjust parser to prevent empty message extractions (`PR#1166`*, `834ce32`*)

- **version**: Fix parsing compatibility w/ custom parsers, closes `#1162`\_ (`PR#1165`*,
  `cf340c5`*)

- **changelog**: Add formatted changelog into hosted documentation (`PR#1155`*, `2f18a6d`*)

- **changelog-templates**: Add description for new `create_pypi_url` filter function (`PR#1160`*,
  `45d49c3`*)

- **changelog-templates**: Add details about license specification in the release notes (`PR#1167`*,
  `41172c1`*)

- **changelog-templates**: Define `create_release_url` & `format_w_official_vcs_name` filters
  (`PR#1161`*, `f853cf0`*)

- **changelog-templates**: Document special separate sections of commit descriptions (`ebb4c67`\_)

- **commit-parsing**: Document new release notice footer detection feature of built-in parsers
  (`cd14e92`\_)

..
  \_#1162:[https://github.com/python-semantic-release/python-semantic-release/issues/1162](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1162)2
  ..
  \_#223[https://github.com/python-semantic-release/python-semantic-release/issues/223](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/223)23
  ..
  \_#22[https://github.com/python-semantic-release/python-semantic-release/issues/228](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/228)228
  .. \_2f18a6d:
  https://github.com/python-semantic-release/python-semantic-release/commit/2f18a6debfa6ef3afcc5611a3e09262998f2d4bf
  .. \_41172c1:
  https://github.com/python-semantic-release/python-semantic-release/commit/41172c1272a402e94e3c68571d013cbdcb5b9023
  .. \_45d49c3:
  https://github.com/python-semantic-release/python-semantic-release/commit/45d49c3da75a7f08c86fc9bab5d232a9b37d9e72
  .. \_463e43b:
  https://github.com/python-semantic-release/python-semantic-release/commit/463e43b897ee80dfaf7ce9d88d22ea8e652bcf55
  .. \_834ce32:
  https://github.com/python-semantic-release/python-semantic-release/commit/834ce323007c58229abf115ef2016a348de9ee66
  .. \_cd14e92:
  https://github.com/python-semantic-release/python-semantic-release/commit/cd14e9209d4e54f0876e737d1f802dded294a48c
  .. \_cf340c5:
  https://github.com/python-semantic-release/python-semantic-release/commit/cf340c5256dea58aedad71a6bdf50b17eee53d2f
  .. \_ebb4c67:
  https://github.com/python-semantic-release/python-semantic-release/commit/ebb4c67d46b86fdf79e32edf744a2ec2b09d6a93
  .. \_f853cf0:
  https://github.com/python-semantic-release/python-semantic-release/commit/f853cf059b3323d7888b06fde09142184e7964e8

.[https://github.com/python-semantic-release/python-semantic-release/pull/1155](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1155)ase/pull/1155

[https://github.com/python-semantic-release/python-semantic-release/pull/1160](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1160)ease/pull/1160[https://github.com/python-semantic-release/python-semantic-release/pull/1161](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1161)lease/pull/116[https://github.com/python-semantic-release/python-semantic-release/pull/1164](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1164)elease/pull/11[https://github.com/python-semantic-release/python-semantic-release/pull/1165](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1165)release/pull/1[https://github.com/python-semantic-release/python-semantic-release/pull/1166](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1166)-release/pull/[https://github.com/python-semantic-release/python-semantic-release/pull/1167](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1167)c-release/pull/1167

.. \_changelog-v9.17.0:

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xNDUuMCIsInVwZGF0ZWRJblZlciI6IjM5LjE3Ni4yIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Code Style

- Improve anki QA prompts
  ([`edf8dfe`](https://github.com/MartinBernstorff/Memium/commit/edf8dfede25ffc0f762a385b87841d33aa597889))

### Documentation

- Add bug report
  ([`8ef4437`](https://github.com/MartinBernstorff/Memium/commit/8ef44375f9e6bd73cf7c59893df7758d30c7af25))

- Planning
  ([`761b198`](https://github.com/MartinBernstorff/Memium/commit/761b198767b32eca31c46d92b5a8ced1818ce75d))

- Update readme.md
  ([`d6ee90a`](https://github.com/MartinBernstorff/Memium/commit/d6ee90ac71e407e0da701c7431d29b097e23642d))

- Update readme.md
  ([`d466543`](https://github.com/MartinBernstorff/Memium/commit/d4665431e335c5552575eddba2e16ece9b4f41a6))

### Features

- Add note title to front of card ([#822](https://github.com/MartinBernstorff/Memium/pull/822),
  [`b2b6b5f`](https://github.com/MartinBernstorff/Memium/commit/b2b6b5ffeb058011282015f3d06cebad7436592c))


## v0.25.35 (2025-01-30)

### Bug Fixes

- **deps**: Update dependency diff-cover to v9.2.2
  ([#812](https://github.com/MartinBernstorff/Memium/pull/812),
  [`b622d27`](https://github.com/MartinBernstorff/Memium/commit/b622d279c40e599eab7fee1b418220ab4ed6426a))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [diff-cover](https://redirect.github.com/Bachmann1234/diff-cover) | `==9.2.1` -> `==9.2.2` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/diff-cover/9.2.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/diff-cover/9.2.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/diff-cover/9.2.1/9.2.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/diff-cover/9.2.1/9.2.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>Bachmann1234/diff-cover (diff-cover)</summary>

### [`v9.2.2`](https://redirect.github.com/Bachmann1234/diff_cover/releases/tag/v9.2.2)

[Compare Source](https://redirect.github.com/Bachmann1234/diff-cover/compare/v9.2.1...v9.2.2)

#### What's Changed

- Fix files only covered by one LCOV report showing 100% coverage by
  [@&#8203;matsjoyce-refeyn](https://redirect.github.com/matsjoyce-refeyn) in
  [https://github.com/Bachmann1234/diff_cover/pull/433](https://redirect.github.com/Bachmann1234/diff_cover/pull/433)

##### Dependency Bumps

- Bump pylint from 3.3.2 to 3.3.3 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in
  [https://github.com/Bachmann1234/diff_cover/pull/429](https://redirect.github.com/Bachmann1234/diff_cover/pull/429)
  - Bump jinja2 from 3.1.4 to 3.1.5 by [@&#8203;dependabot](https://redirect.github.com/dependabot)
  in
  [https://github.com/Bachmann1234/diff_cover/pull/431](https://redirect.github.com/Bachmann1234/diff_cover/pull/431)
  - Bump pytest-cov from 5.0.0 to 6.0.0 by
  [@&#8203;dependabot](https://redirect.github.com/dependabot) in
  [https://github.com/Bachmann1234/diff_cover/pull/430](https://redirect.github.com/Bachmann1234/diff_cover/pull/430)

**Full Changelog**: https://github.com/Bachmann1234/diff_cover/compare/v9.2.1...v9.2.2

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xNDUuMCIsInVwZGF0ZWRJblZlciI6IjM5LjE0NS4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.34 (2025-01-29)

### Bug Fixes

- **deps**: Update dependency pyright to v1.1.393
  ([#811](https://github.com/MartinBernstorff/Memium/pull/811),
  [`1e41edd`](https://github.com/MartinBernstorff/Memium/commit/1e41edd400f62a2f205710168e49c333b81afd15))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pyright](https://redirect.github.com/RobertCraigie/pyright-python) | `==1.1.392.post0` ->
  `==1.1.393` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pyright/1.1.393?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pyright/1.1.393?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pyright/1.1.392.post0/1.1.393?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pyright/1.1.392.post0/1.1.393?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>RobertCraigie/pyright-python (pyright)</summary>

###
  [`v1.1.393`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.392...v1.1.393)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.392.post0...v1.1.393)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xMjUuMSIsInVwZGF0ZWRJblZlciI6IjM5LjEyNS4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Chores

- **deps**: Update python-semantic-release/python-semantic-release action to v9.17.0
  ([#810](https://github.com/MartinBernstorff/Memium/pull/810),
  [`c3649aa`](https://github.com/MartinBernstorff/Memium/commit/c3649aa2e2e20b585bd35169a8ec977172b07f67))

This PR contains the following updates:

| Package | Type | Update | Change | |---|---|---|---| |
  [python-semantic-release/python-semantic-release](https://redirect.github.com/python-semantic-release/python-semantic-release)
  | action | minor | `v9.16.1` -> `v9.17.0` |

---

### Release Notes

<details> <summary>python-semantic-release/python-semantic-release
  (python-semantic-release/python-semantic-release)</summary>

###
  [`v9.17.0`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.md#v9170-2025-01-26)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.16.1...v9.17.0)

##### Bug Fixes

- **github-action**: Disable writing python bytecode in action execution

([#&#8203;1152](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1152),

[`315ae21`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/315ae2176e211b00b13374560d81e127a3065d1a))

File permission issues can occur when using the github-action and dynamically loading files from the
  repository. When importing, python generally will create bytecode files and write to disk as the
  current user. Because the default user in the github action is root, those files are written as
  root which means when it returns to the rest of the workflow, those files cannot be modified or
  deleted. With this change, we disable writing of bytecode files which prevents any failures that
  may result after the python-semantic-release action is executed.

##### Features

- **changelog**: Add `sort_numerically` filter function to template environment

([#&#8203;1146](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1146),

[`7792388`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/77923885c585171e8888aacde989837ecbabf3fc))

<!---->

- test(helpers): add unit tests for various prefixed number lists

- test(changelog-context): add unit tests to validate use of `sort_numerically` filter

- test(release-notes-context): add unit tests to validate use of `sort_numerically` filter

- refactor(util): relocate `sort_numerically` function to top level

- docs(changelog-templates): add description for new `sort_numerically` filter function

- **config**: Extend support of remote urls aliased using git `insteadOf` configurations

([#&#8203;1151](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1151),

[`4045037`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/40450375c7951dafddb09bef8001db7180d95f3a))

Resolves:
  [#&#8203;1150](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1150)

- refactor(hvcs): add validation of git urls upon vcs client initialization

- test(hvcs): refactor unit test to catch validation error immediately of bad git url

- test(config): add test case of a git `insteadOf` aliased origin

- **parsers**: Parse squashed commits individually

([#&#8203;1112](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1112),

[`cf785ca`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/cf785ca79a49eb4ee95c148e0ae6a19e230e915c))

- test(parser-angular): update unit tests for parser return value compatibility

- test(parser-scipy): update unit tests for parser return value compatibility

- test(parser-emoji): update unit tests for parser return value compatibility

- feat(version): parse squashed commits individually

adds the functionality to separately parse each commit message within a squashed merge commit to
  detect combined commit types that could change the version bump

- feat(changelog): parse squashed commits individually

adds functionality to separately parse each commit message within a squashed merge commit which
  decouples the commits into their respective type categories in the changelog.

- refactor(helpers): centralize utility for applying multiple text substitutions

- feat(parser-angular): upgrade angular parser to parse squashed commits individually

Resolves:
  [#&#8203;1085](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1085)

- feat(parser-angular): apply PR/MR numbers to all parsed commits from a squash merge

- feat(parser-emoji): add functionality to interpret scopes from gitmoji commit messages

- feat(parser-emoji): upgrade emoji parser to parse squashed commits individually

- test(fixtures): adjust parser for squashed commit definitions

- test(fixtures): change config of github flow repo to parse squash commits

- test(fixtures): add fixture to create gitlab formatted merge commit

- refactor(parser-scipy): standardize all category spelling applied to commits

- docs(commit-parsing): add description for squash commit evaluation option of default parsers

- docs(configuration): update the `commit_parser_options` setting description

##### Performance Improvements

- **logging**: Remove irrelevant debug logging statements

([#&#8203;1147](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1147),

[`f1ef4ec`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/f1ef4ecf5f22684a870b958f87d1ca2650e612db))

- refactor: adjust logging output

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xMjUuMSIsInVwZGF0ZWRJblZlciI6IjM5LjEyNS4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.33 (2025-01-24)

### Bug Fixes

- **deps**: Update dependency pydantic to v2.10.6
  ([#809](https://github.com/MartinBernstorff/Memium/pull/809),
  [`1cd1f2f`](https://github.com/MartinBernstorff/Memium/commit/1cd1f2f58d5aabcc126d1352a9c2dc596e7f6e3b))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pydantic](https://redirect.github.com/pydantic/pydantic)
  ([changelog](https://docs.pydantic.dev/latest/changelog/)) | `==2.10.5` -> `==2.10.6` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pydantic/2.10.6?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pydantic/2.10.6?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pydantic/2.10.5/2.10.6?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pydantic/2.10.5/2.10.6?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pydantic/pydantic (pydantic)</summary>

### [`v2.10.6`](https://redirect.github.com/pydantic/pydantic/blob/HEAD/HISTORY.md#v2106-2025-01-23)

[GitHub release](https://redirect.github.com/pydantic/pydantic/releases/tag/v2.10.6)

##### What's Changed

##### Fixes

- Fix JSON Schema reference collection with `'examples'` keys by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11325](https://redirect.github.com/pydantic/pydantic/pull/11325) - Fix url python
  serialization by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;11331](https://redirect.github.com/pydantic/pydantic/pull/11331)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xMjUuMSIsInVwZGF0ZWRJblZlciI6IjM5LjEyNS4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.32 (2025-01-21)

### Bug Fixes

- **deps**: Update dependency pre-commit to v4.1.0
  ([#808](https://github.com/MartinBernstorff/Memium/pull/808),
  [`89a91cd`](https://github.com/MartinBernstorff/Memium/commit/89a91cd55ba29e4b447b422de2682fa56fd0f05a))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pre-commit](https://redirect.github.com/pre-commit/pre-commit) | `==4.0.1` -> `==4.1.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pre-commit/4.1.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pre-commit/4.1.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pre-commit/4.0.1/4.1.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pre-commit/4.0.1/4.1.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pre-commit/pre-commit (pre-commit)</summary>

###
  [`v4.1.0`](https://redirect.github.com/pre-commit/pre-commit/blob/HEAD/CHANGELOG.md#410---2025-01-20)

[Compare Source](https://redirect.github.com/pre-commit/pre-commit/compare/v4.0.1...v4.1.0)

\==================

##### Features

- Add `language: julia`. -
  [#&#8203;3348](https://redirect.github.com/pre-commit/pre-commit/issues/3348) PR by
  [@&#8203;fredrikekre](https://redirect.github.com/fredrikekre). -
  [#&#8203;2689](https://redirect.github.com/pre-commit/pre-commit/issues/2689) issue
  [@&#8203;jmuchovej](https://redirect.github.com/jmuchovej).

##### Fixes

- Disable automatic toolchain switching for `language: golang`. -
  [#&#8203;3304](https://redirect.github.com/pre-commit/pre-commit/issues/3304) PR by
  [@&#8203;AleksaC](https://redirect.github.com/AleksaC). -
  [#&#8203;3300](https://redirect.github.com/pre-commit/pre-commit/issues/3300) issue by
  [@&#8203;AleksaC](https://redirect.github.com/AleksaC). -
  [#&#8203;3149](https://redirect.github.com/pre-commit/pre-commit/issues/3149) issue by
  [@&#8203;nijel](https://redirect.github.com/nijel). - Fix `language: r` installation when
  initiated by RStudio. -
  [#&#8203;3389](https://redirect.github.com/pre-commit/pre-commit/issues/3389) PR by
  [@&#8203;lorenzwalthert](https://redirect.github.com/lorenzwalthert). -
  [#&#8203;3385](https://redirect.github.com/pre-commit/pre-commit/issues/3385) issue by
  [@&#8203;lorenzwalthert](https://redirect.github.com/lorenzwalthert).

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xMDcuMCIsInVwZGF0ZWRJblZlciI6IjM5LjEwNy4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.31 (2025-01-15)

### Bug Fixes

- **deps**: Update dependency pyright to v1.1.392.post0
  ([#807](https://github.com/MartinBernstorff/Memium/pull/807),
  [`a7ba499`](https://github.com/MartinBernstorff/Memium/commit/a7ba499ae72d7bf4a0252a54f0a06bc01aa9e19e))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pyright](https://redirect.github.com/RobertCraigie/pyright-python) | `==1.1.392` ->
  `==1.1.392.post0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pyright/1.1.392.post0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pyright/1.1.392.post0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pyright/1.1.392/1.1.392.post0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pyright/1.1.392/1.1.392.post0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>RobertCraigie/pyright-python (pyright)</summary>

###
  [`v1.1.392.post0`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.392...v1.1.392.post0)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.392...v1.1.392.post0)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xMDcuMCIsInVwZGF0ZWRJblZlciI6IjM5LjEwNy4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.30 (2025-01-15)

### Bug Fixes

- **deps**: Update dependency pyright to v1.1.392
  ([#806](https://github.com/MartinBernstorff/Memium/pull/806),
  [`29ecb1b`](https://github.com/MartinBernstorff/Memium/commit/29ecb1b06537f46893f3cd0a837925bde7721f23))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pyright](https://redirect.github.com/RobertCraigie/pyright-python) | `==1.1.391` -> `==1.1.392` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pyright/1.1.392?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pyright/1.1.392?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pyright/1.1.391/1.1.392?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pyright/1.1.391/1.1.392?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xMDcuMCIsInVwZGF0ZWRJblZlciI6IjM5LjEwNy4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.29 (2025-01-14)

### Bug Fixes

- **deps**: Update dependency sentry-sdk to v2.20.0
  ([#805](https://github.com/MartinBernstorff/Memium/pull/805),
  [`25cb10e`](https://github.com/MartinBernstorff/Memium/commit/25cb10e1d78c599ed9520027399b1821aaeb852f))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [sentry-sdk](https://redirect.github.com/getsentry/sentry-python)
  ([changelog](https://redirect.github.com/getsentry/sentry-python/blob/master/CHANGELOG.md)) |
  `==2.19.2` -> `==2.20.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/sentry-sdk/2.20.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/sentry-sdk/2.20.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/sentry-sdk/2.19.2/2.20.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/sentry-sdk/2.19.2/2.20.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>getsentry/sentry-python (sentry-sdk)</summary>

### [`v2.20.0`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2200)

[Compare Source](https://redirect.github.com/getsentry/sentry-python/compare/2.19.2...2.20.0)

- **New integration:** Add [Typer](https://typer.tiangolo.com/) integration
  ([#&#8203;3869](https://redirect.github.com/getsentry/sentry-python/issues/3869)) by
  [@&#8203;patrick91](https://redirect.github.com/patrick91)

For more information, see the documentation for the
  [TyperIntegration](https://docs.sentry.io/platforms/python/integrations/typer/).

- **New integration:** Add [Unleash](https://www.getunleash.io/) feature flagging integration
  ([#&#8203;3888](https://redirect.github.com/getsentry/sentry-python/issues/3888)) by
  [@&#8203;aliu39](https://redirect.github.com/aliu39)

For more information, see the documentation for the
  [UnleashIntegration](https://docs.sentry.io/platforms/python/integrations/unleash/).

- Add custom tracking of feature flag evaluations
  ([#&#8203;3860](https://redirect.github.com/getsentry/sentry-python/issues/3860)) by
  [@&#8203;aliu39](https://redirect.github.com/aliu39)

- Feature Flags: Register LD hook in setup instead of init, and don't check for initialization
  ([#&#8203;3890](https://redirect.github.com/getsentry/sentry-python/issues/3890)) by
  [@&#8203;aliu39](https://redirect.github.com/aliu39)

- Feature Flags: Moved adding of `flags` context into Scope
  ([#&#8203;3917](https://redirect.github.com/getsentry/sentry-python/issues/3917)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker)

- Create a separate group for feature flag test suites
  ([#&#8203;3911](https://redirect.github.com/getsentry/sentry-python/issues/3911)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Fix flaky LaunchDarkly tests
  ([#&#8203;3896](https://redirect.github.com/getsentry/sentry-python/issues/3896)) by
  [@&#8203;aliu39](https://redirect.github.com/aliu39)

- Fix LRU cache copying
  ([#&#8203;3883](https://redirect.github.com/getsentry/sentry-python/issues/3883)) by
  [@&#8203;ffelixg](https://redirect.github.com/ffelixg)

- Fix cache pollution from mutable reference
  ([#&#8203;3887](https://redirect.github.com/getsentry/sentry-python/issues/3887)) by
  [@&#8203;cmanallen](https://redirect.github.com/cmanallen)

- Centralize minimum version checking
  ([#&#8203;3910](https://redirect.github.com/getsentry/sentry-python/issues/3910)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Support SparkIntegration activation after SparkContext created
  ([#&#8203;3411](https://redirect.github.com/getsentry/sentry-python/issues/3411)) by
  [@&#8203;seyoon-lim](https://redirect.github.com/seyoon-lim)

- Preserve ARQ enqueue_job **kwdefaults** after patching
  ([#&#8203;3903](https://redirect.github.com/getsentry/sentry-python/issues/3903)) by
  [@&#8203;danmr](https://redirect.github.com/danmr)

- Add Github workflow to comment on issues when a fix was released
  ([#&#8203;3866](https://redirect.github.com/getsentry/sentry-python/issues/3866)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker)

- Update test matrix for Sanic
  ([#&#8203;3904](https://redirect.github.com/getsentry/sentry-python/issues/3904)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker)

- Rename scripts ([#&#8203;3885](https://redirect.github.com/getsentry/sentry-python/issues/3885))
  by [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Fix CI ([#&#8203;3878](https://redirect.github.com/getsentry/sentry-python/issues/3878)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- Treat `potel-base` as release branch in CI
  ([#&#8203;3912](https://redirect.github.com/getsentry/sentry-python/issues/3912)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana)

- build(deps): bump actions/create-github-app-token from 1.11.0 to 1.11.1
  ([#&#8203;3893](https://redirect.github.com/getsentry/sentry-python/issues/3893)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot)

- build(deps): bump codecov/codecov-action from 5.0.7 to 5.1.1
  ([#&#8203;3867](https://redirect.github.com/getsentry/sentry-python/issues/3867)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot)

- build(deps): bump codecov/codecov-action from 5.1.1 to 5.1.2
  ([#&#8203;3892](https://redirect.github.com/getsentry/sentry-python/issues/3892)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xMDcuMCIsInVwZGF0ZWRJblZlciI6IjM5LjEwNy4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6W119-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.28 (2025-01-13)

### Bug Fixes

- **deps**: Update dependency syrupy to v4.8.1
  ([#804](https://github.com/MartinBernstorff/Memium/pull/804),
  [`ac2ad78`](https://github.com/MartinBernstorff/Memium/commit/ac2ad78cba4172c65b270c23c379e76ea60883ab))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [syrupy](https://redirect.github.com/syrupy-project/syrupy) | `==4.8.0` -> `==4.8.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/syrupy/4.8.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/syrupy/4.8.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/syrupy/4.8.0/4.8.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/syrupy/4.8.0/4.8.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>syrupy-project/syrupy (syrupy)</summary>

###
  [`v4.8.1`](https://redirect.github.com/syrupy-project/syrupy/blob/HEAD/CHANGELOG.md#481-2025-01-13)

[Compare Source](https://redirect.github.com/syrupy-project/syrupy/compare/v4.8.0...v4.8.1)

##### Bug Fixes

- check current session's pending-write queue when recalling snapshots (e.g. diffing)
  ([#&#8203;927](https://redirect.github.com/syrupy-project/syrupy/issues/927))
  ([0f6bb55](https://redirect.github.com/syrupy-project/syrupy/commit/0f6bb55000593e5d5198feb2bd9ccbb1376a37fb))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS45Mi4wIiwidXBkYXRlZEluVmVyIjoiMzkuOTIuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Chores

- **deps**: Update python-semantic-release/python-semantic-release action to v9.16.0
  ([#802](https://github.com/MartinBernstorff/Memium/pull/802),
  [`2e87a03`](https://github.com/MartinBernstorff/Memium/commit/2e87a036a8f68bddf9fa00ece46469a707d149d3))

This PR contains the following updates:

| Package | Type | Update | Change | |---|---|---|---| |
  [python-semantic-release/python-semantic-release](https://redirect.github.com/python-semantic-release/python-semantic-release)
  | action | minor | `v9.15.2` -> `v9.16.0` |

---

### Release Notes

<details> <summary>python-semantic-release/python-semantic-release
  (python-semantic-release/python-semantic-release)</summary>

###
  [`v9.16.0`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.md#v9160-2025-01-12)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.15.2...v9.16.0)

##### Bug Fixes

- **changelog**: Fixes PSR release commit exclusions for customized commit messages

([#&#8203;1139](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1139),

[`f9a2078`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/f9a20787437d0f26074fe2121bf0a29576a96df0))

<!---->

- fix(config-changelog): validate `changelog.exclude_commit_patterns` on config load

- test(fixtures): relocate sanitize changelog functions

- test(cmd-version): add test to validate that custom release messages are ignored in changelog

- test(config): add `changelog.exclude_commit_patterns` validation check

- style(config): refactor import names of `re` module

- **cmd-version**: Fix `--print-tag` result to match configured tag format

([#&#8203;1134](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1134),

[`a990aa7`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/a990aa7ab0a9d52d295c04d54d20e9c9f2db2ca5))

- test(fixtures): add new trunk repo that has a different tag format

- test(fixtures): add helper to extract config settings from repo action definition

- test(cmd-version): expand testing of `--print-tag` & `--print-last-released-tag`

PSR did not have enough testing to demonstrate testing of the tag generation when the tag format was
  configured differently than normal. This commit adds a significant portion of testing to exercise
  the print tag functionality which must match the configured tag format.

- **cmd-version**: Fix tag format on default version when force bump for initial release

([#&#8203;1138](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1138),

[`007fd00`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/007fd00a3945ed211ece4baab0b79ad93dc018f5))

Resolves:
  [#&#8203;1137](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1137)

- test(fixtures): add new unreleased trunk repo with a different tag format

- test(cmd-version): ensure forced bump version on initial release follows tag format

ref:
  [#&#8203;1137](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1137)

##### Features

- **config**: Expand dynamic parser import to handle a filepath to module

([#&#8203;1135](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1135),

[`0418fd8`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/0418fd8d27aac14925aafa50912e751e3aeff2f7))

- test(fixtures): remove import checking/loading of custom parser in `use_custom_parser`

- test(config): extend import parser unit tests to evaluate file paths to modules

- docs(commit-parsing): add the new custom parser import spec description for direct path imports

Resolves:
  [#&#8203;687](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/687)

- docs(configuration): adjust `commit_parser` option definition for direct path imports

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS45Mi4wIiwidXBkYXRlZEluVmVyIjoiMzkuOTIuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update python-semantic-release/python-semantic-release action to v9.16.1
  ([#803](https://github.com/MartinBernstorff/Memium/pull/803),
  [`4536178`](https://github.com/MartinBernstorff/Memium/commit/4536178d7ee47442d824738801da902705aac2f3))

This PR contains the following updates:

| Package | Type | Update | Change | |---|---|---|---| |
  [python-semantic-release/python-semantic-release](https://redirect.github.com/python-semantic-release/python-semantic-release)
  | action | patch | `v9.16.0` -> `v9.16.1` |

---

### Release Notes

<details> <summary>python-semantic-release/python-semantic-release
  (python-semantic-release/python-semantic-release)</summary>

###
  [`v9.16.1`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.md#v9161-2025-01-12)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.16.0...v9.16.1)

##### Bug Fixes

- **parser-custom**: Handle relative parent directory paths to module file better

([#&#8203;1142](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1142),

[`c4056fc`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/c4056fc2e1fb3bddb78728793716ac6fb8522b1a))

The dynamic import originally would just replace "/" with "." to make the import module name more
  pythonic, however this would be problematic in monorepos which would use
  "../../misc/commit_parser.py" to locate the parser and so the resulting `sys.modules` entry would
  have numerous periods (.) as a prefix. This removes that possibility. Still always an issue if the
  imported module name matches an existing module but the likelihood is low.

##### Documentation

- **github-actions**: Update PSR versions in github workflow examples

([#&#8203;1140](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1140),

[`9bdd626`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/9bdd626bf8f8359d35725cebe803931063260cac))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS45Mi4wIiwidXBkYXRlZEluVmVyIjoiMzkuOTIuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.27 (2025-01-09)

### Bug Fixes

- **deps**: Update dependency pydantic to v2.10.5
  ([#801](https://github.com/MartinBernstorff/Memium/pull/801),
  [`6603ef7`](https://github.com/MartinBernstorff/Memium/commit/6603ef7c5127589375afe975552ed926edc254f9))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pydantic](https://redirect.github.com/pydantic/pydantic)
  ([changelog](https://docs.pydantic.dev/latest/changelog/)) | `==2.10.4` -> `==2.10.5` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pydantic/2.10.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pydantic/2.10.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pydantic/2.10.4/2.10.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pydantic/2.10.4/2.10.5?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pydantic/pydantic (pydantic)</summary>

### [`v2.10.5`](https://redirect.github.com/pydantic/pydantic/blob/HEAD/HISTORY.md#v2105-2025-01-08)

[Compare Source](https://redirect.github.com/pydantic/pydantic/compare/v2.10.4...v2.10.5)

[GitHub release](https://redirect.github.com/pydantic/pydantic/releases/tag/v2.10.5)

##### What's Changed

- Remove custom MRO implementation of Pydantic models by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11184](https://redirect.github.com/pydantic/pydantic/pull/11184) - Fix URL serialization
  for unions by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;11233](https://redirect.github.com/pydantic/pydantic/pull/11233)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS45Mi4wIiwidXBkYXRlZEluVmVyIjoiMzkuOTIuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.26 (2024-12-25)

### Bug Fixes

- **deps**: Update dependency cruft to v2.16.0
  ([#800](https://github.com/MartinBernstorff/Memium/pull/800),
  [`4c83d17`](https://github.com/MartinBernstorff/Memium/commit/4c83d172bb4f6d57c61f5906859b94a4592d0f5a))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| | cruft |
  `==2.15.0` -> `==2.16.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/cruft/2.16.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/cruft/2.16.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/cruft/2.15.0/2.16.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/cruft/2.15.0/2.16.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS44MC4wIiwidXBkYXRlZEluVmVyIjoiMzkuODAuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.25 (2024-12-22)

### Bug Fixes

- **deps**: Update dependency pytest-testmon to v2.1.3
  ([#799](https://github.com/MartinBernstorff/Memium/pull/799),
  [`34b6e28`](https://github.com/MartinBernstorff/Memium/commit/34b6e28b20fe775f8793feb114bccb02a2f7d47e))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  pytest-testmon | `==2.1.1` -> `==2.1.3` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pytest-testmon/2.1.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pytest-testmon/2.1.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pytest-testmon/2.1.1/2.1.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pytest-testmon/2.1.1/2.1.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS43Mi41IiwidXBkYXRlZEluVmVyIjoiMzkuNzIuNSIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.24 (2024-12-18)

### Bug Fixes

- **deps**: Update dependency pydantic to v2.10.4
  ([#798](https://github.com/MartinBernstorff/Memium/pull/798),
  [`3d51c5b`](https://github.com/MartinBernstorff/Memium/commit/3d51c5b9b930f22ea574e96e944c8fe654ab8b33))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pydantic](https://redirect.github.com/pydantic/pydantic)
  ([changelog](https://docs.pydantic.dev/latest/changelog/)) | `==2.10.3` -> `==2.10.4` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pydantic/2.10.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pydantic/2.10.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pydantic/2.10.3/2.10.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pydantic/2.10.3/2.10.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pydantic/pydantic (pydantic)</summary>

### [`v2.10.4`](https://redirect.github.com/pydantic/pydantic/blob/HEAD/HISTORY.md#v2104-2024-12-18)

[Compare Source](https://redirect.github.com/pydantic/pydantic/compare/v2.10.3...v2.10.4)

[GitHub release](https://redirect.github.com/pydantic/pydantic/releases/tag/v2.10.4)

##### What's Changed

##### Packaging

- Bump `pydantic-core` to v2.27.2 by [@&#8203;davidhewitt](https://redirect.github.com/davidhewitt)
  in [#&#8203;11138](https://redirect.github.com/pydantic/pydantic/pull/11138)

##### Fixes

- Fix for comparison of `AnyUrl` objects by
  [@&#8203;alexprabhat99](https://redirect.github.com/alexprabhat99) in
  [#&#8203;11082](https://redirect.github.com/pydantic/pydantic/pull/11082) - Properly fetch PEP 695
  type params for functions, do not fetch annotations from signature by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11093](https://redirect.github.com/pydantic/pydantic/pull/11093) - Include JSON Schema
  input core schema in function schemas by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11085](https://redirect.github.com/pydantic/pydantic/pull/11085) - Add `len` to
  `_BaseUrl` to avoid TypeError by [@&#8203;Kharianne](https://redirect.github.com/Kharianne) in
  [#&#8203;11111](https://redirect.github.com/pydantic/pydantic/pull/11111) - Make sure the type
  reference is removed from the seen references by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11143](https://redirect.github.com/pydantic/pydantic/pull/11143)

##### New Contributors

- [@&#8203;FyZzyss](https://redirect.github.com/FyZzyss) made their first contribution in
  [#&#8203;10789](https://redirect.github.com/pydantic/pydantic/pull/10789) -
  [@&#8203;tamird](https://redirect.github.com/tamird) made their first contribution in
  [#&#8203;10948](https://redirect.github.com/pydantic/pydantic/pull/10948) -
  [@&#8203;felixxm](https://redirect.github.com/felixxm) made their first contribution in
  [#&#8203;11077](https://redirect.github.com/pydantic/pydantic/pull/11077) -
  [@&#8203;alexprabhat99](https://redirect.github.com/alexprabhat99) made their first contribution
  in [#&#8203;11082](https://redirect.github.com/pydantic/pydantic/pull/11082) -
  [@&#8203;Kharianne](https://redirect.github.com/Kharianne) made their first contribution in
  [#&#8203;11111](https://redirect.github.com/pydantic/pydantic/pull/11111)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS43Mi41IiwidXBkYXRlZEluVmVyIjoiMzkuNzIuNSIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.23 (2024-12-18)

### Bug Fixes

- **deps**: Update dependency pyright to v1.1.391
  ([#797](https://github.com/MartinBernstorff/Memium/pull/797),
  [`86ece60`](https://github.com/MartinBernstorff/Memium/commit/86ece60ca48f8ec5d58aa95ab26e20cadda5860e))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pyright](https://redirect.github.com/RobertCraigie/pyright-python) | `==1.1.390` -> `==1.1.391` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pyright/1.1.391?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pyright/1.1.391?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pyright/1.1.390/1.1.391?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pyright/1.1.390/1.1.391?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>RobertCraigie/pyright-python (pyright)</summary>

###
  [`v1.1.391`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.390...v1.1.391)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.390...v1.1.391)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS43Mi41IiwidXBkYXRlZEluVmVyIjoiMzkuNzIuNSIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Chores

- **deps**: Update python-semantic-release/python-semantic-release action to v9.15.2
  ([#796](https://github.com/MartinBernstorff/Memium/pull/796),
  [`fe2a452`](https://github.com/MartinBernstorff/Memium/commit/fe2a452d7ad546455b38f3d0b524a83373bbc838))

This PR contains the following updates:

| Package | Type | Update | Change | |---|---|---|---| |
  [python-semantic-release/python-semantic-release](https://redirect.github.com/python-semantic-release/python-semantic-release)
  | action | patch | `v9.15.1` -> `v9.15.2` |

---

### Release Notes

<details> <summary>python-semantic-release/python-semantic-release
  (python-semantic-release/python-semantic-release)</summary>

###
  [`v9.15.2`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.md#v9152-2024-12-16)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.15.1...v9.15.2)

##### Bug Fixes

- **changelog**: Ensures user rendered files are trimmed to end with a single newline

([#&#8203;1118](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1118),

[`6dfbbb0`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/6dfbbb0371aef6b125cbcbf89b80dc343ed97360))

- **cli**: Add error message of how to gather full error output

([#&#8203;1116](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1116),

[`ba85532`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/ba85532ddd6fcf1a2205f7ce0b88ea5be76cb621))

- **cmd-version**: Enable maintenance prereleases

([#&#8203;864](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/864),

[`b88108e`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/b88108e189e1894e36ae4fdf8ad8a382b5c8c90a))

<!---->

- test(fixtures): improve changelog generator to filter by max version

- test(fixtures): add repo fixture of a trunk only repo w/ dual version support

- test(fixtures): add repo fixture of a trunk only repo w/ dual version support & prereleases

- test(cmd-version): add rebuild repo tests for new dual version support repos

- test(version-determination): adjust unit tests of increment_version logic

This clarifies repeated function calls and pytest parameter names included the unclear assert diff.
  Adds additional tests to check bad states for failures and refactored to match new function
  signature.

- fix(version-bump): increment based on current commit's history only

Refactor duplicate logging messages and flow to process out odd cases in a fail fast methodology.
  This removes the reliance on any last full release that is not within the history of the current
  branch.

Resolves:
  [#&#8203;861](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/861)

- **cmd-version**: Fix handling of multiple prerelease token variants & git flow merges

([#&#8203;1120](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1120),

[`8784b9a`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/8784b9ad4bc59384f855b5af8f1b8fb294397595))

- refactor: define a custom logging level of silly

- fix(version): remove some excessive log msgs from debug to silly level

- test(fixtures): refactor builder functions for version file updates

- test(fixtures): adjust build command to handle versions w/ build metadata

- test(fixtures): fix gitflow repo that included an invalid build metadata string

- test(fixtures): fix major_on_zero setting in repos to match expected behavior

- test(cmd-version): add test cases to run an example repo rebuild w/ psr

- test(cmd-version): enable git flow repo rebuild w/ psr test cases

- fix(cmd-version): handle multiple prerelease token variants properly

In the case where there are alpha and beta releases, we must only consider the previous beta release
  even if alpha releases exist due to merging into beta release only branches which have no changes
  considerable changes from alphas but must be marked otherwise.

Resolves:
  [#&#8203;789](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/789)

- fix(cmd-version): fix version determination algorithm to capture commits across merged branches

- perf(cmd-version): refactor version determination algorithm for accuracy & speed

- test(algorithm): refactor test to match new function signature

- style(algorithm): drop unused functions & imports

- test(algorithm): adapt test case for new DFS commit traversal implementation

- **cmd-version**: Forces tag timestamp to be same time as release commit

([#&#8203;1117](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1117),

[`7898b11`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/7898b1185fc1ad10e96bf3f5e48d9473b45d2b51))

- **config**: Ensure default config loads on network mounted windows environments

([#&#8203;1124](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1124),

[`a64cbc9`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/a64cbc96c110e32f1ec5d1a7b61e950472491b87))

Resolves:
  [#&#8203;1123](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1123)

- test(cmd-generate-config): added noop version execution to validate config at runtime

ref:
  [#&#8203;1123](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1123)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS41OC4xIiwidXBkYXRlZEluVmVyIjoiMzkuNTguMSIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.22 (2024-12-15)

### Bug Fixes

- **deps**: Update dependency iterpy to v1.11.1
  ([#795](https://github.com/MartinBernstorff/Memium/pull/795),
  [`6381c1b`](https://github.com/MartinBernstorff/Memium/commit/6381c1bbb15585da5029d59ffd7d32dddbd97093))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [iterpy](https://redirect.github.com/MartinBernstorff/iterpy) | `==1.11.0` -> `==1.11.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/iterpy/1.11.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/iterpy/1.11.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/iterpy/1.11.0/1.11.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/iterpy/1.11.0/1.11.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>MartinBernstorff/iterpy (iterpy)</summary>

###
  [`v1.11.1`](https://redirect.github.com/MartinBernstorff/iterpy/blob/HEAD/CHANGELOG.md#v1111-2024-12-15)

[Compare Source](https://redirect.github.com/MartinBernstorff/iterpy/compare/v1.11.0...v1.11.1)

##### Build

- build: update Makefile
  ([`c240a88`](https://redirect.github.com/MartinBernstorff/iterpy/commit/c240a889de3ba5d8ccc009e1051ae602df071ea8))

- build(deps): update arr.py, pyproject.toml and uv.lock
  ([`c844e66`](https://redirect.github.com/MartinBernstorff/iterpy/commit/c844e667f3ca22f39868015f4f2d65333152a499))

##### Fix

- fix: Arr is immutable, use sequence, not list
  ([#&#8203;212](https://redirect.github.com/MartinBernstorff/iterpy/issues/212))
  ([`6895330`](https://redirect.github.com/MartinBernstorff/iterpy/commit/6895330eb0a524ee00ae5bd37fff50e91d384d23))

##### Unknown

- update .gitignore, arr.py and test_arr.py
  ([`959821a`](https://redirect.github.com/MartinBernstorff/iterpy/commit/959821ae1ebd05668d58d1948d359964c25926c7))

- Initial commit
  ([`96deab9`](https://redirect.github.com/MartinBernstorff/iterpy/commit/96deab9dbd0b4080fc69c6ae3805b95f36485699))

- Update README.md
  ([`f06a276`](https://redirect.github.com/MartinBernstorff/iterpy/commit/f06a276139fd06cdc26377bfd127cf178a0492b4))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS41OC4xIiwidXBkYXRlZEluVmVyIjoiMzkuNTguMSIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.21 (2024-12-14)

### Bug Fixes

- **deps**: Update dependency diff-cover to v9.2.1
  ([#794](https://github.com/MartinBernstorff/Memium/pull/794),
  [`625992b`](https://github.com/MartinBernstorff/Memium/commit/625992b669b462c84fe06da81e56bce45e78965e))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [diff-cover](https://redirect.github.com/Bachmann1234/diff-cover) | `==9.2.0` -> `==9.2.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/diff-cover/9.2.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/diff-cover/9.2.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/diff-cover/9.2.0/9.2.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/diff-cover/9.2.0/9.2.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>Bachmann1234/diff-cover (diff-cover)</summary>

### [`v9.2.1`](https://redirect.github.com/Bachmann1234/diff_cover/releases/tag/v9.2.1): Version
  9.2.1

[Compare Source](https://redirect.github.com/Bachmann1234/diff-cover/compare/v9.2.0...v9.2.1)

#### What's Changed

- Fix inline comments by [@&#8203;Bachmann1234](https://redirect.github.com/Bachmann1234) in
  [https://github.com/Bachmann1234/diff_cover/pull/423](https://redirect.github.com/Bachmann1234/diff_cover/pull/423)

- Add support for py313 by [@&#8203;ssbarnea](https://redirect.github.com/ssbarnea) in
  [https://github.com/Bachmann1234/diff_cover/pull/427](https://redirect.github.com/Bachmann1234/diff_cover/pull/427)

- Drop 3.8 by [@&#8203;Bachmann1234](https://redirect.github.com/Bachmann1234) in
  [https://github.com/Bachmann1234/diff_cover/pull/428](https://redirect.github.com/Bachmann1234/diff_cover/pull/428)

- Bump tomli from 2.0.1 to 2.0.2 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in
  [https://github.com/Bachmann1234/diff_cover/pull/422](https://redirect.github.com/Bachmann1234/diff_cover/pull/422)

- Bump doc8 from 1.1.1 to 1.1.2 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in
  [https://github.com/Bachmann1234/diff_cover/pull/421](https://redirect.github.com/Bachmann1234/diff_cover/pull/421)

- Bump tomli from 2.0.2 to 2.2.1 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in
  [https://github.com/Bachmann1234/diff_cover/pull/425](https://redirect.github.com/Bachmann1234/diff_cover/pull/425)

#### New Contributors

- [@&#8203;ssbarnea](https://redirect.github.com/ssbarnea) made their first contribution in
  [https://github.com/Bachmann1234/diff_cover/pull/427](https://redirect.github.com/Bachmann1234/diff_cover/pull/427)

**Full Changelog**: https://github.com/Bachmann1234/diff_cover/compare/v9.2.0...v9.2.1

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS41OC4xIiwidXBkYXRlZEluVmVyIjoiMzkuNTguMSIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.20 (2024-12-11)

### Bug Fixes

- **deps**: Update dependency iterpy to v1.11.0
  ([#793](https://github.com/MartinBernstorff/Memium/pull/793),
  [`8029894`](https://github.com/MartinBernstorff/Memium/commit/80298949b7ddb5234b60667ea98872ef71034f07))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [iterpy](https://redirect.github.com/MartinBernstorff/iterpy) | `==1.9.1` -> `==1.11.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/iterpy/1.11.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/iterpy/1.11.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/iterpy/1.9.1/1.11.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/iterpy/1.9.1/1.11.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>MartinBernstorff/iterpy (iterpy)</summary>

###
  [`v1.11.0`](https://redirect.github.com/MartinBernstorff/iterpy/blob/HEAD/CHANGELOG.md#v1110-2024-12-11)

[Compare Source](https://redirect.github.com/MartinBernstorff/iterpy/compare/v1.10.0...v1.11.0)

##### Feature

- feat: make arr a subclass of list
  ([#&#8203;211](https://redirect.github.com/MartinBernstorff/iterpy/issues/211))

BREAKING: Renames `.count()` to `.len()` to avoid conflicts with Python `list` while maintaining
  backwards compatability.
  ([`5e1cffd`](https://redirect.github.com/MartinBernstorff/iterpy/commit/5e1cffd7f59c1865524129f1b53b5c585109926d))

##### Unknown

- Revert "feat: make arr a subclass of list"
  ([#&#8203;210](https://redirect.github.com/MartinBernstorff/iterpy/issues/210))
  ([`9b143f5`](https://redirect.github.com/MartinBernstorff/iterpy/commit/9b143f542e8648450f98ad3d778d25e9ef893f15))

- Revert "feat: make arr a subclass of list
  ([#&#8203;209](https://redirect.github.com/MartinBernstorff/iterpy/issues/209))"

This reverts commit
  [`05b4a70`](https://redirect.github.com/MartinBernstorff/iterpy/commit/05b4a7079237d97cd47e00375b3829f264f81670).
  ([`a335413`](https://redirect.github.com/MartinBernstorff/iterpy/commit/a33541325846e12f0c9e5bdeb92c92d98cdbc940))

###
  [`v1.10.0`](https://redirect.github.com/MartinBernstorff/iterpy/blob/HEAD/CHANGELOG.md#v1100-2024-12-11)

[Compare Source](https://redirect.github.com/MartinBernstorff/iterpy/compare/v1.9.1...v1.10.0)

##### Chore

- chore: move to uv ([#&#8203;208](https://redirect.github.com/MartinBernstorff/iterpy/issues/208))
  ([`3052556`](https://redirect.github.com/MartinBernstorff/iterpy/commit/305255646e8b8d24f608998aa69514a11a15a68b))

- chore: delete dependabot.yml
  ([`0b60b52`](https://redirect.github.com/MartinBernstorff/iterpy/commit/0b60b52dc7a452bfa78ba20e1a971edd85b8cba8))

- feat: make arr a subclass of list
  ([#&#8203;209](https://redirect.github.com/MartinBernstorff/iterpy/issues/209))
  ([`05b4a70`](https://redirect.github.com/MartinBernstorff/iterpy/commit/05b4a7079237d97cd47e00375b3829f264f81670))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS41OC4xIiwidXBkYXRlZEluVmVyIjoiMzkuNTguMSIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.19 (2024-12-06)

### Bug Fixes

- **deps**: Update dependency sentry-sdk to v2.19.2
  ([#792](https://github.com/MartinBernstorff/Memium/pull/792),
  [`95402e2`](https://github.com/MartinBernstorff/Memium/commit/95402e2590a219fc669aab6b3cc33efe00069f10))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [sentry-sdk](https://redirect.github.com/getsentry/sentry-python)
  ([changelog](https://redirect.github.com/getsentry/sentry-python/blob/master/CHANGELOG.md)) |
  `==2.19.1` -> `==2.19.2` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/sentry-sdk/2.19.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/sentry-sdk/2.19.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/sentry-sdk/2.19.1/2.19.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/sentry-sdk/2.19.1/2.19.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>getsentry/sentry-python (sentry-sdk)</summary>

### [`v2.19.2`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2192)

[Compare Source](https://redirect.github.com/getsentry/sentry-python/compare/2.19.1...2.19.2)

##### Various fixes & improvements

- Deepcopy and ensure get_all function always terminates
  ([#&#8203;3861](https://redirect.github.com/getsentry/sentry-python/issues/3861)) by
  [@&#8203;cmanallen](https://redirect.github.com/cmanallen) - Cleanup chalice test environment
  ([#&#8203;3858](https://redirect.github.com/getsentry/sentry-python/issues/3858)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS40Mi40IiwidXBkYXRlZEluVmVyIjoiMzkuNDIuNCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.18 (2024-12-05)

### Bug Fixes

- **deps**: Update dependency sentry-sdk to v2.19.1
  ([#791](https://github.com/MartinBernstorff/Memium/pull/791),
  [`b9ba9ab`](https://github.com/MartinBernstorff/Memium/commit/b9ba9ab7fe9ffab9d63f4c1ee14d670b5559d0e3))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [sentry-sdk](https://redirect.github.com/getsentry/sentry-python)
  ([changelog](https://redirect.github.com/getsentry/sentry-python/blob/master/CHANGELOG.md)) |
  `==2.19.0` -> `==2.19.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/sentry-sdk/2.19.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/sentry-sdk/2.19.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/sentry-sdk/2.19.0/2.19.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/sentry-sdk/2.19.0/2.19.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>getsentry/sentry-python (sentry-sdk)</summary>

### [`v2.19.1`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2191)

[Compare Source](https://redirect.github.com/getsentry/sentry-python/compare/2.19.0...2.19.1)

##### Various fixes & improvements

- Fix errors when instrumenting Django cache
  ([#&#8203;3855](https://redirect.github.com/getsentry/sentry-python/issues/3855)) by
  [@&#8203;BYK](https://redirect.github.com/BYK) - Copy `scope.client` reference as well
  ([#&#8203;3857](https://redirect.github.com/getsentry/sentry-python/issues/3857)) by
  [@&#8203;sl0thentr0py](https://redirect.github.com/sl0thentr0py) - Don't give up on Spotlight on 3
  errors ([#&#8203;3856](https://redirect.github.com/getsentry/sentry-python/issues/3856)) by
  [@&#8203;BYK](https://redirect.github.com/BYK) - Add missing stack frames
  ([#&#8203;3673](https://redirect.github.com/getsentry/sentry-python/issues/3673)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Fix wrong metadata type in async
  gRPC interceptor ([#&#8203;3205](https://redirect.github.com/getsentry/sentry-python/issues/3205))
  by [@&#8203;fdellekart](https://redirect.github.com/fdellekart) - Rename launch darkly hook to
  match JS SDK ([#&#8203;3743](https://redirect.github.com/getsentry/sentry-python/issues/3743)) by
  [@&#8203;aliu39](https://redirect.github.com/aliu39) - Script for checking if our instrumented
  libs are Python 3.13 compatible
  ([#&#8203;3425](https://redirect.github.com/getsentry/sentry-python/issues/3425)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Improve Ray tests
  ([#&#8203;3846](https://redirect.github.com/getsentry/sentry-python/issues/3846)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - Test with Celery `5.5.0rc3`
  ([#&#8203;3842](https://redirect.github.com/getsentry/sentry-python/issues/3842)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Fix asyncio testing setup
  ([#&#8203;3832](https://redirect.github.com/getsentry/sentry-python/issues/3832)) by
  [@&#8203;sl0thentr0py](https://redirect.github.com/sl0thentr0py) - Bump `codecov/codecov-action`
  from `5.0.2` to `5.0.7`
  ([#&#8203;3821](https://redirect.github.com/getsentry/sentry-python/issues/3821)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot) - Fix CI
  ([#&#8203;3834](https://redirect.github.com/getsentry/sentry-python/issues/3834)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - Use new ClickHouse GH action
  ([#&#8203;3826](https://redirect.github.com/getsentry/sentry-python/issues/3826)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS40Mi40IiwidXBkYXRlZEluVmVyIjoiMzkuNDIuNCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.17 (2024-12-04)

### Bug Fixes

- **deps**: Update dependency pyright to v1.1.390
  ([#789](https://github.com/MartinBernstorff/Memium/pull/789),
  [`286d9b0`](https://github.com/MartinBernstorff/Memium/commit/286d9b08abfeb3113639b52c7117b2c25fd3a4ac))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pyright](https://redirect.github.com/RobertCraigie/pyright-python) | `==1.1.389` -> `==1.1.390` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pyright/1.1.390?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pyright/1.1.390?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pyright/1.1.389/1.1.390?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pyright/1.1.389/1.1.390?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>RobertCraigie/pyright-python (pyright)</summary>

###
  [`v1.1.390`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.389...v1.1.390)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.389...v1.1.390)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS40Mi40IiwidXBkYXRlZEluVmVyIjoiMzkuNDIuNCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency typer to v0.15.1
  ([#790](https://github.com/MartinBernstorff/Memium/pull/790),
  [`5c4f61f`](https://github.com/MartinBernstorff/Memium/commit/5c4f61f91b4e4f56a98b5402fe06f965e5ddab53))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [typer](https://redirect.github.com/fastapi/typer)
  ([changelog](https://typer.tiangolo.com/release-notes/)) | `==0.15.0` -> `==0.15.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/typer/0.15.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/typer/0.15.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/typer/0.15.0/0.15.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/typer/0.15.0/0.15.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS40Mi40IiwidXBkYXRlZEluVmVyIjoiMzkuNDIuNCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.16 (2024-12-03)

### Bug Fixes

- **deps**: Update dependency pydantic to v2.10.3
  ([#787](https://github.com/MartinBernstorff/Memium/pull/787),
  [`620dc5e`](https://github.com/MartinBernstorff/Memium/commit/620dc5e778ea694178c53b18acda1e1740ac3d17))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pydantic](https://redirect.github.com/pydantic/pydantic)
  ([changelog](https://docs.pydantic.dev/latest/changelog/)) | `==2.10.2` -> `==2.10.3` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pydantic/2.10.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pydantic/2.10.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pydantic/2.10.2/2.10.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pydantic/2.10.2/2.10.3?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pydantic/pydantic (pydantic)</summary>

### [`v2.10.3`](https://redirect.github.com/pydantic/pydantic/blob/HEAD/HISTORY.md#v2103-2024-12-03)

[Compare Source](https://redirect.github.com/pydantic/pydantic/compare/v2.10.2...v2.10.3)

[GitHub release](https://redirect.github.com/pydantic/pydantic/releases/tag/v2.10.3)

##### What's Changed

##### Fixes

- Set fields when `defer_build` is set on Pydantic dataclasses by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10984](https://redirect.github.com/pydantic/pydantic/pull/10984) - Do not resolve the
  JSON Schema reference for `dict` core schema keys by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10989](https://redirect.github.com/pydantic/pydantic/pull/10989) - Use the globals of the
  function when evaluating the return type for `PlainSerializer` and `WrapSerializer` functions by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11008](https://redirect.github.com/pydantic/pydantic/pull/11008) - Fix host required
  enforcement for urls to be compatible with v2.9 behavior by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;11027](https://redirect.github.com/pydantic/pydantic/pull/11027) - Add a
  `default_factory_takes_validated_data` property to `FieldInfo` by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;11034](https://redirect.github.com/pydantic/pydantic/pull/11034) - Fix url json schema in
  `serialization` mode by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;11035](https://redirect.github.com/pydantic/pydantic/pull/11035)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS40Mi40IiwidXBkYXRlZEluVmVyIjoiMzkuNDIuNCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency typer to v0.15.0
  ([#788](https://github.com/MartinBernstorff/Memium/pull/788),
  [`2eff4ff`](https://github.com/MartinBernstorff/Memium/commit/2eff4fff092edcd6ffa0a5edf6d3e22bae6492c0))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [typer](https://redirect.github.com/fastapi/typer)
  ([changelog](https://typer.tiangolo.com/release-notes/)) | `==0.14.0` -> `==0.15.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/typer/0.15.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/typer/0.15.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/typer/0.14.0/0.15.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/typer/0.14.0/0.15.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>fastapi/typer (typer)</summary>

### [`v0.15.0`](https://redirect.github.com/fastapi/typer/releases/tag/0.15.0)

[Compare Source](https://redirect.github.com/fastapi/typer/compare/0.14.0...0.15.0)

##### Features

- ✨ Add support for extending typer apps without passing a name, add commands to the top level. PR
  [#&#8203;1037](https://redirect.github.com/fastapi/typer/pull/1037) by
  [@&#8203;patrick91](https://redirect.github.com/patrick91). - New docs: [One File Per
  Command](https://typer.tiangolo.com/tutorial/one-file-per-command/).

##### Internal

- ⬆ Bump mkdocs-material from 9.5.46 to 9.5.47. PR
  [#&#8203;1070](https://redirect.github.com/fastapi/typer/pull/1070) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump ruff from 0.8.0
  to 0.8.1. PR [#&#8203;1066](https://redirect.github.com/fastapi/typer/pull/1066) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot).

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS40Mi40IiwidXBkYXRlZEluVmVyIjoiMzkuNDIuNCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Chores

- **deps**: Update python-semantic-release/python-semantic-release action to v9.15.0
  ([#785](https://github.com/MartinBernstorff/Memium/pull/785),
  [`f61e539`](https://github.com/MartinBernstorff/Memium/commit/f61e5392398f4db47443e954313c528fc832d587))

This PR contains the following updates:

| Package | Type | Update | Change | |---|---|---|---| |
  [python-semantic-release/python-semantic-release](https://redirect.github.com/python-semantic-release/python-semantic-release)
  | action | minor | `v9.14.0` -> `v9.15.0` |

---

### Release Notes

<details> <summary>python-semantic-release/python-semantic-release
  (python-semantic-release/python-semantic-release)</summary>

###
  [`v9.15.0`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.md#v9150-2024-12-02)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.14.0...v9.15.0)

##### Bug Fixes

- **cmd-version**: Ensure release utilizes a timezone aware datetime

([`ca817ed`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/ca817ed9024cf84b306a047675534cc36dc116b2))

- **default-changelog**: Alphabetically sort commit descriptions in version type sections

([`bdaaf5a`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/bdaaf5a460ca77edc40070ee799430122132dc45))

##### Features

- **commit-parser**: Enable parsers to flag commit to be ignored for changelog

([#&#8203;1108](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1108),

[`0cc668c`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/0cc668c36490401dff26bb2c3141f6120a2c47d0))

This adds an attribute to the ParsedCommit object that allows custom parsers to set to false if it
  is desired to ignore the commit completely from entry into the changelog.

Resolves:
  [#&#8203;778](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/778)

- test(parser-custom): add test w/ parser that toggles if a parsed commit is included in changelog

<!---->

- **default-changelog**: Add a separate formatted breaking changes section

([#&#8203;1110](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1110),

[`4fde30e`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/4fde30e0936ecd186e448f1caf18d9ba377c55ad))

Resolves:
  [#&#8203;244](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/244)

- test(fixtures): update repo changelog generator to add breaking descriptions

- test(default-changelog): add unit tests to demonstrate breaking change descriptions

- test(release-notes): add unit tests to demonstrate breaking change descriptions

- feat(changelog-md): add a breaking changes section to default Markdown template

- feat(changelog-rst): add a breaking changes section to default reStructuredText template

- feat(changelog-md): alphabetize breaking change descriptions in markdown changelog template

- feat(changelog-rst): alphabetize breaking change descriptions in ReStructuredText template

- **default-changelog**: Alphabetize commit summaries & scopes in change sections

([#&#8203;1111](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1111),

[`8327068`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/83270683fd02b626ed32179d94fa1e3c7175d113))

- test(fixtures): force non-alphabetical release history to validate template sorting

- test(default-changelog): update unit test to enforce sorting of commit desc in version sections

- test(release-notes): update unit test to enforce sorting of commit desc in version sections

- feat(changelog-md): alphabetize commit summaries & scopes in markdown changelog template

- feat(changelog-rst): alphabetize commit summaries & scopes in ReStructuredText template

- **parsers**: Enable parsers to identify linked issues on a commit

([#&#8203;1109](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1109),

[`f90b8dc`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/f90b8dc6ce9f112ef2c98539d155f9de24398301))

- refactor(parsers): add parser option validation to commit parsing

- docs(api-parsers): add option documentation to parser options

- feat(parsers): add `other_allowed_tags` option for commit parser options

- feat(parser-custom): enable custom parsers to identify linked issues on a commit

- test(parser-angular): add unit tests to verify parsing of issue numbers

- test(parser-emoji): add unit tests to verify parsing of issue numbers

- test(parser-scipy): add unit tests to verify parsing of issue numbers

- fix(util): prevent git footers from being collapsed during parse

- feat(parser-angular): automatically parse angular issue footers from commit messages

- feat(parser-emoji): parse issue reference footers from commit messages

- docs(commit-parsing): improve & expand commit parsing w/ parser descriptions

- docs(changelog-templates): update examples using new `commit.linked_issues` attribute

- chore(docs): update documentation configuration for team publishing

- **release-notes**: Add tag comparison link to release notes when supported

([#&#8203;1107](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1107),

[`9073344`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/9073344164294360843ef5522e7e4c529985984d))

- test(release-notes): adjust test case to include a version compare link

- test(cmd-changelog): add test to ensure multiple variants of release notes are published

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update python-semantic-release/python-semantic-release action to v9.15.1
  ([#786](https://github.com/MartinBernstorff/Memium/pull/786),
  [`f448567`](https://github.com/MartinBernstorff/Memium/commit/f448567765a7add8f3a298ff57e48714bec3bc0b))

This PR contains the following updates:

| Package | Type | Update | Change | |---|---|---|---| |
  [python-semantic-release/python-semantic-release](https://redirect.github.com/python-semantic-release/python-semantic-release)
  | action | patch | `v9.15.0` -> `v9.15.1` |

---

### Release Notes

<details> <summary>python-semantic-release/python-semantic-release
  (python-semantic-release/python-semantic-release)</summary>

###
  [`v9.15.1`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.md#v9151-2024-12-03)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.15.0...v9.15.1)

##### Bug Fixes

- **changelog-md**: Fix commit sort of breaking descriptions section

([`75b342e`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/75b342e6259412cb82d8b7663e5ee4536d14f407))

- **parser-angular**: Ensure issues are sorted by numeric value rather than text sorted

([`3858add`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/3858add582fe758dc2ae967d0cd051d43418ecd0))

- **parser-emoji**: Ensure issues are sorted by numeric value rather than text sorted

([`7b8d2d9`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/7b8d2d92e135ab46d1be477073ccccc8c576f121))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS40Mi40IiwidXBkYXRlZEluVmVyIjoiMzkuNDIuNCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.15 (2024-12-01)

### Bug Fixes

- **deps**: Update dependency pytest to v8.3.4
  ([#784](https://github.com/MartinBernstorff/Memium/pull/784),
  [`b41fdb2`](https://github.com/MartinBernstorff/Memium/commit/b41fdb24477c93475b295eece903fd57f36a546c))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pytest](https://redirect.github.com/pytest-dev/pytest)
  ([changelog](https://docs.pytest.org/en/stable/changelog.html)) | `==8.3.3` -> `==8.3.4` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pytest/8.3.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pytest/8.3.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pytest/8.3.3/8.3.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pytest/8.3.3/8.3.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pytest-dev/pytest (pytest)</summary>

### [`v8.3.4`](https://redirect.github.com/pytest-dev/pytest/releases/tag/8.3.4)

[Compare Source](https://redirect.github.com/pytest-dev/pytest/compare/8.3.3...8.3.4)

### pytest 8.3.4 (2024-12-01)

#### Bug fixes

- [#&#8203;12592](https://redirect.github.com/pytest-dev/pytest/issues/12592): Fixed
  `KeyError`{.interpreted-text role="class"} crash when using `--import-mode=importlib` in a
  directory layout where a directory contains a child directory with the same name.

- [#&#8203;12818](https://redirect.github.com/pytest-dev/pytest/issues/12818): Assertion rewriting
  now preserves the source ranges of the original instructions, making it play well with tools that
  deal with the `AST`, like [executing](https://redirect.github.com/alexmojaki/executing).

- [#&#8203;12849](https://redirect.github.com/pytest-dev/pytest/issues/12849): ANSI escape codes for
  colored output now handled correctly in `pytest.fail`{.interpreted-text role="func"} with
  \[pytrace=False]{.title-ref}.

- [#&#8203;9353](https://redirect.github.com/pytest-dev/pytest/issues/9353):
  `pytest.approx`{.interpreted-text role="func"} now uses strict equality when given booleans.

#### Improved documentation

- [#&#8203;10558](https://redirect.github.com/pytest-dev/pytest/issues/10558): Fix ambiguous
  docstring of `pytest.Config.getoption`{.interpreted-text role="func"}.

- [#&#8203;10829](https://redirect.github.com/pytest-dev/pytest/issues/10829): Improve documentation
  on the current handling of the `--basetemp` option and its lack of retention functionality
  (`temporary directory location and retention`{.interpreted-text role="ref"}).

- [#&#8203;12866](https://redirect.github.com/pytest-dev/pytest/issues/12866): Improved
  cross-references concerning the `recwarn`{.interpreted-text role="fixture"} fixture.

- [#&#8203;12966](https://redirect.github.com/pytest-dev/pytest/issues/12966): Clarify
  `filterwarnings`{.interpreted-text role="ref"} docs on filter precedence/order when using multiple
  `@pytest.mark.filterwarnings <pytest.mark.filterwarnings ref>`{.interpreted-text role="ref"}
  marks.

#### Contributor-facing changes

- [#&#8203;12497](https://redirect.github.com/pytest-dev/pytest/issues/12497): Fixed two failing
  pdb-related tests on Python 3.13.

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.14 (2024-11-29)

### Bug Fixes

- **deps**: Update dependency typer to v0.14.0
  ([#783](https://github.com/MartinBernstorff/Memium/pull/783),
  [`a5f1d7f`](https://github.com/MartinBernstorff/Memium/commit/a5f1d7f23d75bd55c681223d2a755cce4bdd4c30))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [typer](https://redirect.github.com/fastapi/typer)
  ([changelog](https://typer.tiangolo.com/release-notes/)) | `==0.13.1` -> `==0.14.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/typer/0.14.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/typer/0.14.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/typer/0.13.1/0.14.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/typer/0.13.1/0.14.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>fastapi/typer (typer)</summary>

### [`v0.14.0`](https://redirect.github.com/fastapi/typer/releases/tag/0.14.0)

[Compare Source](https://redirect.github.com/fastapi/typer/compare/0.13.1...0.14.0)

##### Breaking Changes

- 🔥 Remove auto naming of groups added via `add_typer` based on the group's callback function name.
  PR [#&#8203;1052](https://redirect.github.com/fastapi/typer/pull/1052) by
  [@&#8203;patrick91](https://redirect.github.com/patrick91).

Before, it was supported to infer the name of a command group from the callback function name in the
  sub-app, so, in this code:

```python import typer

app = typer.Typer() users_app = typer.Typer()

app.add_typer(users_app)

@&#8203;users_app.callback() def users(): # <-- This was the inferred command group name """ Manage
  users in the app. """

@&#8203;users_app.command() def create(name: str): print(f"Creating user: {name}") ```

...the command group would be named `users`, based on the name of the function `def users()`.

Now you need to set it explicitly:

app.add_typer(users_app, name="users") # <-- Explicitly set the command group name

@&#8203;users_app.callback() def users(): """ Manage users in the app. """

Updated docs [SubCommand Name and
  Help](https://typer.tiangolo.com/tutorial/subcommands/name-and-help/).

**Note**: this change will enable important features in the next release. 🤩

##### Internal

- ⬆ Bump pypa/gh-action-pypi-publish from 1.10.3 to 1.12.2. PR
  [#&#8203;1043](https://redirect.github.com/fastapi/typer/pull/1043) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump mkdocs-material
  from 9.5.44 to 9.5.46. PR [#&#8203;1062](https://redirect.github.com/fastapi/typer/pull/1062) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump ruff from 0.7.4
  to 0.8.0. PR [#&#8203;1059](https://redirect.github.com/fastapi/typer/pull/1059) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  astral-sh/setup-uv from 3 to 4. PR
  [#&#8203;1061](https://redirect.github.com/fastapi/typer/pull/1061) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1053](https://redirect.github.com/fastapi/typer/pull/1053) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci).

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.13 (2024-11-27)

### Bug Fixes

- **deps**: Update dependency iterpy to v1.9.1
  ([#782](https://github.com/MartinBernstorff/Memium/pull/782),
  [`b94875d`](https://github.com/MartinBernstorff/Memium/commit/b94875da21cb10f24365ca5b46c624db1e92355a))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [iterpy](https://redirect.github.com/MartinBernstorff/iterpy) | `==1.9.0` -> `==1.9.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/iterpy/1.9.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/iterpy/1.9.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/iterpy/1.9.0/1.9.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/iterpy/1.9.0/1.9.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>MartinBernstorff/iterpy (iterpy)</summary>

###
  [`v1.9.1`](https://redirect.github.com/MartinBernstorff/iterpy/blob/HEAD/CHANGELOG.md#v191-2024-11-27)

[Compare Source](https://redirect.github.com/MartinBernstorff/iterpy/compare/v1.9.0...v1.9.1)

##### Chore

- chore: remove placeholder file
  ([`c19a07d`](https://redirect.github.com/MartinBernstorff/iterpy/commit/c19a07dbb7e1761ec8badb6ec001d88c1c11578a))

##### Documentation

- docs: update readme
  ([`c3c614a`](https://redirect.github.com/MartinBernstorff/iterpy/commit/c3c614a363612800e7af8f09e8418b85444e4dae))

- docs: documentation for eager iters
  ([#&#8203;143](https://redirect.github.com/MartinBernstorff/iterpy/issues/143))
  ([`7f45065`](https://redirect.github.com/MartinBernstorff/iterpy/commit/7f4506553e3604451e1544cd447d69902068580c))

- docs: documentation for eager iters
  ([`108d3b5`](https://redirect.github.com/MartinBernstorff/iterpy/commit/108d3b5ca895c81b18bdc66c9b2f8315541f8406))

##### Fix

- fix: improve export robustness
  ([`b9e61be`](https://redirect.github.com/MartinBernstorff/iterpy/commit/b9e61be72db4eb4067f66fc5ba3339f8e9d90194))

##### Refactor

- refactor([#&#8203;146](https://redirect.github.com/MartinBernstorff/iterpy/issues/146)): most
  logic from Arr should call Iter
  ([#&#8203;147](https://redirect.github.com/MartinBernstorff/iterpy/issues/147))

Fixes [#&#8203;146](https://redirect.github.com/MartinBernstorff/iterpy/issues/146)
  ([`17d637d`](https://redirect.github.com/MartinBernstorff/iterpy/commit/17d637d844880521da35dfcb3e1df887304cff5e))

- refactor([#&#8203;146](https://redirect.github.com/MartinBernstorff/iterpy/issues/146)): most
  logic from Arr should call Iter

Fixes [#&#8203;146](https://redirect.github.com/MartinBernstorff/iterpy/issues/146)
  ([`fcffbff`](https://redirect.github.com/MartinBernstorff/iterpy/commit/fcffbffb84dc01b97af85e05b912e8f1f0123891))

##### Unknown

- deps:(deps): bump pyright from 1.1.362 to 1.1.363
  ([#&#8203;175](https://redirect.github.com/MartinBernstorff/iterpy/issues/175))
  ([`4296b87`](https://redirect.github.com/MartinBernstorff/iterpy/commit/4296b87f6c3352728d800afaa615aca9a6c9418b))

- deps:(deps): bump pyright from 1.1.362 to 1.1.363

Bumps [pyright](https://redirect.github.com/RobertCraigie/pyright-python) from 1.1.362 to 1.1.363.

- [Release notes](https://redirect.github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.362...v1.1.363)

***

updated-dependencies:

- dependency-name: pyright dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot\[bot] \<support@github.com>

([`7115348`](https://redirect.github.com/MartinBernstorff/iterpy/commit/7115348d9920dc2ffa2564d9b3574a385411102f))

- deps:(deps): bump pytest from 8.2.0 to 8.2.1
  ([#&#8203;174](https://redirect.github.com/MartinBernstorff/iterpy/issues/174))
  ([`a84c9e1`](https://redirect.github.com/MartinBernstorff/iterpy/commit/a84c9e144b55d3806157bbace240d9fe05215379))

- deps:(deps): bump pytest from 8.2.0 to 8.2.1

Bumps [pytest](https://redirect.github.com/pytest-dev/pytest) from 8.2.0 to 8.2.1.

- [Release notes](https://redirect.github.com/pytest-dev/pytest/releases) -
  [Changelog](https://redirect.github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://redirect.github.com/pytest-dev/pytest/compare/8.2.0...8.2.1)

- dependency-name: pytest dependency-type: direct:production update-type:
  version-update:semver-patch ...

([`3f75218`](https://redirect.github.com/MartinBernstorff/iterpy/commit/3f7521807f5b8ae63e6841a6d9e994a8636f8148))

- deps:(deps): bump pyright from 1.1.361 to 1.1.362
  ([#&#8203;173](https://redirect.github.com/MartinBernstorff/iterpy/issues/173))
  ([`47c2e9a`](https://redirect.github.com/MartinBernstorff/iterpy/commit/47c2e9a987b83849bb0ee8773921cb5618bf9d54))

- deps:(deps): bump ruff from 0.4.3 to 0.4.4
  ([#&#8203;172](https://redirect.github.com/MartinBernstorff/iterpy/issues/172))
  ([`f8a9a30`](https://redirect.github.com/MartinBernstorff/iterpy/commit/f8a9a3000679f48b552052f3adcd3a6ced6b2c81))

- deps:(deps): bump pyright from 1.1.361 to 1.1.362

Bumps [pyright](https://redirect.github.com/RobertCraigie/pyright-python) from 1.1.361 to 1.1.362.

- [Release notes](https://redirect.github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.361...v1.1.362)

([`10259b3`](https://redirect.github.com/MartinBernstorff/iterpy/commit/10259b36aff8b1ab7f8c9fb848ac32f36b2df234))

- deps:(deps): bump ruff from 0.4.3 to 0.4.4

Bumps [ruff](https://redirect.github.com/astral-sh/ruff) from 0.4.3 to 0.4.4.

- [Release notes](https://redirect.github.com/astral-sh/ruff/releases) -
  [Changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://redirect.github.com/astral-sh/ruff/compare/v0.4.3...v0.4.4)

- dependency-name: ruff dependency-type: direct:production update-type: version-update:semver-patch
  ...

([`7614f83`](https://redirect.github.com/MartinBernstorff/iterpy/commit/7614f83bec9a5e679b5bac9e8ff1757d3bf58578))

- Update README.md
  ([`03836f3`](https://redirect.github.com/MartinBernstorff/iterpy/commit/03836f3a6a82e151e083c226bf30d3fcd9821e1d))

- deps:(deps): bump pyright from 1.1.360 to 1.1.361
  ([#&#8203;170](https://redirect.github.com/MartinBernstorff/iterpy/issues/170))
  ([`b27c82e`](https://redirect.github.com/MartinBernstorff/iterpy/commit/b27c82ea0afb266253577116afcd0450993ca717))

- deps:(deps): bump ruff from 0.4.2 to 0.4.3
  ([#&#8203;169](https://redirect.github.com/MartinBernstorff/iterpy/issues/169))
  ([`1da3055`](https://redirect.github.com/MartinBernstorff/iterpy/commit/1da305513eb06e78ece780a98f629e203b14b765))

- deps:(deps): bump pyright from 1.1.360 to 1.1.361

Bumps [pyright](https://redirect.github.com/RobertCraigie/pyright-python) from 1.1.360 to 1.1.361.

- [Release notes](https://redirect.github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.360...v1.1.361)

([`4a05bb3`](https://redirect.github.com/MartinBernstorff/iterpy/commit/4a05bb3f53db922405a3507d16dbd3d9556a4d41))

- deps:(deps): bump ruff from 0.4.2 to 0.4.3

Bumps [ruff](https://redirect.github.com/astral-sh/ruff) from 0.4.2 to 0.4.3.

- [Release notes](https://redirect.github.com/astral-sh/ruff/releases) -
  [Changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://redirect.github.com/astral-sh/ruff/compare/v0.4.2...v0.4.3)

([`62e0ac9`](https://redirect.github.com/MartinBernstorff/iterpy/commit/62e0ac9775f84abd0eaaf0203c757acfa8fc1c43))

- deps:(deps): bump pyright from 1.1.359 to 1.1.360
  ([#&#8203;168](https://redirect.github.com/MartinBernstorff/iterpy/issues/168))
  ([`75eace3`](https://redirect.github.com/MartinBernstorff/iterpy/commit/75eace3b85730c3ceae00c15fc02dc5c3577fc53))

- deps:(deps): bump pyright from 1.1.359 to 1.1.360

Bumps [pyright](https://redirect.github.com/RobertCraigie/pyright-python) from 1.1.359 to 1.1.360.

- [Release notes](https://redirect.github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.359...v1.1.360)

([`a5471ba`](https://redirect.github.com/MartinBernstorff/iterpy/commit/a5471ba8bb032d5c8c08997b29e777f310fe7008))

- deps:(deps): bump pytest from 8.1.1 to 8.2.0
  ([#&#8203;167](https://redirect.github.com/MartinBernstorff/iterpy/issues/167))
  ([`f686475`](https://redirect.github.com/MartinBernstorff/iterpy/commit/f686475b154f6f0461491fc728d79f356fabcf32))

- deps:(deps): bump ruff from 0.4.1 to 0.4.2
  ([#&#8203;166](https://redirect.github.com/MartinBernstorff/iterpy/issues/166))
  ([`42ee1ed`](https://redirect.github.com/MartinBernstorff/iterpy/commit/42ee1ed363c00b34071f7f6e245c4672dc8c16ce))

- deps:(deps): bump pytest-xdist from 3.5.0 to 3.6.1
  ([#&#8203;165](https://redirect.github.com/MartinBernstorff/iterpy/issues/165))
  ([`1891ce5`](https://redirect.github.com/MartinBernstorff/iterpy/commit/1891ce5932f3b46cd80f54808c3acdaefcd8fc8b))

- deps:(deps): bump pytest from 8.1.1 to 8.2.0

Bumps [pytest](https://redirect.github.com/pytest-dev/pytest) from 8.1.1 to 8.2.0.

- [Release notes](https://redirect.github.com/pytest-dev/pytest/releases) -
  [Changelog](https://redirect.github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://redirect.github.com/pytest-dev/pytest/compare/8.1.1...8.2.0)

- dependency-name: pytest dependency-type: direct:production update-type:
  version-update:semver-minor ...

([`46f1158`](https://redirect.github.com/MartinBernstorff/iterpy/commit/46f11588d883c932eff77f7150608774c93c5ba1))

- deps:(deps): bump ruff from 0.4.1 to 0.4.2

Bumps [ruff](https://redirect.github.com/astral-sh/ruff) from 0.4.1 to 0.4.2.

- [Release notes](https://redirect.github.com/astral-sh/ruff/releases) -
  [Changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://redirect.github.com/astral-sh/ruff/compare/v0.4.1...v0.4.2)

([`d28a08f`](https://redirect.github.com/MartinBernstorff/iterpy/commit/d28a08fcd7f03ce660410413b270bca9037eef02))

- deps:(deps): bump pytest-xdist from 3.5.0 to 3.6.1

Bumps [pytest-xdist](https://redirect.github.com/pytest-dev/pytest-xdist) from 3.5.0 to 3.6.1.

- [Release notes](https://redirect.github.com/pytest-dev/pytest-xdist/releases) -
  [Changelog](https://redirect.github.com/pytest-dev/pytest-xdist/blob/master/CHANGELOG.rst) -
  [Commits](https://redirect.github.com/pytest-dev/pytest-xdist/compare/v3.5.0...v3.6.1)

- dependency-name: pytest-xdist dependency-type: direct:production update-type:
  version-update:semver-minor ...

([`5d918ab`](https://redirect.github.com/MartinBernstorff/iterpy/commit/5d918ab10088238ef5c7f3b5ca9c33a5ab588baa))

- deps:(deps): bump ruff from 0.3.7 to 0.4.1
  ([#&#8203;164](https://redirect.github.com/MartinBernstorff/iterpy/issues/164))
  ([`813d1ee`](https://redirect.github.com/MartinBernstorff/iterpy/commit/813d1ee6142da075f52610418cb6ef2c4500b65d))

- deps:(deps): bump pyright from 1.1.358 to 1.1.359
  ([#&#8203;163](https://redirect.github.com/MartinBernstorff/iterpy/issues/163))
  ([`67dff5c`](https://redirect.github.com/MartinBernstorff/iterpy/commit/67dff5cca03ba4a0a937559b2bc8721999b69183))

- deps:(deps): bump ruff from 0.3.7 to 0.4.1

Bumps [ruff](https://redirect.github.com/astral-sh/ruff) from 0.3.7 to 0.4.1.

- [Release notes](https://redirect.github.com/astral-sh/ruff/releases) -
  [Changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://redirect.github.com/astral-sh/ruff/compare/v0.3.7...v0.4.1)

- dependency-name: ruff dependency-type: direct:production update-type: version-update:semver-minor
  ...

([`cc14105`](https://redirect.github.com/MartinBernstorff/iterpy/commit/cc14105e134393abff98f6f9cf37f3669a4004d0))

- deps:(deps): bump pyright from 1.1.358 to 1.1.359

Bumps [pyright](https://redirect.github.com/RobertCraigie/pyright-python) from 1.1.358 to 1.1.359.

- [Release notes](https://redirect.github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.358...v1.1.359)

([`ee59060`](https://redirect.github.com/MartinBernstorff/iterpy/commit/ee59060f501ca8b6f873380383a68cd4d4ebe9e2))

- deps:(deps): bump diff-cover from 8.0.3 to 9.0.0
  ([#&#8203;162](https://redirect.github.com/MartinBernstorff/iterpy/issues/162))
  ([`c839ce6`](https://redirect.github.com/MartinBernstorff/iterpy/commit/c839ce6c20314e0490f9ad3f017ad11d18a3ef18))

- deps:(deps): bump diff-cover from 8.0.3 to 9.0.0

Bumps [diff-cover](https://redirect.github.com/Bachmann1234/diff-cover) from 8.0.3 to 9.0.0.

- [Release notes](https://redirect.github.com/Bachmann1234/diff-cover/releases) -
  [Changelog](https://redirect.github.com/Bachmann1234/diff_cover/blob/main/CHANGELOG) -
  [Commits](https://redirect.github.com/Bachmann1234/diff-cover/compare/v8.0.3...v9.0.0)

- dependency-name: diff-cover dependency-type: direct:production update-type:
  version-update:semver-major ...

([`2cc8fd3`](https://redirect.github.com/MartinBernstorff/iterpy/commit/2cc8fd38647995d5bbdfe6228ef00bdc478babbb))

- deps:(deps): bump pyright from 1.1.357 to 1.1.358
  ([#&#8203;161](https://redirect.github.com/MartinBernstorff/iterpy/issues/161))
  ([`c2b6b5b`](https://redirect.github.com/MartinBernstorff/iterpy/commit/c2b6b5b05768d7437177c1154d2aeb2574034460))

- deps:(deps): bump ruff from 0.3.5 to 0.3.7
  ([#&#8203;160](https://redirect.github.com/MartinBernstorff/iterpy/issues/160))
  ([`88cb96a`](https://redirect.github.com/MartinBernstorff/iterpy/commit/88cb96a9ec66311231e06fa457276f3a579ee216))

- deps:(deps): bump pyright from 1.1.357 to 1.1.358

Bumps [pyright](https://redirect.github.com/RobertCraigie/pyright-python) from 1.1.357 to 1.1.358.

- [Release notes](https://redirect.github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.357...v1.1.358)

([`45cadab`](https://redirect.github.com/MartinBernstorff/iterpy/commit/45cadaba03f375053ba03d5ee3a5d0180b3e4e97))

- deps:(deps): bump ruff from 0.3.5 to 0.3.7

Bumps [ruff](https://redirect.github.com/astral-sh/ruff) from 0.3.5 to 0.3.7.

- [Release notes](https://redirect.github.com/astral-sh/ruff/releases) -
  [Changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://redirect.github.com/astral-sh/ruff/compare/v0.3.5...v0.3.7)

([`971e00e`](https://redirect.github.com/MartinBernstorff/iterpy/commit/971e00e666aa5646896f6e9e600eef11e6b5e673))

- deps:(deps-dev): bump ruff from 0.3.3 to 0.3.5
  ([#&#8203;159](https://redirect.github.com/MartinBernstorff/iterpy/issues/159))
  ([`484431b`](https://redirect.github.com/MartinBernstorff/iterpy/commit/484431bb0e1889bfdd6a43810fec7d34f8f9cb39))

- deps:(deps-dev): bump pyright from 1.1.356 to 1.1.357
  ([#&#8203;158](https://redirect.github.com/MartinBernstorff/iterpy/issues/158))
  ([`234cf14`](https://redirect.github.com/MartinBernstorff/iterpy/commit/234cf14447e709e3f8627d3efdf3726973aeaf6e))

- deps:(deps-dev): bump ruff from 0.3.3 to 0.3.5

Bumps [ruff](https://redirect.github.com/astral-sh/ruff) from 0.3.3 to 0.3.5.

- [Release notes](https://redirect.github.com/astral-sh/ruff/releases) -
  [Changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://redirect.github.com/astral-sh/ruff/compare/v0.3.3...v0.3.5)

([`c8d72c0`](https://redirect.github.com/MartinBernstorff/iterpy/commit/c8d72c06519c43794031c3daef1ca45a189e9005))

- deps:(deps-dev): bump pyright from 1.1.356 to 1.1.357

Bumps [pyright](https://redirect.github.com/RobertCraigie/pyright-python) from 1.1.356 to 1.1.357.

- [Release notes](https://redirect.github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.356...v1.1.357)

([`0cb9591`](https://redirect.github.com/MartinBernstorff/iterpy/commit/0cb95916d74a0254ad20f94b633a8195b5f1043a))

- deps:(deps-dev): bump pytest-cov from 4.1.0 to 5.0.0
  ([#&#8203;154](https://redirect.github.com/MartinBernstorff/iterpy/issues/154))
  ([`ca100c3`](https://redirect.github.com/MartinBernstorff/iterpy/commit/ca100c338e40973bb08cd453eacb5365cef44fa4))

- deps:(deps-dev): bump pytest-cov from 4.1.0 to 5.0.0

Bumps [pytest-cov](https://redirect.github.com/pytest-dev/pytest-cov) from 4.1.0 to 5.0.0.

- [Changelog](https://redirect.github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst) -
  [Commits](https://redirect.github.com/pytest-dev/pytest-cov/compare/v4.1.0...v5.0.0)

- dependency-name: pytest-cov dependency-type: direct:production update-type:
  version-update:semver-major ...

([`6030217`](https://redirect.github.com/MartinBernstorff/iterpy/commit/6030217a03f9174d2ea8b0bcd5da7ec01d756775))

- deps:(deps-dev): bump pyright from 1.1.353 to 1.1.356
  ([#&#8203;156](https://redirect.github.com/MartinBernstorff/iterpy/issues/156))
  ([`83f8ebf`](https://redirect.github.com/MartinBernstorff/iterpy/commit/83f8ebf99fbb0553b0a74c40142594c69ef1a258))

- deps:(deps-dev): bump pyright from 1.1.353 to 1.1.356

Bumps [pyright](https://redirect.github.com/RobertCraigie/pyright-python) from 1.1.353 to 1.1.356.

- [Release notes](https://redirect.github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.353...v1.1.356)

([`19b3a4d`](https://redirect.github.com/MartinBernstorff/iterpy/commit/19b3a4d0770677a7a4b55a488a4c2f06de2f6c08))

- deps:(deps-dev): bump ruff from 0.3.2 to 0.3.3
  ([#&#8203;151](https://redirect.github.com/MartinBernstorff/iterpy/issues/151))
  ([`b3e1fa6`](https://redirect.github.com/MartinBernstorff/iterpy/commit/b3e1fa621041c25ed3b187fc434d27275b96b315))

- deps:(deps-dev): bump ruff from 0.3.2 to 0.3.3

Bumps [ruff](https://redirect.github.com/astral-sh/ruff) from 0.3.2 to 0.3.3.

- [Release notes](https://redirect.github.com/astral-sh/ruff/releases) -
  [Changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://redirect.github.com/astral-sh/ruff/compare/v0.3.2...v0.3.3)

([`1b159da`](https://redirect.github.com/MartinBernstorff/iterpy/commit/1b159dab4feae1c7e078ad6aa4603133264b70ca))

- deps:(deps-dev): bump pytest from 8.1.0 to 8.1.1
  ([#&#8203;150](https://redirect.github.com/MartinBernstorff/iterpy/issues/150))
  ([`e7dff51`](https://redirect.github.com/MartinBernstorff/iterpy/commit/e7dff51c48fbcc4af2426ec4dad1c03a4fef1a49))

- deps:(deps-dev): bump pytest from 8.1.0 to 8.1.1

Bumps [pytest](https://redirect.github.com/pytest-dev/pytest) from 8.1.0 to 8.1.1.

- [Release notes](https://redirect.github.com/pytest-dev/pytest/releases) -
  [Changelog](https://redirect.github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://redirect.github.com/pytest-dev/pytest/compare/8.1.0...8.1.1)

([`7cebc14`](https://redirect.github.com/MartinBernstorff/iterpy/commit/7cebc146d72d542961ec083d112ef72701d1afc7))

- deps:(deps-dev): bump ruff from 0.3.0 to 0.3.2
  ([#&#8203;148](https://redirect.github.com/MartinBernstorff/iterpy/issues/148))
  ([`73b4237`](https://redirect.github.com/MartinBernstorff/iterpy/commit/73b423778ebb98045f091f237dd12c6b70afb31d))

- deps:(deps-dev): bump pyright from 1.1.352 to 1.1.353
  ([#&#8203;149](https://redirect.github.com/MartinBernstorff/iterpy/issues/149))
  ([`0614de4`](https://redirect.github.com/MartinBernstorff/iterpy/commit/0614de4a1c14d3c58c8327401dfa0caca7e88691))

- deps:(deps-dev): bump pyright from 1.1.352 to 1.1.353

Bumps [pyright](https://redirect.github.com/RobertCraigie/pyright-python) from 1.1.352 to 1.1.353.

- [Release notes](https://redirect.github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.352...v1.1.353)

([`2ade1d6`](https://redirect.github.com/MartinBernstorff/iterpy/commit/2ade1d6b0c0420182d47cfc860876bca544874de))

- deps:(deps-dev): bump ruff from 0.3.0 to 0.3.2

Bumps [ruff](https://redirect.github.com/astral-sh/ruff) from 0.3.0 to 0.3.2.

- [Release notes](https://redirect.github.com/astral-sh/ruff/releases) -
  [Changelog](https://redirect.github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://redirect.github.com/astral-sh/ruff/compare/v0.3.0...v0.3.2)

([`3de2f20`](https://redirect.github.com/MartinBernstorff/iterpy/commit/3de2f20e86655b60712d21dac27f3006f4562546))

- tests([#&#8203;144](https://redirect.github.com/MartinBernstorff/iterpy/issues/144)): test
  comprehensions ([#&#8203;145](https://redirect.github.com/MartinBernstorff/iterpy/issues/145))

Fixes [#&#8203;144](https://redirect.github.com/MartinBernstorff/iterpy/issues/144)
  ([`440e189`](https://redirect.github.com/MartinBernstorff/iterpy/commit/440e189f2bb094a28c0d9bdfdd59f394deda5c22))

- tests([#&#8203;144](https://redirect.github.com/MartinBernstorff/iterpy/issues/144)): test
  comprehensions

Fixes [#&#8203;144](https://redirect.github.com/MartinBernstorff/iterpy/issues/144)
  ([`2e14944`](https://redirect.github.com/MartinBernstorff/iterpy/commit/2e14944d9ac8ec85db6aedc3100cd2377e78804b))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.12 (2024-11-26)

### Bug Fixes

- **deps**: Update dependency pydantic to v2.10.2
  ([#781](https://github.com/MartinBernstorff/Memium/pull/781),
  [`ee21963`](https://github.com/MartinBernstorff/Memium/commit/ee21963ed57a81d89d4c2880e2dae0b60f284b2b))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pydantic](https://redirect.github.com/pydantic/pydantic)
  ([changelog](https://docs.pydantic.dev/latest/changelog/)) | `==2.10.1` -> `==2.10.2` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pydantic/2.10.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pydantic/2.10.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pydantic/2.10.1/2.10.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pydantic/2.10.1/2.10.2?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pydantic/pydantic (pydantic)</summary>

### [`v2.10.2`](https://redirect.github.com/pydantic/pydantic/blob/HEAD/HISTORY.md#v2102-2024-11-25)

[Compare Source](https://redirect.github.com/pydantic/pydantic/compare/v2.10.1...v2.10.2)

[GitHub release](https://redirect.github.com/pydantic/pydantic/releases/tag/v2.10.2)

##### What's Changed

##### Fixes

- Only evaluate FieldInfo annotations if required during schema building by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10769](https://redirect.github.com/pydantic/pydantic/pull/10769) - Do not evaluate
  annotations for private fields by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10962](https://redirect.github.com/pydantic/pydantic/pull/10962) - Support serialization
  as any for `Secret` types and `Url` types by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10947](https://redirect.github.com/pydantic/pydantic/pull/10947) - Fix type hint of
  `Field.default` to be compatible with Python 3.8 and 3.9 by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10972](https://redirect.github.com/pydantic/pydantic/pull/10972) - Add hashing support
  for URL types by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10975](https://redirect.github.com/pydantic/pydantic/pull/10975) - Hide
  `BaseModel.__replace__` definition from type checkers by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [10979](https://redirect.github.com/pydantic/pydantic/pull/10979)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.11 (2024-11-24)

### Bug Fixes

- **deps**: Update dependency tqdm to v4.67.1
  ([#780](https://github.com/MartinBernstorff/Memium/pull/780),
  [`76b15b1`](https://github.com/MartinBernstorff/Memium/commit/76b15b122707c2dd2d6de7b868eed23182dfa5f9))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [tqdm](https://redirect.github.com/tqdm/tqdm) ([changelog](https://tqdm.github.io/releases)) |
  `==4.67.0` -> `==4.67.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/tqdm/4.67.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/tqdm/4.67.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/tqdm/4.67.0/4.67.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/tqdm/4.67.0/4.67.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>tqdm/tqdm (tqdm)</summary>

### [`v4.67.1`](https://redirect.github.com/tqdm/tqdm/compare/v4.67.0...v4.67.1)

[Compare Source](https://redirect.github.com/tqdm/tqdm/compare/v4.67.0...v4.67.1)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.10 (2024-11-24)

### Bug Fixes

- **deps**: Update dependency syrupy to v4.8.0
  ([#779](https://github.com/MartinBernstorff/Memium/pull/779),
  [`a3ac024`](https://github.com/MartinBernstorff/Memium/commit/a3ac024185d291614b360df4ebb963dd31b52b45))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [syrupy](https://redirect.github.com/syrupy-project/syrupy) | `==4.7.2` -> `==4.8.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/syrupy/4.8.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/syrupy/4.8.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/syrupy/4.7.2/4.8.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/syrupy/4.7.2/4.8.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>syrupy-project/syrupy (syrupy)</summary>

###
  [`v4.8.0`](https://redirect.github.com/syrupy-project/syrupy/blob/HEAD/CHANGELOG.md#480-2024-11-23)

[Compare Source](https://redirect.github.com/syrupy-project/syrupy/compare/v4.7.2...v4.8.0)

##### Features

- add option to disable diffing
  ([#&#8203;924](https://redirect.github.com/syrupy-project/syrupy/issues/924))
  ([d283e87](https://redirect.github.com/syrupy-project/syrupy/commit/d283e87c2b8d1d5623ea3258653d579757bfa78c))

#### [4.7.2](https://redirect.github.com/syrupy-project/syrupy/compare/v4.7.1...v4.7.2) (2024-10-06)

##### Bug Fixes

- allow snapshot dir to be different
  ([#&#8203;892](https://redirect.github.com/syrupy-project/syrupy/issues/892))
  ([548ec06](https://redirect.github.com/syrupy-project/syrupy/commit/548ec0660c2f8f3c80f2b7f0188e8bb2b0c81fc8))

#### [4.7.1](https://redirect.github.com/syrupy-project/syrupy/compare/v4.7.0...v4.7.1) (2024-08-23)

- pytest-rerunfailures compatibility
  ([#&#8203;881](https://redirect.github.com/syrupy-project/syrupy/issues/881))
  ([16911ad](https://redirect.github.com/syrupy-project/syrupy/commit/16911ad0541c642118f3f1ac2d1347362d80c854))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.9 (2024-11-22)

### Bug Fixes

- **deps**: Update dependency pydantic to v2.10.1
  ([#778](https://github.com/MartinBernstorff/Memium/pull/778),
  [`5a5606b`](https://github.com/MartinBernstorff/Memium/commit/5a5606bdaee9c87e2667b0d6d2c6fd553c3404ce))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pydantic](https://redirect.github.com/pydantic/pydantic)
  ([changelog](https://docs.pydantic.dev/latest/changelog/)) | `==2.10.0` -> `==2.10.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pydantic/2.10.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pydantic/2.10.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pydantic/2.10.0/2.10.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pydantic/2.10.0/2.10.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pydantic/pydantic (pydantic)</summary>

### [`v2.10.1`](https://redirect.github.com/pydantic/pydantic/blob/HEAD/HISTORY.md#v2101-2024-11-21)

[Compare Source](https://redirect.github.com/pydantic/pydantic/compare/v2.10.0...v2.10.1)

[GitHub release](https://redirect.github.com/pydantic/pydantic/releases/tag/v2.10.1)

##### What's Changed

##### Packaging

- Bump `pydantic-core` version to `v2.27.1` by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10938](https://redirect.github.com/pydantic/pydantic/pull/10938)

##### Fixes

- Use the correct frame when instantiating a parametrized `TypeAdapter` by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10893](https://redirect.github.com/pydantic/pydantic/pull/10893) - Relax check for
  validated data in `default_factory` utils by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10909](https://redirect.github.com/pydantic/pydantic/pull/10909) - Fix type checking
  issue with `model_fields` and `model_computed_fields` by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10911](https://redirect.github.com/pydantic/pydantic/pull/10911) - Use the parent
  configuration during schema generation for stdlib `dataclass`es by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10928](https://redirect.github.com/pydantic/pydantic/pull/10928) - Use the `globals` of
  the function when evaluating the return type of serializers and `computed_field`s by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10929](https://redirect.github.com/pydantic/pydantic/pull/10929) - Fix URL constraint
  application by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10922](https://redirect.github.com/pydantic/pydantic/pull/10922) - Fix URL equality with
  different validation methods by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle)
  in [#&#8203;10934](https://redirect.github.com/pydantic/pydantic/pull/10934) - Fix JSON schema
  title when specified as `''` by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle)
  in [#&#8203;10936](https://redirect.github.com/pydantic/pydantic/pull/10936) - Fix `python` mode
  serialization for `complex` inference by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [pydantic-core#1549](https://redirect.github.com/pydantic/pydantic-core/pull/1549)

##### New Contributors

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.8 (2024-11-21)

### Bug Fixes

- **deps**: Update dependency sentry-sdk to v2.19.0
  ([#777](https://github.com/MartinBernstorff/Memium/pull/777),
  [`e5849dd`](https://github.com/MartinBernstorff/Memium/commit/e5849ddb81232caca8ec59395d2c5073ac5f3b58))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [sentry-sdk](https://redirect.github.com/getsentry/sentry-python)
  ([changelog](https://redirect.github.com/getsentry/sentry-python/blob/master/CHANGELOG.md)) |
  `==2.18.0` -> `==2.19.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/sentry-sdk/2.19.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/sentry-sdk/2.19.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/sentry-sdk/2.18.0/2.19.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/sentry-sdk/2.18.0/2.19.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>getsentry/sentry-python (sentry-sdk)</summary>

### [`v2.19.0`](https://redirect.github.com/getsentry/sentry-python/blob/HEAD/CHANGELOG.md#2190)

[Compare Source](https://redirect.github.com/getsentry/sentry-python/compare/2.18.0...2.19.0)

##### Various fixes & improvements

- New: introduce `rust_tracing` integration. See
  https://docs.sentry.io/platforms/python/integrations/rust_tracing/
  ([#&#8203;3717](https://redirect.github.com/getsentry/sentry-python/issues/3717)) by
  [@&#8203;matt-codecov](https://redirect.github.com/matt-codecov) - Auto enable Litestar
  integration ([#&#8203;3540](https://redirect.github.com/getsentry/sentry-python/issues/3540)) by
  [@&#8203;provinzkraut](https://redirect.github.com/provinzkraut) - Deprecate `sentry_sdk.init`
  context manager ([#&#8203;3729](https://redirect.github.com/getsentry/sentry-python/issues/3729))
  by [@&#8203;szokeasaurusrex](https://redirect.github.com/szokeasaurusrex) - feat(spotlight): Send
  PII to Spotlight when no DSN is set
  ([#&#8203;3804](https://redirect.github.com/getsentry/sentry-python/issues/3804)) by
  [@&#8203;BYK](https://redirect.github.com/BYK) - feat(spotlight): Add info logs when Sentry is
  enabled ([#&#8203;3735](https://redirect.github.com/getsentry/sentry-python/issues/3735)) by
  [@&#8203;BYK](https://redirect.github.com/BYK) - feat(spotlight): Inject Spotlight button on
  Django ([#&#8203;3751](https://redirect.github.com/getsentry/sentry-python/issues/3751)) by
  [@&#8203;BYK](https://redirect.github.com/BYK) - feat(spotlight): Auto enable cache_spans for
  Spotlight on DEBUG
  ([#&#8203;3791](https://redirect.github.com/getsentry/sentry-python/issues/3791)) by
  [@&#8203;BYK](https://redirect.github.com/BYK) - fix(logging): Handle parameter `stack_info` for
  the `LoggingIntegration`
  ([#&#8203;3745](https://redirect.github.com/getsentry/sentry-python/issues/3745)) by
  [@&#8203;gmcrocetti](https://redirect.github.com/gmcrocetti) - fix(pure-eval): Make
  sentry-sdk\[pure-eval] installable with pip==24.0
  ([#&#8203;3757](https://redirect.github.com/getsentry/sentry-python/issues/3757)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - fix(rust_tracing):
  include_tracing_fields arg to control unvetted data in rust_tracing integration
  ([#&#8203;3780](https://redirect.github.com/getsentry/sentry-python/issues/3780)) by
  [@&#8203;matt-codecov](https://redirect.github.com/matt-codecov) - fix(aws) Fix aws lambda tests
  (by reducing event size)
  ([#&#8203;3770](https://redirect.github.com/getsentry/sentry-python/issues/3770)) by
  [@&#8203;antonpirker](https://redirect.github.com/antonpirker) - fix(arq): fix integration with
  Worker settings as a dict
  ([#&#8203;3742](https://redirect.github.com/getsentry/sentry-python/issues/3742)) by
  [@&#8203;saber-solooki](https://redirect.github.com/saber-solooki) - fix(httpx): Prevent Sentry
  baggage duplication
  ([#&#8203;3728](https://redirect.github.com/getsentry/sentry-python/issues/3728)) by
  [@&#8203;szokeasaurusrex](https://redirect.github.com/szokeasaurusrex) - fix(falcon): Don't
  exhaust request body stream
  ([#&#8203;3768](https://redirect.github.com/getsentry/sentry-python/issues/3768)) by
  [@&#8203;szokeasaurusrex](https://redirect.github.com/szokeasaurusrex) - fix(integrations): Check
  `retries_left` before capturing exception
  ([#&#8203;3803](https://redirect.github.com/getsentry/sentry-python/issues/3803)) by
  [@&#8203;malkovro](https://redirect.github.com/malkovro) - fix(openai): Use name instead of
  description ([#&#8203;3807](https://redirect.github.com/getsentry/sentry-python/issues/3807)) by
  [@&#8203;sourceful-rob](https://redirect.github.com/sourceful-rob) - test(gcp): Only run GCP tests
  when they should ([#&#8203;3721](https://redirect.github.com/getsentry/sentry-python/issues/3721))
  by [@&#8203;szokeasaurusrex](https://redirect.github.com/szokeasaurusrex) - chore: Shorten CI
  workflow names ([#&#8203;3805](https://redirect.github.com/getsentry/sentry-python/issues/3805))
  by [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - chore: Test with pyspark
  prerelease ([#&#8203;3760](https://redirect.github.com/getsentry/sentry-python/issues/3760)) by
  [@&#8203;sentrivana](https://redirect.github.com/sentrivana) - build(deps): bump
  codecov/codecov-action from 4.6.0 to 5.0.2
  ([#&#8203;3792](https://redirect.github.com/getsentry/sentry-python/issues/3792)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot) - build(deps): bump actions/checkout
  from 4.2.1 to 4.2.2
  ([#&#8203;3691](https://redirect.github.com/getsentry/sentry-python/issues/3691)) by
  [@&#8203;dependabot](https://redirect.github.com/dependabot)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.7 (2024-11-20)

### Bug Fixes

- **deps**: Update dependency pydantic to v2.10.0
  ([#776](https://github.com/MartinBernstorff/Memium/pull/776),
  [`4dcce97`](https://github.com/MartinBernstorff/Memium/commit/4dcce9792d82df32a763aa2068f3cce21910d665))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pydantic](https://redirect.github.com/pydantic/pydantic)
  ([changelog](https://docs.pydantic.dev/latest/changelog/)) | `==2.9.2` -> `==2.10.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pydantic/2.10.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pydantic/2.10.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pydantic/2.9.2/2.10.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pydantic/2.9.2/2.10.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pydantic/pydantic (pydantic)</summary>

### [`v2.10.0`](https://redirect.github.com/pydantic/pydantic/blob/HEAD/HISTORY.md#v2100-2024-11-20)

[Compare Source](https://redirect.github.com/pydantic/pydantic/compare/v2.9.2...v2.10.0)

The code released in v2.10.0 is practically identical to that of v2.10.0b2.

[GitHub release](https://redirect.github.com/pydantic/pydantic/releases/tag/v2.10.0)

See the [v2.10 release blog post](https://pydantic.dev/articles/pydantic-v2-10-release) for the
  highlights!

##### What's Changed

##### Packaging

- Bump `pydantic-core` to `v2.27.0` by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10825](https://redirect.github.com/pydantic/pydantic/pull/10825) - Replaced pdm with uv
  by [@&#8203;frfahim](https://redirect.github.com/frfahim) in
  [#&#8203;10727](https://redirect.github.com/pydantic/pydantic/pull/10727)

##### New Features

- Support `fractions.Fraction` by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle)
  in [#&#8203;10318](https://redirect.github.com/pydantic/pydantic/pull/10318) - Support `Hashable`
  for json validation by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10324](https://redirect.github.com/pydantic/pydantic/pull/10324) - Add a `SocketPath`
  type for `linux` systems by [@&#8203;theunkn0wn1](https://redirect.github.com/theunkn0wn1) in
  [#&#8203;10378](https://redirect.github.com/pydantic/pydantic/pull/10378) - Allow arbitrary refs
  in JSON schema `examples` by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10417](https://redirect.github.com/pydantic/pydantic/pull/10417) - Support `defer_build`
  for Pydantic dataclasses by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10313](https://redirect.github.com/pydantic/pydantic/pull/10313) - Adding v1 / v2
  incompatibility warning for nested v1 model by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10431](https://redirect.github.com/pydantic/pydantic/pull/10431) - Add support for
  unpacked `TypedDict` to type hint variadic keyword arguments with `@validate_call` by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10416](https://redirect.github.com/pydantic/pydantic/pull/10416) - Support compiled
  patterns in `protected_namespaces` by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10522](https://redirect.github.com/pydantic/pydantic/pull/10522) - Add support for
  `propertyNames` in JSON schema by [@&#8203;FlorianSW](https://redirect.github.com/FlorianSW) in
  [#&#8203;10478](https://redirect.github.com/pydantic/pydantic/pull/10478) - Adding `__replace__`
  protocol for Python 3.13+ support by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10596](https://redirect.github.com/pydantic/pydantic/pull/10596) - Expose public `sort`
  method for JSON schema generation by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10595](https://redirect.github.com/pydantic/pydantic/pull/10595) - Add runtime validation
  of `@validate_call` callable argument by [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10627](https://redirect.github.com/pydantic/pydantic/pull/10627) - Add
  `experimental_allow_partial` support by
  [@&#8203;samuelcolvin](https://redirect.github.com/samuelcolvin) in
  [#&#8203;10748](https://redirect.github.com/pydantic/pydantic/pull/10748) - Support default
  factories taking validated data as an argument by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10678](https://redirect.github.com/pydantic/pydantic/pull/10678) - Allow subclassing
  `ValidationError` and `PydanticCustomError` by
  [@&#8203;Youssefares](https://redirect.github.com/Youssefares) in
  [pydantic/pydantic-core#1413](https://redirect.github.com/pydantic/pydantic-core/pull/1413) - Add
  `trailing-strings` support to `experimental_allow_partial` by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10825](https://redirect.github.com/pydantic/pydantic/pull/10825) - Add `rebuild()` method
  for `TypeAdapter` and simplify `defer_build` patterns by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10537](https://redirect.github.com/pydantic/pydantic/pull/10537) - Improve `TypeAdapter`
  instance repr by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10872](https://redirect.github.com/pydantic/pydantic/pull/10872)

##### Changes

- Don't allow customization of `SchemaGenerator` until interface is more stable by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10303](https://redirect.github.com/pydantic/pydantic/pull/10303) - Cleanly `defer_build`
  on `TypeAdapters`, removing experimental flag by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10329](https://redirect.github.com/pydantic/pydantic/pull/10329) - Fix `mro` of generic
  subclass by [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10100](https://redirect.github.com/pydantic/pydantic/pull/10100) - Strip whitespaces on
  JSON Schema title generation by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle)
  in [#&#8203;10404](https://redirect.github.com/pydantic/pydantic/pull/10404) - Use `b64decode` and
  `b64encode` for `Base64Bytes` type by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10486](https://redirect.github.com/pydantic/pydantic/pull/10486) - Relax protected
  namespace config default by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10441](https://redirect.github.com/pydantic/pydantic/pull/10441) - Revalidate
  parametrized generics if instance's origin is subclass of OG class by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10666](https://redirect.github.com/pydantic/pydantic/pull/10666) - Warn if configuration
  is specified on the `@dataclass` decorator and with the `__pydantic_config__` attribute by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10406](https://redirect.github.com/pydantic/pydantic/pull/10406) - Recommend against
  using `Ellipsis` (...) with `Field` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10661](https://redirect.github.com/pydantic/pydantic/pull/10661) - Migrate to subclassing
  instead of annotated approach for pydantic url types by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10662](https://redirect.github.com/pydantic/pydantic/pull/10662) - Change JSON schema
  generation of `Literal`s and `Enums` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10692](https://redirect.github.com/pydantic/pydantic/pull/10692) - Simplify unions
  involving `Any` or `Never` when replacing type variables by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10338](https://redirect.github.com/pydantic/pydantic/pull/10338) - Do not require padding
  when decoding `base64` bytes by
  [@&#8203;bschoenmaeckers](https://redirect.github.com/bschoenmaeckers) in
  [pydantic/pydantic-core#1448](https://redirect.github.com/pydantic/pydantic-core/pull/1448) -
  Support dates all the way to 1BC by [@&#8203;changhc](https://redirect.github.com/changhc) in
  [pydantic/speedate#77](https://redirect.github.com/pydantic/speedate/pull/77)

##### Performance

- Schema cleaning: skip unnecessary copies during schema walking by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10286](https://redirect.github.com/pydantic/pydantic/pull/10286) - Refactor namespace
  logic for annotations evaluation by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10530](https://redirect.github.com/pydantic/pydantic/pull/10530) - Improve email regexp
  on edge cases by [@&#8203;AlekseyLobanov](https://redirect.github.com/AlekseyLobanov) in
  [#&#8203;10601](https://redirect.github.com/pydantic/pydantic/pull/10601) - `CoreMetadata`
  refactor with an emphasis on documentation, schema build time performance, and reducing complexity
  by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10675](https://redirect.github.com/pydantic/pydantic/pull/10675)

##### Fixes

- Remove guarding check on `computed_field` with `field_serializer` by
  [@&#8203;nix010](https://redirect.github.com/nix010) in
  [#&#8203;10390](https://redirect.github.com/pydantic/pydantic/pull/10390) - Fix `Predicate` issue
  in `v2.9.0` by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10321](https://redirect.github.com/pydantic/pydantic/pull/10321) - Fixing
  `annotated-types` bound by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10327](https://redirect.github.com/pydantic/pydantic/pull/10327) - Turn `tzdata` install
  requirement into optional `timezone` dependency by
  [@&#8203;jakob-keller](https://redirect.github.com/jakob-keller) in
  [#&#8203;10331](https://redirect.github.com/pydantic/pydantic/pull/10331) - Use correct types
  namespace when building `namedtuple` core schemas by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10337](https://redirect.github.com/pydantic/pydantic/pull/10337) - Fix evaluation of
  stringified annotations during namespace inspection by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10347](https://redirect.github.com/pydantic/pydantic/pull/10347) - Fix `IncEx` type alias
  definition by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10339](https://redirect.github.com/pydantic/pydantic/pull/10339) - Do not error when
  trying to evaluate annotations of private attributes by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10358](https://redirect.github.com/pydantic/pydantic/pull/10358) - Fix nested type
  statement by [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10369](https://redirect.github.com/pydantic/pydantic/pull/10369) - Improve typing of
  `ModelMetaclass.mro` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10372](https://redirect.github.com/pydantic/pydantic/pull/10372) - Fix class access of
  deprecated `computed_field`s by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10391](https://redirect.github.com/pydantic/pydantic/pull/10391) - Make sure
  `inspect.iscoroutinefunction` works on coroutines decorated with `@validate_call` by
  [@&#8203;MovisLi](https://redirect.github.com/MovisLi) in
  [#&#8203;10374](https://redirect.github.com/pydantic/pydantic/pull/10374) - Fix `NameError` when
  using `validate_call` with PEP 695 on a class by
  [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10380](https://redirect.github.com/pydantic/pydantic/pull/10380) - Fix `ZoneInfo` with
  various invalid types by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10408](https://redirect.github.com/pydantic/pydantic/pull/10408) - Fix
  `PydanticUserError` on empty `model_config` with annotations by
  [@&#8203;cdwilson](https://redirect.github.com/cdwilson) in
  [#&#8203;10412](https://redirect.github.com/pydantic/pydantic/pull/10412) - Fix variance issue in
  `_IncEx` type alias, only allow `True` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10414](https://redirect.github.com/pydantic/pydantic/pull/10414) - Fix serialization
  schema generation when using `PlainValidator` by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10427](https://redirect.github.com/pydantic/pydantic/pull/10427) - Fix schema generation
  error when serialization schema holds references by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10444](https://redirect.github.com/pydantic/pydantic/pull/10444) - Inline references if
  possible when generating schema for `json_schema_input_type` by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10439](https://redirect.github.com/pydantic/pydantic/pull/10439) - Fix recursive
  arguments in `Representation` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10480](https://redirect.github.com/pydantic/pydantic/pull/10480) - Fix representation for
  builtin function types by [@&#8203;kschwab](https://redirect.github.com/kschwab) in
  [#&#8203;10479](https://redirect.github.com/pydantic/pydantic/pull/10479) - Add python validators
  for decimal constraints (`max_digits` and `decimal_places`) by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10506](https://redirect.github.com/pydantic/pydantic/pull/10506) - Only fetch
  `__pydantic_core_schema__` from the current class during schema generation by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10518](https://redirect.github.com/pydantic/pydantic/pull/10518) - Fix `stacklevel` on
  deprecation warnings for `BaseModel` by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10520](https://redirect.github.com/pydantic/pydantic/pull/10520) - Fix warning
  `stacklevel` in `BaseModel.__init__` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10526](https://redirect.github.com/pydantic/pydantic/pull/10526) - Improve error handling
  for in-evaluable refs for discriminator application by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10440](https://redirect.github.com/pydantic/pydantic/pull/10440) - Change the signature
  of `ConfigWrapper.core_config` to take the title directly by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10562](https://redirect.github.com/pydantic/pydantic/pull/10562) - Do not use the
  previous config from the stack for dataclasses without config by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10576](https://redirect.github.com/pydantic/pydantic/pull/10576) - Fix serialization for
  IP types with `mode='python'` by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10594](https://redirect.github.com/pydantic/pydantic/pull/10594) - Support constraint
  application for `Base64Etc` types by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10584](https://redirect.github.com/pydantic/pydantic/pull/10584) - Fix `validate_call`
  ignoring `Field` in `Annotated` by [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10610](https://redirect.github.com/pydantic/pydantic/pull/10610) - Raise an error when
  `Self` is invalid by [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10609](https://redirect.github.com/pydantic/pydantic/pull/10609) - Using
  `core_schema.InvalidSchema` instead of metadata injection + checks by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10523](https://redirect.github.com/pydantic/pydantic/pull/10523) - Tweak type alias logic
  by [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10643](https://redirect.github.com/pydantic/pydantic/pull/10643) - Support usage of
  `type` with `typing.Self` and type aliases by [@&#8203;kc0506](https://redirect.github.com/kc0506)
  in [#&#8203;10621](https://redirect.github.com/pydantic/pydantic/pull/10621) - Use overloads for
  `Field` and `PrivateAttr` functions by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10651](https://redirect.github.com/pydantic/pydantic/pull/10651) - Clean up the `mypy`
  plugin implementation by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10669](https://redirect.github.com/pydantic/pydantic/pull/10669) - Properly check for
  `typing_extensions` variant of `TypeAliasType` by
  [@&#8203;Daraan](https://redirect.github.com/Daraan) in
  [#&#8203;10713](https://redirect.github.com/pydantic/pydantic/pull/10713) - Allow any mapping in
  `BaseModel.model_copy()` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10751](https://redirect.github.com/pydantic/pydantic/pull/10751) - Fix `isinstance`
  behavior for urls by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10766](https://redirect.github.com/pydantic/pydantic/pull/10766) - Ensure
  `cached_property` can be set on Pydantic models by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10774](https://redirect.github.com/pydantic/pydantic/pull/10774) - Fix equality checks
  for primitives in literals by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle)
  in [pydantic/pydantic-core#1459](https://redirect.github.com/pydantic/pydantic-core/pull/1459) -
  Properly enforce `host_required` for URLs by [@&#8203;Viicos](https://redirect.github.com/Viicos)
  in [pydantic/pydantic-core#1488](https://redirect.github.com/pydantic/pydantic-core/pull/1488) -
  Fix when `coerce_numbers_to_str` enabled and string has invalid Unicode character by
  [@&#8203;andrey-berenda](https://redirect.github.com/andrey-berenda) in
  [pydantic/pydantic-core#1515](https://redirect.github.com/pydantic/pydantic-core/pull/1515) - Fix
  serializing `complex` values in `Enum`s by [@&#8203;changhc](https://redirect.github.com/changhc)
  in [pydantic/pydantic-core#1524](https://redirect.github.com/pydantic/pydantic-core/pull/1524) -
  Refactor `_typing_extra` module by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10725](https://redirect.github.com/pydantic/pydantic/pull/10725) - Support intuitive
  equality for urls by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10798](https://redirect.github.com/pydantic/pydantic/pull/10798) - Add `bytearray` to
  `TypeAdapter.validate_json` signature by
  [@&#8203;samuelcolvin](https://redirect.github.com/samuelcolvin) in
  [#&#8203;10802](https://redirect.github.com/pydantic/pydantic/pull/10802) - Ensure class access of
  method descriptors is performed when used as a default with `Field` by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10816](https://redirect.github.com/pydantic/pydantic/pull/10816) - Fix circular import
  with `validate_call` by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10807](https://redirect.github.com/pydantic/pydantic/pull/10807) - Fix error when using
  type aliases referencing other type aliases by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10809](https://redirect.github.com/pydantic/pydantic/pull/10809) - Fix `IncEx` type alias
  to be compatible with mypy by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10813](https://redirect.github.com/pydantic/pydantic/pull/10813) - Make `__signature__` a
  lazy property, do not deepcopy defaults by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10818](https://redirect.github.com/pydantic/pydantic/pull/10818) - Make `__signature__`
  lazy for dataclasses, too by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10832](https://redirect.github.com/pydantic/pydantic/pull/10832) - Subclass all single
  host url classes from `AnyUrl` to preserve behavior from v2.9 by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10856](https://redirect.github.com/pydantic/pydantic/pull/10856)

##### New Contributors

- [@&#8203;jakob-keller](https://redirect.github.com/jakob-keller) made their first contribution in
  [#&#8203;10331](https://redirect.github.com/pydantic/pydantic/pull/10331) -
  [@&#8203;MovisLi](https://redirect.github.com/MovisLi) made their first contribution in
  [#&#8203;10374](https://redirect.github.com/pydantic/pydantic/pull/10374) -
  [@&#8203;joaopalmeiro](https://redirect.github.com/joaopalmeiro) made their first contribution in
  [#&#8203;10405](https://redirect.github.com/pydantic/pydantic/pull/10405) -
  [@&#8203;theunkn0wn1](https://redirect.github.com/theunkn0wn1) made their first contribution in
  [#&#8203;10378](https://redirect.github.com/pydantic/pydantic/pull/10378) -
  [@&#8203;cdwilson](https://redirect.github.com/cdwilson) made their first contribution in
  [#&#8203;10412](https://redirect.github.com/pydantic/pydantic/pull/10412) -
  [@&#8203;dlax](https://redirect.github.com/dlax) made their first contribution in
  [#&#8203;10421](https://redirect.github.com/pydantic/pydantic/pull/10421) -
  [@&#8203;kschwab](https://redirect.github.com/kschwab) made their first contribution in
  [#&#8203;10479](https://redirect.github.com/pydantic/pydantic/pull/10479) -
  [@&#8203;santibreo](https://redirect.github.com/santibreo) made their first contribution in
  [#&#8203;10453](https://redirect.github.com/pydantic/pydantic/pull/10453) -
  [@&#8203;FlorianSW](https://redirect.github.com/FlorianSW) made their first contribution in
  [#&#8203;10478](https://redirect.github.com/pydantic/pydantic/pull/10478) -
  [@&#8203;tkasuz](https://redirect.github.com/tkasuz) made their first contribution in
  [#&#8203;10555](https://redirect.github.com/pydantic/pydantic/pull/10555) -
  [@&#8203;AlekseyLobanov](https://redirect.github.com/AlekseyLobanov) made their first contribution
  in [#&#8203;10601](https://redirect.github.com/pydantic/pydantic/pull/10601) -
  [@&#8203;NiclasvanEyk](https://redirect.github.com/NiclasvanEyk) made their first contribution in
  [#&#8203;10667](https://redirect.github.com/pydantic/pydantic/pull/10667) -
  [@&#8203;mschoettle](https://redirect.github.com/mschoettle) made their first contribution in
  [#&#8203;10677](https://redirect.github.com/pydantic/pydantic/pull/10677) -
  [@&#8203;Daraan](https://redirect.github.com/Daraan) made their first contribution in
  [#&#8203;10713](https://redirect.github.com/pydantic/pydantic/pull/10713) -
  [@&#8203;k4nar](https://redirect.github.com/k4nar) made their first contribution in
  [#&#8203;10736](https://redirect.github.com/pydantic/pydantic/pull/10736) -
  [@&#8203;UriyaHarpeness](https://redirect.github.com/UriyaHarpeness) made their first contribution
  in [#&#8203;10740](https://redirect.github.com/pydantic/pydantic/pull/10740) -
  [@&#8203;frfahim](https://redirect.github.com/frfahim) made their first contribution in
  [#&#8203;10727](https://redirect.github.com/pydantic/pydantic/pull/10727)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency typer to v0.13.1
  ([#775](https://github.com/MartinBernstorff/Memium/pull/775),
  [`2f355ad`](https://github.com/MartinBernstorff/Memium/commit/2f355ad1b7622a5079959e81fd3af8cdc38ccfe7))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [typer](https://redirect.github.com/fastapi/typer)
  ([changelog](https://typer.tiangolo.com/release-notes/)) | `==0.13.0` -> `==0.13.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/typer/0.13.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/typer/0.13.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/typer/0.13.0/0.13.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/typer/0.13.0/0.13.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>fastapi/typer (typer)</summary>

### [`v0.13.1`](https://redirect.github.com/fastapi/typer/releases/tag/0.13.1)

[Compare Source](https://redirect.github.com/fastapi/typer/compare/0.13.0...0.13.1)

##### Features

- ✨ Remove Rich tags when showing completion text. PR
  [#&#8203;877](https://redirect.github.com/fastapi/typer/pull/877) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - ✨ Render Rich markup as HTML in
  Markdown docs. PR [#&#8203;847](https://redirect.github.com/fastapi/typer/pull/847) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - ✨ Support cp850 encoding for
  auto-completion in PowerShell. PR
  [#&#8203;808](https://redirect.github.com/fastapi/typer/pull/808) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - ✨ Allow gettext translation of help
  message. PR [#&#8203;886](https://redirect.github.com/fastapi/typer/pull/886) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg).

##### Refactors

- 🐛 Fix printing HTML from Rich output. PR
  [#&#8203;1055](https://redirect.github.com/fastapi/typer/pull/1055) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo).

##### Docs

- 📝 Update markdown includes to use the new simpler format. PR
  [#&#8203;1054](https://redirect.github.com/fastapi/typer/pull/1054) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo).

##### Internal

- ⬆ Bump ruff from 0.7.3 to 0.7.4. PR
  [#&#8203;1051](https://redirect.github.com/fastapi/typer/pull/1051) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1047](https://redirect.github.com/fastapi/typer/pull/1047) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.7.2 to 0.7.3. PR [#&#8203;1046](https://redirect.github.com/fastapi/typer/pull/1046) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  tiangolo/latest-changes from 0.3.1 to 0.3.2. PR
  [#&#8203;1044](https://redirect.github.com/fastapi/typer/pull/1044) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Update pytest-cov
  requirement from <6.0.0,>=2.10.0 to >=2.10.0,<7.0.0. PR
  [#&#8203;1033](https://redirect.github.com/fastapi/typer/pull/1033) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot).

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.6 (2024-11-13)

### Bug Fixes

- **deps**: Update dependency pyright to v1.1.389
  ([#774](https://github.com/MartinBernstorff/Memium/pull/774),
  [`42e7e14`](https://github.com/MartinBernstorff/Memium/commit/42e7e14cfcf2ca454ccae03a61ac6173066b726a))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pyright](https://redirect.github.com/RobertCraigie/pyright-python) | `==1.1.388` -> `==1.1.389` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pyright/1.1.389?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pyright/1.1.389?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pyright/1.1.388/1.1.389?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pyright/1.1.388/1.1.389?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>RobertCraigie/pyright-python (pyright)</summary>

###
  [`v1.1.389`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.388...v1.1.389)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.388...v1.1.389)

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xMS41IiwidXBkYXRlZEluVmVyIjoiMzkuMTEuNSIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Chores

- **deps**: Update python-semantic-release/python-semantic-release action to v9.13.0
  ([#772](https://github.com/MartinBernstorff/Memium/pull/772),
  [`947dead`](https://github.com/MartinBernstorff/Memium/commit/947dead0a0dcf7cdef5d5caedab73a3adfd42881))

This PR contains the following updates:

| Package | Type | Update | Change | |---|---|---|---| |
  [python-semantic-release/python-semantic-release](https://redirect.github.com/python-semantic-release/python-semantic-release)
  | action | minor | `v9.12.2` -> `v9.13.0` |

---

### Release Notes

<details> <summary>python-semantic-release/python-semantic-release
  (python-semantic-release/python-semantic-release)</summary>

###
  [`v9.13.0`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.md#v9130-2024-11-10)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.12.2...v9.13.0)

##### Bug Fixes

- Ignore unknown parsed commit types in default RST changelog

([`77609b1`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/77609b1917a00b106ce254e6f6d5edcd1feebba7))

- Drop the `breaking` category but still maintain a major level bump

([`f1ffa54`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/f1ffa5411892de34cdc842fd55c460a24b6685c6))

- Improve reliability of text unwordwrap of descriptions

([`436374b`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/436374b04128d1550467ae97ba90253f1d1b3878))

##### Documentation

- Fix api class reference links

([`7a5bdf2`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/7a5bdf29b3df0f9a1346ea5301d2a7fee953667b))

- Add `linked_merge_request` field to examples

([`d4376bc`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/d4376bc2ae4d3708d501d91211ec3ee3a923e9b5))

- Add `linked_merge_request` field to Parsed Commit definition

([`ca61889`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/ca61889d4ac73e9864fbf637fb87ab2d5bc053ea))

##### Features

- Add PR/MR url linking to default reStructuredText template

([`5f018d6`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/5f018d630b4c625bdf6d329b27fd966eba75b017))

Resolves:
  [#&#8203;924](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/924),
  [#&#8203;953](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/953)

- Add PR/MR url linking to default Markdown changelog

([`cd8d131`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/cd8d1310a4000cc79b529fbbdc58933f4c6373c6))

- Automatically parse PR/MR numbers from subject lines in commits

([`2b3f738`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/2b3f73801f5760bac29acd93db3ffb2bc790cda0))

([`bca9909`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/bca9909c1b61fdb1f9ccf823fceb6951cd059820))

([`2ac798f`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/2ac798f92e0c13c1db668747f7e35a65b99ae7ce))

- Add linked merge requests list to the `ParsedCommit` object

([`9a91062`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/9a9106212d6c240e9d3358e139b4c4694eaf9c4b))

##### Performance Improvements

- Increase speed & decrease complexity of commit parsing

([`2b661ed`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/2b661ed122a6f0357a6b92233ac1351c54c7794e))

- Increase speed of commit parsing

([`2c9c468`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/2c9c4685a66feb35cd78571cf05f76344dd6d66a))

- Simplify commit parsing type pre-calculation

([`a86a28c`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/a86a28c5e26ed766cda71d26b9382c392e377c61))

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS43LjEiLCJ1cGRhdGVkSW5WZXIiOiIzOS43LjEiLCJ0YXJnZXRCcmFuY2giOiJtYWluIiwibGFiZWxzIjpbXX0=-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update python-semantic-release/python-semantic-release action to v9.14.0
  ([#773](https://github.com/MartinBernstorff/Memium/pull/773),
  [`1cd4ba2`](https://github.com/MartinBernstorff/Memium/commit/1cd4ba23acc1c16cf872d8cf00364c3caeb59d00))

This PR contains the following updates:

| Package | Type | Update | Change | |---|---|---|---| |
  [python-semantic-release/python-semantic-release](https://redirect.github.com/python-semantic-release/python-semantic-release)
  | action | minor | `v9.13.0` -> `v9.14.0` |

---

### Release Notes

<details> <summary>python-semantic-release/python-semantic-release
  (python-semantic-release/python-semantic-release)</summary>

###
  [`v9.14.0`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.md#v9140-2024-11-11)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.13.0...v9.14.0)

##### Bug Fixes

- **release-notes**: Override default wordwrap to non-wrap for in default template

([`99ab99b`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/99ab99bb0ba350ca1913a2bde9696f4242278972))

##### Documentation

- **changelog-templates**: Document new `mask_initial_release` changelog context variable

([`f294957`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/f2949577dfb2dbf9c2ac952c1bbcc4ab84da080b))

- **configuration**: Document new `mask_initial_release` option usage & effect

([`3cabcdc`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/3cabcdcd9473e008604e74cc2d304595317e921d))

- **homepage**: Fix reference to new ci workflow for test status badge

([`6760069`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/6760069e7489f50635beb5aedbbeb2cb82b7c584))

##### Features

- **context**: Add `mask_initial_release` setting to changelog context

([`6f2ee39`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/6f2ee39414b3cf75c0b67dee4db0146bbc1041bb))

- **configuration**: Add `changelog.default_templates.mask_initial_release` option

([`595a70b`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/595a70bcbc8fea1f8ccf6c5069c41c35ec4efb8d))

- **release-notes**: Define first release w/o change descriptions in default template

([`83167a3`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/83167a3dcceb7db16b790e1b0efd5fc75fee8942))

- **changelog**: Define first release w/o change descriptions for default RST template

([`e30c94b`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/e30c94bffe62b42e8dc6ed4fed6260e57b4d532b))

- **changelog**: Define first release w/o change descriptions for default MD template

([`fa89dec`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/fa89dec239efbae7544b187f624a998fa9ecc309))

- **changelog**: Add md to rst conversion for markdown inline links

([`cb2af1f`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/cb2af1f17cf6c8ae037c6cd8bb8b4d9c019bb47e))

- **changelog-md**: Add markdown inline link format macro

([`c6d8211`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/c6d8211c859442df17cb41d2ff19fdb7a81cdb76))

- **changelogs**: Prefix scopes on commit descriptions in default template

([#&#8203;1093](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1093),

[`560fd2c`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/560fd2c0d58c97318377cb83af899a336d24cfcc))

<!---->

- test(changelog): update default changelog unit tests to handle commit scope

- test(release-notes): update default release notes unit tests to handle commit scope

- test(fixtures): update changelog generator fixture to handle scope additions

- test(cmd-version): update implementation for test resiliency

- feat(changelog-md): prefix scopes on commit descriptions in Markdown changelog template

- feat(changelog-rst): prefix scopes on commit descriptions in ReStructuredText template

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS43LjEiLCJ1cGRhdGVkSW5WZXIiOiIzOS43LjEiLCJ0YXJnZXRCcmFuY2giOiJtYWluIiwibGFiZWxzIjpbXX0=-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.5 (2024-11-07)

### Bug Fixes

- **deps**: Update dependency typer to v0.13.0
  ([#771](https://github.com/MartinBernstorff/Memium/pull/771),
  [`0ffe1cf`](https://github.com/MartinBernstorff/Memium/commit/0ffe1cfe4f5569d06e49fee9bffb79e9eebc2e08))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [typer](https://redirect.github.com/fastapi/typer)
  ([changelog](https://typer.tiangolo.com/release-notes/)) | `==0.12.5` -> `==0.13.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/typer/0.13.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/typer/0.13.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/typer/0.12.5/0.13.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/typer/0.12.5/0.13.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>fastapi/typer (typer)</summary>

### [`v0.13.0`](https://redirect.github.com/fastapi/typer/releases/tag/0.13.0)

[Compare Source](https://redirect.github.com/fastapi/typer/compare/0.12.5...0.13.0)

##### Features

- ✨ Handle `KeyboardInterrupt` separately from other exceptions. PR
  [#&#8203;1039](https://redirect.github.com/fastapi/typer/pull/1039) by
  [@&#8203;patrick91](https://redirect.github.com/patrick91). - ✨ Update `launch` to not print
  anything when opening urls. PR [#&#8203;1035](https://redirect.github.com/fastapi/typer/pull/1035)
  by [@&#8203;patrick91](https://redirect.github.com/patrick91). - ✨ Show help items in order of
  definition. PR [#&#8203;944](https://redirect.github.com/fastapi/typer/pull/944) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg).

##### Fixes

- 🐛 Fix equality check for custom classes. PR
  [#&#8203;979](https://redirect.github.com/fastapi/typer/pull/979) by
  [@&#8203;AryazE](https://redirect.github.com/AryazE). - 🐛 Allow colon in zsh autocomplete values
  and descriptions. PR [#&#8203;988](https://redirect.github.com/fastapi/typer/pull/988) by
  [@&#8203;snapbug](https://redirect.github.com/snapbug).

##### Refactors

- 🗑️ Deprecate support for `is_flag` and `flag_value` parameters. PR
  [#&#8203;987](https://redirect.github.com/fastapi/typer/pull/987) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - 🔥 Remove unused functionality from
  `_typing.py` file. PR [#&#8203;805](https://redirect.github.com/fastapi/typer/pull/805) by
  [@&#8203;ivantodorovich](https://redirect.github.com/ivantodorovich). - ✏️ Fix typo in function
  name `_make_rich_text`. PR [#&#8203;959](https://redirect.github.com/fastapi/typer/pull/959) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg).

##### Internal

- ✅ Only run completion installation tests when the env var `_TYPER_RUN_INSTALL_COMPLETION_TESTS` is
  set. PR [#&#8203;995](https://redirect.github.com/fastapi/typer/pull/995) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - 📝 Update the docstring of the
  `_make_rich_text` method. PR [#&#8203;972](https://redirect.github.com/fastapi/typer/pull/972) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - ⬆ \[pre-commit.ci] pre-commit
  autoupdate. PR [#&#8203;1040](https://redirect.github.com/fastapi/typer/pull/1040) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump
  mkdocs-material from 9.5.42 to 9.5.44. PR
  [#&#8203;1042](https://redirect.github.com/fastapi/typer/pull/1042) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump ruff from 0.7.1
  to 0.7.2. PR [#&#8203;1038](https://redirect.github.com/fastapi/typer/pull/1038) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  mkdocs-macros-plugin from 1.3.6 to 1.3.7. PR
  [#&#8203;1031](https://redirect.github.com/fastapi/typer/pull/1031) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1032](https://redirect.github.com/fastapi/typer/pull/1032) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.7.0 to 0.7.1. PR [#&#8203;1029](https://redirect.github.com/fastapi/typer/pull/1029) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump pillow from
  10.4.0 to 11.0.0. PR [#&#8203;1023](https://redirect.github.com/fastapi/typer/pull/1023) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump mkdocs-material
  from 9.5.35 to 9.5.42. PR [#&#8203;1027](https://redirect.github.com/fastapi/typer/pull/1027) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump ruff from 0.6.5
  to 0.7.0. PR [#&#8203;1026](https://redirect.github.com/fastapi/typer/pull/1026) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  mkdocs-macros-plugin from 1.2.0 to 1.3.6. PR
  [#&#8203;1025](https://redirect.github.com/fastapi/typer/pull/1025) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Update pre-commit
  requirement from <4.0.0,>=2.17.0 to >=2.17.0,<5.0.0. PR
  [#&#8203;1012](https://redirect.github.com/fastapi/typer/pull/1012) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  pypa/gh-action-pypi-publish from 1.10.1 to 1.10.3. PR
  [#&#8203;1009](https://redirect.github.com/fastapi/typer/pull/1009) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1001](https://redirect.github.com/fastapi/typer/pull/1001) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - 👷 Update Deploy
  docs CI to use uv. PR [#&#8203;1021](https://redirect.github.com/fastapi/typer/pull/1021) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - 👷 Fix smokeshow, checkout files on CI.
  PR [#&#8203;1020](https://redirect.github.com/fastapi/typer/pull/1020) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - 👷 Use uv in CI. PR
  [#&#8203;1019](https://redirect.github.com/fastapi/typer/pull/1019) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - 👷 Update `labeler.yml`. PR
  [#&#8203;1014](https://redirect.github.com/fastapi/typer/pull/1014) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - 👷 Update worfkow deploy-docs-notify
  URL. PR [#&#8203;1011](https://redirect.github.com/fastapi/typer/pull/1011) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - 👷 Upgrade Cloudflare GitHub Action. PR
  [#&#8203;1010](https://redirect.github.com/fastapi/typer/pull/1010) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - ⬆ Bump mkdocs-macros-plugin from 1.0.5
  to 1.2.0. PR [#&#8203;992](https://redirect.github.com/fastapi/typer/pull/992) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump ruff from 0.6.4
  to 0.6.5. PR [#&#8203;991](https://redirect.github.com/fastapi/typer/pull/991) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump mkdocs-material
  from 9.5.34 to 9.5.35. PR [#&#8203;996](https://redirect.github.com/fastapi/typer/pull/996) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;993](https://redirect.github.com/fastapi/typer/pull/993) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆
  \[pre-commit.ci] pre-commit autoupdate. PR
  [#&#8203;982](https://redirect.github.com/fastapi/typer/pull/982) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump
  tiangolo/issue-manager from 0.5.0 to 0.5.1. PR
  [#&#8203;980](https://redirect.github.com/fastapi/typer/pull/980) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - 👷 Update
  `issue-manager.yml`. PR [#&#8203;978](https://redirect.github.com/fastapi/typer/pull/978) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - ⬆ Bump ruff from 0.6.3 to 0.6.4. PR
  [#&#8203;975](https://redirect.github.com/fastapi/typer/pull/975) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump mkdocs-material
  from 9.5.33 to 9.5.34. PR [#&#8203;963](https://redirect.github.com/fastapi/typer/pull/963) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  pypa/gh-action-pypi-publish from 1.9.0 to 1.10.1. PR
  [#&#8203;973](https://redirect.github.com/fastapi/typer/pull/973) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;966](https://redirect.github.com/fastapi/typer/pull/966) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - 💚 Set
  `include-hidden-files` to `True` when using the `upload-artifact` GH action. PR
  [#&#8203;967](https://redirect.github.com/fastapi/typer/pull/967) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - ⬆ Bump ruff from 0.6.1 to 0.6.3. PR
  [#&#8203;961](https://redirect.github.com/fastapi/typer/pull/961) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;689](https://redirect.github.com/fastapi/typer/pull/689) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.2.0 to 0.6.1. PR [#&#8203;938](https://redirect.github.com/fastapi/typer/pull/938) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - 👷 Update
  `latest-changes` GitHub Action. PR
  [#&#8203;955](https://redirect.github.com/fastapi/typer/pull/955) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo).

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS43LjEiLCJ1cGRhdGVkSW5WZXIiOiIzOS43LjEiLCJ0YXJnZXRCcmFuY2giOiJtYWluIiwibGFiZWxzIjpbXX0=-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Chores

- **deps**: Update python-semantic-release/python-semantic-release action to v9.12.2
  ([`344ed9a`](https://github.com/MartinBernstorff/Memium/commit/344ed9afc3ce08094003692507c6f61ba3b045ad))


## v0.25.4 (2024-11-06)

### Bug Fixes

- **deps**: Update dependency tqdm to v4.67.0
  ([`ab27f1b`](https://github.com/MartinBernstorff/Memium/commit/ab27f1b9ce89f4d2dbe849f3397124f72e475925))


## v0.25.3 (2024-11-06)

### Bug Fixes

- **deps**: Update dependency pyright to v1.1.388
  ([`6763193`](https://github.com/MartinBernstorff/Memium/commit/6763193c733442854d88c375d85d45724e5d5709))

### Chores

- **deps**: Update python-semantic-release/python-semantic-release action to v9.12.1
  ([`be2a1fb`](https://github.com/MartinBernstorff/Memium/commit/be2a1fbcd129ec35895ed1abdfee8276b020eb77))


## v0.25.2 (2024-11-05)

### Performance Improvements

- Check for anki before note sync ([#766](https://github.com/MartinBernstorff/Memium/pull/766),
  [`d4f33b9`](https://github.com/MartinBernstorff/Memium/commit/d4f33b958a8671e1bf69bb5f941d2d2a1894e423))


## v0.25.1 (2024-11-04)

### Bug Fixes

- **deps**: Update dependency sentry-sdk to v2.18.0
  ([`483feb4`](https://github.com/MartinBernstorff/Memium/commit/483feb4cf274a2e787e20f8292af2621f67d1a16))


## v0.25.0 (2024-11-01)

### Features

- Simplify code visualisation ([#764](https://github.com/MartinBernstorff/Memium/pull/764),
  [`315eb24`](https://github.com/MartinBernstorff/Memium/commit/315eb24381048ae0b56566a2e5a13bf50a3f4468))


## v0.24.10 (2024-10-30)

### Bug Fixes

- **deps**: Update dependency pyright to v1.1.387
  ([`5ac08cb`](https://github.com/MartinBernstorff/Memium/commit/5ac08cbe50223007916976cbdbbc83555147b122))


## v0.24.9 (2024-10-29)

### Bug Fixes

- **deps**: Update dependency pytest-cov to v6
  ([`f00e1ad`](https://github.com/MartinBernstorff/Memium/commit/f00e1ad36ab7169240fb62f8caa5dc9e3c14e6a4))


## v0.24.8 (2024-10-29)

### Bug Fixes

- **deps**: Update dependency pre-commit to v4
  ([`93053e7`](https://github.com/MartinBernstorff/Memium/commit/93053e7908ed767e447b4627234fecc43557fb90))

- **deps**: Update dependency pytest to v8
  ([`2004f7c`](https://github.com/MartinBernstorff/Memium/commit/2004f7c0cc9a8591a9e31790642b5a391bf504cd))


## v0.24.7 (2024-10-29)

### Bug Fixes

- **deps**: Update dependency pydantic to v2.9.2
  ([`279286b`](https://github.com/MartinBernstorff/Memium/commit/279286b31f76c0d5f98498f0341f586edc8f9c0b))

- **deps**: Update dependency syrupy to v4.7.2
  ([`90ac769`](https://github.com/MartinBernstorff/Memium/commit/90ac7695e893caa126899ef1a1f23f17b51b437c))


## v0.24.6 (2024-10-28)

### Bug Fixes

- **deps**: Update dependency markdown to v3.7
  ([`c4bbd4f`](https://github.com/MartinBernstorff/Memium/commit/c4bbd4fbd93b8d888c1e75afbffb834ab927f57f))


## v0.24.5 (2024-10-28)

### Bug Fixes

- **deps**: Update dependency pre-commit to v3.8.0
  ([`8233a4e`](https://github.com/MartinBernstorff/Memium/commit/8233a4e75e2453141c0d5d24c9b93143491f0882))


## v0.24.4 (2024-10-28)

### Bug Fixes

- **deps**: Update dependency cffi to v1.17.1
  ([`77c8997`](https://github.com/MartinBernstorff/Memium/commit/77c89976ea4e126ab00607b95e60717759c59167))

- **deps**: Update dependency diff-cover to v9.2.0
  ([`df00d82`](https://github.com/MartinBernstorff/Memium/commit/df00d825e0d0adde3c4070fe234ea03f7fca3011))


## v0.24.3 (2024-10-28)

### Bug Fixes

- **deps**: Update dependency bs4 to v0.0.2
  ([`44ca48d`](https://github.com/MartinBernstorff/Memium/commit/44ca48d7b05bace5a01ad60639a2540211c48d30))

- **deps**: Update dependency typer to v0.12.5
  ([`4c55218`](https://github.com/MartinBernstorff/Memium/commit/4c55218434fc0c196b0fda5eb2fc2e8d868625d1))

### Chores

- **deps**: Update dependency tqdm to v4.66.6
  ([`40f0c52`](https://github.com/MartinBernstorff/Memium/commit/40f0c528c4694b6c4fdb40532529948394c0c09e))


## v0.24.2 (2024-10-27)

### Bug Fixes

- Typo ([#750](https://github.com/MartinBernstorff/Memium/pull/750),
  [`c6ff00e`](https://github.com/MartinBernstorff/Memium/commit/c6ff00eb3876a5789cff9f3a40fafec4d368efd4))


## v0.24.1 (2024-10-27)

### Bug Fixes

- Further improve duplicate loggig ([#749](https://github.com/MartinBernstorff/Memium/pull/749),
  [`2d6431b`](https://github.com/MartinBernstorff/Memium/commit/2d6431bc30a3fee1a53f147c27980bc7c23c058f))

### Refactoring

- Html parsing ([#748](https://github.com/MartinBernstorff/Memium/pull/748),
  [`a9578ce`](https://github.com/MartinBernstorff/Memium/commit/a9578cefe03d9336982af153bb7e966b46ab5d86))


## v0.24.0 (2024-10-27)

### Features

- Improve styling of code blocks ([#747](https://github.com/MartinBernstorff/Memium/pull/747),
  [`c513731`](https://github.com/MartinBernstorff/Memium/commit/c513731321eb822d2d2d4c9afba588783d7c4ff6))


## v0.23.0 (2024-10-27)

### Features

- Improve logging ([#746](https://github.com/MartinBernstorff/Memium/pull/746),
  [`a4647d3`](https://github.com/MartinBernstorff/Memium/commit/a4647d345db8a3dd04c63547ad30b5763b52fabe))


## v0.22.2 (2024-10-27)

### Bug Fixes

- Improve logging of parser errors ([#745](https://github.com/MartinBernstorff/Memium/pull/745),
  [`6a101d4`](https://github.com/MartinBernstorff/Memium/commit/6a101d40e35a0dd00da42ab77e419ecbabfdcbe4))


## v0.22.1 (2024-10-27)

### Bug Fixes

- Disable irrelevant genanki warnings ([#744](https://github.com/MartinBernstorff/Memium/pull/744),
  [`bbf5458`](https://github.com/MartinBernstorff/Memium/commit/bbf5458f768519f9ff27e0d9a81c309900431bb5))


## v0.22.0 (2024-10-27)

### Features

- Add codeblock parsing ([#742](https://github.com/MartinBernstorff/Memium/pull/742),
  [`cc48a3b`](https://github.com/MartinBernstorff/Memium/commit/cc48a3bda50b64808e6adceb818d9622737e3a5a))


## v0.21.6 (2024-10-27)

### Bug Fixes

- Empty rows in table parsing ([#741](https://github.com/MartinBernstorff/Memium/pull/741),
  [`03de23e`](https://github.com/MartinBernstorff/Memium/commit/03de23e7362f8a84a87a30b7d8d3513c2adf0b0e))


## v0.21.5 (2024-10-27)

### Bug Fixes

- Handle dashes in wikilinks ([#740](https://github.com/MartinBernstorff/Memium/pull/740),
  [`97d1cf0`](https://github.com/MartinBernstorff/Memium/commit/97d1cf0e92db1b9ab9e00de883d37b24870930c0))


## v0.21.4 (2024-10-27)

### Bug Fixes

- More generous parsing of italics ([#739](https://github.com/MartinBernstorff/Memium/pull/739),
  [`39298c1`](https://github.com/MartinBernstorff/Memium/commit/39298c1cdc75db95acbd02c3b7fc631e1456c444))

### Chores

- Cleanup ([#696](https://github.com/MartinBernstorff/Memium/pull/696),
  [`035ea7c`](https://github.com/MartinBernstorff/Memium/commit/035ea7c3b076de669ef9cd2a8cc6a3e0a4366547))

- **deps**: Update dependency dev/pre-commit to v3.7.1
  ([`3e41364`](https://github.com/MartinBernstorff/Memium/commit/3e41364c651315adcb2a743cc5f475e76f3fb11d))

- **deps**: Update dependency dev/pyright to v1.1.362
  ([`ed72e3f`](https://github.com/MartinBernstorff/Memium/commit/ed72e3fbebfa6f653ebe7b8ac975efa00f18a8b5))

- **deps**: Update dependency dev/pyright to v1.1.363
  ([`f58bde5`](https://github.com/MartinBernstorff/Memium/commit/f58bde57b3ec756895157ca64e3d1a3dacb4c068))

- **deps**: Update dependency dev/pyright to v1.1.364
  ([`71f2f73`](https://github.com/MartinBernstorff/Memium/commit/71f2f739cb70320f8f9e57e1b3c0a1a2cc73aaf3))

- **deps**: Update dependency dev/pyright to v1.1.365
  ([`788df39`](https://github.com/MartinBernstorff/Memium/commit/788df390436ba6f767b22b98aba56dfee5fd2852))

- **deps**: Update dependency dev/pyright to v1.1.367
  ([`7df6c4e`](https://github.com/MartinBernstorff/Memium/commit/7df6c4ecdaacec8cea27ec813040c6a311ebdaf9))

- **deps**: Update dependency dev/pyright to v1.1.368
  ([`e807fc9`](https://github.com/MartinBernstorff/Memium/commit/e807fc943f2486eedfe402938e680889a92a2f00))

- **deps**: Update dependency dev/pyright to v1.1.369
  ([`56a257e`](https://github.com/MartinBernstorff/Memium/commit/56a257ec62e10c496c538dc6a29000bbc0c9c3ca))

- **deps**: Update dependency dev/pyright to v1.1.370
  ([`595e89e`](https://github.com/MartinBernstorff/Memium/commit/595e89ec0f1a326cecb058fdee638119b6bdf9aa))

- **deps**: Update dependency dev/pyright to v1.1.371
  ([`b215832`](https://github.com/MartinBernstorff/Memium/commit/b2158322a0bef68e5eb7e15c66574a49ec7ff977))

- **deps**: Update dependency dev/ruff to v0.4.4
  ([`e0896bd`](https://github.com/MartinBernstorff/Memium/commit/e0896bd41b79cdd8dc324dd685fd066b640a2901))

- **deps**: Update dependency dev/ruff to v0.4.5
  ([`7006e4f`](https://github.com/MartinBernstorff/Memium/commit/7006e4ff49cd64ff059a72fd05d99292624b3c7e))

- **deps**: Update dependency pydantic to v2.7.2
  ([`469dd43`](https://github.com/MartinBernstorff/Memium/commit/469dd43e0039be7f7f976acce7e0413befd0fd33))

- **deps**: Update dependency pydantic to v2.7.3
  ([`ade33b9`](https://github.com/MartinBernstorff/Memium/commit/ade33b9b8708c6c59a8d0db8f19fe4ebe838cc0f))

- **deps**: Update dependency pydantic to v2.7.4
  ([`ef47449`](https://github.com/MartinBernstorff/Memium/commit/ef474490c539413fba3463945059aa59b5a1c047))

- **deps**: Update dependency pydantic to v2.8.0
  ([`c89414c`](https://github.com/MartinBernstorff/Memium/commit/c89414cd483aaf15071d6efdd95a6cd98567309b))

- **deps**: Update dependency pydantic to v2.8.1
  ([`2d711d9`](https://github.com/MartinBernstorff/Memium/commit/2d711d97ade8b64783de5e443ceddb1adbda2f62))

- **deps**: Update dependency pydantic to v2.8.2
  ([`8b2c12e`](https://github.com/MartinBernstorff/Memium/commit/8b2c12e58cd395862ea4b10b57479ab2aa924472))

- **deps**: Update dependency pyright to v1.1.386
  ([`a7afc33`](https://github.com/MartinBernstorff/Memium/commit/a7afc33dafde6c45ad06aba5ab59c7b6b4dc3c40))

- **deps**: Update dependency sentry-sdk to v2.10.0
  ([`1625ea0`](https://github.com/MartinBernstorff/Memium/commit/1625ea072855013f4b6c96de28e4b0b0312cf2b3))

- **deps**: Update dependency sentry-sdk to v2.17.0
  ([`c35c510`](https://github.com/MartinBernstorff/Memium/commit/c35c51091cedd9b68956e5ff26a904caf5691d2c))

- **deps**: Update dependency sentry-sdk to v2.2.0
  ([`3892955`](https://github.com/MartinBernstorff/Memium/commit/38929558ece763fda12b0b0b0ef770efa762b1ee))

- **deps**: Update dependency sentry-sdk to v2.2.1
  ([`58d33db`](https://github.com/MartinBernstorff/Memium/commit/58d33db77b94ec915f9aa9e436bf3805011f3adf))

- **deps**: Update dependency sentry-sdk to v2.3.0
  ([`68eba46`](https://github.com/MartinBernstorff/Memium/commit/68eba46fc5026e98d780f541e05767d046bd127c))

- **deps**: Update dependency sentry-sdk to v2.3.1
  ([`8973609`](https://github.com/MartinBernstorff/Memium/commit/897360944183d39de31ff5d2320b3add26a0673e))

- **deps**: Update dependency sentry-sdk to v2.4.0
  ([`cb38267`](https://github.com/MartinBernstorff/Memium/commit/cb38267aad20cfdf25d4710ba1e17fdedf07036e))

- **deps**: Update dependency sentry-sdk to v2.5.0
  ([`6141c7b`](https://github.com/MartinBernstorff/Memium/commit/6141c7b3b82195346c8981c59d01d26241c5ace9))

- **deps**: Update dependency sentry-sdk to v2.5.1
  ([`85d1211`](https://github.com/MartinBernstorff/Memium/commit/85d12110fb114120f9a4c1fb6ad93b073e5e3f45))

- **deps**: Update dependency sentry-sdk to v2.6.0
  ([`da39d73`](https://github.com/MartinBernstorff/Memium/commit/da39d735c2b40ca6da41f85bbf9614f950a0f0d3))

- **deps**: Update dependency sentry-sdk to v2.7.0
  ([`525ad14`](https://github.com/MartinBernstorff/Memium/commit/525ad146d6763a62f4df549ec486c445c09441c9))

- **deps**: Update dependency sentry-sdk to v2.7.1
  ([`7f9163e`](https://github.com/MartinBernstorff/Memium/commit/7f9163e435af045c85182c61451efe55ea36f2d8))

- **deps**: Update dependency sentry-sdk to v2.8.0
  ([`23a5ce0`](https://github.com/MartinBernstorff/Memium/commit/23a5ce030b61a2f6a67c7cb90ee9ab66d3bd35fd))

- **deps**: Update dependency sentry-sdk to v2.9.0
  ([`93f2d18`](https://github.com/MartinBernstorff/Memium/commit/93f2d1834095f19cbefc69f4fe2110ff257969da))

- **deps**: Update dependency tests/diff-cover to v9.1.0
  ([`a7d11e1`](https://github.com/MartinBernstorff/Memium/commit/a7d11e1cfe9557ee1a7fcbc92fe0171a9ed7d523))

- **deps**: Update dependency wasabi to v1.1.3
  ([`a639a64`](https://github.com/MartinBernstorff/Memium/commit/a639a640fca2dd551cc22816603d79e3368054b5))

- **deps**: Update docker/build-push-action action to v6
  ([`05d754c`](https://github.com/MartinBernstorff/Memium/commit/05d754c62e6c606f8eae7bfd1f49dce013549922))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.12.0
  ([`c2587b8`](https://github.com/MartinBernstorff/Memium/commit/c2587b81eede1cb71c560a0b0d778710167f44d6))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.7.1
  ([`b36a693`](https://github.com/MartinBernstorff/Memium/commit/b36a693ea8c8c2656716504c8e5710bda2d54e10))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.7.2
  ([`a8ce44c`](https://github.com/MartinBernstorff/Memium/commit/a8ce44c3412ff9fbae155f1feff3d334948c6ad7))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.7.3
  ([`b6a0329`](https://github.com/MartinBernstorff/Memium/commit/b6a03293423ff8c9d105d49a9666e0ffa3bdf56b))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.0
  ([`40a7f7f`](https://github.com/MartinBernstorff/Memium/commit/40a7f7f039c8414b03914ce619af1ed73dab0b1b))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.1
  ([`243b1fe`](https://github.com/MartinBernstorff/Memium/commit/243b1fe2122cb7005aef5aab87e2867fe00584c9))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.2
  ([`c27b50d`](https://github.com/MartinBernstorff/Memium/commit/c27b50d6c84ea4c36194fea34b95a29fcf666495))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.3
  ([`368a2d0`](https://github.com/MartinBernstorff/Memium/commit/368a2d0816ae559c2d5f522243ea3eba0fe133c5))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.4
  ([`d0d62b6`](https://github.com/MartinBernstorff/Memium/commit/d0d62b65890aa70abd2852ec2e1049db4d74a45e))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.5
  ([`c306ac5`](https://github.com/MartinBernstorff/Memium/commit/c306ac5508d7d86195c7c73ed9b7cf2c4d8d9384))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.6
  ([`dc51102`](https://github.com/MartinBernstorff/Memium/commit/dc51102619b15a82e7da4d2a44934ef218ccedce))


## v0.21.3 (2024-05-06)

### Bug Fixes

- Do not escape html ([#664](https://github.com/MartinBernstorff/Memium/pull/664),
  [`dcf5b28`](https://github.com/MartinBernstorff/Memium/commit/dcf5b28ac57a9df8996fc7abbd7ae05d676d215f))

- update anki_prompt_qa.py - test: update test_anki_prompt_qa.ambr

### Chores

- Delete test.py
  ([`f1854dc`](https://github.com/MartinBernstorff/Memium/commit/f1854dc65643c430df9db0ce62cafb94680abb03))

- Delete test.py ([#656](https://github.com/MartinBernstorff/Memium/pull/656),
  [`1505b0f`](https://github.com/MartinBernstorff/Memium/commit/1505b0f8d8fbea4785f5935a79e717e38fece8c5))

- **deps**: Update dependency dev/pyright to v1.1.361
  ([`9fdb56b`](https://github.com/MartinBernstorff/Memium/commit/9fdb56b8a2390e37a2e5cc8a85cb1d4a9488fa65))

- **deps**: Update dependency dev/ruff to v0.4.3
  ([`e8f6541`](https://github.com/MartinBernstorff/Memium/commit/e8f6541bf1bbf49e738ec381ae5b609be2b52d4b))

- **deps**: Update dependency sentry-sdk to v2.1.0
  ([`625b0bf`](https://github.com/MartinBernstorff/Memium/commit/625b0bfeb337895b6dc47fddae68836676cd3b1f))

- **deps**: Update dependency sentry-sdk to v2.1.1
  ([`94c4d3c`](https://github.com/MartinBernstorff/Memium/commit/94c4d3c80cf75f241470ef5211a68e7037be775c))

- **deps**: Update dependency tqdm to v4.66.4
  ([`168a75e`](https://github.com/MartinBernstorff/Memium/commit/168a75e9afcae0b7cac8ce4d06a58427048467f2))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.7.0
  ([`05181e1`](https://github.com/MartinBernstorff/Memium/commit/05181e1b3367c9231b1219728d2f54a7ddd769b9))

### Testing

- Update test_anki_prompt_qa.ambr
  ([`b08f56a`](https://github.com/MartinBernstorff/Memium/commit/b08f56ae8517f5b5a5c04ac58b79022fd9c29aaf))


## v0.21.2 (2024-04-30)

### Bug Fixes

- Only escape relevant sections
  ([`5e6d403`](https://github.com/MartinBernstorff/Memium/commit/5e6d4034bfb35a02c224241ddfb32ba7c29b3be3))

- Only escape relevant sections ([#655](https://github.com/MartinBernstorff/Memium/pull/655),
  [`9f1cb01`](https://github.com/MartinBernstorff/Memium/commit/9f1cb01f86e83b82b7e92fd04bd05fab759a6458))

### Chores

- **deps**: Update dependency tests/pytest-xdist to v3.6.1
  ([`dcd0182`](https://github.com/MartinBernstorff/Memium/commit/dcd0182171c349ea94848c6289d71cc39d4b90c3))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.6.0
  ([`6acdc9c`](https://github.com/MartinBernstorff/Memium/commit/6acdc9cb1c02282ea392d2185ee26a6305628078))

### Refactoring

- Split cli and main
  ([`a316423`](https://github.com/MartinBernstorff/Memium/commit/a316423f5d4b4235848af9300f0b66919ee5bc90))

- Split cli and main ([#651](https://github.com/MartinBernstorff/Memium/pull/651),
  [`3e2fab4`](https://github.com/MartinBernstorff/Memium/commit/3e2fab401f0b397553746ba8c5b0fda3203ea1ce))

### Testing

- Update test_anki_prompt_qa.py
  ([`0dbd6c3`](https://github.com/MartinBernstorff/Memium/commit/0dbd6c37077c7acc56bef711f44f1944d0aad2d7))


## v0.21.1 (2024-04-27)

### Bug Fixes

- Html escaping ([#641](https://github.com/MartinBernstorff/Memium/pull/641),
  [`6f97f55`](https://github.com/MartinBernstorff/Memium/commit/6f97f55d85764265e4fbe6af58af832c6f3695a7))

### Testing

- Update test_anki_prompt_qa.py
  ([`e142041`](https://github.com/MartinBernstorff/Memium/commit/e1420419b3740c8a23281ff95254d107440e8ef2))


## v0.21.0 (2024-04-27)

### Features

- **#637**: Append log to output folder
  ([`178ff35`](https://github.com/MartinBernstorff/Memium/commit/178ff358501080b699f1173a3241d493e774e567))

Fixes #637

- **#637**: Append log to output folder
  ([#649](https://github.com/MartinBernstorff/Memium/pull/649),
  [`f03969c`](https://github.com/MartinBernstorff/Memium/commit/f03969c17296c48ecd67f81df411435fe17384b9))

Fixes #637


## v0.20.0 (2024-04-27)

### Chores

- **deps**: Update dependency dev/pyright to v1.1.360
  ([`601e013`](https://github.com/MartinBernstorff/Memium/commit/601e0131a358c2a516701a7c3b6f523362342938))

- **deps**: Update dependency dev/ruff to v0.4.2
  ([`f7413f5`](https://github.com/MartinBernstorff/Memium/commit/f7413f5bdb96444623a0e447a390e04d9c256f94))

- **deps**: Update dependency pydantic to v2.7.1
  ([`ea0ad67`](https://github.com/MartinBernstorff/Memium/commit/ea0ad67acfeb7dd53ef1833c4208597af3c12c1f))

- **deps**: Update dependency sentry-sdk to v2
  ([`782b27b`](https://github.com/MartinBernstorff/Memium/commit/782b27b613d4cdb1bde0912b6e8e259204cbef7b))

- **deps**: Update dependency sentry-sdk to v2.0.1
  ([`37dc0ed`](https://github.com/MartinBernstorff/Memium/commit/37dc0ed92635d1c82cfe60fa705c638fe3be2054))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.5.0
  ([`335798b`](https://github.com/MartinBernstorff/Memium/commit/335798bde44aee34346a9ecd5d0220a33e27cbd4))

### Features

- Move obsidian link to top of AnkiQA
  ([`8802e01`](https://github.com/MartinBernstorff/Memium/commit/8802e015d449ab63d9c50601cca1ccea5b053299))

- Move obsidian link to top of AnkiQA ([#648](https://github.com/MartinBernstorff/Memium/pull/648),
  [`f45cdf9`](https://github.com/MartinBernstorff/Memium/commit/f45cdf9bb65c06b4a9d470e866347db62a2bbfe9))


## v0.19.1 (2024-04-22)

### Bug Fixes

- Calling method instead of getting link contents
  ([`121fa88`](https://github.com/MartinBernstorff/Memium/commit/121fa8821f76c33d911b0264023dfd637d6ed3ff))

- Calling method instead of getting link contents
  ([#639](https://github.com/MartinBernstorff/Memium/pull/639),
  [`81e68b4`](https://github.com/MartinBernstorff/Memium/commit/81e68b4cbaab50984aaab17aa683c8ebefdf74b7))


## v0.19.0 (2024-04-20)

### Chores

- **deps**: Update dependency dev/pyright to v1.1.358
  ([`08ea850`](https://github.com/MartinBernstorff/Memium/commit/08ea850e29b3c374038367968fa8a3cde098a8ec))

- **deps**: Update dependency dev/pyright to v1.1.359
  ([`ad3ad6b`](https://github.com/MartinBernstorff/Memium/commit/ad3ad6b2ca2c736adbb7cfe91608db83107805bd))

- **deps**: Update dependency dev/ruff to v0.3.6
  ([`9243d80`](https://github.com/MartinBernstorff/Memium/commit/9243d80a285d24d519cc12b86b2ab751e7d4236b))

- **deps**: Update dependency dev/ruff to v0.3.7
  ([`ae3928c`](https://github.com/MartinBernstorff/Memium/commit/ae3928c0e8b8964d83733134119c28b779c9d332))

- **deps**: Update dependency dev/ruff to v0.4.0
  ([`122bf50`](https://github.com/MartinBernstorff/Memium/commit/122bf5073a9debc3467bcb77b56c4edce0ba974f))

- **deps**: Update dependency dev/ruff to v0.4.1
  ([`5d56819`](https://github.com/MartinBernstorff/Memium/commit/5d5681946cacf21cfbd331f4baadee8aa960198d))

- **deps**: Update dependency pydantic to v2.7.0
  ([`b3a32f0`](https://github.com/MartinBernstorff/Memium/commit/b3a32f0b862c8054cdaf255bb6ccb9e0582e1df3))

- **deps**: Update dependency sentry-sdk to v1.45.0
  ([`eae82e6`](https://github.com/MartinBernstorff/Memium/commit/eae82e68846c6dfe1cec45817aec0234bd448047))

- **deps**: Update dependency tests/diff-cover to v9
  ([`573571f`](https://github.com/MartinBernstorff/Memium/commit/573571f9380ef749552ee1f69c378d2ad00c47ef))

- **deps**: Update dependency tests/pytest-xdist to v3.6.0
  ([`ab9face`](https://github.com/MartinBernstorff/Memium/commit/ab9face94242ce642b6801526cc7a2d666ea1605))

- **deps**: Update dependency typer to v0.12.3
  ([`e2f44fc`](https://github.com/MartinBernstorff/Memium/commit/e2f44fc0b9c9cc89518bf3e597ada32964fdbcde))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.4.2
  ([`c14629d`](https://github.com/MartinBernstorff/Memium/commit/c14629dfe91b787c09985d90719c2f8b43297164))

### Features

- Add obsidian URI
  ([`78cfbcd`](https://github.com/MartinBernstorff/Memium/commit/78cfbcd9420b122bb872d12c896ef1b57568fbf8))

- Add open in obsidian button ([#635](https://github.com/MartinBernstorff/Memium/pull/635),
  [`8843a65`](https://github.com/MartinBernstorff/Memium/commit/8843a65ffac535ce5aa1768f9ca35bfb24ddd620))

### Testing

- Update test_extractor_table.py and test_prompt.py
  ([`a862723`](https://github.com/MartinBernstorff/Memium/commit/a86272353d500b47f1c56970e690b8d63a28f413))


## v0.18.0 (2024-04-09)

### Features

- Support slashes in wikilinks
  ([`7d207ff`](https://github.com/MartinBernstorff/Memium/commit/7d207ff8964b390881a9169ed236db3541eb58cc))

- Support slashes in wikilinks ([#622](https://github.com/MartinBernstorff/Memium/pull/622),
  [`8fc90ac`](https://github.com/MartinBernstorff/Memium/commit/8fc90acdff2dc77bdff564e8ad27eda668a57b46))


## v0.17.0 (2024-04-09)

### Features

- Sort terms before generating subdecks
  ([`9564ff7`](https://github.com/MartinBernstorff/Memium/commit/9564ff740ebd8a32540dd514b0d0e1475289441c))

- Sort terms before generating subdecks
  ([#621](https://github.com/MartinBernstorff/Memium/pull/621),
  [`fd7e703`](https://github.com/MartinBernstorff/Memium/commit/fd7e703ad17e5edfc2d4e07f15f974e48a7f65bf))


## v0.16.1 (2024-04-09)

### Bug Fixes

- Term extraction ([#620](https://github.com/MartinBernstorff/Memium/pull/620),
  [`8816e48`](https://github.com/MartinBernstorff/Memium/commit/8816e48b87dda53ad57e8e3db10406db2f2366ed))

### Testing

- Update test_anki_prompt_qa.py
  ([`ec2f0d2`](https://github.com/MartinBernstorff/Memium/commit/ec2f0d2b72107b7dd738c4bf3042894969c374b5))


## v0.16.0 (2024-04-09)

### Features

- Create model if it does not exist
  ([`e979d45`](https://github.com/MartinBernstorff/Memium/commit/e979d4567139e8ef095146193672e4bde65c0f2b))

- Create model if it does not exist ([#619](https://github.com/MartinBernstorff/Memium/pull/619),
  [`380ed4e`](https://github.com/MartinBernstorff/Memium/commit/380ed4eb659e82704565299e798c2d0200c7c6ab))


## v0.15.0 (2024-04-09)

### Chores

- **deps**: Update dependency dev/pre-commit to v3.6.1
  ([`c020f67`](https://github.com/MartinBernstorff/Memium/commit/c020f676cf9a46f9509f7f37b8adea1b5aefbb2e))

- **deps**: Update dependency dev/pre-commit to v3.6.2
  ([`4e52e8d`](https://github.com/MartinBernstorff/Memium/commit/4e52e8d5604a68eb9276afe9614298f38bf13370))

- **deps**: Update dependency dev/pre-commit to v3.7.0
  ([`fa48661`](https://github.com/MartinBernstorff/Memium/commit/fa4866192533ce4a4bae393c59e64e2481b6b000))

- **deps**: Update dependency dev/pyright to v1.1.351
  ([`0d18783`](https://github.com/MartinBernstorff/Memium/commit/0d187834784d4fd1b57f6400424f81940d78f735))

- **deps**: Update dependency dev/pyright to v1.1.352
  ([`4341487`](https://github.com/MartinBernstorff/Memium/commit/4341487e9fa78cdbbeed2162b75a1779c6c77933))

- **deps**: Update dependency dev/pyright to v1.1.353
  ([`80d8b97`](https://github.com/MartinBernstorff/Memium/commit/80d8b97e4797934bd01af7549f32abaadd93a4a6))

- **deps**: Update dependency dev/pyright to v1.1.356
  ([`64b2cf1`](https://github.com/MartinBernstorff/Memium/commit/64b2cf1a17f4a22d0164011b82c406535ef432ca))

- **deps**: Update dependency dev/pyright to v1.1.357
  ([`d8c851d`](https://github.com/MartinBernstorff/Memium/commit/d8c851d4c24e8dde3143c982bad093e49ddc7195))

- **deps**: Update dependency dev/ruff to v0.2.2
  ([`81544f3`](https://github.com/MartinBernstorff/Memium/commit/81544f3cc9801c0fb72fb14d0db73e05e983b6c2))

- **deps**: Update dependency dev/ruff to v0.3.0
  ([`7a93e73`](https://github.com/MartinBernstorff/Memium/commit/7a93e73674faf1ec614bdacfc20699393d13a76e))

- **deps**: Update dependency dev/ruff to v0.3.1
  ([`6095ed2`](https://github.com/MartinBernstorff/Memium/commit/6095ed24df306ef93c8eeb8d827a93d04f8c92ee))

- **deps**: Update dependency dev/ruff to v0.3.2
  ([`8525583`](https://github.com/MartinBernstorff/Memium/commit/8525583632ace4464590d0246760b1f0f73f7a91))

- **deps**: Update dependency dev/ruff to v0.3.5
  ([`a96013f`](https://github.com/MartinBernstorff/Memium/commit/a96013f9311e1b19b5d73c90ba9c3e77a89860fc))

- **deps**: Update dependency iterpy to v1
  ([`455ff31`](https://github.com/MartinBernstorff/Memium/commit/455ff31a3389f809ed0055d49cd94512e349df67))

- **deps**: Update dependency iterpy to v1.5.0
  ([`81cbf94`](https://github.com/MartinBernstorff/Memium/commit/81cbf940b25f088eaa4cce306bd5bcde1dcc0b60))

- **deps**: Update dependency iterpy to v1.5.1
  ([`67c93bd`](https://github.com/MartinBernstorff/Memium/commit/67c93bd85639e7daf00a0027cd7f73ef393175bf))

- **deps**: Update dependency iterpy to v1.6.0
  ([`25ee384`](https://github.com/MartinBernstorff/Memium/commit/25ee384a10ce5e28b9fc7ef492d287650411371a))

- **deps**: Update dependency iterpy to v1.7.0
  ([`1153826`](https://github.com/MartinBernstorff/Memium/commit/1153826e756961ef24379300d1a808fdc402b794))

- **deps**: Update dependency iterpy to v1.8.1
  ([`68ece09`](https://github.com/MartinBernstorff/Memium/commit/68ece09d05296ff0494a9f7f190781385cf869e0))

- **deps**: Update dependency iterpy to v1.9.0
  ([`906e640`](https://github.com/MartinBernstorff/Memium/commit/906e640fd54e2a63f9bf4c8a82792ab86fdad113))

- **deps**: Update dependency markdown to v3.6
  ([`1748178`](https://github.com/MartinBernstorff/Memium/commit/1748178470228ed879b02981d0d6ce6d2b3ba159))

- **deps**: Update dependency pydantic to v2.6.2
  ([`70d8084`](https://github.com/MartinBernstorff/Memium/commit/70d808475f854593e17de61cf482dc0b09b0620b))

- **deps**: Update dependency pydantic to v2.6.3
  ([`69ef4fb`](https://github.com/MartinBernstorff/Memium/commit/69ef4fb8fa6789849f3441ddff6ac15e65846899))

- **deps**: Update dependency pydantic to v2.6.4
  ([`e734d3e`](https://github.com/MartinBernstorff/Memium/commit/e734d3e80212d1a55e1ba4dcf92c5dbe2bc06e52))

- **deps**: Update dependency sentry-sdk to v1.40.2
  ([`658a8c3`](https://github.com/MartinBernstorff/Memium/commit/658a8c30d8c24a2efdcf3aff174a093bd8aac446))

- **deps**: Update dependency sentry-sdk to v1.40.3
  ([`87a1e83`](https://github.com/MartinBernstorff/Memium/commit/87a1e8388147038211a3574e75a4f6721c5a386c))

- **deps**: Update dependency sentry-sdk to v1.40.4
  ([`3abd2d5`](https://github.com/MartinBernstorff/Memium/commit/3abd2d5432baa3c627fd05fcbc289f863ac85b1a))

- **deps**: Update dependency sentry-sdk to v1.40.5
  ([`737cb25`](https://github.com/MartinBernstorff/Memium/commit/737cb25023abd55df145ef77ddc17dcf458c8e45))

- **deps**: Update dependency sentry-sdk to v1.40.6
  ([`f4a8f0e`](https://github.com/MartinBernstorff/Memium/commit/f4a8f0e2cd02edd5faf27b2d2cad94b64744091a))

- **deps**: Update dependency sentry-sdk to v1.41.0
  ([`b422c1e`](https://github.com/MartinBernstorff/Memium/commit/b422c1ea25535acaa859e410b1f4f5f5f6d8f149))

- **deps**: Update dependency sentry-sdk to v1.44.0
  ([`0f4dade`](https://github.com/MartinBernstorff/Memium/commit/0f4dade1b0bdf962433e301bc42221d8383e6188))

- **deps**: Update dependency sentry-sdk to v1.44.1
  ([`0607674`](https://github.com/MartinBernstorff/Memium/commit/0607674265c1b680faad4901be09486d7d4a5130))

- **deps**: Update dependency tests/pytest-cov to v5
  ([`874eaaa`](https://github.com/MartinBernstorff/Memium/commit/874eaaa7755585a8b8ac5d8a7e6a53e6088d475a))

- **deps**: Update dependency tests/pytest-testmon to v2.1.1
  ([`eda5e2c`](https://github.com/MartinBernstorff/Memium/commit/eda5e2c99d60a4a68f947a2f70a32f9fcbf34a51))

- **deps**: Update dependency tqdm to v4.66.2
  ([`4fa5a3d`](https://github.com/MartinBernstorff/Memium/commit/4fa5a3d6e34c384109864b0d6cb7de4aceef126b))

- **deps**: Update dependency typer to v0.12.0
  ([`e6e049d`](https://github.com/MartinBernstorff/Memium/commit/e6e049d58e2a8ee9493ac586ca7494fa32dcd175))

- **deps**: Update dependency typer to v0.12.1
  ([`dc7edb0`](https://github.com/MartinBernstorff/Memium/commit/dc7edb0bc96cdbf67542dfdbcfd69b099ee8d951))

- **deps**: Update dependency typer to v0.12.2
  ([`92e40a1`](https://github.com/MartinBernstorff/Memium/commit/92e40a182c0dc5f7320e7a11a5090a19d8f5cc51))

- **deps**: Update python-semantic-release/python-semantic-release action to v9
  ([`b4a4dd6`](https://github.com/MartinBernstorff/Memium/commit/b4a4dd654ba2ff09d70022089842565d82790565))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.0.2
  ([`ddeba70`](https://github.com/MartinBernstorff/Memium/commit/ddeba707e96634657053bac2b42199c86f6cc56e))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.0.3
  ([`4d28b59`](https://github.com/MartinBernstorff/Memium/commit/4d28b5966a97102b5db802b5c609d06f5080014b))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.1.0
  ([`19ddce7`](https://github.com/MartinBernstorff/Memium/commit/19ddce77d14b1b4ebbc61ad23ebbb80af7367ed2))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.1.1
  ([`9a91fbf`](https://github.com/MartinBernstorff/Memium/commit/9a91fbf50c673c75a6075f9c715ece08bdc5eb87))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.4.0
  ([`eed8164`](https://github.com/MartinBernstorff/Memium/commit/eed816481f2ca1f2ad603178183b997e61d88305))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.4.1
  ([`1f58fa3`](https://github.com/MartinBernstorff/Memium/commit/1f58fa3c6636a20e477ce2df699712948fed30aa))

### Features

- Create decks based on wikilinks in qa question
  ([`448976b`](https://github.com/MartinBernstorff/Memium/commit/448976ba82f92a0b3909861e746f28e5ceafb58f))

- Create decks based on wikilinks in qa question
  ([#618](https://github.com/MartinBernstorff/Memium/pull/618),
  [`bcd61e3`](https://github.com/MartinBernstorff/Memium/commit/bcd61e32384799e6791af0eb5acc5fca930a6a05))

feat: create decks based on wikilinks in qa question

update 8 files


## v0.14.3 (2024-02-06)

### Bug Fixes

- Remove cloze extraction from default
  ([`3d4c889`](https://github.com/MartinBernstorff/Memium/commit/3d4c889c9ad56b51a4de4a9efbc2c163866909a0))

- Remove cloze extraction from default ([#571](https://github.com/MartinBernstorff/Memium/pull/571),
  [`48074a8`](https://github.com/MartinBernstorff/Memium/commit/48074a8194becd2bfc4c5391453d5df7726dde2c))

### Chores

- **deps**: Update dependency tests/pytest to v7.4.4
  ([`427d6a8`](https://github.com/MartinBernstorff/Memium/commit/427d6a813bae2ee3c799bc53e4df517c144015b5))

- **deps**: Update dependency tests/pytest to v7.4.4
  ([#559](https://github.com/MartinBernstorff/Memium/pull/559),
  [`a481ede`](https://github.com/MartinBernstorff/Memium/commit/a481ede81df0bf67e6c67cf3dbacf18bcc8ce1b2))

[![Mend Renovate](https://app.renovatebot.com/images/banner.svg)](https://renovatebot.com)

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [tests/pytest](https://docs.pytest.org/en/latest/)
  ([source](https://togithub.com/pytest-dev/pytest),
  [changelog](https://docs.pytest.org/en/stable/changelog.html)) | `==7.4.0` -> `==7.4.4` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/tests%2fpytest/7.4.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/tests%2fpytest/7.4.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/tests%2fpytest/7.4.0/7.4.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/tests%2fpytest/7.4.0/7.4.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pytest-dev/pytest (tests/pytest)</summary>

### [`v7.4.4`](https://togithub.com/pytest-dev/pytest/compare/7.4.3...7.4.4)

[Compare Source](https://togithub.com/pytest-dev/pytest/compare/7.4.3...7.4.4)

### [`v7.4.3`](https://togithub.com/pytest-dev/pytest/releases/tag/v7.4.3): pytest 7.4.3
  (2023-10-24)

[Compare Source](https://togithub.com/pytest-dev/pytest/compare/7.4.2...7.4.3)

## Bug Fixes

- [#&#8203;10447](https://togithub.com/pytest-dev/pytest/issues/10447): Markers are now considered
  in the reverse mro order to ensure base class markers are considered first -- this resolves a
  regression.

- [#&#8203;11239](https://togithub.com/pytest-dev/pytest/issues/11239): Fixed `:=` in asserts
  impacting unrelated test cases.

- [#&#8203;11439](https://togithub.com/pytest-dev/pytest/issues/11439): Handled an edge case where
  :data:`sys.stderr` might already be closed when :ref:`faulthandler` is tearing down.

### [`v7.4.2`](https://togithub.com/pytest-dev/pytest/releases/tag/7.4.2): pytest 7.4.2 (2023-09-07)

[Compare Source](https://togithub.com/pytest-dev/pytest/compare/7.4.1...7.4.2)

##### Bug Fixes

- [#&#8203;11237](https://togithub.com/pytest-dev/pytest/issues/11237): Fix doctest collection of
  `functools.cached_property` objects.

- [#&#8203;11306](https://togithub.com/pytest-dev/pytest/issues/11306): Fixed bug using
  `--importmode=importlib` which would cause package `__init__.py` files to be imported more than
  once in some cases.

- [#&#8203;11367](https://togithub.com/pytest-dev/pytest/issues/11367): Fixed bug where
  `user_properties` where not being saved in the JUnit XML file if a fixture failed during teardown.

- [#&#8203;11394](https://togithub.com/pytest-dev/pytest/issues/11394): Fixed crash when parsing
  long command line arguments that might be interpreted as files.

##### Improved Documentation

- [#&#8203;11391](https://togithub.com/pytest-dev/pytest/issues/11391): Improved disclaimer on
  pytest plugin reference page to better indicate this is an automated, non-curated listing.

### [`v7.4.1`](https://togithub.com/pytest-dev/pytest/releases/tag/7.4.1): pytest 7.4.1 (2023-09-02)

[Compare Source](https://togithub.com/pytest-dev/pytest/compare/7.4.0...7.4.1)

- [#&#8203;10337](https://togithub.com/pytest-dev/pytest/issues/10337): Fixed bug where fake
  intermediate modules generated by `--import-mode=importlib` would not include the child modules as
  attributes of the parent modules.

- [#&#8203;10702](https://togithub.com/pytest-dev/pytest/issues/10702): Fixed error assertion
  handling in `pytest.approx` when `None` is an expected or received value when comparing
  dictionaries.

- [#&#8203;10811](https://togithub.com/pytest-dev/pytest/issues/10811): Fixed issue when using
  `--import-mode=importlib` together with `--doctest-modules` that caused modules to be imported
  more than once, causing problems with modules that have import side effects.

</details>

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Disabled because a matching PR was automerged previously.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

This PR has been generated by [Mend Renovate](https://www.mend.io/free-developer-tools/renovate/).
  View repository job log [here](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzNy4xNzAuMCIsInVwZGF0ZWRJblZlciI6IjM3LjE3MC4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiJ9-->


## v0.14.2 (2024-02-06)

### Bug Fixes

- Duplicate prompt detection
  ([`5e3e37e`](https://github.com/MartinBernstorff/Memium/commit/5e3e37ef2ebb6b420cd58e455641acf158f1977d))

- Duplicate prompt detection ([#569](https://github.com/MartinBernstorff/Memium/pull/569),
  [`31b39c6`](https://github.com/MartinBernstorff/Memium/commit/31b39c657839e038fa65331099cd9fc620a6d280))

### Continuous Integration

- Do not disable on concurrency
  ([`05223f7`](https://github.com/MartinBernstorff/Memium/commit/05223f7ada7320dc494a28b1382a8063812bf9d1))

- Do not disable on concurrency ([#570](https://github.com/MartinBernstorff/Memium/pull/570),
  [`9e1fc1b`](https://github.com/MartinBernstorff/Memium/commit/9e1fc1b59b9446f60fbd350087c54ef97f55fae4))


## v0.14.1 (2024-02-06)

### Bug Fixes

- Gracefully fail if block cannot be parsed
  ([`4691aa8`](https://github.com/MartinBernstorff/Memium/commit/4691aa85b88abd2b30b33130f3026f79e42c1a49))

- Gracefully fail if block cannot be parsed
  ([#565](https://github.com/MartinBernstorff/Memium/pull/565),
  [`7a49b05`](https://github.com/MartinBernstorff/Memium/commit/7a49b0533e0e3b9cc076112141d9e179803bc369))

### Chores

- **deps**: Update dependency dev/pyright to v1.1.350
  ([`7b4c9f7`](https://github.com/MartinBernstorff/Memium/commit/7b4c9f7ea9f1dcbce079f76e0c102c79a972f9c3))

- **deps**: Update dependency dev/ruff to v0.2.1
  ([`125e96d`](https://github.com/MartinBernstorff/Memium/commit/125e96d16d710401eee7b669f6fd23794c594f9c))

- **deps**: Update dependency pydantic to v2.6.1
  ([`bdf76a5`](https://github.com/MartinBernstorff/Memium/commit/bdf76a51fa1ccb3e643ed9e06d18ece5bf60e2de))

- **deps**: Update dependency sentry-sdk to v1.40.1
  ([`caf7852`](https://github.com/MartinBernstorff/Memium/commit/caf78528062e62d6a876605e7017db47db5a43d5))


## v0.14.0 (2024-02-05)

### Chores

- **deps**: Update dependency pydantic to v2.6.0
  ([`74776d2`](https://github.com/MartinBernstorff/Memium/commit/74776d26748fa3a902ea628d27bfca0bd7e8267b))

### Features

- **#534**: Allow both rowwise and row-wise when parsing tables
  ([`5fdbac7`](https://github.com/MartinBernstorff/Memium/commit/5fdbac7d0868852c0024f5852120fb0dd58ed154))

Fixes #534

- **#534**: Allow both rowwise and row-wise when parsing tables
  ([#558](https://github.com/MartinBernstorff/Memium/pull/558),
  [`6a454bd`](https://github.com/MartinBernstorff/Memium/commit/6a454bd60fda1d7b1e7201a5f375fef09922d76d))

Fixes #534


## v0.13.1 (2024-02-04)

### Bug Fixes

- Migrate to iterpy
  ([`bf8fba0`](https://github.com/MartinBernstorff/Memium/commit/bf8fba0882a08323e2f3819c85c72bf4330d3c6d))

- Migrate to iterpy ([#555](https://github.com/MartinBernstorff/Memium/pull/555),
  [`752db8e`](https://github.com/MartinBernstorff/Memium/commit/752db8ec27587de1abbd9deb7557f14ff948335c))

fix: migrate to iterpy

update prompt_source.py

### Chores

- **deps**: Update dependency dev/pyright to v1.1.349
  ([`0be7671`](https://github.com/MartinBernstorff/Memium/commit/0be76718ac5b2608128a4be04ab3b209c70975de))

- **deps**: Update dependency dev/ruff to v0.2.0
  ([`9f7c810`](https://github.com/MartinBernstorff/Memium/commit/9f7c810213e4e0892d94a3f5ce25e0c370cb3d00))

- **deps**: Update dependency sentry-sdk to v1.40.0
  ([`ce58593`](https://github.com/MartinBernstorff/Memium/commit/ce585936d688359bba1e9d1612986e0c8f31427b))

- **deps**: Update dependency tests/pytest to v8
  ([`cdb09b3`](https://github.com/MartinBernstorff/Memium/commit/cdb09b3b4d667ceaf320a1b074d7a0992cefbde0))

- **deps**: Update dependency tests/pytest-sugar to v1
  ([`1a9d95b`](https://github.com/MartinBernstorff/Memium/commit/1a9d95ba72319bdbed17b69a4b9160fb77ca5ecf))


## v0.13.0 (2024-01-15)

### Chores

- **deps**: Update dependency dev/pyright to v1.1.346
  ([`f0f6cb5`](https://github.com/MartinBernstorff/Memium/commit/f0f6cb518c5d2e6380620da4b58eab1301defa70))

- **deps**: Update dependency dev/pyright to v1.1.347
  ([`23224db`](https://github.com/MartinBernstorff/Memium/commit/23224dbeeaba28b81147c52cf94a678893d83738))

### Features

- Exclude sparse cells from TableExtractor
  ([#542](https://github.com/MartinBernstorff/Memium/pull/542),
  [`244dabc`](https://github.com/MartinBernstorff/Memium/commit/244dabce4ec3a855e2bbdb3d0d69406f0fdb48d1))

misc.


## v0.12.1 (2024-01-14)

### Bug Fixes

- Correct table extraction without trailing spaces
  ([`8cb789c`](https://github.com/MartinBernstorff/Memium/commit/8cb789c3c756dcc6ea419bfac01995e271708e98))

- Correct table extraction without trailing spaces
  ([#535](https://github.com/MartinBernstorff/Memium/pull/535),
  [`9a1e1ba`](https://github.com/MartinBernstorff/Memium/commit/9a1e1ba7f826d74249e1de6f2dccfcd5176df3a4))


## v0.12.0 (2024-01-13)

### Chores

- **deps**: Update dependency dev/pyright to v1.1.345
  ([`9ead8ac`](https://github.com/MartinBernstorff/Memium/commit/9ead8ac6f1d0e6c7b3be7819235c42fcb623e467))

- **deps**: Update dependency dev/ruff to v0.1.12
  ([`0ce963f`](https://github.com/MartinBernstorff/Memium/commit/0ce963fd0ee95751ccfe419b8b2385f6750fe092))

- **deps**: Update dependency dev/ruff to v0.1.13
  ([`1a1d6e2`](https://github.com/MartinBernstorff/Memium/commit/1a1d6e260e9a82bae5daf0a7fcddb4ac06d9c688))

- **deps**: Update dependency markdown to v3.5.2
  ([`7c2c0c4`](https://github.com/MartinBernstorff/Memium/commit/7c2c0c45f2938701b377144b99127f461d89fe82))

- **deps**: Update dependency sentry-sdk to v1.39.2
  ([`9159fec`](https://github.com/MartinBernstorff/Memium/commit/9159fec58de91091e92dc7c2c58fb4aa6ffd16d0))

- **deps**: Update dependency unidecode to v1.3.8
  ([`59b5add`](https://github.com/MartinBernstorff/Memium/commit/59b5addf89e500f59a5ab8a15ff416cb204a7440))

- **deps**: Update python-semantic-release/python-semantic-release action to v8.7.2
  ([`66341e5`](https://github.com/MartinBernstorff/Memium/commit/66341e56aa17eb6793edbc331cfc3a5051c386c8))

### Features

- Add table parser
  ([`dc3fac7`](https://github.com/MartinBernstorff/Memium/commit/dc3fac74bee7c60e2560754c050b028a6a663993))

- Table parser ([#531](https://github.com/MartinBernstorff/Memium/pull/531),
  [`8c0d109`](https://github.com/MartinBernstorff/Memium/commit/8c0d109fd745c995ca521f172c91395e03dccd3c))


## v0.11.0 (2024-01-03)

### Documentation

- Recommend naming memium container ([#521](https://github.com/MartinBernstorff/Memium/pull/521),
  [`d71ab7f`](https://github.com/MartinBernstorff/Memium/commit/d71ab7f3969c21e6b408f5febb5c7179e9af621a))

### Features

- Add delays before erroring
  ([`9ef8e6c`](https://github.com/MartinBernstorff/Memium/commit/9ef8e6cb3544b6fa4c0723af22802f3efa408155))

Fixes #522

- Add delays before erroring
  ([`869d2a8`](https://github.com/MartinBernstorff/Memium/commit/869d2a86a27c233623cda3801bc3379cbbc2b5e5))

Fixes #522

- Add delays before erroring ([#523](https://github.com/MartinBernstorff/Memium/pull/523),
  [`610aad2`](https://github.com/MartinBernstorff/Memium/commit/610aad2bfeeadb347c6c7691b6b104afdda264e9))

feat: add delays before erroring

Fixes #522


## v0.10.3 (2024-01-03)

### Bug Fixes

- Improve content-extraction for scheduling uuid detection
  ([`4acfd59`](https://github.com/MartinBernstorff/Memium/commit/4acfd598ddf12df573f5151e6e3374209f91bf1c))

Fixes #519

- Improve content-extraction for scheduling uuid detection
  ([#520](https://github.com/MartinBernstorff/Memium/pull/520),
  [`b0ac0ce`](https://github.com/MartinBernstorff/Memium/commit/b0ac0cef0c047324cfa418ced7654f60006df670))

fix: improve content-extraction for scheduling uuid detection

Fixes #519

misc.

- Only remove list markup if at beginning of line
  ([`a112e11`](https://github.com/MartinBernstorff/Memium/commit/a112e1187f5898f8d55d86a279a27c770f3561fe))


## v0.10.2 (2024-01-03)

### Bug Fixes

- Handle unicode encoding for uids
  ([`94b4c7f`](https://github.com/MartinBernstorff/Memium/commit/94b4c7fb389692b8267454fa72c4ba8ef92242c7))

- Unicode encoding for uuids ([#518](https://github.com/MartinBernstorff/Memium/pull/518),
  [`2415f6a`](https://github.com/MartinBernstorff/Memium/commit/2415f6a4707625b3d10e29b1a60c7932b8ceee3b))

fix: Å encoding

Fixes #517

fix: handle unicode encoding for uids

- Å encoding
  ([`edba7e0`](https://github.com/MartinBernstorff/Memium/commit/edba7e04687902990b108d8d95d9c5e26d820bae))

Fixes #517


## v0.10.1 (2024-01-03)

### Bug Fixes

- Deduplicate prompts on extraction
  ([`8f6cd54`](https://github.com/MartinBernstorff/Memium/commit/8f6cd5495891cdabfb22a6b848e32282370c425b))

- Deduplicate prompts on extraction ([#516](https://github.com/MartinBernstorff/Memium/pull/516),
  [`cb1592b`](https://github.com/MartinBernstorff/Memium/commit/cb1592b4aa307946ad99ef432c368a7db15fb60d))

fix: handle duplicate prompts

Fixes #512

fix: deduplicate prompts on extraction

- Handle duplicate prompts
  ([`683955a`](https://github.com/MartinBernstorff/Memium/commit/683955aa9261f3cdf19c2d326e5854966cf1af7a))

Fixes #512

### Code Style

- Lint
  ([`9bb033d`](https://github.com/MartinBernstorff/Memium/commit/9bb033d2f686d2f13ad58972d1efc2b6a39a5fd5))

### Refactoring

- Easier hash debugging
  ([`ff2e8c7`](https://github.com/MartinBernstorff/Memium/commit/ff2e8c782a5abc9ce13afbc5ab3b7bb66abcec08))

Fixes #513

- Easier hash debugging
  ([`1b89c23`](https://github.com/MartinBernstorff/Memium/commit/1b89c2331e39cfde8a6626963a60a34df17b81be))

Fixes #513

- Easier hash debugging ([#514](https://github.com/MartinBernstorff/Memium/pull/514),
  [`5b03293`](https://github.com/MartinBernstorff/Memium/commit/5b03293d55d702eda97709750c410ca014477c9d))

refactor: easier hash debugging

Fixes #513

misc.


## v0.10.0 (2024-01-03)

### Continuous Integration

- Fix docker tag
  ([`3abf5b4`](https://github.com/MartinBernstorff/Memium/commit/3abf5b47074335216bdddb01b303d8da2b11eac9))

- No need to manually specify latest tag
  ([`b71247c`](https://github.com/MartinBernstorff/Memium/commit/b71247cb91b10db88ce417cd0bf8ab4dc79d16a7))

### Features

- Update tag
  ([`84c845b`](https://github.com/MartinBernstorff/Memium/commit/84c845bf7964d329c872b767c7cc47ae098ef9bf))


## v0.9.0 (2024-01-03)

### Continuous Integration

- Push docker image with version tag
  ([`cab954e`](https://github.com/MartinBernstorff/Memium/commit/cab954e8a90370507eb73eb901991589cf89b7ff))

Fixes #509

- Push docker image with version tag
  ([`e77d102`](https://github.com/MartinBernstorff/Memium/commit/e77d10217bc58e350e82916ff1b9246b70e41430))

Fixes #509

- Push docker image with version tag ([#510](https://github.com/MartinBernstorff/Memium/pull/510),
  [`5b37eda`](https://github.com/MartinBernstorff/Memium/commit/5b37edabed3e0c4f045b9f4fa561fba5a6a1fd0d))

ci: push docker image with version tag

Fixes #509

### Features

- Update tag
  ([`ec0c75c`](https://github.com/MartinBernstorff/Memium/commit/ec0c75c9ee9dcad4c8676bc686174b7a84257925))


## v0.8.4 (2024-01-03)

### Bug Fixes

- Ankiconnect uuid handling ([#506](https://github.com/MartinBernstorff/Memium/pull/506),
  [`112a7f1`](https://github.com/MartinBernstorff/Memium/commit/112a7f126c7d2f3b05fdd941d4885e2d9d49fb91))

refactor: What is the AnkiPrompt UUID used for?

Fixes #504

refactor: clarify anki uuid usage

- Tests
  ([`4069335`](https://github.com/MartinBernstorff/Memium/commit/406933579f4d4746ae2d9bdd3603c2cbb87e9142))

### Refactoring

- Clarify anki uuid usage
  ([`146bd44`](https://github.com/MartinBernstorff/Memium/commit/146bd44baa5d026c716498181b8c9e1280105c0c))

- What is the AnkiPrompt UUID used for?
  ([`3d79f93`](https://github.com/MartinBernstorff/Memium/commit/3d79f93eba858f12495fa8212f9da93c017e019a))

Fixes #504


## v0.8.3 (2024-01-03)

### Bug Fixes

- Ankiconnect sync does not appear idempotent
  ([`1cba106`](https://github.com/MartinBernstorff/Memium/commit/1cba106630f9f5fd2fde046296dc943254cdbc57))

Fixes #503

- Ankiconnect sync does not appear idempotent
  ([#505](https://github.com/MartinBernstorff/Memium/pull/505),
  [`afe06ba`](https://github.com/MartinBernstorff/Memium/commit/afe06baca3d1cd09a0e3487bd10a68420e7041c9))

fix: AnkiConnect sync does not appear idempotent

Fixes #503

refactor: pure-ish functions for ankiconverter

fix: apply the html cleaner

- Apply the html cleaner
  ([`9aa0aaa`](https://github.com/MartinBernstorff/Memium/commit/9aa0aaaf23f909225a87d33a05d53a1b07f10d6b))

### Chores

- **deps**: Update dependency dev/pyright to v1.1.344
  ([`8519b4f`](https://github.com/MartinBernstorff/Memium/commit/8519b4fc8dd823608888c3f77501219b2119c0b1))

- **deps**: Update dependency dev/ruff to v0.1.10
  ([`d491d3f`](https://github.com/MartinBernstorff/Memium/commit/d491d3f1ac75ec4aed2e7fc2e5c8fd0788fcf1a4))

- **deps**: Update dependency dev/ruff to v0.1.11
  ([`6fee03d`](https://github.com/MartinBernstorff/Memium/commit/6fee03d4fe2fc7f00aae79eec26eee5a70dd37e7))

- **deps**: Update dependency functionalpy to v0.15.0
  ([`937b6db`](https://github.com/MartinBernstorff/Memium/commit/937b6dbcb515237f660abc4879abe210c0d4b7f9))

- **deps**: Update dependency tests/pytest to v7.4.4
  ([`4f716ae`](https://github.com/MartinBernstorff/Memium/commit/4f716aec3dc662913c2a0e72503759e2409f2269))

### Refactoring

- Pure-ish functions for ankiconverter
  ([`ac82416`](https://github.com/MartinBernstorff/Memium/commit/ac82416fa2d834314d069cd30db53d14b37e174e))


## v0.8.2 (2023-12-27)

### Bug Fixes

- False positives on brackets
  ([`b2b656b`](https://github.com/MartinBernstorff/Memium/commit/b2b656be603a1af31c78b3e7a399190116482d0f))

Fixes #495

- False positives on brackets ([#496](https://github.com/MartinBernstorff/Memium/pull/496),
  [`5606322`](https://github.com/MartinBernstorff/Memium/commit/56063221e2d3e02bf915e460d345d250b93c77f2))

fix: false positives on brackets

Fixes #495

fix: remove entire code blocks

- Remove entire code blocks
  ([`780ec6f`](https://github.com/MartinBernstorff/Memium/commit/780ec6f8f825f93160524211c25ddd4a6870521c))


## v0.8.1 (2023-12-27)

### Bug Fixes

- False positives on cloze for html comments
  ([`2fe2136`](https://github.com/MartinBernstorff/Memium/commit/2fe2136765783749eedea6a4b82ff750b2cff390))

Fixes #492

- False positives on cloze for html comments
  ([#494](https://github.com/MartinBernstorff/Memium/pull/494),
  [`df5ff29`](https://github.com/MartinBernstorff/Memium/commit/df5ff2933f33e06c230253741ed267fb5fdf82cf))

Fixes #492


## v0.8.0 (2023-12-27)

### Continuous Integration

- Fix smoketest permissions
  ([`a36bbd3`](https://github.com/MartinBernstorff/Memium/commit/a36bbd3b05addc03c9a6ae6a0baf866fade89cfe))

Fixes #481

- Fix smoketest permissions
  ([`9c6fc8e`](https://github.com/MartinBernstorff/Memium/commit/9c6fc8e6c03243242157665ea11307e2a744e4ec))

Fixes #481

- Fix smoketest permissions ([#482](https://github.com/MartinBernstorff/Memium/pull/482),
  [`056a6e0`](https://github.com/MartinBernstorff/Memium/commit/056a6e058b439e34f92e4bc2e55c1932b7ae7947))

ci: fix smoketest permissions

Fixes #481

- Smoketests don't need ghcr
  ([`927668c`](https://github.com/MartinBernstorff/Memium/commit/927668cc2dbfc8fd15be82e8d387f9a7113a013b))

### Features

- Handle wikilinks
  ([`18023f6`](https://github.com/MartinBernstorff/Memium/commit/18023f631ac3acba9745961d6aca1c5a6bf393bf))

Fixes #485

- Handle wikilinks
  ([`19355d8`](https://github.com/MartinBernstorff/Memium/commit/19355d89805d2fd50c3e13ec63e02a61c6610fec))

Fixes #485

- Handle wikilinks and aliases ([#487](https://github.com/MartinBernstorff/Memium/pull/487),
  [`1c5dff5`](https://github.com/MartinBernstorff/Memium/commit/1c5dff5065dc784539c5af0359e1aa167fa9b5b5))

feat: handle wikilinks

Fixes #485 and fixes #486.


## v0.7.1 (2023-12-27)

### Bug Fixes

- Cli entrypoint
  ([`c7edcb3`](https://github.com/MartinBernstorff/Memium/commit/c7edcb3c61ce29abcf24b98aca459e1050b1c25b))

- Type errors
  ([`725f3d3`](https://github.com/MartinBernstorff/Memium/commit/725f3d380f8767cc307a28e12355bff0987eb803))

### Refactoring

- Misc. ([#480](https://github.com/MartinBernstorff/Memium/pull/480),
  [`907ab9f`](https://github.com/MartinBernstorff/Memium/commit/907ab9f544c40e249ad5ce6ffe412a26aabceacc))


## v0.7.0 (2023-12-27)

### Bug Fixes

- Anki subdecks are not used
  ([`4762a48`](https://github.com/MartinBernstorff/Memium/commit/4762a481695947508937e11cb7470779889acfb2))

- Anki subdecks are not used
  ([`3c71336`](https://github.com/MartinBernstorff/Memium/commit/3c713366f3400d84766ef8589ba488d4e178ec5a))

- Anki subdecks are not used ([#400](https://github.com/MartinBernstorff/Memium/pull/400),
  [`0aa8473`](https://github.com/MartinBernstorff/Memium/commit/0aa84734c4f855ff17c03cbbe1afce4c27b2047b))

fix: anki subdecks are not used

fix: use anki subdecks

- Anki subdecks are not used ([#404](https://github.com/MartinBernstorff/Memium/pull/404),
  [`7ca3781`](https://github.com/MartinBernstorff/Memium/commit/7ca3781c10bdee78b4773cb610fcf3763f1a3b99))

fix: anki subdecks are not used

Fixes #396

tests: ensure ankiconnect gets correct subdecks

fix: extract all tags from markdown documents

fix: tag strings should not contain "#"

fix: import all decks

feat: support arbitrary subdeck nesting

- Anki tags are not added
  ([`27432d1`](https://github.com/MartinBernstorff/Memium/commit/27432d194e52732a57237ba913e9a140b84d471a))

- Anki tags are not added ([#398](https://github.com/MartinBernstorff/Memium/pull/398),
  [`5e05ab5`](https://github.com/MartinBernstorff/Memium/commit/5e05ab5ac31cad478d4674655e3dbb941649aac6))

fix: anki tags are not added

feat: implement

misc.

- Append \ to docker command
  ([`2778bbb`](https://github.com/MartinBernstorff/Memium/commit/2778bbbb2465a9f142e82857bca7087b6b3af3e3))

- Create a subdir, so it can never delete an existing dir
  ([`0978523`](https://github.com/MartinBernstorff/Memium/commit/0978523972239e54064be61c0c6e15fea9690bfa))

- Do not delete entire dir
  ([`9dc5bef`](https://github.com/MartinBernstorff/Memium/commit/9dc5beffc0a3501e5f6006da925ed0a577a1f278))

- Extract all tags from markdown documents
  ([`9ab65fa`](https://github.com/MartinBernstorff/Memium/commit/9ab65fa34217c6c99cbdcc9844f9c359c0a5d9f8))

- Import all decks
  ([`dda73bd`](https://github.com/MartinBernstorff/Memium/commit/dda73bd8e9b670a274e43b3d86ccefd75e71089b))

- Imports
  ([`3244f6e`](https://github.com/MartinBernstorff/Memium/commit/3244f6ee4a7c303b97672e2dc086a62223f5ef0f))

- Inherit from protocol ([#287](https://github.com/MartinBernstorff/Memium/pull/287),
  [`6e2862f`](https://github.com/MartinBernstorff/Memium/commit/6e2862f8b1b1ab7ccc528c503479f01f2f8028f3))

- Only update unique models
  ([`cfbae0e`](https://github.com/MartinBernstorff/Memium/commit/cfbae0e6364a6ef28af20f6a30c4df35591c0785))

- Promptid to NoteID mapping
  ([`2f981b1`](https://github.com/MartinBernstorff/Memium/commit/2f981b1313689201e7ed539ea1a1a3f5618f6514))

Fixes #284

- Qa uuid should include answer
  ([`9cc2991`](https://github.com/MartinBernstorff/Memium/commit/9cc29910f572b9663993483a384b7e0193e00a11))

Fixes #346

- Readme casing
  ([`35828d5`](https://github.com/MartinBernstorff/Memium/commit/35828d56a6bfae18f84cd1ae7fe8034643d8ed3a))

- Release flow
  ([`e6def83`](https://github.com/MartinBernstorff/Memium/commit/e6def83a9d0d5b351895a4846b1ec937d5bc1de8))

Fixes #465

- Release flow
  ([`0db976e`](https://github.com/MartinBernstorff/Memium/commit/0db976e0183b36576a4457a81d23d0e3e65dfda4))

Fixes #465

- Release flow ([#467](https://github.com/MartinBernstorff/Memium/pull/467),
  [`56f6422`](https://github.com/MartinBernstorff/Memium/commit/56f64223a10da8c0cf094b7d9a52de14798a0cb1))

fix: release flow

Fixes #465

major: release to pypi

- Release to pypi ([#475](https://github.com/MartinBernstorff/Memium/pull/475),
  [`199ed12`](https://github.com/MartinBernstorff/Memium/commit/199ed125cc5cddff16a72665bfc36df871979152))

- Smokestest
  ([`da1e4ad`](https://github.com/MartinBernstorff/Memium/commit/da1e4ad4ecd9393153709ed71e600a7427319fcd))

- Smokestest
  ([`b472748`](https://github.com/MartinBernstorff/Memium/commit/b4727483335fb44411790f80fb7bbf94b14d2bd8))

- Smokestest
  ([`fa7c5bb`](https://github.com/MartinBernstorff/Memium/commit/fa7c5bb53bd7cb6775349c07fa1fee61522e8964))

- Submit entire stack
  ([`1b37e1b`](https://github.com/MartinBernstorff/Memium/commit/1b37e1bb6d7cb5c55b9c7c816798bc6370d0779e))

- Tag strings should not contain "#"
  ([`5a220ff`](https://github.com/MartinBernstorff/Memium/commit/5a220ff2543ed582c30f90418f67915b005ac4a7))

- Use anki subdecks
  ([`7fc378e`](https://github.com/MartinBernstorff/Memium/commit/7fc378eebd3539831b3c058a1549f0ae4f618eb9))

- Use answer when generating hash for QA
  ([`2919d77`](https://github.com/MartinBernstorff/Memium/commit/2919d7766005a00bc264ca654ef3bc6d13e6d48a))

- Use answer when generating hash for QA
  ([#399](https://github.com/MartinBernstorff/Memium/pull/399),
  [`3345bff`](https://github.com/MartinBernstorff/Memium/commit/3345bff7b27135ad903d7886108ba6a941e7fc78))

- Use correct id for remote sync
  ([`526480b`](https://github.com/MartinBernstorff/Memium/commit/526480becd316737871ca871dcb8b2349f2eaef0))

- Use invoke on devcontainer.json
  ([`3adb865`](https://github.com/MartinBernstorff/Memium/commit/3adb86501b98ab291abfa4c8d1fe3d106f5ded95))

- Use localhost for ANKICONNECT_URL if not on docker
  ([`045eaa4`](https://github.com/MartinBernstorff/Memium/commit/045eaa414d4b8ef634a0f0cf331251bee41bcbff))

- Use remote id for sync ([#334](https://github.com/MartinBernstorff/Memium/pull/334),
  [`b3e98f5`](https://github.com/MartinBernstorff/Memium/commit/b3e98f5026313cf4290fcb78aae14d46db70d5b6))

### Chores

- Cleanup ([#476](https://github.com/MartinBernstorff/Memium/pull/476),
  [`c064b68`](https://github.com/MartinBernstorff/Memium/commit/c064b68c5a929ad3400665b67fe0e3dfcd840f45))

- Configure Renovate ([#368](https://github.com/MartinBernstorff/Memium/pull/368),
  [`d9fa9c0`](https://github.com/MartinBernstorff/Memium/commit/d9fa9c0f05fe9e17d1e0d7efe133f3ba925bf9ef))

Fixes #260.

- **deps**: Update actions/checkout action to v4
  ([`b15c5d6`](https://github.com/MartinBernstorff/Memium/commit/b15c5d6c70d802504db4111dd519c587030acb82))

- **deps**: Update actions/setup-python action to v5
  ([`45a6637`](https://github.com/MartinBernstorff/Memium/commit/45a663750576c6885403a11cb7038f6bfa9a677e))

- **deps**: Update actions/stale action to v9
  ([`e5967b0`](https://github.com/MartinBernstorff/Memium/commit/e5967b06f4b7314e4ece77327bd3214af1f7b69b))

- **deps**: Update dependency dev/pre-commit to v2.21.0
  ([`02eb2cc`](https://github.com/MartinBernstorff/Memium/commit/02eb2cca0fef89e9fda62a16386f1e1a8fe78de9))

- **deps**: Update dependency dev/pre-commit to v3
  ([`f506653`](https://github.com/MartinBernstorff/Memium/commit/f5066538bb066327be10e384718676836a5c6bb8))

- **deps**: Update dependency dev/pyright to v1.1.341
  ([`8466592`](https://github.com/MartinBernstorff/Memium/commit/84665922ab7c8341c4239cec8e7f0b413f4c052a))

- **deps**: Update dependency dev/pyright to v1.1.342
  ([`cf5a8b1`](https://github.com/MartinBernstorff/Memium/commit/cf5a8b16e8a87727730cff04dc2678c6fcac4b73))

- **deps**: Update dependency dev/pyright to v1.1.343
  ([`a2dbeb6`](https://github.com/MartinBernstorff/Memium/commit/a2dbeb6137026e5e836040921321837570c262dd))

- **deps**: Update dependency dev/ruff to v0.1.8
  ([`e670f8e`](https://github.com/MartinBernstorff/Memium/commit/e670f8e07459afe2e02ad5a8d609557c7e5f78ba))

- **deps**: Update dependency dev/ruff to v0.1.9
  ([`b69d658`](https://github.com/MartinBernstorff/Memium/commit/b69d6584163869ab9c63393d658d76863faf9180))

- **deps**: Update dependency genanki to v0.13.1
  ([`abf835a`](https://github.com/MartinBernstorff/Memium/commit/abf835a61a0b2de54615c69528a73c774a3fd16b))

- **deps**: Update dependency pydantic to v2.5.3
  ([`11a85a9`](https://github.com/MartinBernstorff/Memium/commit/11a85a9b6bfbecf1bb5c2753dfcc4dfafaf5a54f))

- **deps**: Update dependency sentry-sdk to v1.39.1
  ([`ff95683`](https://github.com/MartinBernstorff/Memium/commit/ff95683807d6e200b8a0dd11aa44b58b6b2c9760))

- **deps**: Update dependency tests/diff-cover to v8.0.2
  ([`a4512f8`](https://github.com/MartinBernstorff/Memium/commit/a4512f827d75570fac95ecfb11e2007dba45c59a))

- **deps**: Update dependency tests/pytest to v7.4.3
  ([`acf432a`](https://github.com/MartinBernstorff/Memium/commit/acf432a8ade8c61c6a1e3612d85e1f974135b606))

- **deps**: Update dependency tests/pytest-xdist to v3.5.0
  ([`2d97f73`](https://github.com/MartinBernstorff/Memium/commit/2d97f73a23dd91791d1efa58655ba89e7b0a0c7a))

- **deps**: Update docker/login-action action to v3
  ([`8e76a16`](https://github.com/MartinBernstorff/Memium/commit/8e76a16e3aee608294ac25269edf1850c409ed7b))

- **deps**: Update python docker tag to v3.12
  ([`e50a018`](https://github.com/MartinBernstorff/Memium/commit/e50a018da3525a0a812a6c5242e1813d4f66ee7d))

- **deps**: Update python-semantic-release/python-semantic-release action to v8.5.1
  ([`ff53391`](https://github.com/MartinBernstorff/Memium/commit/ff53391d9bfabc36a76fb9b46189730a5fc81ff9))

- **deps**: Update python-semantic-release/python-semantic-release action to v8.5.2
  ([`6e6496b`](https://github.com/MartinBernstorff/Memium/commit/6e6496bc5cc14b83a54c2272352b8fa456a0306f))

- **deps**: Update python-semantic-release/python-semantic-release action to v8.7.0
  ([`3d4b538`](https://github.com/MartinBernstorff/Memium/commit/3d4b538212c079097878b5ab16e1623d3b6c6fae))

### Code Style

- Lint
  ([`e5f11a9`](https://github.com/MartinBernstorff/Memium/commit/e5f11a9d3706f378d1d8f95da0bb63797f08ddba))

- Linting
  ([`554fedc`](https://github.com/MartinBernstorff/Memium/commit/554fedc7e2c73761fcfaabc855bd67a604d60d01))

### Continuous Integration

- Add automerge
  ([`5f15b7d`](https://github.com/MartinBernstorff/Memium/commit/5f15b7d02404071218deb8917ea9017f8b037a80))

- Add codecov ([#199](https://github.com/MartinBernstorff/Memium/pull/199),
  [`4d546d4`](https://github.com/MartinBernstorff/Memium/commit/4d546d473228c7977b3843c028fb72092e1ce48e))

- Add manual trigger to release
  ([`32470a5`](https://github.com/MartinBernstorff/Memium/commit/32470a5f24ce24bfe6f37ead8b9aff7ae0141874))

- Clean up
  ([`8ad85f1`](https://github.com/MartinBernstorff/Memium/commit/8ad85f101a4b7b04019bfb4ded226867d82e6e07))

- Correct path to docker smoketest
  ([`ee50f34`](https://github.com/MartinBernstorff/Memium/commit/ee50f34ccd2977c7af4a36a86c3a1eca629fa2e7))

Fixes #343

- Release override permissions ([#479](https://github.com/MartinBernstorff/Memium/pull/479),
  [`975630d`](https://github.com/MartinBernstorff/Memium/commit/975630d2bd7efd5b53d4397a70ebd8bd3c93475f))

- Release to memium on pypi
  ([`b8fdb6b`](https://github.com/MartinBernstorff/Memium/commit/b8fdb6ba563aa2ba009fa41ad44f2c56bb4efb6b))

Fixes #455

- Remove codecov
  ([`8d7f9d7`](https://github.com/MartinBernstorff/Memium/commit/8d7f9d7a10ff88836fe05ccd9ae10ea5290727ba))

- Remove codecov ([#283](https://github.com/MartinBernstorff/Memium/pull/283),
  [`b65cb11`](https://github.com/MartinBernstorff/Memium/commit/b65cb11e6681ef895548ee1727aa00754c5a3685))

- Remove dependabot
  ([`e2e0721`](https://github.com/MartinBernstorff/Memium/commit/e2e07211b5c1a497aa3ac2253dc7dcf06ae22705))

- Remove github release ([#477](https://github.com/MartinBernstorff/Memium/pull/477),
  [`941f587`](https://github.com/MartinBernstorff/Memium/commit/941f587455531f1e4f2d3eeb3cfcc9e946d582f8))

- Typo in release.yml
  ([`72c7a08`](https://github.com/MartinBernstorff/Memium/commit/72c7a0896aea44d431dd4dfc8eb21364d885109c))

- Update
  ([`75b3f22`](https://github.com/MartinBernstorff/Memium/commit/75b3f22e5e4fa38c2fb86f80c8a34829b4d31116))

- Update
  ([`126f81a`](https://github.com/MartinBernstorff/Memium/commit/126f81a2f3b413e923413ccaa4717af5acaa3352))

- Update ref groups.
  ([`a18ccaa`](https://github.com/MartinBernstorff/Memium/commit/a18ccaa5b8f76654aa8db9fd7a8ce02b6a4d2744))

Fixes #446

- Update ref groups. ([#447](https://github.com/MartinBernstorff/Memium/pull/447),
  [`1387d00`](https://github.com/MartinBernstorff/Memium/commit/1387d00a319f04961a448e19d91acd09b9245453))

ci: update ref groups.

Fixes #446

implement

- Update release token
  ([`b4f1f2e`](https://github.com/MartinBernstorff/Memium/commit/b4f1f2e6b8bc0ca76dedefeff587b981ffc3877b))

- Use invoke
  ([`ca61482`](https://github.com/MartinBernstorff/Memium/commit/ca614829284d0d9db7b410beb23191726025cd0b))

### Documentation

- Update readme
  ([`adb5527`](https://github.com/MartinBernstorff/Memium/commit/adb552751f0198092f9ff1df41b2c7bc2b423069))

Fixes #462

- Update readme ([#466](https://github.com/MartinBernstorff/Memium/pull/466),
  [`01aa23d`](https://github.com/MartinBernstorff/Memium/commit/01aa23d51813436bf23b849c779484b29813a9e0))

docs: update readme

Fixes #462

misc.

- Use ghcr in readme for docker image
  ([`04229f1`](https://github.com/MartinBernstorff/Memium/commit/04229f16d4363f63e0e28cbd5c0355f9cc9cbd93))

Fixes #470

- Use ghcr in readme for docker image
  ([`0b3f810`](https://github.com/MartinBernstorff/Memium/commit/0b3f810d815c7f22a23fc1d2b3df1e78f2b9b578))

Fixes #470

- Use ghcr in readme for docker image ([#471](https://github.com/MartinBernstorff/Memium/pull/471),
  [`52cbec6`](https://github.com/MartinBernstorff/Memium/commit/52cbec631a5760fb1f19dff6cd7bc78b54a648b2))

docs: use ghcr in readme for docker image

Fixes #470

misc.

### Features

- Add `push_all` option to CLI ([#439](https://github.com/MartinBernstorff/Memium/pull/439),
  [`bfd76ba`](https://github.com/MartinBernstorff/Memium/commit/bfd76ba4bbb4ad8047c502be750dfdbc076b222d))

feat: update_all option.

Fixes #409

- Add ankiconnect destination get all
  ([`60f52d8`](https://github.com/MartinBernstorff/Memium/commit/60f52d8a3b2320bdce0ecfd28bb21e64ba8cda09))

- Add diffdeterminer
  ([`9d708f2`](https://github.com/MartinBernstorff/Memium/commit/9d708f2928af270c53e06f3ca285c8ff588f899e))

- Add dry-run
  ([`ccde648`](https://github.com/MartinBernstorff/Memium/commit/ccde648621495d3b42f082559a62a31413fd3126))

Fixes #336

- Add markdown ingester
  ([`728de65`](https://github.com/MartinBernstorff/Memium/commit/728de65c47bd722bfdeb247dd54f8520d652e1d2))

- Add optional arguments to cli
  ([`e20142a`](https://github.com/MartinBernstorff/Memium/commit/e20142a8bb38283fc073a08197ae7d1156f4a7ef))

- Add optional arguments to cli ([#422](https://github.com/MartinBernstorff/Memium/pull/422),
  [`bec9363`](https://github.com/MartinBernstorff/Memium/commit/bec93639b68be0687fc027bb78ff0f813aab16fc))

feat: add optional arguments to cli

misc.

- Add remoteid and use for prompt deletion
  ([`3c47d7e`](https://github.com/MartinBernstorff/Memium/commit/3c47d7ee4cdff588a4f654d15c62bb2580ea74b2))

Fixes #321

- Add sentry_dsn flag which enables/disables sentry.
  ([`9c45c7b`](https://github.com/MartinBernstorff/Memium/commit/9c45c7b9192eff0fbb0ee9d8eb3491f20d04056e))

Fixes #421

- Add sentry_dsn flag which enables/disables sentry.
  ([`6db2467`](https://github.com/MartinBernstorff/Memium/commit/6db2467ce812ea6edae63ea0ab158c07e7ee293b))

Fixes #421

- Add sentry_dsn flag which enables/disables sentry.
  ([#437](https://github.com/MartinBernstorff/Memium/pull/437),
  [`7e001cf`](https://github.com/MartinBernstorff/Memium/commit/7e001cfc10b6a9d3a4a04ccf7f436d3204dbe91e))

feat: add sentry_dsn flag which enables/disables sentry.

Fixes #421

- Anki `prompts_to_cards` ([#288](https://github.com/MartinBernstorff/Memium/pull/288),
  [`d9fd7aa`](https://github.com/MartinBernstorff/Memium/commit/d9fd7aa0549afeaade55cb3c873cfc5d2755f138))

- Ankiconnect destination `get_all_prompts`
  ([#286](https://github.com/MartinBernstorff/Memium/pull/286),
  [`3184006`](https://github.com/MartinBernstorff/Memium/commit/31840062f2f4612beca2db83109fcdad852f2972))

- Ankiconnect support delete notes ([#285](https://github.com/MartinBernstorff/Memium/pull/285),
  [`99b507a`](https://github.com/MartinBernstorff/Memium/commit/99b507a646ec4d6447aa236312b4c6ed8a6d77ec))

- Change document ingestion to best-effort
  ([`5b4401c`](https://github.com/MartinBernstorff/Memium/commit/5b4401c67251be967a81092c4f64cb09b4d48bf6))

- Change document ingestion to best-effort
  ([#416](https://github.com/MartinBernstorff/Memium/pull/416),
  [`bbe1196`](https://github.com/MartinBernstorff/Memium/commit/bbe1196d1f0197d967e377f86cf17d367bf61fc1))

feat: change document ingestion to best-effort

feat: implement

- Fail with user friendly error if ankiconnect is not live
  ([`e489e2f`](https://github.com/MartinBernstorff/Memium/commit/e489e2ff2dd5d09c0b87692ef963dbe59997290b))

- Finalise push on `AnkiConnectPromptDestination`
  ([#289](https://github.com/MartinBernstorff/Memium/pull/289),
  [`8edeee7`](https://github.com/MartinBernstorff/Memium/commit/8edeee7e1e400496c83224ac916f1b012f025e60))

- First run on v2 ([#397](https://github.com/MartinBernstorff/Memium/pull/397),
  [`49d0501`](https://github.com/MartinBernstorff/Memium/commit/49d0501d2fca55c773c5ffb374d5a4aee982f5c5))

fix: only update unique models Fixes #315

dev: add run cli launch option

fix: use localhost for ANKICONNECT_URL if not on docker

misc: formatting

- If n+ notes are scheduled for deletion, do not sync
  ([`0915e7f`](https://github.com/MartinBernstorff/Memium/commit/0915e7fa56f2de747f1f0ded1667203058ad2d6b))

Fixes #251

- Implement
  ([`bb00c4c`](https://github.com/MartinBernstorff/Memium/commit/bb00c4c0ad55e58d06d1709fbf181c6e92d47cc4))

- Implement
  ([`10eecf4`](https://github.com/MartinBernstorff/Memium/commit/10eecf49e1d832ac8cea012250953328040cdbd3))

- Implement ClozeExtractor
  ([`a9afe36`](https://github.com/MartinBernstorff/Memium/commit/a9afe36c9b6530dc8fd97f9d5577c5dee93c2c1c))

Fixes #297

- Implement diffdeterminer
  ([`174add1`](https://github.com/MartinBernstorff/Memium/commit/174add194efb4d57de0e0627a9bfc24e15a318fb))

Fixes #292 Add GeneralSyncer

- Implement QA extractor
  ([`aa7079c`](https://github.com/MartinBernstorff/Memium/commit/aa7079c815e892f3ba3c1b5adcd628b9b4dd07f0))

Fixes #294

- Implement sleep for ankiconnectdestination
  ([`2204f4d`](https://github.com/MartinBernstorff/Memium/commit/2204f4dcd21608adb485b627a21d297a693bc0ce))

- Make `pipx` installable.
  ([`540588a`](https://github.com/MartinBernstorff/Memium/commit/540588a38ca7e7b735ca63b865fc1ad281b79bff))

Fixes #413

- Make `pipx` installable. ([#441](https://github.com/MartinBernstorff/Memium/pull/441),
  [`61c397d`](https://github.com/MartinBernstorff/Memium/commit/61c397dcacfd567bd005f1e9d76fb3e786e6ab50))

Fixes #413

- Polish cli
  ([`bd11c10`](https://github.com/MartinBernstorff/Memium/commit/bd11c108c9114042958de7b313802891c127c9f7))

Fixes #338

- Raise error if input dir is not writeable
  ([`883f16e`](https://github.com/MartinBernstorff/Memium/commit/883f16eae653bd58d33445a3ba92b7636b6f9ed6))

Fixes #473

- Raise error if input dir is not writeable
  ([`f837faa`](https://github.com/MartinBernstorff/Memium/commit/f837faa25f6e2299b964c1211ef97683f23554cf))

Fixes #473

- Raise error if input dir is not writeable
  ([#474](https://github.com/MartinBernstorff/Memium/pull/474),
  [`4f0ea80`](https://github.com/MartinBernstorff/Memium/commit/4f0ea807b017ce99d018dbcf9404411cdbbe672d))

feat: raise error if input dir is not writeable

Fixes #473

- Remove temp dir from cli interface. Fixes #374
  ([`a07738a`](https://github.com/MartinBernstorff/Memium/commit/a07738acb86da80c94b5eba9bf8b73f4ba0b71e5))

- Remove temp dir from cli interface. Fixes #374
  ([#428](https://github.com/MartinBernstorff/Memium/pull/428),
  [`cb6c95c`](https://github.com/MartinBernstorff/Memium/commit/cb6c95cc7f3a13d32da107f1d26b9fe599d79421))

feat: remove temp dir from cli interface. Fixes #374

misc.

- Rename to memium ([#448](https://github.com/MartinBernstorff/Memium/pull/448),
  [`41fbe4a`](https://github.com/MartinBernstorff/Memium/commit/41fbe4aefc57bd677543c985f44994ac644371bc))

feat: rename to memium.

Fixes #419

implement

- Rename to memium.
  ([`fb02dc2`](https://github.com/MartinBernstorff/Memium/commit/fb02dc27c435369766b2db19c256b5f1bdfc5c53))

Fixes #419

- Set max_wait_seconds for ankiconnect destination
  ([`da53a73`](https://github.com/MartinBernstorff/Memium/commit/da53a7313577d971055cef731f7d8c238e7a54de))

- Stub out `main` for cli in v2 ([#291](https://github.com/MartinBernstorff/Memium/pull/291),
  [`f2b4cf0`](https://github.com/MartinBernstorff/Memium/commit/f2b4cf05cc0595fa1837cc8e57d60671ae001fb4))

- Stub out ankiconnect destination ([#282](https://github.com/MartinBernstorff/Memium/pull/282),
  [`7de7bec`](https://github.com/MartinBernstorff/Memium/commit/7de7beccec96a655c271b456e2340006bbd064ff))

- Stub out main cli v2
  ([`24954c7`](https://github.com/MartinBernstorff/Memium/commit/24954c72dc1d7a720b2c6080da40aefa85145bd8))

- Stub out main cli v2
  ([`79f2d09`](https://github.com/MartinBernstorff/Memium/commit/79f2d098bce415ad0367618790f756aaf5052340))

- Stub out promptsource
  ([`0e2e2f2`](https://github.com/MartinBernstorff/Memium/commit/0e2e2f235c1dad0a3c2112dfe754fe61bf209689))

Fixes #293

- Support arbitrary subdeck nesting
  ([`3ba0c90`](https://github.com/MartinBernstorff/Memium/commit/3ba0c9092fa06a61fbacbb50b7d6fccad438f499))

- Update remote if tags have changed
  ([`e9b06f7`](https://github.com/MartinBernstorff/Memium/commit/e9b06f707b9cce3308471891709d15abaf9ccd87))

- Update remote if tags have changed ([#410](https://github.com/MartinBernstorff/Memium/pull/410),
  [`908ed5e`](https://github.com/MartinBernstorff/Memium/commit/908ed5e4885bb2d4d111a2b550c1f1780012a327))

feat: update remote if tags have changed

misc.

tests: make tests more readable

- Update_all option.
  ([`d6a184f`](https://github.com/MartinBernstorff/Memium/commit/d6a184f73c64e893fe84f5dbd11d5eb9d3d53e25))

Fixes #409

- Use context manager to temp deck file deletion. Fixes #423
  ([`d1c7e3d`](https://github.com/MartinBernstorff/Memium/commit/d1c7e3d83bc6d4fd053114022578d3e869ea906a))

- Use context manager to temp deck file deletion. Fixes #423
  ([#427](https://github.com/MartinBernstorff/Memium/pull/427),
  [`be4999d`](https://github.com/MartinBernstorff/Memium/commit/be4999dca85607781872b67b5014e8297d7c1550))

feat: use context manager to temp deck file deletion. Fixes #423

implement

- Use markdown promptsource
  ([`464d8fa`](https://github.com/MartinBernstorff/Memium/commit/464d8facd83191666f051bd372173447f3d44257))

Fixes #309

- Use v2 when running docker smoketest
  ([`510eb33`](https://github.com/MartinBernstorff/Memium/commit/510eb330886fcb0d4fa191e345f4206b06ef844b))

Fixes #331

### Refactoring

- `int_hash_str` location ([#303](https://github.com/MartinBernstorff/Memium/pull/303),
  [`02eea89`](https://github.com/MartinBernstorff/Memium/commit/02eea8903fba90803a7a7cf321357c8b68c56193))

- Abstract outline
  ([`6fb9675`](https://github.com/MartinBernstorff/Memium/commit/6fb9675533fee3882f2af15694c7cf678636c1f6))

- Decrease file nesting
  ([`15938e1`](https://github.com/MartinBernstorff/Memium/commit/15938e114034a7f7dd4e6a29e28f0d86664c1c0a))

- Decrease file nesting ([#414](https://github.com/MartinBernstorff/Memium/pull/414),
  [`0acd631`](https://github.com/MartinBernstorff/Memium/commit/0acd631b47e69c31ff9f7fda92c62082a60412dd))

refactor: decrease file nesting

Fixes #350

phase 1

fix: imports

style: linting

misc.

- Decrease makefile verbosity ([#212](https://github.com/MartinBernstorff/Memium/pull/212),
  [`464453b`](https://github.com/MartinBernstorff/Memium/commit/464453b72b8f2a414fd2c75f928dd301b77fd8e5))

Auto-created

- Fix import errors after folder restructure
  ([#202](https://github.com/MartinBernstorff/Memium/pull/202),
  [`5680ad9`](https://github.com/MartinBernstorff/Memium/commit/5680ad9663075465f5454b1f34311b349ade30e6))

Auto-created

---------

Co-authored-by: github-actions <github-actions@github.com>

- Get rid of tmp_read_dir and tmp_write_dir
  ([`93116a4`](https://github.com/MartinBernstorff/Memium/commit/93116a4b5cb6384b6e31601ee1c2258f02195575))

Fixes #308

- Minor cleanup ([#290](https://github.com/MartinBernstorff/Memium/pull/290),
  [`2564780`](https://github.com/MartinBernstorff/Memium/commit/2564780d30f2e2ae6dafe1417730948a15c05195))

- Minor cleanup of markdown ingester ([#246](https://github.com/MartinBernstorff/Memium/pull/246),
  [`c542d8e`](https://github.com/MartinBernstorff/Memium/commit/c542d8e3afeb78fd83e012856ca1236f85a3b092))

- Misc
  ([`56fc926`](https://github.com/MartinBernstorff/Memium/commit/56fc9260921aaa1f5c1627f90353414bfd62e30a))

- Move cli to top-level
  ([`e14a694`](https://github.com/MartinBernstorff/Memium/commit/e14a694e23f9d3f0b8c94e3300f41154b78c9ef3))

- Move max wait duration to gateway
  ([`b237169`](https://github.com/MartinBernstorff/Memium/commit/b237169fc65eb76ef6350e6f81f22660c6eb52c4))

- Move things out of globals ([#224](https://github.com/MartinBernstorff/Memium/pull/224),
  [`05a83b6`](https://github.com/MartinBernstorff/Memium/commit/05a83b6cf07f00e35751c8a796e60af067845984))

Auto-created

- Move v2 to top level
  ([`8afcb5a`](https://github.com/MartinBernstorff/Memium/commit/8afcb5adfc62017c1f6bfc7ad6287b5eceae22ba))

- Remove makefile
  ([`6c97f96`](https://github.com/MartinBernstorff/Memium/commit/6c97f96e5985957f7d03bd45124541aedeeebaa8))

- Remove tmp_dirs from PushPrompts and `PromptDiffDeterminer`
  ([`9fc4e3e`](https://github.com/MartinBernstorff/Memium/commit/9fc4e3efa9e89c26461795b535309ecfad85f3ac))

Fixes #323

- Remove tmp_dirs from pushprompts and promptdiffdeterminer
  ([`8e80469`](https://github.com/MartinBernstorff/Memium/commit/8e804696b5ddd7832a27c9ebc19caa1b1c313b92))

- Remove top level git
  ([`eff9e9e`](https://github.com/MartinBernstorff/Memium/commit/eff9e9e7f751e0aa8347bbaa2fdecd525a826f07))

- Remove top level git
  ([`a2913b7`](https://github.com/MartinBernstorff/Memium/commit/a2913b73e35af64d18a365dd0456b7bf62fa92de))

- Remove top level git ([#472](https://github.com/MartinBernstorff/Memium/pull/472),
  [`3000b65`](https://github.com/MartinBernstorff/Memium/commit/3000b65fbed633f68ec77779acb92f8c02e64923))

- Remove v1
  ([`3df182b`](https://github.com/MartinBernstorff/Memium/commit/3df182bfee0e03987e4eaf2b07a69fea70d9d416))

Fixes #338

- Remove v1 ([#344](https://github.com/MartinBernstorff/Memium/pull/344),
  [`f1be2d3`](https://github.com/MartinBernstorff/Memium/commit/f1be2d3d814832c581ed1b3358759ef30f408932))

- Renames
  ([`003b523`](https://github.com/MartinBernstorff/Memium/commit/003b5236ef126cb3732cfdf72908a54d24f06547))

- Simplify prompts
  ([`1b4c802`](https://github.com/MartinBernstorff/Memium/commit/1b4c802d8eeaf094ad735ed9a9e663225303c1a9))

- Simplify prompts ([#312](https://github.com/MartinBernstorff/Memium/pull/312),
  [`be6a5db`](https://github.com/MartinBernstorff/Memium/commit/be6a5dbeb787fd9c94ad8c87ec52352a25cdc7d2))

- Simplify tests and remove defaults from extractors
  ([`e259578`](https://github.com/MartinBernstorff/Memium/commit/e2595786ab7b752b1480b5b79307b36eea118817))

Fixes #245

- Split tasks into multiple files
  ([`c533a9e`](https://github.com/MartinBernstorff/Memium/commit/c533a9e4911a4646b608b3ac4d4df501483d873d))

- Sync decks into functional core imperative shell
  ([#270](https://github.com/MartinBernstorff/Memium/pull/270),
  [`80f956d`](https://github.com/MartinBernstorff/Memium/commit/80f956d3f45e5521219190f4a896c0938dddb03c))

- Sync decks into functional core, imperative shell
  ([`32a0e3a`](https://github.com/MartinBernstorff/Memium/commit/32a0e3a54e03c80d1aae9587a6d1f643b8fab52d))

Fixes #240

- Sync decks into functional core, imperative shell
  ([`9e709ff`](https://github.com/MartinBernstorff/Memium/commit/9e709ff93bface18fa2874c440c3dd9614c55ce6))

Fixes #240

- Sync decks into functional core, imperative shell
  ([`562d46f`](https://github.com/MartinBernstorff/Memium/commit/562d46f93d96c3cd0f88ca1d3d17d030317338a0))

Fixes #240

### Testing

- Tags
  ([`f493ed4`](https://github.com/MartinBernstorff/Memium/commit/f493ed492c55766d56c85dcbb633b0de3988032e))


## v0.6.0 (2023-11-18)

### Bug Fixes

- Add mounts points for devcontainer
  ([`c2497ee`](https://github.com/MartinBernstorff/Memium/commit/c2497eeb7a0cc76763d45db4694b1a0c9d6d55ac))

- Do not mount input dir on remote ([#201](https://github.com/MartinBernstorff/Memium/pull/201),
  [`83cedae`](https://github.com/MartinBernstorff/Memium/commit/83cedaeb83c918248d52ad2f09233232761972b6))

Auto-created

### Build System

- Update dockerfile for new dir structure
  ([`0f1e8c0`](https://github.com/MartinBernstorff/Memium/commit/0f1e8c0f3bfbc1610c159ea6e0f0c40cc86bd1b1))

### Continuous Integration

- Add arm64 to deploy
  ([`a6fb2c5`](https://github.com/MartinBernstorff/Memium/commit/a6fb2c58b1ef39ead800263a33b2e56210c8f9dc))

- Fix integration tests with new path ([#200](https://github.com/MartinBernstorff/Memium/pull/200),
  [`b734f9e`](https://github.com/MartinBernstorff/Memium/commit/b734f9ee8f103586cdf7718ae13a50bf9dc5eb12))

Auto-created

- Run docker publish independently of integration test
  ([`d1402c6`](https://github.com/MartinBernstorff/Memium/commit/d1402c6a29d5ef2878ed8342ca237edb5d3b5ae5))

- Run type checks on application script as well
  ([`849c0f5`](https://github.com/MartinBernstorff/Memium/commit/849c0f552ae9ae785bdb515d480dca811f0436ef))

- Setup multiplatform conditions ([#192](https://github.com/MartinBernstorff/Memium/pull/192),
  [`5120b18`](https://github.com/MartinBernstorff/Memium/commit/5120b18685cce3af0930473d8981d5f87e0016c0))

- Update docker build action
  ([`6724cd4`](https://github.com/MartinBernstorff/Memium/commit/6724cd4c6475924d5780420d6446e5d869c82cda))

### Features

- Move cli to separate file
  ([`f91216b`](https://github.com/MartinBernstorff/Memium/commit/f91216b9cf9fdd04eb7227de4b7d497472dc4ccd))

### Refactoring

- Rename pipeline to not hit test
  ([`1b5cbf2`](https://github.com/MartinBernstorff/Memium/commit/1b5cbf2ed84aa1459853cf143509f690ede4ea79))


## v0.5.1 (2023-10-28)

### Bug Fixes

- Docker deploy should be lowercase
  ([`56d0517`](https://github.com/MartinBernstorff/Memium/commit/56d0517da01ba25c950e5c01e13e190fd4bbeabe))


## v0.5.0 (2023-10-28)

### Continuous Integration

- Add docker deploy
  ([`a658f15`](https://github.com/MartinBernstorff/Memium/commit/a658f15e9818449262f123ddc63d6ae64e1b4bbe))

- Build prod image as part of tests
  ([`b595956`](https://github.com/MartinBernstorff/Memium/commit/b59595611de1bc208501cdb09c630d20cfbc7728))

- Make integration test unique
  ([`85753df`](https://github.com/MartinBernstorff/Memium/commit/85753df8d6270f53fa85eaf8496e456e0efb5631))

- Remove unused section
  ([`79bb2d2`](https://github.com/MartinBernstorff/Memium/commit/79bb2d21327e243398ffbe56a17055e9e44f4b10))

- Support multiline comment
  ([`273d2c9`](https://github.com/MartinBernstorff/Memium/commit/273d2c980b67e0b12a52246e1d98e1144cc5111a))

### Documentation

- Update contribution
  ([`a804fc7`](https://github.com/MartinBernstorff/Memium/commit/a804fc7627e330cfa21fc92c0a0c360d0da88175))

- Update readme
  ([`704ae21`](https://github.com/MartinBernstorff/Memium/commit/704ae21840118a826d0e8a4d3ce38e93e8a261fe))

### Features

- Add integration test
  ([`e0526b6`](https://github.com/MartinBernstorff/Memium/commit/e0526b60bfb06f2e0d75d0c52ebb8d1ed5d7966c))

- Add prod docker image
  ([`ed5f350`](https://github.com/MartinBernstorff/Memium/commit/ed5f35099d7d79295726967545b6bce87b0927d2))


## v0.4.0 (2023-10-27)

### Bug Fixes

- Duplicate version toml
  ([`8526eed`](https://github.com/MartinBernstorff/Memium/commit/8526eed202a59021c15b258fcdf422172f7972b7))

### Features

- Add build command
  ([`d6cb133`](https://github.com/MartinBernstorff/Memium/commit/d6cb1330cbc7b7fbc4babc2e9e480da6a37bb5b0))


## v0.3.0 (2023-10-27)

### Bug Fixes

- Add field to attribute, not property
  ([`274370f`](https://github.com/MartinBernstorff/Memium/commit/274370f914078c8c8b00bd1cc42fe26bacce2f2f))

- Correctly sync dirs in bind mounts
  ([`3e269ee`](https://github.com/MartinBernstorff/Memium/commit/3e269ee2dfceb005b7418336cf0f3a5d821c3027))

- Do not point to non-existing license
  ([`5197292`](https://github.com/MartinBernstorff/Memium/commit/5197292ddd6b30e549cd46167a89495a29623a88))

- Incorrect type hints from misaka
  ([`6988e7a`](https://github.com/MartinBernstorff/Memium/commit/6988e7a63957a9f23c4b8296b44b64768e798ea2))

- Infinite loop
  ([`ce7470a`](https://github.com/MartinBernstorff/Memium/commit/ce7470a08570d14a5d6667a3b08f989d302936b6))

- Overlapping commands
  ([`dd66cc1`](https://github.com/MartinBernstorff/Memium/commit/dd66cc11ceda6b1890b1c69a11e36578f515b2da))

- Pin invoke to version 2.1.0
  ([`a5c56b9`](https://github.com/MartinBernstorff/Memium/commit/a5c56b946ae5083cf67aaed0dd51c0876ad61b7c))

- Re-add required import
  ([`3d0d51d`](https://github.com/MartinBernstorff/Memium/commit/3d0d51d5354ce31ddbc18d3d3fa662635cc38933))

- Remove da references
  ([`1b32634`](https://github.com/MartinBernstorff/Memium/commit/1b326345dfa2ce65814a4412c91bd67e59354f85))

- Remove rej
  ([`152f124`](https://github.com/MartinBernstorff/Memium/commit/152f124d4bb608f041da4b53dcd34666803b84c5))

- Shrink matching
  ([`5dc43d7`](https://github.com/MartinBernstorff/Memium/commit/5dc43d7b62752affc4a9d3ee73fc723084727472))

- Typo
  ([`e687c3e`](https://github.com/MartinBernstorff/Memium/commit/e687c3ed239ea8abdabf06143657c5a2a9a5f577))

### Build System

- Add more emojis
  ([`bb858f9`](https://github.com/MartinBernstorff/Memium/commit/bb858f9bd191316997990219531f392b3e2f795d))

- Add timeout to pr list
  ([`d76f8d1`](https://github.com/MartinBernstorff/Memium/commit/d76f8d1f840385130fb4b8e89b325a8955371483))

- Ask for commit if uncommitted changes before PR
  ([`4b4f7d3`](https://github.com/MartinBernstorff/Memium/commit/4b4f7d39d316e7d920ea637279241f175a28f065))

- Auto-fix formatting by default
  ([`16806cf`](https://github.com/MartinBernstorff/Memium/commit/16806cfb1d5caa54f41626148dd6d779405fbf44))

- Complete migration to Invoke
  ([`4c77a87`](https://github.com/MartinBernstorff/Memium/commit/4c77a87fe1b1cc50581991b4c1698cc7953b8d89))

- First makefile
  ([`e446e8b`](https://github.com/MartinBernstorff/Memium/commit/e446e8b61ec74ecf14308a685e9fea406339174a))

- Fix quotation marks
  ([`d833bc5`](https://github.com/MartinBernstorff/Memium/commit/d833bc599dd3139d2d5539485a7e0c2599cbda65))

- Hide output of branch_exists_on_remote
  ([`9bef312`](https://github.com/MartinBernstorff/Memium/commit/9bef31295b03348c52649193d3fc6129cffedc08))

- Hide result from gh pr lsit
  ([`9c91fa1`](https://github.com/MartinBernstorff/Memium/commit/9c91fa19cf96d944d4c7ed8ace8f4fd42677e665))

- Make tests only show minimal effect
  ([`65c3ddc`](https://github.com/MartinBernstorff/Memium/commit/65c3ddcf80afc187de6192e4c6d20f44329ac61d))

- Misc.
  ([`968cd47`](https://github.com/MartinBernstorff/Memium/commit/968cd4713f315ad77b0d1516cf18903fa5a9ecfe))

- Misc.
  ([`0d94a1d`](https://github.com/MartinBernstorff/Memium/commit/0d94a1df383e873ccc71cbf48494bc8931ceab8d))

- Missing backslash
  ([`0fa130e`](https://github.com/MartinBernstorff/Memium/commit/0fa130e9fb611b3795f1dfeba8b306191a4c523d))

- More informative messaging when syncing
  ([`d351a16`](https://github.com/MartinBernstorff/Memium/commit/d351a169c723f524e96ebe8c6618c4881097ab24))

- Only open browser if PR does not exist
  ([`883ddca`](https://github.com/MartinBernstorff/Memium/commit/883ddca4bdb160ce809e161d4d17345d7927e7d7))

- Pre_commit before mypy
  ([`d2a5c40`](https://github.com/MartinBernstorff/Memium/commit/d2a5c4008945e3f8e532987d04be009b65de9bfb))

- Prettier messages
  ([`4c5d961`](https://github.com/MartinBernstorff/Memium/commit/4c5d96153067b555571d05834cd1541ed1249b6a))

- Pull before push
  ([`027d426`](https://github.com/MartinBernstorff/Memium/commit/027d426159a89893249e698a8a00b38c60a7761c))

- Push branch to origin if doesn't exist
  ([`2b07dd9`](https://github.com/MartinBernstorff/Memium/commit/2b07dd9f3c63033fc6a9abe35f36017b9b900fdc))

- Push to PR if exists
  ([`137aa06`](https://github.com/MartinBernstorff/Memium/commit/137aa0616c0e2f6409becf47ab8c88c0bf6d9ab6))

- Remove @task decorator from utils function
  ([`2e7a61d`](https://github.com/MartinBernstorff/Memium/commit/2e7a61d46d39b45dc0d7cf37c966733f2de5bdc6))

- Remove unused readme
  ([`7f00c19`](https://github.com/MartinBernstorff/Memium/commit/7f00c19a6635e0168ae16126b40d7db6db1611d7))

- Run failed tests first
  ([`af11fcb`](https://github.com/MartinBernstorff/Memium/commit/af11fcbadb72778574257f8163915cea13e159c3))

- Separate exist and does not exist flow
  ([`b044fe6`](https://github.com/MartinBernstorff/Memium/commit/b044fe67b9b523c0644a0bebf2ab710ee47ddc4d))

- Typo
  ([`c3b4ed0`](https://github.com/MartinBernstorff/Memium/commit/c3b4ed0e1bccc0f72abec5d60d8a13c2d1d5c983))

- Update tasks.py
  ([`cef2666`](https://github.com/MartinBernstorff/Memium/commit/cef266634fecb9546ccd149b53d3116f81764bb5))

- Use all available cores
  ([`f9916e8`](https://github.com/MartinBernstorff/Memium/commit/f9916e8147819a47642a157900305bc56e4bf149))

### Chores

- Cleanup repo
  ([`2f7c31f`](https://github.com/MartinBernstorff/Memium/commit/2f7c31f97139275964d034da616f7d8ca1ad5c79))

### Code Style

- Auto-fixes from pre-commit
  ([`45d16ee`](https://github.com/MartinBernstorff/Memium/commit/45d16eea207f5a337de8878f82dfd9a28657e402))

- Auto-fixes from pre-commit
  ([`8c79758`](https://github.com/MartinBernstorff/Memium/commit/8c7975885265bce9de1a9919fcb929e841e8862c))

- Lint
  ([`1998401`](https://github.com/MartinBernstorff/Memium/commit/19984014599e94f84ff46d128de126feb05e9818))

- Linting
  ([`2db1686`](https://github.com/MartinBernstorff/Memium/commit/2db1686bcf4a4e09b87cbdaf5605efc9f2ad879f))

- Linting
  ([`98f0a06`](https://github.com/MartinBernstorff/Memium/commit/98f0a0604de83de09d33922ebbd61986bdde6bf7))

- Linting
  ([`521cf42`](https://github.com/MartinBernstorff/Memium/commit/521cf42889a64bd8c3de873657643b03e0a0e483))

- Linting
  ([`1b59dcc`](https://github.com/MartinBernstorff/Memium/commit/1b59dccd5bfc4d59cfca8a05bb7f4144671460c7))

- Linting
  ([`6198058`](https://github.com/MartinBernstorff/Memium/commit/6198058164273d63d4de0dc597854915b5a90d75))

- Linting
  ([`17c3163`](https://github.com/MartinBernstorff/Memium/commit/17c31631ce35ed2c03dcf87247f0f69e5476980a))

- Remove unused type: ignore
  ([`0fb4b28`](https://github.com/MartinBernstorff/Memium/commit/0fb4b28d598a16e91ea7db562eafaeff05ef01eb))

### Continuous Integration

- Add dockerignore
  ([`35f6ecf`](https://github.com/MartinBernstorff/Memium/commit/35f6ecfc8cb47be58b75246fc16a8954c43b0acb))

- Add mypy to pre-commit
  ([`9746c27`](https://github.com/MartinBernstorff/Memium/commit/9746c2722e862159844fe10c22cb8ac68e7f79c0))

- Align dockerfile devcontainer python with rest of project
  ([`fd0a59d`](https://github.com/MartinBernstorff/Memium/commit/fd0a59d97bc3e72c5ad1e22c1349e3168012eb04))

- Broader ignore for venv
  ([`a5f534f`](https://github.com/MartinBernstorff/Memium/commit/a5f534f83c434da9c18e92495d3bf3c7e2e3c0cb))

- Create hosts before push
  ([`6d38c59`](https://github.com/MartinBernstorff/Memium/commit/6d38c59ba3b38d3a71c09d2ea08cecfc84dd4a64))

- Create pr on web
  ([`654349a`](https://github.com/MartinBernstorff/Memium/commit/654349a36bab5bd1ef9015a572dab176fcdecb09))

- Disable release
  ([`a73a8d3`](https://github.com/MartinBernstorff/Memium/commit/a73a8d3827e0d918c09e66852c54efa824fa31a3))

- Do not automatically commit formatting changes
  ([`9073d12`](https://github.com/MartinBernstorff/Memium/commit/9073d12f21ba7cec2bc178c997005fa33598654b))

- Install pre-commit hooks on setup
  ([`61bfc12`](https://github.com/MartinBernstorff/Memium/commit/61bfc1257ec01476c331cf2d6e586268aed2b121))

- Install test deps in dev container
  ([`0a03465`](https://github.com/MartinBernstorff/Memium/commit/0a034657ff9ed42a8a4727c37115d45b2c1a9e56))

- Invalidate cache
  ([`4eb6aae`](https://github.com/MartinBernstorff/Memium/commit/4eb6aaef43e2df931b56de953cb5f9b847a8ccd7))

- Minimal test interface
  ([`0059b80`](https://github.com/MartinBernstorff/Memium/commit/0059b803ead752006d1943b06b351d8591324fad))

- Move dependencies to correct subheading
  ([`fea7ee1`](https://github.com/MartinBernstorff/Memium/commit/fea7ee1f89829974fa8bee49f9724b5848fe093f))

- Optimise layers for deps
  ([`eea7e9b`](https://github.com/MartinBernstorff/Memium/commit/eea7e9b6412071dae6dc6b2f28af73cf93307047))

- Print branch name
  ([`3e3dbf2`](https://github.com/MartinBernstorff/Memium/commit/3e3dbf247e79c196896239c1b6f3103d750f9831))

- Re-enable caching in tests
  ([`dee7316`](https://github.com/MartinBernstorff/Memium/commit/dee7316908ab7d8ffbcf813500943af622f6a7c6))

- Reenable release
  ([`6a81185`](https://github.com/MartinBernstorff/Memium/commit/6a81185f68c81d5b0ac23369c480687015f4acb0))

- Reenable release
  ([`1d2d20a`](https://github.com/MartinBernstorff/Memium/commit/1d2d20affac9d21f9f376a37c3836c6c918fca0d))

- Remove poetry
  ([`a7c091d`](https://github.com/MartinBernstorff/Memium/commit/a7c091d668eab47f24fccfd708b02a115fa3a1e1))

- Remove pull-request template
  ([`bfbe55d`](https://github.com/MartinBernstorff/Memium/commit/bfbe55d2241c9ec260e0d2b9d762e30443f453bb))

- Remove unused PR
  ([`949e2e3`](https://github.com/MartinBernstorff/Memium/commit/949e2e312b75ed38541e0354518bd8753e96d034))

- Run release after tests
  ([`345abc3`](https://github.com/MartinBernstorff/Memium/commit/345abc37ad64191113de7b9afac81a001170059d))

- Run tests
  ([`26473be`](https://github.com/MartinBernstorff/Memium/commit/26473bef39f6acf0fd2fd7d7f2441544f8678954))

- Send alert if script fails
  ([`25f88c2`](https://github.com/MartinBernstorff/Memium/commit/25f88c2773a55b1a1fa8ac20cf4793f85cf116ae))

- Simplify
  ([`abae734`](https://github.com/MartinBernstorff/Memium/commit/abae734e498eedc95537e2579101f56e32d75a26))

- Simplify call
  ([`c072a29`](https://github.com/MartinBernstorff/Memium/commit/c072a294bd354f45b491a896e9fda18cf329e566))

- Update cruft
  ([`28c6125`](https://github.com/MartinBernstorff/Memium/commit/28c61258104da50093e9762387c8e50269112c9f))

- Update cruft
  ([`357ac0a`](https://github.com/MartinBernstorff/Memium/commit/357ac0a10ad7409b5d725d8c03ed8669cec0032b))

- Update cruft
  ([`4e5a414`](https://github.com/MartinBernstorff/Memium/commit/4e5a414bc3af76b690806c9acc47b343e3c5faa2))

- Update cruft
  ([`bda3461`](https://github.com/MartinBernstorff/Memium/commit/bda3461e914fcd421b2fcc9107f267a98734bff5))

- Update cruft
  ([`169171c`](https://github.com/MartinBernstorff/Memium/commit/169171ce0677d21e9559784f99deb811d2b536b4))

- Update cruft
  ([`382231d`](https://github.com/MartinBernstorff/Memium/commit/382231db184585973869738e581f9f2323e8fead))

- Update cruft
  ([`9a3c0fb`](https://github.com/MartinBernstorff/Memium/commit/9a3c0fb10b7d9e258aa6df00e0d621f101c8b380))

- Update paths
  ([`29cc8ce`](https://github.com/MartinBernstorff/Memium/commit/29cc8cea1aaa789f69b48b89a34fe8e8b3c94f2c))

- Update tasks
  ([`2837861`](https://github.com/MartinBernstorff/Memium/commit/283786145c625efd9e942d090a06fa05b977c978))

- Update tasks
  ([`687cdb8`](https://github.com/MartinBernstorff/Memium/commit/687cdb8dec71d5a1a21a8f91cbbf412a5239393c))

- Use nimble-python
  ([`9da7e6c`](https://github.com/MartinBernstorff/Memium/commit/9da7e6cc0d4e45fd7abf1d2536ed59be76215fb6))

### Documentation

- Clean up readme
  ([`bcf2480`](https://github.com/MartinBernstorff/Memium/commit/bcf2480cf1eb3a2532338d82e27f7ad6b02b1658))

- Improve readme
  ([`b5a4ccc`](https://github.com/MartinBernstorff/Memium/commit/b5a4ccc2684f1fc55ab02608fd9b8cf9f92fb607))

- Update docs
  ([`d0b646d`](https://github.com/MartinBernstorff/Memium/commit/d0b646df07910a25e357d24d6554ca2e1a7f2674))

### Features

- Add dev_container
  ([`0e29b4d`](https://github.com/MartinBernstorff/Memium/commit/0e29b4dbe41a6df5728026db66e22fb1a56ed988))

- Add docker image
  ([`2c0b7c6`](https://github.com/MartinBernstorff/Memium/commit/2c0b7c6e3233f235c2b5fee1c8f0deeb6558a9f3))

- Add guid test for qa ankinotes
  ([`dfdf04c`](https://github.com/MartinBernstorff/Memium/commit/dfdf04cf962cdb906427f9339eeadb18256583bf))

- Add Obsidian URI to AnkiCards
  ([`b04f44b`](https://github.com/MartinBernstorff/Memium/commit/b04f44b89db5df81de2ba2a805899a48f88c0ee8))

- Add preferred extensions
  ([`388dce3`](https://github.com/MartinBernstorff/Memium/commit/388dce336c8fc8497da338729c6cb34727137dfc))

- Add support for markdown link aliases
  ([`add7e2a`](https://github.com/MartinBernstorff/Memium/commit/add7e2ac3769ad99b0bb8841a93fa21af4718ba3))

- Add tts
  ([`5eaf984`](https://github.com/MartinBernstorff/Memium/commit/5eaf9848937678588b84213acbb81a663f6e1d5d))

- Add vscode setting sto tracking
  ([`147716e`](https://github.com/MartinBernstorff/Memium/commit/147716e164d13a1474001905ac24d4465446e974))

- Attempt tts addition
  ([`3ccb493`](https://github.com/MartinBernstorff/Memium/commit/3ccb49365eec003ce98bb6ae1c3e0a7f491ff7b7))

- Bump
  ([`26ea9fb`](https://github.com/MartinBernstorff/Memium/commit/26ea9fb53ac4693a834b3c2fd65846e8850fb43d))

- Decrease length of note id
  ([`6075894`](https://github.com/MartinBernstorff/Memium/commit/6075894de68d34b5a2db7277bf82d9aba604c798))

- Delete cards on sync
  ([`cfd82c9`](https://github.com/MartinBernstorff/Memium/commit/cfd82c968a39c3ba82341d04c39d1f9fc3f90019))

- Dynamic user dir in debug main launch.json
  ([`0aa5d38`](https://github.com/MartinBernstorff/Memium/commit/0aa5d386d073a8e3d77c3a5957f6beb45fed6f31))

- Improve dir parsing speed
  ([`e17dea6`](https://github.com/MartinBernstorff/Memium/commit/e17dea693d268eeebeedbe83125a3b1e2f81aef2))

- Pre-populate msic
  ([`73dcb46`](https://github.com/MartinBernstorff/Memium/commit/73dcb46273e88509ae4fb872c979d2ab1144635d))

- Restrict polling time
  ([`00f163e`](https://github.com/MartinBernstorff/Memium/commit/00f163ea912b35278fa0f3fdf6ec18b88c632b13))

- Robustness to cards with errors
  ([`d340b50`](https://github.com/MartinBernstorff/Memium/commit/d340b50f1bf5bae9f49794e86dfd65d46d893a99))

- Support dash in links
  ([`add5191`](https://github.com/MartinBernstorff/Memium/commit/add51919ccd246d84225b5989b3f04a6b110b858))

- Sync deletions
  ([`14c24e2`](https://github.com/MartinBernstorff/Memium/commit/14c24e21cb09d34ecb7aefc95f535b815e02cda2))

- Update guid for qa
  ([`f88d7ad`](https://github.com/MartinBernstorff/Memium/commit/f88d7ad44e9ddc3dbe181c9f8866257d9b308090))

- Use functionalpy
  ([`b7352f1`](https://github.com/MartinBernstorff/Memium/commit/b7352f1961177661ce7de8b5f4c5a754564140dd))

- Use functionalpy
  ([`72d106a`](https://github.com/MartinBernstorff/Memium/commit/72d106a5e9597798f329d502401c4d4848a9721d))

- Use obsidian uris
  ([`e107087`](https://github.com/MartinBernstorff/Memium/commit/e1070871474f9205fd905d0e33a6e5e374ae0143))

### Refactoring

- Extract url generation
  ([`b740700`](https://github.com/MartinBernstorff/Memium/commit/b7407001d357a5e814394effaa5bd45a4b9c130b))

- Major rewrite of input pipeline
  ([`88793cd`](https://github.com/MartinBernstorff/Memium/commit/88793cd886c444e4cbe2e3dd55d010ff33590b78))

- Modularise
  ([`5eba16c`](https://github.com/MartinBernstorff/Memium/commit/5eba16ceefb68fb8b6a5a0ec6f68897716fe2db2))

- Remove support for QA DK card
  ([`125c725`](https://github.com/MartinBernstorff/Memium/commit/125c725a23cdf68f6a5edd317ec6a863665500a7))

- Remove unused arguments from config
  ([`c27068b`](https://github.com/MartinBernstorff/Memium/commit/c27068bb735cae85c8d85b1353ab3181e76b6b75))

- Renaming
  ([`61baacc`](https://github.com/MartinBernstorff/Memium/commit/61baacc5d6374dff99f4707887afce02d040a1d0))

- Specify anki packagegenerator
  ([`8b52a42`](https://github.com/MartinBernstorff/Memium/commit/8b52a42c32e443188684fe825894d636dc3e4083))

- Split ankicard into AnkiQA and AnkiCloze
  ([`824660c`](https://github.com/MartinBernstorff/Memium/commit/824660c165e70be08d0d4992ac69f4a400b9cf28))

- Split cards_to_decks
  ([`fa183f0`](https://github.com/MartinBernstorff/Memium/commit/fa183f08bc883a81bf41fd94beb0d9765e04053b))

- Split git sync and github pr handling
  ([`981d105`](https://github.com/MartinBernstorff/Memium/commit/981d105a222b2f90c61adbb1a6d71a2ead1dee8a))


## v0.2.0 (2023-03-12)

### Continuous Integration

- Ignore bearimages
  ([`32bf9e4`](https://github.com/MartinBernstorff/Memium/commit/32bf9e4069a575dda3ac45cd62e4b00608368525))

- Update cruft
  ([`89b9e86`](https://github.com/MartinBernstorff/Memium/commit/89b9e8697ea20a53e44f4e511d91061e951b7013))

### Features

- Exclude q. and a. fields from cloze prompts
  ([`5b2d6cd`](https://github.com/MartinBernstorff/Memium/commit/5b2d6cda3825582381444b36c6ef1dbc8779d4af))


## v0.1.0 (2023-03-11)

### Bug Fixes

- Better support for TTS
  ([`78032e7`](https://github.com/MartinBernstorff/Memium/commit/78032e761e7661e1974d5595f39eaf43b8965264))

- Cruft typography
  ([`99b7a25`](https://github.com/MartinBernstorff/Memium/commit/99b7a25ec613b8017309662354ed3def767975f3))

- Do not use tts for now
  ([`7e3bab5`](https://github.com/MartinBernstorff/Memium/commit/7e3bab580adf7d50d556024db29dd343db6a8cb3))

- Don't fail on missing media references
  ([`5274e3f`](https://github.com/MartinBernstorff/Memium/commit/5274e3fb3f494c56c99624ec76cbbd307de548a4))

- Ensure guids match cloze
  ([`694f701`](https://github.com/MartinBernstorff/Memium/commit/694f701aa44a1962168cb3256062f70371aef1cd))

- Hash anki cards on markdown
  ([`b5a35b9`](https://github.com/MartinBernstorff/Memium/commit/b5a35b91f58c3d43e237f495a30940e3ea780a00))

- Match guide for first test case
  ([`ee41799`](https://github.com/MartinBernstorff/Memium/commit/ee41799941a027792588821f22003fc2a4c99171))

- Typo in toml
  ([`be9499e`](https://github.com/MartinBernstorff/Memium/commit/be9499e60f9e872112cedd6454ff6fa16af1eabe))

### Chores

- Housekeeping
  ([`3c93bd7`](https://github.com/MartinBernstorff/Memium/commit/3c93bd738fbb122ba5d9f4babebeaa8ef9a9a391))

- More typing
  ([`dcb04d0`](https://github.com/MartinBernstorff/Memium/commit/dcb04d043ae173b02c6b86f707d4d24008d95241))

- Remove unused type ignore
  ([`4cbd2b8`](https://github.com/MartinBernstorff/Memium/commit/4cbd2b88cc86c2d8ecc0716d15b64ef5596fa7de))

- Type everything
  ([`884deea`](https://github.com/MartinBernstorff/Memium/commit/884deeaa9c5e58f5d82ade7cdad4575900b8f793))

### Code Style

- Final linting
  ([`8e59770`](https://github.com/MartinBernstorff/Memium/commit/8e597700e268a2f26cc5dc940dfe1fb13789d0ab))

- Linting
  ([`057d034`](https://github.com/MartinBernstorff/Memium/commit/057d0348763f1c3b11dba4bd83877cbb65ac0831))

- Linting
  ([`ba808b6`](https://github.com/MartinBernstorff/Memium/commit/ba808b66ab4d83f919512cfce5d853d19714bdaa))

- Linting
  ([`186208c`](https://github.com/MartinBernstorff/Memium/commit/186208c9b009c211c66f57c1ce2efadf7ef2b909))

- Linting
  ([`9f0d580`](https://github.com/MartinBernstorff/Memium/commit/9f0d5802cc6155f2774faeeb293f72d72112a58d))

- Linting
  ([`66e30e1`](https://github.com/MartinBernstorff/Memium/commit/66e30e1b97e7ebed29b1552a0a48c659f09ffe9a))

### Continuous Integration

- Cruft
  ([`55b6232`](https://github.com/MartinBernstorff/Memium/commit/55b62321376b3fee21252f4b2878f6e8bdaf2d4e))

- Cruft
  ([`eca6564`](https://github.com/MartinBernstorff/Memium/commit/eca65640591eeac6bd7edcb4aa6e3bdb3f450b80))

- Cruft check
  ([`c3b5353`](https://github.com/MartinBernstorff/Memium/commit/c3b5353b7febd1337acd3addc1a1711e47472bc5))

- Fix error in cruft
  ([`c3114e5`](https://github.com/MartinBernstorff/Memium/commit/c3114e5809a7135ad7dabf088abc99cec35a0968))

- Permissions for setup_for_dev
  ([`8f23875`](https://github.com/MartinBernstorff/Memium/commit/8f23875ad5e970bdb64503dc2a72a909e6c22e74))

- Test
  ([`62ea30c`](https://github.com/MartinBernstorff/Memium/commit/62ea30c0e8d504409bd91fbdcd01540b99752268))

- Test
  ([`babf357`](https://github.com/MartinBernstorff/Memium/commit/babf357b30cecd73e8c202a80d881cfd2c2399fa))

- Test new cruft procedure
  ([`e41862c`](https://github.com/MartinBernstorff/Memium/commit/e41862c0433c7838282cd7e880dc6a3847c32f54))

- Try new cruft ci
  ([`6412ae8`](https://github.com/MartinBernstorff/Memium/commit/6412ae8eaf9626de016abbef28e4c291e093c088))

- Update cruft
  ([`aea9b87`](https://github.com/MartinBernstorff/Memium/commit/aea9b870cd52a2d4784e98d11710971d19c6006b))

- Update cruft
  ([`12bd8a9`](https://github.com/MartinBernstorff/Memium/commit/12bd8a9736da761c405af7e42f0747073a1364bf))

- Update cruft failed template
  ([`2d793c5`](https://github.com/MartinBernstorff/Memium/commit/2d793c53579cb2665039a35c11f13168b4f5b52c))

- Update cruft logic
  ([`9d2109a`](https://github.com/MartinBernstorff/Memium/commit/9d2109ac5d29195bb103a84e5cb8ebb08f7d07b0))

- Update cruft message
  ([`2343489`](https://github.com/MartinBernstorff/Memium/commit/234348919d8f39546aadf1ff14de0873e30e9100))

- Update find comment
  ([`3de3a91`](https://github.com/MartinBernstorff/Memium/commit/3de3a91015f316e5c651ef3f3de0e38704cf12fd))

### Features

- Add cloze extractor
  ([`8fda355`](https://github.com/MartinBernstorff/Memium/commit/8fda355e9ab7b9e945c61c7b2853a3418cfa4458))

- Add markdown to card logic
  ([`f1a204f`](https://github.com/MartinBernstorff/Memium/commit/f1a204ff74c898374f8399f34aba8577830391a0))

- Add qa_prompt_extractor
  ([`377b426`](https://github.com/MartinBernstorff/Memium/commit/377b426d97ab985832cb577cfbfa4e4c01d73fd6))

- Add source notes to QAPrompts
  ([`08bae17`](https://github.com/MartinBernstorff/Memium/commit/08bae173fcd0ce96aa54319cbe529a918e0b3229))

- Better sh file
  ([`fc0b2e6`](https://github.com/MartinBernstorff/Memium/commit/fc0b2e6197940906061e22f069c361d3f379685c))

- Compile fields to html
  ([`13f8c07`](https://github.com/MartinBernstorff/Memium/commit/13f8c079a2db56c0b80161488d2831cc9d9eadf2))

- Create a unified pipeline
  ([`a703fcc`](https://github.com/MartinBernstorff/Memium/commit/a703fcc8158d2412170dda333d24cc87bf4c3daf))

- Disable automatic tts (replaced by AwesomeTTS)
  ([`5f37882`](https://github.com/MartinBernstorff/Memium/commit/5f37882a9ce24ba84e36b7d2d1939cc035144dbe))

- Don't update bear
  ([`59fef60`](https://github.com/MartinBernstorff/Memium/commit/59fef60eb4d22fc9e3e5443b7456a1687689d4e3))

- First stab at main package
  ([`069accd`](https://github.com/MartinBernstorff/Memium/commit/069accdfff488ed285dabebdbb847fb1ba064c3b))

- First working rewrite
  ([`9a16d98`](https://github.com/MartinBernstorff/Memium/commit/9a16d983054fa03c005922778f1e4bc33222496d))

- Fit uuid generation to qa prompt extractor
  ([`4e33b0d`](https://github.com/MartinBernstorff/Memium/commit/4e33b0d37075d897aba0a932316d10284572e1e4))

- Ignore cloze-likes in code blocks
  ([`80b0888`](https://github.com/MartinBernstorff/Memium/commit/80b0888839ea8206fc1697674be4ac2e42e0627f))

- Migrate main to use new pipeline
  ([`fa71108`](https://github.com/MartinBernstorff/Memium/commit/fa7110896aa326cf44646cb0fe7353c0d8ffa337))

- Remove filepath requirement
  ([`65c97a5`](https://github.com/MartinBernstorff/Memium/commit/65c97a5262965cd0776bfb36bc7108a27e83fd6d))

- Working version
  ([`a8438c7`](https://github.com/MartinBernstorff/Memium/commit/a8438c7b3cb42f4cb2718008b8e2ed4f2514c7ab))

### Refactoring

- Add guards
  ([`c92eeb7`](https://github.com/MartinBernstorff/Memium/commit/c92eeb7c101f7a3c30e57827b8d5e696c7c82b49))

- Clean up subdeck
  ([`7f03b42`](https://github.com/MartinBernstorff/Memium/commit/7f03b42bdb46733683459d5b8e21df39e44bc427))

- Disambiguate note and prompt uuids
  ([`db5c457`](https://github.com/MartinBernstorff/Memium/commit/db5c4570378fd7f50265b8ca3991cfb4dab7bbb5))

- Misc.
  ([`8a366b3`](https://github.com/MartinBernstorff/Memium/commit/8a366b3fc2dce6788ae93a5f80c0a57e40fc75b7))

- Rename factory classes
  ([`af592f4`](https://github.com/MartinBernstorff/Memium/commit/af592f4f51c4ed531582be5b7d538a27fd4680fb))

- Stylise pipeline
  ([`34ba2a3`](https://github.com/MartinBernstorff/Memium/commit/34ba2a317f61f1ff0771ac4388ac634b99e67773))
