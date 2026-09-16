# Updating Rowan

Prefer a specific failure, a small fix and evidence that the fix works. For issues, include the skill version, host, expected behavior and a de-identified example. Do not post health records, private conversations, credentials or paid program libraries.

Nontechnical feedback is welcome: use the [feedback form](https://github.com/MuscleOtter/rowan-fitness-skill/issues/new/choose) for setup friction, unclear instructions or a useful missing workflow. For public descriptions and reusable artwork, see [Share Rowan](docs/SHARE.md). Keep marketing claims tied to actual capabilities and the published validation limits.

1. Edit `skills/fitness-review-board/`. Keep personal state outside the repository.
2. Bump the version in `SKILL.md` and add a short `CHANGELOG.md` entry.
3. Exercise the relevant cases in `references/verification.md`. Preserve required reviewers, grading floors and exact-final approval. Every applicable final specialist score must reach 8.8; existing 9.0 and stricter requirements remain. Recursion or maintenance changes require three independent critique/revision passes under `references/maintenance-rubric.md`, with every final dimension at least 8.8. Never regrade historical reports automatically or lower criteria to pass.
4. Run `python3 tools/package.py`, then `python3 tools/package.py --check`. The script builds a deterministic ZIP and SHA-256 list from the skill folder. It does not assess coaching quality.
5. Review every changed file and the final archive for private information. Commit the source, docs and generated distribution together. Publish a versioned GitHub release with the ZIP and checksum file.

Documentation-only corrections need proportionate checks. Do not rerun unrelated fitness tests or raise scores merely to produce a more impressive release. Do not describe earlier-version execution as a test of changed behavior.

For the optional visualization helper, run `python3 -B -m unittest discover -s tools`. The packager excludes interpreter bytecode and allows only the named helper and `assets/rowan-visual.css`, not arbitrary executable files or stylesheets. Tests cover contract validation, Markdown output and packaging, not native chart rendering or coaching effectiveness. Follow the on-demand visual style reference for real-output checks at phone width and in both themes; record the actual host and separate preview evidence from in-message integration.

The optional parsed-output test uses an existing Node/`marked` installation: set `MARKED_MODULE` to that module's absolute ESM path before running the same tests. It explicitly skips when unavailable; no runtime dependency is added to the skill.

For changes only to repository documentation, check links and `python3 tools/package.py --check`; keep the skill version and published ZIP unchanged. Keep README download and release links on `/latest/`, without a hardcoded current version. When publishing a new skill version, verify that the public download matches the packaged checksum without signing in.

Publication and installation are separate completion checks. If the user requested installation updates, track each requested destination: local Codex desktop/CLI, local Claude Code, Claude account upload and ChatGPT Project files. Back up replaced folders outside skill discovery, preserve the Training Record, and verify the installed files or account upload directly. Report inaccessible destinations as unverified. Keep machine paths, personal setup receipts and user-specific job state outside the public repository; public validation may summarize the checks and their limits. See [installation verification](docs/SETUP.md#verify-each-installation).

When reporting a scan, identify **both** the Rowan target (repository, commit or release, and package checksum) and the evaluator (repository and exact commit). Link each commit to its own repository. Record scan configuration, date and incomplete checks; retain the raw report privately and publish a summary without local paths or personal records. [The 1.5.2 receipt](docs/validation-1.5.2.json) is an example. Preserve failed and incomplete results as reported; neither is a passing security assessment.

The source of truth for the distributable is `skills/fitness-review-board/`; `dist/` is generated. `.gitattributes` keeps `dist/` out of GitHub's source-code downloads, so they never contain a ZIP inside a ZIP; the release asset is the installable skill. A package rollback restores instructions only, never an athlete's old record.

For discovery-only changes, keep `README.md`, `llms.txt`, `CITATION.cff` and `docs/DISCOVERY.md` consistent with the canonical skill name/path and current capability limits. Check local links, citation syntax and anonymous raw-document access; preserve the version-free `/latest/` release links. Keep community submission rules dated and source-linked. Do not claim a directory listing, ranking improvement or endorsement without evidence. These files describe the project; they do not replace runtime rules or belong in the skill ZIP.
