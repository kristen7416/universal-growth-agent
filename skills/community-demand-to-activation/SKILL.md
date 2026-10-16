---
name: community-demand-to-activation
description: Search the web and supported communities (Reddit, Quora, X, YouTube, public forums) for current, real user questions matching your product, rank the opportunities, and draft or publish helpful, transparent, platform-compliant replies with optional UTM attribution and activation tracking. Suitable for community lead generation, social listening, answering user help requests, and converting discussions into SEO content.
---

# Community Demand To Activation

Search for concrete user questions first, then answer the best matches in their original context. Help the user solve their problem genuinely before presenting your product. Treat longer content and download attribution as optional follow-up work.

## Source Of Truth

Before making any product claims, read the product fact sheet in the workspace:
- `templates/product-fact-sheet.md` (or workspace equivalent product specification)

If sources conflict or a claim is marked conditional, preserve the uncertainty and keep that claim out of copy until confirmed. Never infer performance, privacy, pricing, background behavior, or full sync from a competitor or similar tool.

## Operating Modes

1. **Search and draft (default):** Search current public discussions, return qualified questions with ready-to-post native replies. Do not mutate external state.
2. **Search and publish:** Use only when the user explicitly asks to `直接评论`, `发布回复`, `post`, or otherwise authorizes publishing. Open the exact thread, verify the signed-in account and final preview, publish one reply at a time, and record the public URL and visible result.
3. **Given-link reply:** When the user supplies a URL, inspect that exact page and write or publish a contextual reply without broad searching unless requested.
4. **Content expansion:** Turn recurring high-intent questions into SEO blogs, YouTube tutorials, X threads, or landing-page use case cards.

## Search And Reply Workflow

1. **Define the search window:** Default to the last 30 days and English-language discussions. Search older durable Quora/Reddit questions only when they rank prominently for target queries.
2. **Search real discussions:** Use web search or browser tools to find Reddit posts/comments, Quora questions, YouTube comments, public forum threads, and X discussions. Discover via search engines, but reply only on the original platform.
3. **Verify every candidate:** Open the source page. Record the exact question, URL, date, platform, community, visible rules, user setup, current workaround, and specific pain point. Never invent a result or cite a snippet without full thread inspection.
4. **Filter before replying:** Reject deleted, locked, stale, off-topic, already-solved, promotional, hostile, duplicate, account-restricted, or self-promotion-prohibited threads. Do not revive a dormant thread merely to place a link.
5. **Rank qualified questions:** Score recency, problem specificity, product fit, ability to add new value, and reply permission from 1-5. Reply only when product fit and added value are each at least 3, and no platform rule blocks participation.
6. **Read the conversation:** Inspect the post and relevant existing replies so the answer does not repeat accepted advice, ignore constraints, or recommend an incompatible workflow.
7. **Answer first (Value First):** Directly solve the user's problem, mention credible free/native alternatives, and explain tradeoffs. The reply must remain completely useful even if the product recommendation is removed.
8. **Mention the product only when relevant:** Use one concise paragraph, disclose team affiliation (`Disclosure: I work on the [Product] team`), state applicable conditions/limitations, and avoid unsupported claims. Omit the product entirely when it is not an ideal fit.
9. **Handle links conservatively:** Do not include a link when the platform disallows it, the account is new, or the answer is already complete. When allowed and useful, use one destination-specific UTM link; never link every reply.
10. **Publish only with authority:** In publish mode, check the active account, thread URL, community rules, draft, disclosure, and link before clicking submit. Stop on login, CAPTCHA, rate limit, moderation warning, ambiguous account identity, or unexpected preview.
11. **Verify and record:** After publishing, reopen or inspect the page, confirm the reply is visible, save its URL, timestamp, account, source question, disclosure, UTM, and follow-up date.
12. **Follow up without spamming:** Answer genuine replies and corrections. Do not post near-identical answers across threads, chase users into DMs, or delete and repost around moderation.

## Community Channel Tactics

- **Reddit:** Prioritize recent help requests and workflow discussions. Follow subreddit rules, disclose team identity, and reply without a link first.
- **Quora:** Answer one durable question thoroughly and completely, then add one relevant link only when it directly aids the answer.
- **YouTube:** Reply to specific workflow questions when comments are accessible and the account can participate naturally.
- **Public forums / X:** Participate only when the question is directly relevant and the platform permits the account to reply.
- **SEO & Blog:** Expand recurring questions into how-to, troubleshooting, compatibility, and comparison pages.

## Safety & Ethics Redlines

- Disclose affiliation wherever platform rules require or where a recommendation could be misunderstood.
- Do not impersonate organic users, buy upvotes/likes, coordinate astroturfing, mass-DM, or evade moderation.
- Do not claim "100% free forever", "zero-knowledge", "unlimited speed", or "replaces everything" without hard facts.
- Exclude all personal data, private IPs, device tokens, and credentials from logs and screenshots.

## Output Contract

For `search-and-draft` work, return:
1. **Candidate Table:** Question, Date, Platform, URL, Fit Score, Reply Permission, Link Recommendation, and Rejection Reason.
2. **Ready-to-Post Native Replies:** High-quality replies for top-ranked questions, including disclosures and step-by-step guidance.
3. **Fact-Check & Blockers:** Any potential risks or blockers.
4. **UTM Attribution:** Formatted URL via `scripts/build_utm.py`.
