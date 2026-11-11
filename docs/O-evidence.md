# O — GitHub Actions hardening

Pinned both workflow actions to full commit SHAs, set workflow defaults to `permissions: {}`, and gave the lint job `contents: read`. Checkout uses `persist-credentials: false`.

[Configuration commit](https://github.com/yu1234552026/a9-devsecops-lab/commit/53cc717485c605ee164eeb303b42281697693937)

[Verified CI](https://github.com/yu1234552026/a9-devsecops-lab/actions/runs/43034092617): the job log shows both expected action SHAs, read-only contents access, zero Flake8 findings and all four regression tests passing.

Full SHAs fix which action code is executed. Job permissions restrict token access. Updating an action requires reviewing the new commit and running checks again. This control reduces workflow supply chain exposure (OWASP A03:2025) and does not scan action code for vulnerabilities.
