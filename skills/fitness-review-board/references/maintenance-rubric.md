# Frozen recursive-coaching release rubric

Rubric version: 1.1
Frozen: 2026-09-09  
Reviewer: independent recursion and maintenance reviewer  
Original v1.0 basis: independently written against the delegated scope before inspecting its candidate or prior scores.

User-authorized amendment, 2026-09-09: raise every dimension floor from 8.5 to 8.8 for subsequent skill reviews. Scores may use tenths so the requested threshold is representable. The eight criteria and weights are unchanged; historical reviews keep their original rubric and are not upgraded. Freeze this v1.1 rubric before the new review sequence; do not change it to fit results.

This raises a minimum; it never lowers a stricter previously agreed requirement. Actual scores can decrease when evidence warrants it; do not inflate them to create an upward trend.

## Scope and scoring contract

Evaluate a portable fitness-coaching skill for intermediate and advanced athletes. Reward useful outcome-driven learning, safe and understandable adaptation, maintainability, and low athlete effort. Do not reward complexity for its own sake. A database, background service, integration, or scheduler is not required merely because it could be built.

Keep these three claims separate in every review:

1. **Authored instruction adequacy:** what the delivered skill actually requires, enables, bounds, and explains. This is the scored release scope.
2. **Demonstrated execution:** which behaviors were actually exercised, in what host or explicit simulation, against which candidate version, with what observable results. A written example is not an execution trace; simulation is not host verification.
3. **Longitudinal athlete outcomes:** changes observed over time in a real athlete, with confounders and uncertainty. Neither a strong specification nor a successful test establishes these outcomes.

Score each dimension from 1 to 10, permitting one-decimal increments. **5 means a credible mid-level implementation:** useful basic behavior with substantial omissions. **8.8 is the release minimum: consistently strong, usable, adequately supported within the stated scope, with no material defect. 10 is aspirational, exceptional capability and usability**, not proof that every athlete wants the skill or that it improves all athletes' outcomes.

Weighted score = sum(weight × dimension score) / 100. Release requires **every dimension ≥ 8.8 and no material defect**; an aggregate score cannot compensate for a weak dimension or reviewer. Apply this to every required final skill-review report; earlier drafts may fail while being revised. Do not round a lower score up to 8.8. Numeric granularity is a reporting convention, not measured precision. An unsupported criterion must be recorded as unverified or deficient, with its effect on the relevant claim and score explained. Do not award credit for planned work, inferred hidden behavior, or confident prose. If evidence is missing, identify the smallest useful check. Do not demand unavailable longitudinal evidence merely to judge authored adequacy; do not silently turn authored adequacy into a claim of demonstrated efficacy.

## Dimensions

