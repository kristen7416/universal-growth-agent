#!/usr/bin/env python3
"""Build a canonical campaign URL with UTM parameters."""

import argparse
from urllib.parse import urlencode, urlsplit, urlunsplit, parse_qsl


def build_utm_url(base_url: str, source: str, medium: str, campaign: str, content: str = "") -> str:
    parts = urlsplit(base_url)
    if parts.scheme not in {"http", "https"} or not parts.netloc:
        raise ValueError("base_url must be an absolute http(s) URL")
    
    params = dict(parse_qsl(parts.query, keep_blank_values=True))
    params.update(
        {
            "utm_source": source.lower(),
            "utm_medium": medium.lower(),
            "utm_campaign": campaign.lower(),
        }
    )
    if content:
        params["utm_content"] = content.lower()
        
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(params), parts.fragment))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate standardized UTM campaign URLs")
    parser.add_argument("base_url", help="Destination landing page URL")
    parser.add_argument("--source", required=True, help="utm_source (e.g., reddit, x, quora, producthunt)")
    parser.add_argument("--medium", required=True, help="utm_medium (e.g., comment, thread, bio, social)")
    parser.add_argument("--campaign", required=True, help="utm_campaign (e.g., launch_v1, community_qa)")
    parser.add_argument("--content", default="", help="utm_content (e.g., thread_id, banner_cta)")
    args = parser.parse_args()

    try:
        url = build_utm_url(args.base_url, args.source, args.medium, args.campaign, args.content)
        print(url)
    except Exception as e:
        parser.error(str(e))


if __name__ == "__main__":
    main()
