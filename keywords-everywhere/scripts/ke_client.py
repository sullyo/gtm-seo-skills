#!/usr/bin/env python3
"""
Keywords Everywhere CLI Client
===============================
Python wrapper for the Keywords Everywhere REST API.
All endpoints verified and tested against the live API.


Available REST Endpoints:
  - GET  account/credits
  - GET  countries
  - GET  currencies
  - POST get_keyword_data         (params: kw[], country, currency, dataSource)
  - POST get_related_keywords     (params: keyword, num, country, currency)
  - POST get_pasf_keywords        (params: keyword, num, country, currency)
  - POST get_domain_keywords      (params: domain, num, country, currency)
  - POST get_domain_backlinks     (params: domain, num)
  - POST get_unique_domain_backlinks (params: domain, num)
  - POST get_url_keywords         (params: url, num, country, currency)
  - POST get_page_backlinks       (params: page, num)
  - POST get_unique_page_backlinks (params: page, num)

Note: Domain/URL traffic endpoints are only available via the MCP connector,
not the REST API. Use the MCP tools (get_domain_traffic, get_url_traffic)
in Claude for traffic data.
"""

import argparse
import json
import sys
from time import sleep
from typing import Any

try:
    import requests
except ImportError:
    print(
        "Missing dependency. Install with:\n  pip install requests --break-system-packages",
        file=sys.stderr,
    )
    sys.exit(1)

# ──────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────
import os

API_KEY = os.environ.get("KEYWORDS_EVERYWHERE_API_KEY", "")
if not API_KEY:
    print(
        "Error: KEYWORDS_EVERYWHERE_API_KEY environment variable is not set.\n"
        "Get your API key from https://keywordseverywhere.com/api-settings.html\n"
        "Then set it:\n"
        "  export KEYWORDS_EVERYWHERE_API_KEY='your-api-key-here'",
        file=sys.stderr,
    )
    sys.exit(1)

BASE_URL = "https://api.keywordseverywhere.com/v1"
HEADERS = {
    "Accept": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}
MAX_KEYWORDS_PER_REQUEST = 100


# ──────────────────────────────────────────────
# HTTP Helpers
# ──────────────────────────────────────────────
def api_post(endpoint: str, data: dict) -> dict:
    """POST request to the Keywords Everywhere API."""
    url = f"{BASE_URL}/{endpoint}"
    resp = requests.post(url, data=data, headers=HEADERS, timeout=30)
    if resp.status_code != 200:
        print(f"API Error ({resp.status_code}): {resp.text}", file=sys.stderr)
        sys.exit(1)
    return resp.json()


def api_get(endpoint: str) -> Any:
    """GET request to the Keywords Everywhere API."""
    url = f"{BASE_URL}/{endpoint}"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    if resp.status_code != 200:
        print(f"API Error ({resp.status_code}): {resp.text}", file=sys.stderr)
        sys.exit(1)
    return resp.json()


# ──────────────────────────────────────────────
# Display Helpers
# ──────────────────────────────────────────────
def print_table(rows: list[dict], columns: list[str] | None = None):
    """Pretty-print a list of dicts as an aligned table."""
    if not rows:
        print("(no results)")
        return
    if columns is None:
        columns = list(rows[0].keys())
    columns = [c for c in columns if any(c in row for row in rows)]
    if not columns:
        columns = list(rows[0].keys())
    widths = {c: len(str(c)) for c in columns}
    for row in rows:
        for c in columns:
            val = row.get(c, "")
            if isinstance(val, dict):
                val = val.get("value", val)
            widths[c] = max(widths[c], min(len(str(val)), 80))
    header = " | ".join(str(c).ljust(widths[c]) for c in columns)
    sep = "-+-".join("-" * widths[c] for c in columns)
    print(header)
    print(sep)
    for row in rows:
        parts = []
        for c in columns:
            val = row.get(c, "")
            if isinstance(val, dict):
                val = val.get("value", val)
            s = str(val)
            if len(s) > 80:
                s = s[:77] + "..."
            parts.append(s.ljust(widths[c]))
        print(" | ".join(parts))


