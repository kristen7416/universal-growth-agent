# Community Demand-to-Activation Content Guidance

## 1. Goal & Loop

Proactively discover real user discussions and questions where users are trying to accomplish a specific task. Deliver value first in the native context, then guide high-intent users through a measurable activation funnel:

```
Search Real Questions -> Filter Opportunities -> High-Value Reply -> Target Landing/Download Page -> First Value Moment (Activation)
```

Never measure success solely by vanity impressions or raw link clicks. Prioritize users experiencing genuine blockers.

---

## 2. Searching for Questions

Default to recent (last 30 days) discussions. Always open and inspect the actual thread (Reddit, Quora, X, YouTube, Forums) before scoring.

Record each candidate in this format:
```text
Original Quote | Thread URL | Post Date | Community / Platform | User Setup / OS | Current Workaround | Pain Point | Can Reply? | Can Link? | Next Action
```

### Search Queries Construction Formulas

- **Pain point / alternative:**
  `site:reddit.com "[task]" "[current problem/error]"`
  `site:reddit.com "alternative to [competitor]" "[platform]"`
- **How-to questions:**
  `site:quora.com "how to [accomplish goal] without [friction]"`
- **Workflow / Tutorial requests:**
  `site:youtube.com "[goal] workflow" "[system]"`
  `"best tool for [specific workflow]" forum`

---

## 3. Opportunity Scoring Matrix (1 to 5 Points Each)

| Metric | Score 1-2 | Score 3-4 | Score 5 |
| :--- | :--- | :--- | :--- |
| **Recency** | > 6 months old | 1 - 4 weeks old | < 48 hours old |
| **Problem Specificity** | Vague complaint ("it sucks") | Specific error or workflow friction | Detailed environment, attempted fixes, clear bottleneck |
| **Product Fit** | Cannot solve directly | Solves part of the problem | Solves the exact blocker directly and elegantly |
| **Added Value** | Repeats existing answers | Adds new insight/tradeoff analysis | Provides comprehensive step-by-step resolution |
| **Community Permission**| Strictly no self-promo / locked | Self-promo allowed with disclosure | Welcomes tools/recommendations |

> **Threshold:** Only proceed with drafting/replying if **Product Fit >= 3** AND **Added Value >= 3**, and the thread is not locked or hostile.

---

## 4. Reply Templates

### Reddit Native Reply Template
```text
[Directly address the user's question with the most straightforward native/free fix or workaround.]

Here are the key tradeoffs to consider:
1. Native method: [Explain native pros/cons]
2. Cloud/Alternative method: [Explain pros/cons]

[Optional - Only if strictly relevant and helpful:]
Disclosure: I work on the [Product Name] team. If you're looking for a dedicated tool that [solves exact pain point], [Product Name] handles this by [briefly state mechanism]. [State any limitations: e.g. requires both devices online].

Hope this helps point you in the right direction!
```

### Quora Detailed Answer Template
```text
Summary: [Direct conclusion answering the question in 1-2 sentences].

Detailed Steps:
- Step 1: [Actionable advice]
- Step 2: [Actionable advice]
- Step 3: [Actionable advice]

Comparison of Approaches:
[Table or bullet points comparing speed, complexity, and cost].

Disclosure: I'm part of the team behind [Product Name]. We built it specifically to address [pain point] by [mechanism]. You can check it out if [condition matches user].
```

---

## 5. UTM Tracking Schema

Use standardized parameters:
- `utm_source`: `reddit`, `quora`, `x`, `youtube`, `forum`
- `utm_medium`: `comment`, `thread`, `reply`, `bio`
- `utm_campaign`: `community_qna` or `[feature_name]`
- `utm_content`: `[subreddit_name_or_thread_id]`
