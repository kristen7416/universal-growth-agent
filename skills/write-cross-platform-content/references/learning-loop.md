# Data-Driven Learning Loop

Use this reference when publication records, performance data, channel strategy, or retrospective analysis is in scope.

## Data layers

Keep four layers separate:

1. **Product facts**: approved capabilities, conditions, prices, privacy, compatibility, and claims. Performance data cannot modify this layer.
2. **Raw observations**: platform metrics, moderation events, links, timestamps, and technical failures.
3. **Hypotheses**: explanations that still require comparable tests.
4. **Operating decisions**: platform mode, cadence, format, next experiment, stop condition, and recovery condition.

Never convert a platform metric directly into a product claim or a customer-demand claim.

## Workspace discovery

Prefer existing conventions. Common inputs are:

- `05-执行与记录/*海外平台发布结果.md`
- `05-执行与记录/运营学习/*platform-metrics.json`
- `05-执行与记录/运营学习/strategy-memory.json`
- content calendars, published-content indexes, UTM reports, product activation reports, and platform analytics exports

If the workspace uses different paths, locate them with `rg --files` and pass explicit paths to the analyzer.

Refresh memory with:

```bash
python3 <skill-dir>/scripts/analyze_content_ops.py \
  --workspace <workspace> \
  --output <workspace>/05-执行与记录/运营学习/strategy-memory.json \
  --markdown-output <workspace>/05-执行与记录/运营学习/strategy-memory.md
```

The analyzer reads all matching publication-result Markdown files and metric snapshots in the operations-learning directory. It writes deterministic evidence summaries and provisional platform modes.

## Metric snapshot contract

Store one immutable snapshot per collection time. Do not overwrite earlier snapshots.

```json
{
  "schema_version": 1,
  "as_of": "2026-08-17T18:00:00+08:00",
  "window": "platform-specific; state it explicitly",
  "platforms": {
    "X": {
      "metrics": {
        "sample_size": 5,
        "median_impressions": 33,
        "organic_engagements": 0
      },
      "measurement_gaps": ["No attributed installs"],
      "source": "Post analytics and public post pages"
    }
  }
}
```

Use explicit metric names and units. Include `sample_size`, `window`, and `source`. Use `null` for unavailable data; never replace missing data with zero.

## Decision discipline

- Treat one result as an observation.
- Treat three comparable results as a directional pattern.
- Require repeated downstream outcomes before scaling a channel.
- Give moderation, policy, account, privacy, or factual-integrity signals immediate weight even with one event.
- Time-decay channel conclusions after 30 days unless the blocker is still visibly active.
- Compare like with like: format, audience, age, CTA, distribution method, and observation window.
- Exclude self-replies, operator previews, test clicks, and unrelated viral content from organic product-performance conclusions.

Platform modes are provisional:

| Mode | Meaning | Default action |
|---|---|---|
| `scale` | Repeated downstream signal | Increase only the validated format and keep measurement. |
| `test` | Plausible but unproven | Run one named experiment with a stop condition. |
| `maintain` | Useful presence, limited evidence | Keep low frequency and reuse strong source material. |
| `reduce` | Repeated weak distribution or engagement | Publish only stronger, materially different evidence. |
| `pause` | Moderation risk or strongly negative efficiency | Stop routine submissions until recovery condition is met. |
| `blocked` | Access, platform, tooling, or measurement prevents execution | Resolve the blocker before creating more drafts. |
| `measure` | Content exists but outcomes are unknown | Collect metrics before increasing volume. |

## Funnel priority

Prefer downstream evidence in this order:

1. first successful product action;
2. activation or install;
3. installer/download completion;
4. qualified landing-page visit;
5. platform click or profile visit;
6. meaningful comment, save, or reply;
7. view, impression, or reaction.

A large top-of-funnel number from an unrelated topic is audience-mismatch evidence, not product-channel success.

## Evolution output

Strategy memory must retain:

- data cutoff and sources;
- platform operational counts;
- latest comparable metrics;
- confidence and measurement gaps;
- provisional mode with reasons;
- next experiment and stop/recovery condition;
- unresolved access, compliance, or factual blockers.

Do not store credentials, private identifiers, raw user messages, private file names, or browsing history in strategy memory.