| Dimension | Weight | Observable criteria for a strong release |
|---|---:|---|
| 1. Outcome-driven personal learning | 16 | Starts from the athlete's effective current program, goals, constraints, and baseline. Reconnects a prior recommendation to subsequent adherence, performance, recovery, and relevant athlete feedback. Distinguishes missing data, nonadherence, noise, and plausible intervention failure. Makes a specific decision to retain, change, test, or stop, with an observable next check and proportionate time horizon. Does not infer causation from one favorable session or rewrite a working program merely to demonstrate activity. |
| 2. Durable, truthful personal memory | 14 | Defines a minimal persistent athlete record and a usable means of carrying it between sessions. Separates athlete statements, measured observations, tentative hypotheses, decisions, and unresolved questions. Records relevant provenance, dates, confidence, and superseded information. Checks whether persistence actually succeeded; otherwise supplies an honest portable handoff without claiming to remember later. Retrieves relevant context without treating every historical note as current truth. |
| 3. Interpretable adaptation and tactic retention | 13 | Each meaningful change has a concise rationale tied to evidence and athlete constraints, an expected effect, and a condition for reconsideration. Retains successful tactics and records unsuccessful or poorly tolerated tactics with enough context to avoid unhelpful repetition. Distinguishes “failed in these conditions” from “never use again.” Learns from disagreement, changed goals, and poor adherence without blaming the athlete or optimizing a proxy against the athlete's priorities. Bounds changes and supports reversals when uncertainty warrants them. |
| 4. Independent recursive critique and revision | 14 | For new prescriptions, explicitly requires at least three bounded critique/revision passes and checks the exact final prescription after its last substantive edit. Reviewers assess the actual candidate, identify actionable defects, and track their resolution; previous-candidate approval cannot approve changed content. Independence is operationally defined and not fabricated when a host cannot supply it. The process has termination and unresolved-defect handling rather than endless polishing, automatic score escalation, or release by exhaustion. User burden and delay remain proportionate; routine observation or faithful recall does not accidentally trigger a full new-prescription workflow. |
| 5. Evidence, host, and data maintenance | 11 | Separates athlete-data freshness, health/fitness evidence freshness, host capabilities, and package maintenance. Uses sensible triggers such as changed symptoms, goals, equipment, medications if relevant, contradictions, or tool failures rather than demanding indiscriminate research on every turn. Rechecks consequential uncertain claims when needed, preserves source context, and handles unavailable sources or integrations honestly. Explains how relevant maintenance reaches the next session through an available mechanism or portable checkpoint. Does not promise background monitoring unless actually configured. |
| 6. Drift, corrections, deletion, and version governance | 11 | Athlete corrections can update or supersede stored facts and downstream decisions. Sensitive or obsolete data can be removed through the actual storage mechanism, with limits of deletion disclosed accurately. A stable athlete preference or safety constraint cannot be silently overwritten by a weak inference. Meaningful package and prescription versions are identifiable; old evidence cannot masquerade as verification of a changed version. The process detects conflicting or stale instructions and has a simple recovery or rollback path. |
| 7. Proportionate athlete effort and portability | 10 | Asks only for information that can change the decision, reuses known context, permits approximate or missing data, and offers a concise actionable response. The athlete can understand what to do, why a meaningful change occurred, and what to report next. Core behavior remains usable without a particular app, wearable, database, scheduler, or agent feature. Capability-dependent improvements have explicit, truthful fallbacks. Internal reviews and recordkeeping do not become repetitive questionnaires or distract from training. |
| 8. Falsifiable verification and honest release claims | 11 | Supplies or supports reproducible, bounded scenarios with inputs, candidate version, expected decisions, and observed outputs. Verification covers at least successful carry-forward, a correction, missing/stale data or a host failure, a failed tactic, and an adaptation that needs critique of its exact final form. Reports failures and limitations rather than merely displaying ideal examples. Distinguishes static inspection, constructed examples, simulations, actual host/tool execution, and athlete outcomes. Final-package verification is traceable to the delivered candidate; evidence from earlier versions is reused only where applicability is justified. |

Weights total 100.

## Review procedure frozen for this sequence

- Run at least three distinct critique/revision passes. In each, inspect the supplied frozen candidate and actual evidence, score against this same rubric, and name concrete defects and useful fixes. Reassess the revised candidate without carrying forward scores as an entitlement.
- Give every dimension a score, a short evidence citation, and any unverified criterion. Cite exact file sections or line locations where practical. Record the candidate identifier and the scope of each test.
- Label each finding by severity and consequence. A **material defect** is one that can invalidate a consequential recommendation, fabricate memory or evidence, lose an important correction/constraint, omit a required independent/final check, misrepresent a capability, or make a central required workflow impractical. A cosmetic preference is not a material defect.
- Fixes must address a demonstrated defect or a necessary user requirement. Prefer a concise rule, better decision boundary, clear fallback, or small evidence check over new infrastructure. Do not add machinery simply to increase a score.
- After the final revision, verify the exact delivered package and reconcile outstanding findings. Three passes are a minimum review process, not evidence of success by themselves. If a material defect remains, report it plainly and do not pass the release.
- Summarize three statuses separately: authored release readiness; execution evidence and limitations; longitudinal outcomes available or not established. Do not compress these into an unsupported “fully validated” claim.
- Do not change this rubric to fit a candidate or its scores. Any user-authorized amendment must be a separately identified rubric version with its reason and prospective effect recorded; it must not retroactively improve previous scores.

## Compact review record

Candidate/version:  
Pass:  
Evidence examined and evidence scope:  

| Dimension | Score / 10 | Evidence | Defect or unverified criterion |
|---|---:|---|---|
| 1. Outcome-driven personal learning | | | |
| 2. Durable, truthful personal memory | | | |
| 3. Interpretable adaptation and tactic retention | | | |
| 4. Independent recursive critique and revision | | | |
| 5. Evidence, host, and data maintenance | | | |
| 6. Drift, corrections, deletion, and version governance | | | |
| 7. Proportionate athlete effort and portability | | | |
| 8. Falsifiable verification and honest release claims | | | |

Weighted score:  
Material defects and required fixes:  
Authored release readiness:  
Demonstrated execution status:  
Longitudinal athlete outcome status:  
Exact-final verification status:
