# Architecture Audit

## Current state
Castor is a modular Python backend with domains for ingestion, analytics, campaigns, reporting, AI, and operations.

## Key findings
1. **RSS ingestion identity robustness gap (fixed):**
   - Prior implementation generated `episode_id` as `guid + publish_date`, which is not stable under malformed GUIDs and feed updates.
   - Duplicate items were not normalized deterministically.

2. **Error telemetry correctness gap (fixed):**
   - Error-type tagging in `poll_feed` relied on dynamic `e` scope assumptions.

3. **Product scope mismatch (documented):**
   - Playback queue/download trust invariants require a first-party listener runtime not present in this repo.

## Remediation implemented
- Deterministic canonical episode IDs via SHA-256 over normalized fields.
- Deterministic fallback GUID when feeds omit GUID.
- Feed-level deduplication and stable ordering for idempotent refresh output.
- Explicit error_type variable handling in telemetry.
- Added unit tests to lock behavior.

## Risk profile
- Low migration risk: changes are isolated to ingestion normalization behavior.
- Potential downstream impact: new `episode_id` format changed from concatenation to hash; consumers should treat ID as opaque.

## Recommendation
- Enforce `episode_id` opacity across API clients and persistence layers.
- Add replay tests against historical feed samples to prevent regressions.
