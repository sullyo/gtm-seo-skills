# Content pipeline: SERP analysis to published article

This document covers the process of scraping what's ranking, combining it with the founder's transcript, and generating a publish-ready article.

## Contents
- [SERP scraping process](#serp-scraping-process)
- [SERP brief format](#serp-brief-format)
- [Combining SERP data with transcript](#combining-serp-data-with-transcript)
- [Article writing process](#article-writing-process)
- [Output format](#output-format)
- [Batch processing](#batch-processing)

---

## SERP scraping process

For each target keyword, follow this exact process:

### Step 1: Search the keyword

Use `web_search` with the exact target keyword phrase. This returns the top results Google is currently showing.

### Step 2: Identify top results

From the search results, pick the top 3-5 organic results (skip ads, skip results from the user's own domain).

### Step 3: Scrape each result

Use `web_fetch` on each URL. For each page, extract:

**Structure analysis:**
- H1 tag (exact text)
- H2 tags (list them all — this shows the outline Google rewards)
- H3 tags if present
- Approximate word count
- Whether it has: FAQ section, comparison table, images, video

**Content analysis:**
- The opening paragraph/hook approach
- Main points or arguments made
- Any statistics, data points, or studies cited
- Questions the article answers
- The conclusion/CTA approach

**Gap analysis:**
- What angles are ALL top results covering? (table stakes — you must cover these)
- What angles are only 1-2 results covering? (differentiators)
- What's missing entirely? (opportunity)

### Step 4: Handle scraping failures

If web_fetch fails on a URL (paywall, bot blocking, etc.):
- Use the search result snippet as your data point for that result
- Try to scrape the next result instead
- 2-3 successfully scraped results is enough to work with

### Copyright compliance

**CRITICAL:** You are extracting themes, structure, and angles — NOT copying content. 
- Never reproduce sentences or paragraphs from scraped pages
- Extract data points and statistics (these are facts, not copyrightable)
- Note structural patterns (e.g., "all top results use a comparison table") without copying the tables
- Identify topic coverage gaps without lifting the actual coverage

---

## SERP brief format

After scraping, compile a SERP brief for the keyword. This is an internal document (not published) that guides the article writing:

```
## SERP Brief: [target keyword]

**Top ranking URLs:**
1. [URL 1] - [Title]
2. [URL 2] - [Title]  
3. [URL 3] - [Title]

**Average word count:** [X words]

**Common H2 themes:**
- [Theme 1 — covered by X/Y results]
- [Theme 2 — covered by X/Y results]
- [Theme 3 — covered by X/Y results]

**Content table stakes (must include):**
- [Point everyone covers]
- [Point everyone covers]

**Differentiation opportunities:**
- [Angle only 1 result covers]
- [Gap no one is covering]

**Structural patterns:**
- [e.g., "3/5 results use comparison tables"]
- [e.g., "4/5 results have FAQ sections"]
- [e.g., "Top result uses numbered list format"]

**Data/stats cited across results:**
- [Stat 1 — source]
- [Stat 2 — source]

**Search intent:** [informational / commercial / comparison]
```

---

## Combining SERP data with transcript

This is the core differentiator of this content engine. Every article is built from two pillars:

### Pillar 1: SERP intelligence (what Google rewards)

From the SERP brief, you know:
- What topics to cover (table stakes)
- How to structure the article (common patterns)
- What depth is expected (word count range)
- What data to reference (cited stats)
- Where the gaps are (your angle)

### Pillar 2: Founder transcript (what makes it human)

The user provides a transcript — could be:
- A voice recording transcript of their take on the topic
- Written notes or bullet points
- A Loom video transcript
- Slack messages or notes about their perspective

**How to weave the transcript in:**

1. **Extract key opinions** — What does the founder actually think about this topic? Pull out 3-5 strong takes.

2. **Find experience-based insights** — Any "we tried X and learned Y" stories? These are gold for E-E-A-T signals and human voice.

3. **Identify unique data** — Does the founder mention specific numbers, customer outcomes, or internal data? These become authority signals.

4. **Map opinions to SERP topics** — For each section the SERP brief says you need to cover, find the founder's relevant perspective. This is where you merge the two pillars.

5. **Use first person naturally** — Where the transcript has personal takes, write them in first person. "In my experience working with [X], the biggest mistake teams make is..." This is what differentiates from competitors.

### The merge formula

For each article section:
```
[What SERP says is needed for this topic]
+ [Founder's perspective on this topic from transcript]
+ [Any unique data or experience from transcript]
= Section that satisfies Google AND sounds human
```

If the transcript doesn't cover a particular SERP topic, write it based on SERP intelligence alone but keep the same voice/tone established by the transcript sections.

---

## Article writing process

### Step 1: Set the frontmatter

```yaml
title: "[Target keyword] — [value add phrase]"  # Under 60 chars, keyword near front
description: "[Sentence with target keyword that compels click]"  # Under 155 chars
slug: "[target-keyword-hyphenated]"  # Exact keyword as URL
date: "[YYYY-MM-DD]"
keywords: ["target keyword", "variation 1", "variation 2"]
```

### Step 2: Write the H1

Must contain the exact target keyword. Can add context but keyword must be present verbatim.

Good: "Best CRM for Startups in 2026: What Actually Works"
Bad: "Finding the Right Customer Relationship Tool for New Companies"

### Step 3: Write the opening paragraph

Must contain the exact target keyword naturally within the first 2-3 sentences. This paragraph should be a direct answer to the search intent — what would someone searching this keyword want to know immediately?

Follow ai-seo-blog's pattern: 40-60 words, self-contained, specific, quotable.

### Step 4: Build sections from SERP brief + transcript

For each major topic from the SERP brief:
1. Use a question-format H2 that matches how people search
2. Open with a direct answer
3. Weave in the founder's perspective from the transcript
4. Include specific data points where available
5. Keep each paragraph self-contained (AI-extractable)

### Step 5: Include the company mention

**One natural section** about the user's company. This should NOT feel like an ad. Good approaches:
- Include in a comparison table alongside competitors
- Mention as a "tool we built to solve this" in context
- Reference in a "what we've seen working with customers" section
- Include in a "tools for this" recommendations list

**One homepage link** — anchor text should be the company name or a natural phrase, not "click here."

### Step 6: Add FAQ section

3-5 questions using natural phrasing (pull from "People Also Ask" data in SERP research). Each answer: direct answer first sentence, then 2-3 supporting sentences.

### Step 7: Add "Last updated" date

Freshness signal. Use current date.

### Step 8: Humanizer pass

**Mandatory.** Read `/mnt/skills/user/ai-seo-blog/humanizer-checklist.md` and audit the draft:
- Kill AI vocabulary (check the blacklist)
- Kill significance inflation
- Kill promotional language around the company mention
- Add voice from the transcript
- Vary sentence rhythm
- Check for opinions and first person where transcript supports it
- Remove any chatbot artifacts

### Step 9: Self-audit

Ask: "If I saw this on page 1, would I think a person wrote it or an AI?" Fix whatever tips you toward AI. Then ask again. Deliver only after two passes.

---

## Output format

Each article is an **MDX file** for **Fumadocs**. The `author` frontmatter field is required (build fails without it).

**Filename:** `[slug].mdx` (e.g., `best-crm-for-startups.mdx`)

**Full structure:**
```mdx
---
title: "Meta title with target keyword (under 60 chars)"
description: "Meta description with target keyword (under 155 chars)"
slug: "target-keyword-as-url"
author: "Cospark Team"
date: "2026-02-25"
keywords: ["primary keyword", "secondary keyword", "tertiary keyword"]
target_keyword: "exact target keyword"
word_count: [approximate]
---

import { Callout } from 'fumadocs-ui/components/callout'
import { Tab, Tabs } from 'fumadocs-ui/components/tabs'
import { Step, Steps } from 'fumadocs-ui/components/steps'
import { Card, Cards } from 'fumadocs-ui/components/card'

# H1 with target keyword

[Opening paragraph with target keyword — 40-60 words, direct answer]

## [Question-format H2]

[Content sections with SERP intelligence + founder perspective]

<Callout type="info">
[Practical tip or important context worth calling out]
</Callout>

## [How-to section H2]

<Steps>
  <Step>
  ### [Step name]
  [Step content]
  </Step>
  <Step>
  ### [Step name]
  [Step content]
  </Step>
</Steps>

## [Comparison or options section H2]

<Tabs items={["Option A", "Option B"]}>
  <Tab value="Option A">[Details]</Tab>
  <Tab value="Option B">[Details]</Tab>
</Tabs>

## About [Company Name]

<Cards>
  <Card title="[Company Name]" href="[homepage URL]">
  [Natural company description]
  </Card>
</Cards>

## Frequently asked questions

### [Natural question phrasing]?
[Direct answer. Supporting detail.]

### [Natural question phrasing]?
[Direct answer. Supporting detail.]

*Last updated: [Month Day, Year]*
```

**Component usage guidelines:**
- Use 3-5 components per article. Don't overdo it.
- `<Callout>` for tips, warnings, pricing caveats, access gotchas
- `<Tabs>` for comparing options side by side (pricing by model, platform access)
- `<Steps>` for how-to sections instead of numbered lists
- `<Cards>` for tool recommendations including the Cospark mention
- Markdown tables are still preferred for detailed spec comparisons

---

## Batch processing

When generating multiple articles (e.g., "today's 3 articles"):

### Process each article sequentially:

1. **SERP scrape** for keyword 1 → write article 1 → save
2. **SERP scrape** for keyword 2 → write article 2 → save
3. **SERP scrape** for keyword 3 → write article 3 → save

### Why sequential, not parallel:
- Each SERP scrape provides fresh context
- The humanizer pass needs focused attention
- Quality matters more than speed at this stage

### After the batch:
- Present all articles to the user
- List what was published: keyword, slug, word count, meta title
- Note any articles that need transcript input or have quality concerns
- Update the content calendar to mark these as complete

### Batch summary format:
```
## Today's content batch — [Date]

| # | Target Keyword | Slug | Word Count | Status |
|---|---------------|------|------------|--------|
| 1 | [keyword] | [slug] | [count] | Done |
| 2 | [keyword] | [slug] | [count] | Done |
| 3 | [keyword] | [slug] | [count] | Needs transcript |
```