def output_result(data: Any, fmt: str, table_columns: list[str] | None = None):
    """Output data in the requested format."""
    if fmt == "json":
        print(json.dumps(data, indent=2, default=str))
        return

    if isinstance(data, dict):
        if "data" in data and isinstance(data["data"], list):
            credits_used = data.get("credits_consumed", "")
            time_taken = data.get("time_taken", "")
            info_parts = []
            if credits_used:
                info_parts.append(f"credits used: {credits_used}")
            if time_taken:
                info_parts.append(f"time: {time_taken}s")
            if info_parts:
                print(f"({', '.join(info_parts)})")
            if data["data"] and isinstance(data["data"][0], dict):
                print_table(data["data"], table_columns)
            elif data["data"] and isinstance(data["data"][0], str):
                for kw in data["data"]:
                    print(f"  {kw}")
            else:
                print("(no results)")
        else:
            for k, v in data.items():
                if isinstance(v, list) and v and isinstance(v[0], dict):
                    print(f"\n── {k} ──")
                    print_table(v)
                else:
                    print(f"{k}: {v}")
    elif isinstance(data, list):
        if data and isinstance(data[0], dict):
            print_table(data, table_columns)
        else:
            for item in data:
                print(item)
    else:
        print(data)


# ──────────────────────────────────────────────
# Keyword batching
# ──────────────────────────────────────────────
def batch_keywords(keywords: list[str]) -> list[list[str]]:
    """Split keywords into batches of 100 (API max per request)."""
    return [
        keywords[i : i + MAX_KEYWORDS_PER_REQUEST]
        for i in range(0, len(keywords), MAX_KEYWORDS_PER_REQUEST)
    ]


# ──────────────────────────────────────────────
# Commands
# ──────────────────────────────────────────────


def cmd_credits(args):
    result = api_get("account/credits")
    if isinstance(result, list) and result:
        print(f"Remaining credits: {result[0]:,}")
    else:
        output_result(result, args.output)


def cmd_countries(args):
    result = api_get("countries")
    if args.output == "json":
        print(json.dumps(result, indent=2))
    else:
        if isinstance(result, dict):
            for code, name in sorted(result.items(), key=lambda x: x[1]):
                print(f"  {code or '(empty)':>5}  {name}")


def cmd_currencies(args):
    result = api_get("currencies")
    if args.output == "json":
        print(json.dumps(result, indent=2))
    else:
        if isinstance(result, dict):
            for code, name in sorted(result.items(), key=lambda x: x[1]):
                print(f"  {code or '(empty)':>5}  {name}")


def cmd_keyword_data(args):
    all_data = []
    batches = batch_keywords(args.keywords)
    for i, batch in enumerate(batches):
        if i > 0:
            sleep(1)
            print(f"Processing batch {i + 1}/{len(batches)}...", file=sys.stderr)
        result = api_post(
            "get_keyword_data",
            {
                "kw[]": batch,
                "country": args.country,
                "currency": args.currency,
                "dataSource": "gkp",
            },
        )
        if "data" in result:
            all_data.extend(result["data"])
    output_result(
        {"data": all_data},
        args.output,
        ["keyword", "vol", "cpc", "competition", "trend"],
    )


def cmd_related(args):
    result = api_post(
        "get_related_keywords",
        {
            "keyword": args.keyword,
            "num": args.num,
            "country": args.country,
            "currency": args.currency,
        },
    )
    output_result(result, args.output, ["keyword", "vol", "cpc", "competition"])


def cmd_pasf(args):
    result = api_post(
        "get_pasf_keywords",
        {
            "keyword": args.keyword,
            "num": args.num,
            "country": args.country,
            "currency": args.currency,
        },
    )
    output_result(result, args.output, ["keyword", "vol", "cpc", "competition"])


def cmd_domain_keywords(args):
    result = api_post(
        "get_domain_keywords",
        {
            "domain": args.domain,
            "num": args.num,
            "country": args.country,
            "currency": args.currency,
        },
    )
    output_result(
        result, args.output, ["keyword", "estimated_monthly_traffic", "serp_position"]
    )


def cmd_domain_backlinks(args):
    result = api_post(
        "get_domain_backlinks",
        {
            "domain": args.domain,
            "num": args.num,
        },
    )
    output_result(
        result,
        args.output,
        ["domain_source", "url_source", "anchor_text", "url_target"],
    )


def cmd_domain_unique_backlinks(args):
    result = api_post(
        "get_unique_domain_backlinks",
        {
            "domain": args.domain,
            "num": args.num,
        },
    )
    output_result(
        result,
        args.output,
        ["domain_source", "url_source", "anchor_text", "url_target"],
    )


def cmd_url_keywords(args):
    result = api_post(
        "get_url_keywords",
        {
            "url": args.url,
            "num": args.num,
            "country": args.country,
            "currency": args.currency,
        },
    )
    output_result(
        result, args.output, ["keyword", "estimated_monthly_traffic", "serp_position"]
    )


def cmd_page_backlinks(args):
    result = api_post(
        "get_page_backlinks",
        {
            "page": args.url,  # API uses 'page' not 'url'
            "num": args.num,
        },
    )
    output_result(
        result,
        args.output,
        ["domain_source", "url_source", "anchor_text", "url_target"],
    )


