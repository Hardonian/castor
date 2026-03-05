# Feature Gap Analysis

| Feature | User value | Engineering complexity | PMF impact |
|---|---|---:|---:|
| Cross-device playback sync | Eliminates trust break in listener UX | High | High |
| Deterministic offline downloads with checksum | Offline reliability + confidence | Medium | High |
| Queue atomicity engine | Prevent duplicate/skipped playback | Medium | High |
| Transcript search + semantic retrieval | Turns episodes into searchable knowledge | Medium | High |
| AI highlights and clip extraction | Shareability and creator growth | Medium | High |
| Personalized discovery feed | Daily return habit | High | High |
| Creator retention drop-off analytics | Better episode optimization | Medium | High |
| Listener-to-topic graph | Defensible recommendations and targeting | High | High |

## What was implemented in this remediation
- RSS episode identity canonicalization and dedupe normalization in ingestion.
- Idempotent feed refresh output ordering.
- Tests for malformed/missing GUID scenarios.

## Remaining platform-level work (outside current backend-only scope)
- First-party playback client (mobile/web) for queue/download/playback trust invariants.
- Download storage subsystem with checksums and local cache integrity checks.
- Real-time recommendation serving APIs fed by listener behavior events.
