# Content Package Contract

Use this structure for a complete saved deliverable. Adapt numbering to existing project conventions.

```text
YYYY-MM-DD-topic-slug/
├── 00-publication-index.md
├── 01-brief-and-fact-ledger.md
├── 02-master-content.md
├── 03-medium.md
├── 04-quora.md
├── 05-x.md
├── 06-reddit.md
├── 07-hacker-news.md
├── 08-product-hunt.md
├── 09-github.md
├── 10-seo.md
├── 11-youtube.md
├── 12-devto.md
├── 13-hashnode.md
├── 14-hackernoon.md
└── 15-reuse-map.md
```

Create only requested or appropriate platform files. Keep the numbering stable within the package even when some platforms are omitted.

## Publication index

```markdown
# Publication Index

## Core decision

- Topic:
- Source insight:
- Primary audience:
- Objective:
- Primary platform:
- Single CTA:
- Language:

## Platform status

| Platform | Artifact | Status | Recommended timing | Link | Notes/blocker |
|---|---|---|---|---|---|

## Important conditions

-

## Required approvals

-
```

Use statuses: `draft`, `needs-fact-check`, `needs-platform-check`, `ready-to-publish`, `published`, `not-recommended`, or `blocked`.

## Brief and fact ledger

```markdown
# Brief and Fact Ledger

## Content brief

- User wording/source:
- User situation:
- One-sentence answer:
- Supporting points:
- Evidence:
- Limitations:
- CTA:

## Claims

| Claim | Status | Evidence/source | Checked date | Allowed wording | Notes |
|---|---|---|---|---|---|

## Assumptions and open questions

-
```

Never mark a package `ready-to-publish` while a material claim remains `unknown` or the draft still contains `[NEEDS CONFIRMATION]`.

## Platform file template

Keep operational metadata outside the copy block.

```markdown
# [Platform] Version

## Publication metadata

- Account:
- Format:
- Objective:
- Audience/context:
- CTA:
- Destination URL:
- UTM URL:
- Disclosure required:
- Fact-check status:
- Platform-check status:
- Recommended timing:

## Publish-ready copy

[Exact text to paste]

## Assets

-

## First responses

-

## Final preview checks

- [ ] No unsupported claim or unresolved placeholder.
- [ ] Conditions and limitations are visible.
- [ ] Identity/AI/sponsorship disclosure is correct.
- [ ] Link, formatting, and current field limits are valid.
- [ ] The text is native to this platform and not a duplicate.
```

## Reuse map

```markdown
# Reuse Map

| Content atom | Source | Platform adaptations | Asset | Feedback to collect |
|---|---|---|---|---|

## Recommended sequence

| Day | Platform/action | Purpose | Dependency |
|---|---|---|---|

## Feedback loop

- New question -> content idea backlog.
- Feature request -> user feedback tracker.
- Fact correction -> update the master and every derivative.
- Repeated objection -> FAQ or product documentation.
- Authorized user story -> case-study library.
```

## Link attribution

When a real destination exists, use a distinct UTM per platform:

```text
utm_source=reddit|quora|x|github|hackernews|producthunt|medium|youtube|devto|hashnode|hackernoon|google
utm_medium=community|answer|social|repository|launch|article|video|organic
utm_campaign=<stable-topic-or-launch-name>
utm_content=<content-id-or-variant>
```

Do not invent a destination URL. Prefer the page that directly completes the promised next step rather than sending every CTA to the homepage.