def cmd_page_unique_backlinks(args):
    result = api_post(
        "get_unique_page_backlinks",
        {
            "page": args.url,  # API uses 'page' not 'url'
            "num": args.num,
        },
    )
    output_result(
        result,
        args.output,
        ["domain_source", "url_source", "anchor_text", "url_target"],
    )


# ──────────────────────────────────────────────
# CLI Parser
# ──────────────────────────────────────────────


def build_parser():
    parser = argparse.ArgumentParser(
        prog="ke_client",
        description="Keywords Everywhere CLI — SEO/SEM data from the command line\n\n"
        "API key is read from the KEYWORDS_EVERYWHERE_API_KEY environment variable.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--output",
        "-o",
        choices=["table", "json"],
        default="table",
        help="Output format (default: table)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # Account
    sub.add_parser("credits", help="Check API credit balance")
    sub.add_parser("countries", help="List supported country codes")
    sub.add_parser("currencies", help="List supported currency codes")

    # Keyword research
    p = sub.add_parser("keyword-data", help="Get volume, CPC & competition")
    p.add_argument(
        "--keywords",
        "-k",
        nargs="+",
        required=True,
        help="Keywords to analyze (auto-batches >100)",
    )
    p.add_argument("--country", "-c", default="us", help="Country code (default: us)")
    p.add_argument("--currency", default="usd", help="Currency code (default: usd)")

    p = sub.add_parser("related", help="Get related keywords")
    p.add_argument("--keyword", "-k", required=True, help="Seed keyword")
    p.add_argument("--num", "-n", type=int, default=10, help="Results (max 1000)")
    p.add_argument("--country", "-c", default="us", help="Country code")
    p.add_argument("--currency", default="usd", help="Currency code")

    p = sub.add_parser("pasf", help="'People Also Search For' keywords")
    p.add_argument("--keyword", "-k", required=True, help="Seed keyword")
    p.add_argument("--num", "-n", type=int, default=10, help="Results (max 1000)")
    p.add_argument("--country", "-c", default="us", help="Country code")
    p.add_argument("--currency", default="usd", help="Currency code")

    # Domain analysis
    p = sub.add_parser("domain-keywords", help="Keywords a domain ranks for")
    p.add_argument("--domain", "-d", required=True, help="Domain (e.g. example.com)")
    p.add_argument("--num", "-n", type=int, default=10, help="Results")
    p.add_argument("--country", "-c", default="us", help="Country code")
    p.add_argument("--currency", default="usd", help="Currency code")

    p = sub.add_parser("domain-backlinks", help="Backlinks to a domain")
    p.add_argument("--domain", "-d", required=True, help="Domain")
    p.add_argument("--num", "-n", type=int, default=10, help="Results")

    p = sub.add_parser("domain-unique-backlinks", help="Unique referring domains")
    p.add_argument("--domain", "-d", required=True, help="Domain")
    p.add_argument("--num", "-n", type=int, default=10, help="Results")

    # URL / Page analysis
    p = sub.add_parser("url-keywords", help="Keywords a URL ranks for")
    p.add_argument("--url", "-u", required=True, help="Full URL")
    p.add_argument("--num", "-n", type=int, default=10, help="Results")
    p.add_argument("--country", "-c", default="us", help="Country code")
    p.add_argument("--currency", default="usd", help="Currency code")

    p = sub.add_parser("page-backlinks", help="Backlinks to a page")
    p.add_argument("--url", "-u", required=True, help="Full URL")
    p.add_argument("--num", "-n", type=int, default=10, help="Results")

    p = sub.add_parser(
        "page-unique-backlinks", help="Unique referring domains to a page"
    )
    p.add_argument("--url", "-u", required=True, help="Full URL")
    p.add_argument("--num", "-n", type=int, default=10, help="Results")

    return parser


COMMANDS = {
    "credits": cmd_credits,
    "countries": cmd_countries,
    "currencies": cmd_currencies,
    "keyword-data": cmd_keyword_data,
    "related": cmd_related,
    "pasf": cmd_pasf,
    "domain-keywords": cmd_domain_keywords,
    "domain-backlinks": cmd_domain_backlinks,
    "domain-unique-backlinks": cmd_domain_unique_backlinks,
    "url-keywords": cmd_url_keywords,
    "page-backlinks": cmd_page_backlinks,
    "page-unique-backlinks": cmd_page_unique_backlinks,
}


def main():
    parser = build_parser()
    args = parser.parse_args()
    COMMANDS[args.command](args)


if __name__ == "__main__":
    main()
