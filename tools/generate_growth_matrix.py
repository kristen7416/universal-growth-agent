#!/usr/bin/env python3
"""Generate a complete 12-channel lifecycle operations growth matrix for any product."""

import argparse
import csv
import sys

CHANNELS = [
    # 实时社媒
    ("Real-time Social", "X (Twitter)", "https://x.com", "P0", "Validation / Beta / Launch / Growth",
     "Build in public, product demos, engineering trade-offs, launch amplification. Use founder accounts.",
     "Makers, developers, power users", "Daily 1-2 tweets, 1 weekly thread", "Avoid spamming naked links; be transparent about failures and choices."),
    ("Real-time Social", "Bluesky", "https://bsky.app", "P1", "Validation / Beta / Growth",
     "Engage in local-first, privacy, and open web discussions. Repurpose technical X content.",
     "Privacy-conscious users, open-source enthusiasts", "1 post daily or 5/week", "Best for conversations, not aggressive conversion."),
    ("Real-time Social", "LinkedIn", "https://www.linkedin.com", "P1", "Beta / Growth / Mature",
     "Target freelancers, small business owners, and remote teams focusing on productivity, security, and efficiency.",
     "Freelancers, consultants, founders, remote teams", "3 posts/week, direct outreach", "Focus on workflow efficiency, ROI, and enterprise data security."),
    ("Real-time Social", "Mastodon", "https://joinmastodon.org", "P1", "Validation / Beta / Growth",
     "Share privacy architecture, open roadmap, and technical specs.",
     "Linux, self-hosted, open-source users", "3-5 posts/week", "Community hates overt marketing; lead with authentic technical value."),
    ("Real-time Social", "Threads", "https://threads.net", "P2", "Launch / Growth",
     "Lightweight pain-point visual posts and creator workflow reels.",
     "Creators, general mobile users", "3-5 posts/week", "Top-of-funnel brand awareness."),

    # 社区论坛
    ("Community Forums", "Reddit", "https://reddit.com", "P0", "Validation / Beta / Launch / Growth",
     "Search for real user pain points in relevant subreddits. Answer thoroughly before mentioning your tool. Observe 10:1 contribution ratio.",
     "Power users, creators, tech early adopters", "10 thoughtful replies daily, 1 deep post weekly", "Strict self-promo rules; always disclose team affiliation."),
    ("Community Forums", "Hacker News", "https://news.ycombinator.com", "P0", "Beta / Launch",
     "Submit 'Show HN' when fully testable. Detail technical architecture, trade-offs, limitations, and security model.",
     "Engineers, technical founders, hackers", "Pre-launch participation, full-day launch day engagement", "Zero marketing fluff; be radically candid about constraints."),
    ("Community Forums", "Indie Hackers", "https://indiehackers.com", "P0", "Validation / Beta / Growth",
     "Share build process, interview insights, conversion data, and pricing experiments.",
     "Indie makers, boot-strappers, SaaS builders", "2-3 posts/week", "Transparency and numbers beat promotional copy."),

    # 文章平台 / SEO
    ("SEO & Articles", "Owned Blog", "Official Site", "P0", "Validation / Beta / Launch / Growth",
     "Main SEO engine: publish How-to guides, competitor comparison pages, troubleshooting guides, and workflow tutorials.",
     "High-intent search users", "1-2 posts/week, 30-50 articles in first 90 days", "All external distributed content must canonical back to main site."),
    ("SEO & Articles", "Medium", "https://medium.com", "P2", "Beta / Growth",
     "Publish founder essays, problem breakdowns, and creator workflows for secondary distribution.",
     "General tech readers, creators", "1 post/week or cross-post", "Always set canonical link back to official blog."),
    ("SEO & Articles", "Dev.to", "https://dev.to", "P1", "Beta / Growth",
     "Deep-dive technical articles: architecture, performance, cross-platform challenges, protocols.",
     "Developers, technical users", "1 post/week", "Must contain real technical substance, code snippets, or architecture diagrams."),

    # 视频平台
    ("Video Platforms", "YouTube", "https://youtube.com", "P0", "Beta / Launch / Growth",
     "Long-form workflow tutorials + Shorts demos. Show complete end-to-end task execution in real-time.",
     "Visual learners, workflow optimizers", "1 long video weekly + 2-3 Shorts", "Optimize title and description for long-term search intent."),
    ("Video Platforms", "Loom", "https://loom.com", "P1", "Beta / Growth",
     "Send personalized 1-on-1 walkthroughs and onboarding videos to beta users and key leads.",
     "Beta testers, VIP users", "On-demand per user interaction", "Extremely effective for feedback collection and activation."),

    # 开源与目录
    ("Open Source / Dev", "GitHub", "https://github.com", "P0", "Beta / Launch / Growth",
     "Open-source core components or maintain public roadmap, docs, and issue tracker.",
     "Developers, technical evaluators", "Continuous release notes and issue triage", "Be transparent about protocols, licenses, and security boundaries."),
    ("Open Source / Dev", "AlternativeTo", "https://alternativeto.net", "P0", "Launch / Growth",
     "List as a clean alternative to legacy incumbent tools. Monitor competitor pages.",
     "High-intent users seeking software alternatives", "Submit at Launch, review monthly", "Keep comparison fair and objective."),

    # 产品发布
    ("Product Launch", "Product Hunt", "https://producthunt.com", "P0", "Launch",
     "Concentrated launch day push with verified hunter, maker story, demo GIFs, and launch day trial discount.",
     "Early adopters, tech enthusiasts", "1 primary launch, follow-up on major v2.0", "Product must be immediately testable without friction."),
    ("Product Launch", "BetaList", "https://betalist.com", "P1", "Beta",
     "Recruit first 100 beta testers with a clear value proposition.",
     "Early tech testers", "One-time submission during Beta", "Clear landing page and signup flow."),

    # 应用商店
    ("App Stores", "Apple App Store / Google Play", "App Stores", "P0", "Beta / Launch / Growth",
     "Mobile conversion engine. ASO keyword optimization, clear preview screenshots, and fast review response.",
     "Mobile users", "Monthly ASO keyword and visual iteration", "Handle permissions and privacy disclosures clearly."),
]


def generate_markdown(product_name: str) -> str:
    lines = [
        f"# {product_name} - 12-Channel Lifecycle Growth Matrix",
        "",
        "> Generated automatically by Universal Growth Agent Toolkit",
        "",
        "| Category | Platform | Priority | Lifecycle Stage | Strategy & Tactics | Target Audience | Frequency | Guidelines & Redlines |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for row in CHANNELS:
        lines.append(f"| **{row[0]}** | [{row[1]}]({row[2]}) | `{row[3]}` | {row[4]} | {row[5]} | {row[6]} | {row[7]} | {row[8]} |")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate 12-channel growth matrix")
    parser.add_argument("--product", default="YourProduct", help="Product Name")
    parser.add_argument("--format", choices=["markdown", "csv"], default="markdown", help="Output format")
    parser.add_argument("--output", help="Output file path (default stdout)")
    args = parser.parse_args()

    if args.format == "markdown":
        content = generate_markdown(args.product)
    else:
        # CSV format
        output = sys.stdout
        writer = csv.writer(output)
        writer.writerow(["Category", "Platform", "URL", "Priority", "Lifecycle Stage", "Strategy", "Target Audience", "Frequency", "Redlines"])
        for row in CHANNELS:
            writer.writerow(row)
        return

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Matrix successfully generated at: {args.output}")
    else:
        print(content)


if __name__ == "__main__":
    main()
