# Data Moats and Network Effects

## Compounding data systems
1. **Listener-topic affinity graph**
   - Nodes: listener, episode, topic, host.
   - Edges: completion, replay, skip, share, highlight.
   - Moat: improves recommendations and ad targeting over time.

2. **Episode concept clustering**
   - Build embeddings/clusters from transcripts + metadata.
   - Moat: semantic discovery and long-tail resurfacing.

3. **Creator performance benchmark graph**
   - Compare retention/drop-off curves by topic, format, duration.
   - Moat: creator optimization insights competitors cannot replicate quickly.

4. **Highlight and clip propagation graph**
   - Track which moments get clipped/shared and downstream engagement.
   - Moat: viral distribution intelligence.

## Near-term architecture recommendations
- Event schema for listening primitives: start, pause, seek, complete, skip, share.
- Daily feature store aggregation (listener × topic, creator × episode, clip × engagement).
- Hybrid recommendation scoring: collaborative + content + recency/diversity.
