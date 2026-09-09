# Updating Rowan

Prefer a specific failure, a small fix and evidence that the fix works. For issues, include the skill version, host, expected behavior and a de-identified example. Do not post health records, private conversations, credentials or paid program libraries.

1. Edit `skills/fitness-review-board/`. Keep personal state outside the repository.
2. Bump the version in `SKILL.md` and add a short `CHANGELOG.md` entry.
3. Exercise the relevant cases in `references/verification.md`. Preserve required reviewers, grading floors and exact-final approval. Recursion or maintenance changes require three independent critique/revision passes under `references/maintenance-rubric.md`.
4. Run `python3 tools/package.py`, then `python3 tools/package.py --check`. The script builds a deterministic ZIP and SHA-256 list from the skill folder. It does not assess coaching quality.
5. Review every changed file and the final archive for private information. Commit the source, docs and generated distribution together. Publish a versioned GitHub release with the ZIP and checksum file.

Documentation-only corrections need proportionate checks. Do not rerun unrelated fitness tests or raise scores merely to produce a more impressive release. Do not describe earlier-version execution as a test of changed behavior.

The source of truth for the distributable is `skills/fitness-review-board/`; `dist/` is generated. A package rollback restores instructions only, never an athlete's old record.
