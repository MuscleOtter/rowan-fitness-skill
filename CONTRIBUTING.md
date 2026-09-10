# Updating Rowan

Prefer a specific failure, a small fix and evidence that the fix works. For issues, include the skill version, host, expected behavior and a de-identified example. Do not post health records, private conversations, credentials or paid program libraries.

1. Edit `skills/fitness-review-board/`. Keep personal state outside the repository.
2. Bump the version in `SKILL.md` and add a short `CHANGELOG.md` entry.
3. Exercise the relevant cases in `references/verification.md`. Preserve required reviewers, grading floors and exact-final approval. Every applicable final specialist score must reach 8.8; existing 9.0 and stricter requirements remain. Recursion or maintenance changes require three independent critique/revision passes under `references/maintenance-rubric.md`, with every final dimension at least 8.8. Never regrade historical reports automatically or lower criteria to pass.
4. Run `python3 tools/package.py`, then `python3 tools/package.py --check`. The script builds a deterministic ZIP and SHA-256 list from the skill folder. It does not assess coaching quality.
5. Review every changed file and the final archive for private information. Commit the source, docs and generated distribution together. Publish a versioned GitHub release with the ZIP and checksum file.

Documentation-only corrections need proportionate checks. Do not rerun unrelated fitness tests or raise scores merely to produce a more impressive release. Do not describe earlier-version execution as a test of changed behavior.

For changes only to repository documentation, check links and `python3 tools/package.py --check`; keep the skill version and published ZIP unchanged. Keep README download and release links on `/latest/`, without a hardcoded current version. When publishing a new skill version, verify that the public download matches the packaged checksum without signing in.

When reporting a scan, identify **both** the Rowan target (repository, commit or release, and package checksum) and the evaluator (repository and exact commit). Link each commit to its own repository. Record scan configuration, date and incomplete checks; retain the raw report privately and publish a summary without local paths or personal records. [The 1.5.2 receipt](docs/validation-1.5.2.json) is an example. Preserve failed and incomplete results as reported; neither is a passing security assessment.

The source of truth for the distributable is `skills/fitness-review-board/`; `dist/` is generated. A package rollback restores instructions only, never an athlete's old record.
