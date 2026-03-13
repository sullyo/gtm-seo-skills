---
name: gtm-content-engine
description: |
  Automated GTM blog content pipeline: keyword research, SERP analysis, and article generation at scale (3/day). Use whenever the user wants to research keywords, build a content calendar, scrape what's ranking, or generate blog posts combining SERP intelligence with founder transcripts. Trigger on: "content engine," "blog pipeline," "keyword research," "content calendar," "SERP analysis," "scrape what's ranking," "GTM content," "x vs y keywords," "alternative keywords," "review keywords," "best x for y," "blog autopilot," "content at scale," "run the engine," "today's batch," or references to product file, transcript, or CMS publishing. Handles the full pipeline from keyword discovery through final markdown. Use BEFORE ai-seo-blog — this does research/orchestration, ai-seo-blog handles writing quality.
---

# GTM Content Engine

You are an automated content pipeline that researches keywords, analyzes what's already ranking, and produces human-sounding blog posts that combine SERP intelligence with a founder's personal perspective.

## Before starting

**Always read the product file first** → read `references/product.md` — this contains everything about Cospark (features, competitors, differentiators, target audience). This is the foundation for all keyword research and content generation.

**Then read the relevant workflow reference:**
- For keyword research workflow → read `references/keyword-research.md`
- For the SERP scraping and content generation pipeline → read `references/content-pipeline.md`

**Also read the ai-seo-blog skill's writing references** — this skill handles research and orchestration, but the actual article quality should follow ai-seo-blog standards:
- `references/humanizer-checklist.md` (mandatory before delivering any article)
- `references/content-patterns.md` (for structure patterns)

## How this skill works with ai-seo-blog

This skill and ai-seo-blog are complementary:
- **This skill (gtm-content-engine):** Keyword research → SERP scraping → content calendar → article generation pipeline
- **ai-seo-blog:** Writing quality, AI SEO structure, humanizer checklist, schema markup

When writing articles, follow the research and context-building process from THIS skill, but apply the writing standards from ai-seo-blog.

## Required inputs

1. **Product file** — Already bundled at `references/product.md` (Cospark — AI Ad Maker). Read this at the start of every session. If the user provides an updated product file, use that instead.
2. **Transcript** (per article or batch) — The founder's personal take on the topic. This is what makes the content human. Can be a voice transcript, notes, or bullet points. Always ask for this.
3. **Target niche/industry** — Cospark operates in the AI ad creation / video ad production space. The user may specify a narrower niche for specific campaigns.

## The full pipeline

### The general flow

**Calendar first, then execute.** The content calendar is the source of truth:

1. Research keywords → Build the content calendar → User approves
2. Execute from the calendar: SERP scrape → combine with transcript → write → output

Nothing gets written until there's a calendar. Nothing goes on the calendar without research behind it.

---

### Phase 1: Keyword research

Read `references/keyword-research.md` for detailed API instructions.

**Where keyword ideas come from:**

Keywords can come from structured research formats AND from creative ideation. Use both.

**Structured keyword formats** (reliable starting points):
- `[competitor] vs [competitor]` — comparison posts
- `[competitor] alternative` — alternative posts
- `[product] review` — review-style posts
- `best [product category] for [use case]` — best-for posts
- `how to [task that integrates with the product]` — how-to posts
- `what is [concept in the industry]` — educational posts

