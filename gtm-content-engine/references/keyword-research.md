# Keyword research workflow

This document covers how to use the available keyword research tools to find and prioritize target keywords for the content engine.

## Contents
- [Available tools](#available-tools)
- [Seed keyword generation](#seed-keyword-generation)
- [Keyword research with Keywords Everywhere MCP](#keyword-research-with-keywords-everywhere-mcp)
- [Supplemental research with Data for SEO MCP](#supplemental-research-with-data-for-seo-mcp)
- [Filtering and prioritization](#filtering-and-prioritization)
- [Fallback: web search research](#fallback-web-search-research)

---

## Available tools

### Keywords Everywhere MCP

The Keywords Everywhere MCP server is connected and provides keyword data including search volume, CPC, competition scores, and related/long-tail keyword suggestions.

**How to use it:**
- The MCP is available as a connected tool in the conversation
- Send keyword queries to get volume, CPC, and competition data
- Use it to expand seed keywords into long-tail variations
- Pull "related keywords" and "people also search for" data

**Typical MCP calls:**
- Get volume/CPC/competition for a list of keywords
- Get related keywords for a seed term
- Get trending keywords in a category
- Get long-tail suggestions

Check the MCP's available tools at runtime — call the MCP and inspect what functions it exposes. The tool names and parameters may vary, so discover them dynamically rather than hardcoding.

### Data for SEO MCP

If configured, the Data for SEO MCP provides deeper SERP analysis data including:
- SERP feature data (featured snippets, PAA boxes, etc.)
- Keyword difficulty scores
- Search intent classification
- Competitor domain analysis

**How to use it:**
- Check if the MCP is available in the current session
- Use it for SERP-level data that Keywords Everywhere doesn't provide
- Particularly useful for understanding keyword difficulty and search intent

### Web search (always available)

Claude's built-in web_search tool works as a fallback and supplement:
- Search for "[keyword] search volume" to find volume estimates
- Search for "best keywords for [industry]" for ideas
- Search Google directly to see what's actually ranking (used heavily in Phase 3)

---

## Seed keyword generation

Before hitting any API, generate seed keywords based on the user's product and niche. Ideas come from two sources: **structured keyword formats** and **creative ideation**. Use both.

---

### Structured keyword formats (reliable, volume-backed)

These are proven templates that almost always have search volume behind them:

#### Comparison keywords (`x vs y`)
```
[your product] vs [competitor 1]
[competitor 1] vs [competitor 2]
[product category A] vs [product category B]
```

To find competitors, check:
- The user's product file (if provided)
- Search "[product category] alternatives" and note what comes up
- Search "[product category] comparison" for common matchups

### Alternative keywords
```
[competitor] alternative
[competitor] alternatives [year]
best [competitor] alternative
[competitor] alternative for [use case]
free [competitor] alternative
```

### Review keywords
```
[product] review
[product] review [year]
is [product] worth it
[product] honest review
[product] pros and cons
```

### Best-for keywords
```
best [category] for [use case 1]
best [category] for [use case 2]
best [category] for small business
best [category] for startups
best [category] for enterprise
best free [category]
top [category] [year]
```

### How-to keywords
```
how to [task the product helps with]
how to [task] with [integration]
how to set up [related tool]
how to migrate from [competitor]
[task] tutorial
[task] guide [year]
```

### Educational keywords
```
what is [industry concept]
[concept] explained
[concept] vs [concept]
[concept] best practices
[concept] for beginners
```

---

### Creative ideation (original, differentiated)

Don't limit yourself to the structured formats above. A strong content calendar also includes original ideas that competitors aren't covering. These might not have obvious seed keywords, but you can research related terms to find the best keyword angle.

**Ways to generate creative topics:**

1. **Mine the transcript** — If the founder has shared any transcripts, notes, or rants, look for strong opinions or unique experiences. These become thought leadership pieces.

2. **Industry trends** — What's changing in the space right now? New regulations, new technologies, market shifts. Search for "[industry] trends [year]" and "[industry] news" to find angles.

3. **Pain points** — What do customers complain about? What frustrations exist in the category? These become "why [X] is broken" or "how to fix [X]" posts.

4. **Contrarian takes** — What does everyone in the industry believe that might be wrong? "Why [common practice] doesn't work anymore" posts get attention and shares.

5. **Use case stories** — Specific workflows or scenarios. "[Product type] for [specific niche]" or "how [specific team type] uses [category]."

6. **Data and original research** — "We analyzed [X]" or "what [N] [customers/companies/data points] taught us about [Y]." Even small datasets are compelling.

7. **Timely content** — Industry events, competitor launches, regulatory changes. Newsjacking with a founder's perspective.

8. **Integration content** — "How to use [tool A] with [tool B]" where one of the tools is a product the company integrates with.

**For creative topics, the research process is:**
1. Come up with the topic idea
2. Search for related keywords around that topic using Keywords Everywhere
3. Find the best keyword angle that has actual search volume
4. Use that keyword as the target, but write the original creative angle

Example: The idea is "why most teams set up their CRM wrong." Research related keywords → find "CRM setup mistakes" (320 vol) or "how to set up CRM" (1,200 vol). Target the keyword with volume, but write the original angle.

---

## Keyword research with Keywords Everywhere MCP

### Step 1: Bulk volume check

Take all seed keywords (aim for 30-50) and send them to Keywords Everywhere for volume/CPC/competition data.

### Step 2: Expand with related keywords

For the top 10-15 seeds by volume, pull related keywords and "people also search for" suggestions. This typically 3-5x your keyword list.

### Step 3: Long-tail discovery

For high-competition head terms, look for long-tail variations that are more achievable:
- Add modifiers: "for startups," "for small teams," "[year]," "free," "open source"
- Look at question variations: "how to," "what is the best," "is [x] good for"

### Step 4: Organize results

Structure all keyword data into a table:

| Keyword | Monthly Volume | CPC | Competition | Format Type | Priority |
|---------|---------------|-----|-------------|-------------|----------|
| [keyword] | [volume] | [cpc] | [low/med/high] | [vs/alt/review/best/howto/edu] | [1-5] |

---

## Supplemental research with Data for SEO MCP

If available, use Data for SEO to enrich the keyword list:

1. **Keyword difficulty** — Get difficulty scores to identify low-hanging fruit
2. **SERP features** — Check which keywords trigger featured snippets, PAA boxes, etc. (these are high-value targets)
3. **Search intent** — Classify keywords as informational, commercial, navigational, or transactional
4. **Competitor gaps** — Find keywords competitors rank for that the user doesn't

---

## Filtering and prioritization

After collecting all keyword data, filter and rank:

### Must-have filters
- Monthly search volume >= 50 (unless highly relevant niche term)
- Competition score: prefer low-medium for new sites, medium-high OK for established domains
- Search intent: prioritize commercial and informational (these convert and build authority)

### Prioritization scoring

Score each keyword 1-5 based on:

**Relevance (weight: 40%)**
- 5 = Directly about the product/category
- 3 = Related to the industry
- 1 = Tangentially related

**Volume (weight: 25%)**
- 5 = 1000+ monthly searches
- 3 = 100-999
- 1 = 50-99

**Competition (weight: 20%)**
- 5 = Low competition
- 3 = Medium competition
- 1 = High competition

**Content fit (weight: 15%)**
- 5 = Have transcript/expertise ready
- 3 = Can write with SERP research
- 1 = Would need significant original research

### Final priority = (Relevance × 0.4) + (Volume × 0.25) + (Competition × 0.2) + (Content fit × 0.15)

Sort by priority score. The top keywords become the content calendar.

---

## Fallback: web search research

If MCP tools are unavailable or return errors:

1. Search "[seed keyword] search volume" — sites like Ahrefs, Semrush, and Ubersuggest often show volume in search results
2. Search "[industry] keywords [year]" for keyword list articles
3. Use Google's autocomplete by searching partial phrases and noting suggestions
4. Check "People Also Ask" boxes in Google results for question-format keywords
5. Search "[competitor] blog" and analyze what topics they're covering

This is less precise than API data but gets you a workable keyword list.
