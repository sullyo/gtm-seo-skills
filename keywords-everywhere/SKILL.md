---
name: keywords-everywhere
description: >
  SEO/SEM data retrieval using the Keywords Everywhere API via a Python CLI script. Use this skill
  whenever the user wants to perform keyword research, analyze search volume, CPC, or competition
  data, find related keywords or "People Also Search For" suggestions, check a domain or URL's
  backlinks, see what keywords a domain/URL ranks for, or get traffic estimates for any domain or URL.
  Trigger on phrases like "keyword research", "search volume", "find keywords", "backlink analysis",
  "what keywords does [site] rank for", "domain traffic", "competitor keywords", "SEO data",
  "CPC data", "keyword difficulty", "PASF keywords", "related keywords", "SERP analysis keywords",
  or any request involving keyword metrics, backlink profiles, or organic traffic estimates.
  Also trigger when the user references the Keywords Everywhere tool, connector, or API by name.
  Do NOT use for general web searching or content writing — this is strictly for SEO/SEM data retrieval.
credentials:
  - KEYWORDS_EVERYWHERE_API_KEY
---

# Keywords Everywhere Skill

Retrieve SEO and SEM data from the Keywords Everywhere REST API using a Python CLI script.


## Prerequisites

```bash
pip install requests --break-system-packages
```

## API Key Setup

This skill requires a **Keywords Everywhere API key**. Set it as an environment variable:

```bash
export KEYWORDS_EVERYWHERE_API_KEY='your-api-key-here'
```

**Where to get your API key:**

1. Go to [keywordseverywhere.com](https://keywordseverywhere.com) and create an account (or log in)
2. Purchase API credits (plans start at $1 for 100,000 credits)
3. Navigate to **API** > **API Settings** at [keywordseverywhere.com/api-settings.html](https://keywordseverywhere.com/api-settings.html)
4. Copy your API key from that page

To make the key persistent, add the export line to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.).

## Quick Start

```bash
python3 <SKILL_DIR>/scripts/ke_client.py <COMMAND> [OPTIONS]
```

Replace `<SKILL_DIR>` with the actual path to this skill folder.

---

## Available Commands

### Keyword Research

```bash
# Get volume, CPC & competition for keywords
python3 <SKILL_DIR>/scripts/ke_client.py keyword-data \
  --keywords "seo tools" "keyword research" "content marketing" \
  --country us --currency usd

# Find related keywords for a seed term
python3 <SKILL_DIR>/scripts/ke_client.py related \
  --keyword "email marketing" --num 20 --country us

# Get "People Also Search For" keywords
python3 <SKILL_DIR>/scripts/ke_client.py pasf \
  --keyword "project management" --num 15 --country us
```

### Domain Analysis

```bash
# Keywords a domain ranks for
python3 <SKILL_DIR>/scripts/ke_client.py domain-keywords \
  --domain competitor.com --country us --num 50

# Backlinks pointing to a domain
python3 <SKILL_DIR>/scripts/ke_client.py domain-backlinks \
  --domain competitor.com --num 25

# Unique referring domains linking to a domain
python3 <SKILL_DIR>/scripts/ke_client.py domain-unique-backlinks \
  --domain competitor.com --num 25
```

### URL / Page Analysis

```bash
# Keywords a specific URL ranks for
python3 <SKILL_DIR>/scripts/ke_client.py url-keywords \
  --url "https://competitor.com/blog/best-tools" --country us --num 30

# Backlinks pointing to a specific page
python3 <SKILL_DIR>/scripts/ke_client.py page-backlinks \
  --url "https://competitor.com/blog/best-tools" --num 20

# Unique referring domains linking to a page
python3 <SKILL_DIR>/scripts/ke_client.py page-unique-backlinks \
  --url "https://competitor.com/blog/best-tools" --num 20
```

### Account & Reference

```bash
# Check remaining API credit balance
python3 <SKILL_DIR>/scripts/ke_client.py credits

# List all supported country codes
python3 <SKILL_DIR>/scripts/ke_client.py countries

# List all supported currency codes
python3 <SKILL_DIR>/scripts/ke_client.py currencies
```

---

## Common Options

- `--country CODE` / `-c` — Country filter (default: `us`). Use `""` for Global, `"gb"`, `"ca"`, etc.
- `--currency CODE` — Currency for CPC values (default: `usd`).
- `--num N` / `-n` — Number of results to return (default: 10, max: 1000).
- `--output json` / `-o json` — Raw JSON output instead of the default table format.

## Output Formats

- **Default:** human-readable aligned table
- **JSON:** pass `--output json` for raw JSON (useful for piping into other tools)

---

## Command Reference

| Command | Description | Key Parameters |
|---|---|---|
| `keyword-data` | Volume, CPC, competition for keywords | `--keywords`, `--country`, `--currency` |
| `related` | Related keywords for a seed term | `--keyword`, `--num`, `--country` |
| `pasf` | "People Also Search For" keywords | `--keyword`, `--num`, `--country` |
| `domain-keywords` | Keywords a domain ranks for | `--domain`, `--num`, `--country` |
| `domain-backlinks` | Backlinks to a domain | `--domain`, `--num` |
| `domain-unique-backlinks` | Unique referring domains | `--domain`, `--num` |
| `url-keywords` | Keywords a URL ranks for | `--url`, `--num`, `--country` |
| `page-backlinks` | Backlinks to a page | `--url`, `--num` |
| `page-unique-backlinks` | Unique referring domains to a page | `--url`, `--num` |
| `credits` | Check API credit balance | (none) |
| `countries` | Supported country codes | (none) |
| `currencies` | Supported currency codes | (none) |

---

## Usage Tips

- The REST API accepts a maximum of **100 keywords** per `keyword-data` request. The script auto-batches larger lists with a 1-second delay between batches.
- Check credits regularly — each keyword lookup costs 1 credit, backlink/domain lookups cost 3+.
- For bulk competitor research, combine `domain-keywords` → `keyword-data` to enrich rankings with volume/CPC.
- Country codes follow ISO 3166-1 alpha-2 (e.g., `us`, `gb`, `ca`, `au`, `de`).
- The `page-backlinks` and `page-unique-backlinks` endpoints use the `page` parameter internally — the script handles this automatically when you pass `--url`.
