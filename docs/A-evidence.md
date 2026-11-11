# A — Static analysis with Flake8

This is an intentionally seeded educational example, not a claim that these defects were discovered in a production project.

## Setup
Python 3.12; Flake8 7.3.0, pinned in requirements-dev.txt.
Configuration: .flake8 (88-character line limit and complexity limit 10).
GitHub Actions: .github/workflows/ci.yml runs on pushes, pull requests and manual dispatch.
The lint step fails on findings; it does not suppress errors.

```bash
python -m pip install -r requirements-dev.txt
python -m flake8 --version
python -m flake8 src/ --count --show-source --statistics
```

## Observed before-fix result
[Failed run](https://github.com/yu1234552026/a9-devsecops-lab/actions/runs/42991225156)
Commit: a3b879fc3bdd39e3cd4e39450bd00c2f21ed5259

```text
src/budget.py:2:1: F401 'os' imported but unused
src/budget.py:6:10: E225 missing whitespace around operator
src/budget.py:13:35: F821 undefined name 'amount'
3
Process completed with exit code 1.
```

| Finding | Fix | Meaning |
|---|---|---|
| F401 | Remove unused import os | Remove unnecessary code |
| E225 | Change total=0 to total = 0 | Improve readability and consistency |
| F821 | Pass amounts instead of undefined amount | Prevent NameError in remaining_budget |

## Reflection
All three findings are valid for this seeded example; no false positives were identified.
F821 detects a correctness defect before execution. E225 is a style finding, not a security vulnerability.
Basic Flake8 is not a comprehensive security scanner. A clean result does not prove security or correct business logic. Dependency vulnerability detection will be added in E and a separate security practice in O.
The failed and corrected commits remain available in Git history.

## References
- https://flake8.pycqa.org/en/latest/user/invocation.html
- https://flake8.pycqa.org/en/latest/user/configuration.html
- https://docs.github.com/en/actions
- https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart
- https://owasp.org/Top10/2025/

Final submission still requires the 6–12 page landscape PDF plus E and O evidence.
