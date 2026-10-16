---
name: write-cross-platform-content
description: Turn a single product topic, launch milestone, user question, or feature update into fact-checked, platform-native content packages for X, Reddit, Hacker News, Product Hunt, Medium, Dev.to, Hashnode, HackerNoon, YouTube, and SEO blogs. Rewrites titles, openings, tone, structure, link placement, and CTAs to suit each platform's culture while learning from past operations memory.
---

# Write Cross-Platform Content

Convert one source idea or product announcement into platform-native, high-conversion content. Reuse core facts, evidence, and architectural insights, while completely rewriting the hook, structure, tone, link placement, and CTA for every platform.

## Default Contract

- **Input:** Accepts a one-line brief, feature release note, user question, or link.
- **Fact Anchoring:** Always inspect `templates/product-fact-sheet.md` (or workspace product facts) before drafting. Never invent product features, pricing, performance benchmarks, or certifications.
- **Drafts First:** Produce ready-to-post drafts with metadata. Never publish or alter external platforms without explicit user authorization.
- **Single Objective per Variant:** Each platform version must focus on one core takeaway, one target reader profile, and one natural CTA.
- **Transparency:** Include team disclosure where community culture expects it (`Disclosure: I work on [Product]`).

## Platform Cultural Calibration

| Platform | Tone & Style | Opening Hook | Primary Goal | Link Placement |
| :--- | :--- | :--- | :--- | :--- |
| **X (Twitter)** | Direct, opinionated, fast-paced | Strong hook / counter-intuitive fact | Engagement, reposts, discussion | Reply to first tweet or thread end |
| **Reddit** | Vulnerable, pragmatic, anti-hype | Honest question / solved specific pain | Community feedback, trust | None by default; only when requested |
| **Hacker News** | Analytical, architectural, humble | "Show HN: [Product] - [What it does]" | Technical critique, engineer adoption | In main URL submission; transparent text |
| **Product Hunt** | Enthusiastic, concise, maker story | The origin story / why we built this | Upvotes, first-day trials, feedback | Product page link in first maker comment |
| **Medium / Blog**| Narrative, editorial, reflective | Compelling user story / industry trend | SEO, brand authority, newsletter signups | Contextual markdown links in body |
| **Dev.to / Hashnode**| Hands-on, code-first, tutorial | "How we solved X with Y" | Developer bookmarking, GitHub stars | GitHub repo link & live demo link |
| **YouTube** | Energetic, visual, step-by-step | Immediate demo of result in first 5s | Watch time, channel subs, download | Top pinned comment & description |

## Workflow

1. **Parse Input:** Identify the core thesis, the target persona, the friction eliminated, and requested channels.
2. **Retrieve Facts:** Ground every statement in `templates/product-fact-sheet.md`. Flag any unverified claims.
3. **Platform Adaptation:** Generate separate markdown files or blocks for each requested platform, fully tailored to character limits, formatting styles, and community redlines.
4. **Operations Learning (Self-Evolution):** Run `scripts/analyze_content_ops.py` to evaluate past performance logs (impressions, conversion, rejections) and automatically adjust platform selection and cadence.
5. **Quality Review:** Check against the pre-flight checklist:
   - Does it sound like a native post or an automated corporate press release?
   - Is the value immediately clear even if the user never clicks the link?
   - Are disclosure and attribution standards respected?