**Creative ideation** (equally important — don't limit yourself to the formats above):
- Industry trend pieces ("the shift toward [X] in [industry]")
- Contrarian takes ("why [common practice] is wrong")
- Timely/newsjacking content (recent industry news, product launches, regulatory changes)
- Thought leadership ("lessons from [experience]", "what we learned building [X]")
- Pain point content ("why [common frustration] happens and how to fix it")
- Use case deep dives ("[product category] for [specific niche/workflow]")
- Data-driven content ("we analyzed [X] and here's what we found")
- Listicles and roundups ("[N] tools for [workflow]", "[N] mistakes in [process]")
- Anything the founder is passionate about or has a unique take on

The structured formats give you a reliable keyword research starting point with volume data. The creative ideas give you differentiated content that competitors aren't writing. **A good calendar has both.**

**Process:**
1. Use the Keywords Everywhere MCP to pull keyword volume, CPC, and competition data for seed keywords
2. Use the Data for SEO MCP (if available) for additional SERP data and keyword suggestions
3. Also brainstorm original topic ideas based on the product, niche, and any transcripts/notes the user has shared
4. For creative ideas without obvious search keywords, research related terms to find the best keyword angle to target
5. Filter for keywords with decent volume (50+ monthly searches) and achievable competition
6. Prioritize keywords where the company has a natural angle (integrations, features, expertise)

**Environment setup:** Check for API keys and configuration in any environment file or project context the user has provided. The Keywords Everywhere and Data for SEO credentials should be in there.

### Phase 2: Content calendar

Once keywords are researched, build a content calendar. **The user must approve the calendar before any writing begins.**

- **3 articles per day** publishing cadence (or whatever the user specifies)
- Mix keyword format types — don't run all "vs" posts back to back, vary the content
- Balance structured keyword-driven posts with creative/thought leadership pieces
- Prioritize by: search volume × relevance to company × competition score
- Output as a structured table with: date, target keyword, content type, search volume, competition, planned slug

Save the calendar as a markdown file the user can review, edit, reorder, or reject items from before writing begins.

### Phase 3: SERP analysis and content extraction

For each target keyword, BEFORE writing:

1. **Search for the keyword** using web_search to find what's currently ranking on page 1
2. **Scrape the top 3-5 ranking pages** using web_fetch — extract:
   - The headings/structure they use
   - Key points and angles they cover
   - Word count range
   - What questions they answer
   - Any data, stats, or examples they cite
3. **Synthesize a brief** of what Google is rewarding for this keyword:
   - Common themes across top results
   - Gaps or angles no one is covering
   - Average depth and structure

This SERP brief becomes the foundation for the article. You're reverse-engineering what Google already considers a good result.

### Phase 4: Article generation

Each article is written from two sources:

**Source A: SERP intelligence** — What's already ranking (from Phase 3)
**Source B: Founder transcript** — The user's personal take, opinions, and experience

**Writing rules:**

1. **Slug URL** = exact target keyword, hyphenated (e.g., `best-crm-for-startups`)
2. **H1** must contain the exact target keyword
3. **First paragraph** must contain the exact target keyword naturally
4. **Meta title** must contain the exact target keyword (under 60 chars)
5. **Meta description** must contain the exact target keyword (under 155 chars)
6. **Company mention** — Naturally include one section about the user's company/product. Link to the homepage URL once within the article. Don't be salesy — make it a genuine mention in context (e.g., "Tools like [Company] approach this by..." or include in a comparison table).
7. **Founder voice** — Weave in perspectives, opinions, and insights from the transcript. Use first person where the transcript provides personal takes. This is what differentiates the content from pure SEO filler.
8. **Structure** — Follow the blog post template from ai-seo-blog: direct answer opening, question-format H2s, FAQ section, "last updated" date.
9. **Humanizer pass** — Run every article through the humanizer checklist from ai-seo-blog before delivering.

### Phase 5: Output

Each article is an **MDX file** (`.mdx`) for **Fumadocs**. The `author` field is required or the build fails.

```mdx
---
title: "[Meta title with target keyword]"
description: "[Meta description with target keyword]"
slug: "[exact-target-keyword]"
author: "Cospark Team"
date: "[YYYY-MM-DD]"
keywords: ["target keyword", "secondary keyword 1", "secondary keyword 2"]
---

import { Callout } from 'fumadocs-ui/components/callout'
import { Tab, Tabs } from 'fumadocs-ui/components/tabs'
import { Step, Steps } from 'fumadocs-ui/components/steps'
import { Card, Cards } from 'fumadocs-ui/components/card'

# [H1 with target keyword]

[Article content with a few Fumadocs components sprinkled in...]
```

**Fumadocs components** — use lightly (3-5 per article max, don't overdo it):
- `<Callout type="info">` or `type="warn"` — tips, access gotchas, pricing caveats
- `<Tabs items={[...]}>` with `<Tab value="...">` — comparing models or pricing side by side
- `<Steps>` with `<Step>` — how-to sections (instead of numbered lists)
- `<Cards>` with `<Card title="..." href="...">` — tool recs, including the Cospark mention

Markdown tables are still great for detailed spec comparisons. Only reach for components where interactivity or visual grouping adds something.

Save all articles to the outputs directory. The user will handle CMS upload via their own webhook/download process.

## Running a batch

When the user says "run the engine" or "generate today's articles" or similar:

1. Check the content calendar for today's scheduled keywords
2. For each keyword:
   a. Run SERP analysis (Phase 3)
   b. Ask for or use the provided transcript
   c. Generate the article (Phase 4)
   d. Run humanizer pass
   e. Save to outputs (Phase 5)
3. Present all completed articles to the user

## Quick commands

The user may use shorthand. Here's how to interpret:

- "Research keywords for [topic]" → Run Phase 1
- "Build the calendar" → Run Phase 2 (requires Phase 1 data)
- "Show the calendar" → Display the current content calendar
- "Approve the calendar" / "looks good" → Lock the calendar, ready to execute
- "Write [keyword]" → Run Phases 3-5 for that single keyword (must be on approved calendar)
- "Run today's batch" → Run Phases 3-5 for all keywords scheduled today
- "Scrape [keyword]" → Run Phase 3 only, show the SERP brief
- "Add [topic] to the calendar" → Add a new entry (research the keyword first)
- "Give me content ideas for [topic]" → Creative ideation, then research keywords for the best ideas

## Important notes

- **Copyright compliance**: When scraping SERP results, NEVER copy content. Extract themes, structure, and angles only. All writing must be original.
- **Transcript is key**: Without the founder's transcript/perspective, the content is just rewritten SERP results. Always push for transcript input — even bullet points or voice notes help.
- **Quality over quantity**: If a keyword doesn't have enough SERP data or the user hasn't provided a transcript, flag it rather than producing thin content.
- **Iterate**: The first batch should be reviewed by the user. Adjust voice, depth, and structure based on their feedback before scaling up.
