# Discovery Engine Design

## Objective
Recommend podcasts/episodes using blended behavioral and content signals.

## Signals
- Session duration and completion ratio
- Skips and replays
- Topic overlap from transcript/topic tags
- Host affinity and recency

## Scoring model
`score = 0.35 * collaborative + 0.35 * content_similarity + 0.15 * recency + 0.10 * diversity + 0.05 * creator_quality`

## Pipeline
1. Ingest events (start/pause/seek/complete/skip/share).
2. Aggregate daily features in a feature store.
3. Generate candidate sets (co-listened, topic-neighbor, trending niches).
4. Re-rank with diversity and novelty constraints.
5. Log impression/click/complete for continual learning.

## Guardrails
- Cold-start fallback to topic + editorial pools.
- Explicit diversity constraints to avoid filter bubbles.
- Tenant/user isolation for event data access.
