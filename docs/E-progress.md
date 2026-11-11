# E — Dependabot evidence

## Completed
- Dependency graph and Dependabot alerts enabled.
- Dependabot security updates enabled.
- Weekly pip and github-actions version updates configured in .github/dependabot.yml.
- Four budget regression tests added; every push and PR runs lint and tests.
- Real bot-authored version update: [PR #1](https://github.com/yu1234552026/a9-devsecops-lab/pull/1), actions/checkout v4 to v7.
- [PR CI](https://github.com/yu1234552026/a9-devsecops-lab/actions/runs/42993039487): lint and four regression tests passed.
- [Alerts](https://github.com/yu1234552026/a9-devsecops-lab/security/dependabot): zero open and zero closed alerts observed on 2026-11-11. This is not proof of absence of all vulnerabilities.
- PR #1 remains open for review; no merge has been claimed.

## Disposable alert demonstration
The isolated, undeployed a9-dependabot-demo repository pinned lodash 4.17.15. Dependabot reported five advisories. Updating the manifest to 4.18.0 produced zero open and five closed alerts.

| CVE | Severity | CVSS | First patched version |
|---|---|---:|---|
| CVE-2021-23337 | High | 7.2 | 4.17.21 |
| CVE-2020-8203 | High | 7.4 | 4.17.19 |
| CVE-2020-28500 | Moderate | 5.3 | 4.17.21 |
| CVE-2025-13465 | Moderate | 6.9 | 4.17.23 |
| CVE-2026-4800 | High | 8.1 | 4.18.0 |

The version recommendation covers all five observed advisories. Prioritize alert #5 by its observed severity score, then consider exposure and compatibility in a deployed app. These matches are valid for the seeded package version. The manifest-only demonstration has no application execution path.

The Python dependency update [PR #3](https://github.com/yu1234552026/a9-devsecops-lab/pull/3) proposed Flake8 7.3.0 to 7.5.0 and its [PR CI](https://github.com/yu1234552026/a9-devsecops-lab/actions/runs/42993074240) passed.

## Discussion
SCA compares dependency information with published vulnerability advisories. It helps address software supply chain risk (OWASP A03:2025), but cannot identify every malicious package, unknown vulnerability, or reachable exploit.
Security updates address known vulnerable versions. Version updates can also propose newer versions without a vulnerability alert. PR #1 is a version update; it must not be described as proof of a particular CVE fix.
CI validates compatibility before a human reviews and merges the update. These tests cover empty expenses, totals, remaining budget and overspending; they do not establish comprehensive security.
The main project had no open alerts at the time of observation.

CVSS v3.1 severity bands: 0 none, 0.1–3.9 low, 4.0–6.9 medium, 7.0–8.9 high, 9.0–10 critical. CVSS describes severity, not the probability of exploitation. When reviewing a future alert, record its CVSS version, affected range, and patched version; assess exposure and test compatibility before upgrading.

## References
- https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart
- https://www.first.org/cvss/v3.1/specification-document
- https://owasp.org/Top10/2025/
