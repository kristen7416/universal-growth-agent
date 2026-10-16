---
name: platform-growth-matrix
description: Plan and orchestrate full-lifecycle overseas and domestic growth operations across 12 distinct channel categories (real-time social, community forums, SEO articles, video platforms, image/visual platforms, open-source/developer hubs, product launch platforms, software directories, app stores, Q&A sites, chat communities, newsletters/podcasts) from Validation to Beta, Launch, and Growth stages.
---

# Platform Growth Matrix & Lifecycle Strategy

A systematic methodology to select, prioritize, and execute marketing across 12 channel categories according to the product's current lifecycle stage.

## 1. The 4 Product Lifecycle Stages

| Stage | Duration | Primary Objective | Core Channels |
| :--- | :--- | :--- | :--- |
| **Stage 1: Validation (验证期)** | Day 1 - 30 | Problem-solution fit, pain point verification | X (Build in public), Reddit comments, Discord |
| **Stage 2: Beta / Seed (测试期)** | Day 30 - 60 | 50-200 active beta users, 1-on-1 feedback | BetaList, MicroLaunch, Indie Hackers, Loom |
| **Stage 3: Launch (集中爆发期)** | Day 60 - 90 | Public visibility, initial downloads, backlinks | Product Hunt, Hacker News, AlternativeTo, Press |
| **Stage 4: Growth (复利增长期)** | Day 90+ | Sustainable organic search & referral flywheel | Owned SEO Blog, YouTube Video SEO, ASO |

---

## 2. The 12 Channel Categories & Priority Matrix

| Category | Priority | Role & Tactics | Key Metrics |
| :--- | :--- | :--- | :--- |
| **1. Real-time Social** (X, Bluesky, Mastodon, Threads, LinkedIn) | **P0 - P1** | Founder trust, Build-in-Public, engineering decisions, launch amplifications. Avoid dry link spam. | Engagement rate, DMs, Waitlist conversions |
| **2. Community Forums** (Reddit, Hacker News, Indie Hackers, Niche Forums) | **P0** | Answer real problems first; 10 value replies before 1 tool mention. Respect community self-promo rules. | Upvotes, interview invites, beta signups |
| **3. SEO & Articles** (Owned Blog, Medium, Dev.to, Hashnode, Substack) | **P0 - P1** | Own long-term search intent. Produce "How to", "Alternatives to X", and "Fix Y" articles. Canonical back to main site. | Organic search clicks, download conversions |
| **4. Video Platforms** (YouTube, TikTok, Reels, Loom) | **P0 - P2** | YouTube is mandatory for long-term video SEO. Loom for 1-on-1 onboarding and user feedback. | Retention rate, CTR, activation |
| **5. Visual Platforms** (Instagram, Pinterest, Dribbble, Behance) | **P2 - P3** | Workflow diagrams, UI visual polish, creator aesthetics. | Saves, shares, bio link clicks |
| **6. Open-Source / Dev Hubs** (GitHub, AlternativeTo, SourceForge) | **P0** | Establish technical trust; capture high-intent competitor replacement searches on AlternativeTo. | Stars, issues, referral traffic |
| **7. Product Launch Platforms** (Product Hunt, BetaList, Uneed, MicroLaunch) | **P0 - P1** | Concentrated launch day traffic and early adopter feedback. Requires a fully testable build. | Upvotes, trial activations, feedback |
| **8. Software Directories** (SaaSHub, Softpedia, FileHorse, G2, Capterra) | **P1 - P3** | Long-tail desktop/software download authority and social proof reviews. | Directory clicks, review score |
| **9. App Stores** (App Store, Google Play, Microsoft Store, Mac App Store) | **P0** | Mobile conversion bedrock. Continuous ASO on keywords, icons, and first 3 screenshots. | Listing views, installs, ratings |
| **10. Q&A Platforms** (Quora, Stack Exchange, Super User) | **P2** | Answer durable high-volume technical questions. Give complete answers, disclaim team role. | Answer views, referral visits |
| **11. Chat Communities** (Discord, Slack, Telegram) | **P1** | Direct feedback channel, high-touch beta tester relationships. | Active discussions, bug reports, retention |
| **12. Newsletters & Podcasts** (Substack, Niche Tech Newsletters, Podcasts) | **P2 - P3** | Deep brand endorsement and founder narrative. Best suited for post-launch growth. | Sponsorship ROI, brand mentions |

---

## 3. Automation Tooling

To generate an updated CSV or Markdown spreadsheet mapping these channels to your specific product:
```bash
python3 tools/generate_growth_matrix.py --product "YourProduct" --output ./growth_matrix.md
```
