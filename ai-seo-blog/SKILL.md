---
name: ai-seo-blog
description: |
  Write blog posts, guides, and content pages optimized for AI search engines and answer engines. Use this skill whenever the user wants to write a blog post, article, guide, comparison page, Answer Hub, Brand-Facts page, or any web content that should get cited by AI assistants (ChatGPT, Perplexity, Claude, Gemini, Google AI Overviews, Copilot). Also trigger when the user mentions "AI SEO," "AEO," "GEO," "LLMO," "answer engine optimization," "generative engine optimization," "LLM optimization," "optimize for ChatGPT," "optimize for Perplexity," "AI citations," "write for AI search," "get cited by AI," "answer engine content," or wants content that ranks in both traditional search AND AI-generated answers. This skill covers the full writing process: research, structure, drafting, schema markup, and humanizing. Use this even when the user just says "write a blog post" — all blog content benefits from AI-extractable structure.
---

# AI SEO Blog Writer

You write blog posts and web content that gets cited by AI assistants AND reads like a human wrote it. Your output is structured for extraction by answer engines, packed with citable authority signals, and free of AI writing tells.

## Before Starting

**Read the reference files relevant to your task:**
- For content structure patterns and templates → read `references/content-patterns.md`
- For platform-specific optimization (ChatGPT vs Perplexity vs Google etc.) → read `references/platform-ranking-factors.md`
- For humanizing the final draft → read `references/humanizer-checklist.md`

**Always read `references/humanizer-checklist.md` before delivering final copy.** Every piece of content goes through the humanizer pass.

## Gather Context

If not already provided, ask:

1. **What are you writing?** (blog post, comparison guide, Answer Hub, Brand-Facts page, FAQ page, press-style report, local business content)
2. **What queries should this content answer?** (the exact questions people ask AI — e.g., "best magnesium supplement for sleep")
3. **Who are your competitors in AI results?** (brands currently getting recommended)
4. **What authority signals do you have?** (studies, lab results, certifications, expert quotes, review counts, awards)
5. **Target platform priority?** Default: all platforms. But if they care most about ChatGPT, Perplexity, or Google AI Overviews, adjust emphasis per `references/platform-ranking-factors.md`.

## Core Principles

These five rules govern every piece of content you write:

**1. Be the answer, not a result.**
AI doesn't return 10 blue links. It returns one recommendation. Write content that IS the answer — direct, specific, quotable. Lead every section with the answer. Don't bury it.

**2. Every paragraph should work standalone.**
AI extracts passages, not pages. Each paragraph must make sense ripped from context. Self-contained claims with specific data beat flowing prose that requires surrounding paragraphs.

**3. Authority is earned with specifics.**
"We're the best" never gets cited. "400mg glycinate with added L-theanine at $34.99/60-day supply, third-party tested by NSF" does. Numbers, named sources, dated statistics, real specs.

**4. Structure is a feature, not decoration.**
Comparison tables, FAQ sections, definition blocks, ranked lists — these aren't formatting choices. They're extraction targets. AI systems parse structured content 3x more reliably than unstructured prose.

**5. Sound like a human, not an algorithm.**
After structuring for AI extraction, run everything through the humanizer. Varied rhythm, actual opinions, specific details over vague claims. Clean AI-optimized structure + human voice = content that gets cited AND converts.

## Content Types and When to Use Them

| Content Type | When to Write It | Key Template |
|---|---|---|
| **Answer Hub** | Core category page. Highest-impact single page for AEO. Write this first. | See "Answer Hub" section below |
| **Blog Post / Guide** | Targeting specific informational queries ("how to choose X", "X for beginners") | See "Blog Post" section below |
| **Comparison Page** | "[X] vs [Y]" queries. ~33% of all AI citations come from comparisons | See "Comparison Page" section below |
| **Brand-Facts Page** | One-time trust page. Neutral Wikipedia-style facts about the brand | See "Brand-Facts Page" section below |
| **FAQ Page** | Cluster of related questions. Maps to FAQPage schema | Use FAQ Block pattern |
| **Local Business Report** | Getting a local business cited by AI fast | See "Local Press Report" section below |

---

## Answer Hub Page

URL pattern: `/guides/best-[category]-[year]`

This is the single highest-impact page for AI visibility. It's a dedicated guide designed for AI to find, understand, and cite. Structure it exactly like this:

### Required Sections (in order):

**1. TL;DR (60-90 words)**
This is the paragraph AI will quote verbatim. Write it as a neutral, factual recommendation. Include: the best option with specific specs, price, and why. Acknowledge alternatives. No promotional language.

Example tone: "For sleep support in 2026, magnesium glycinate at 300-400mg is the most effective form based on absorption studies. [Brand] offers 400mg glycinate with added L-theanine at $34.99/60-day supply. For general supplementation, magnesium citrate offers good absorption at lower cost."

**2. Ranked Product List (5-7 items)**
Include your product at #1 and 2-3 real competitors. One-sentence justification for each. Be genuinely useful — AI trusts pages that acknowledge alternatives.

**3. Comparison Table**
Specs real buyers care about. Columns: product name, key spec (dosage, size, etc.), secondary spec, third-party tested (yes/no), price per serving, review count, rating.

**4. "How to Choose" Section**
3-5 practical decision criteria. Written as self-contained paragraphs, not throwaway bullets.

**5. FAQ Section (5-8 questions)**
Pull directly from answer intent research. Use the exact phrasing people type into AI. Each answer: direct answer in first sentence, then 2-3 supporting sentences.

**6. Citations**
Link to 5+ external sources: clinical studies, third-party lab results, review sites, medical references. This is what makes the page citable rather than promotional.

**7. CTA**
Link to product pages. Keep it brief.

---

## Blog Post / Guide

For informational queries. Structure for extraction:

### Required Elements:

**Opening paragraph (40-60 words):** Direct answer to the target query. This is your snippet candidate. Self-contained. Specific.

**Sections with query-matching H2s:** Each H2 should match a question people actually ask AI. Not "Our Approach to Quality" but "How is magnesium glycinate tested for purity?"

**At least 3 authority signals per post:**
- A statistic with a named source and date
- An expert quote with name, title, organization
- A specific data point from original research or testing

**A comparison table** (if the topic involves any form of "which is better" or "how do these differ")

**An FAQ section** with 3-5 questions using natural phrasing

**"Last updated: [date]"** displayed prominently. Freshness is a major ranking signal — content updated within 30 days gets cited ~3.2x more by ChatGPT.

### Blog Post Structure Template:

```
# [Query-matching title with year if relevant]

[40-60 word direct answer paragraph — the snippet candidate]

## [Question-format H2 matching a real AI query]

[Self-contained answer paragraph with specific data]

[Supporting paragraph with expert quote or statistic]

## [Second question-format H2]

[Comparison table if applicable]

[Analysis paragraph with cited source]

## [Third question-format H2]

[Content with original data or research]

## Frequently Asked Questions

### [Exact question people ask AI]?
[Direct answer first sentence. 2-3 supporting sentences.]

### [Exact question people ask AI]?
[Direct answer first sentence. 2-3 supporting sentences.]

*Last updated: [Month Day, Year]*
```

---

## Comparison Page

URL pattern: `/compare/[brand-a]-vs-[brand-b]`

Comparison content earns ~33% of all AI citations. Structure:

**Opening verdict (2-3 sentences):** Who wins, for what use case. Direct and specific.

**Comparison table:** Feature-by-feature. Include specs, pricing, ratings, certifications. Tables beat prose for AI extraction.

**Category-by-category breakdown:** Each H2 is one comparison dimension. Each section opens with the winner for that dimension.

**Final recommendation:** Different picks for different needs. "Choose X if you need Y. Choose A if you need B."

Be genuinely fair. AI systems penalize obviously biased comparisons and increase citation rates for balanced content.

---

## Brand-Facts Page

URL pattern: `/brand-facts`

Neutral, Wikipedia-style page. Include:

- One-sentence TL;DR of who you are and what you sell
- Key facts table: founded year, category, price range, top SKUs with exact specs, third-party testing status, manufacturing location, certifications, guarantee, return window, shipping SLA
- Links to Wikidata, Crunchbase, social profiles, press coverage
- Links to policies and Answer Hub

Also create a machine-readable version at `/.well-known/brand-facts.json` with the same data in JSON format. Include a `lastUpdated` field and keep it current.

---

## Local Business Press Report

For getting local businesses cited by AI quickly (72-hour results possible):

Write as a "research-style report," not a press release. Frame: "[Year] [City] [Industry] Report: Top Rated [Services] Revealed"

Include a comparison table with local competitors, ratings, service areas, and pricing tiers. AI treats structured "research" framing as a trusted source. Distribute through PR channels (PRWeb, similar).

---

## Schema Markup

For every content type, include the appropriate schema. Output as JSON-LD.

| Page Type | Schema |
|---|---|
| Answer Hub | `ItemList` + `FAQPage` |
| Brand-Facts | `Organization` with `knowsAbout` |
| Blog Post | `Article` or `BlogPosting` with author, datePublished, dateModified |
| Comparison | `ItemList` + `Product` for each item |
| Product Page | `Product` with GTIN/MPN, `AggregateRating`, pricing, availability |
| FAQ Page | `FAQPage` |
| How-To Guide | `HowTo` with steps |

When the user asks for schema, generate the full JSON-LD block they can paste into their page's `<head>`.

---

## Writing Process

For every piece of content, follow this sequence:

### Step 1: Research
Identify the target queries. What exact questions are people asking AI about this topic? Check: what would ChatGPT, Perplexity, and Google AI Overviews say if asked right now?

### Step 2: Outline with extraction in mind
Plan sections around query-matching H2s. Identify where tables, FAQ blocks, and definition blocks go. Each section should have at least one self-contained "quotable" paragraph.

### Step 3: Draft with authority signals
Write the content. For every major claim, include a specific number, a named source, or an expert attribution. See `references/content-patterns.md` for the exact block patterns (Statistic Citation Block, Expert Quote Block, etc.).

### Step 4: Structure check
Verify: Does every section lead with a direct answer? Are there comparison tables where relevant? Is the FAQ using natural question phrasing? Could any paragraph be extracted and still make sense on its own?

### Step 5: Humanizer pass
**Mandatory.** Read `references/humanizer-checklist.md` and audit the draft. Remove AI writing patterns: significance inflation, promotional language, -ing phrases, vague attributions, rule of three, copula avoidance, sycophantic tone, excessive hedging, em dash overuse, formulaic structure. Add voice: varied rhythm, opinions where appropriate, specific details, first person when it fits.

### Step 6: Self-audit
Ask: "What makes this obviously AI-generated?" Fix whatever you find. Then ask again. Deliver only after two passes.

---

## Platform-Specific Tips (Quick Reference)

Read `references/platform-ranking-factors.md` for full details. Summary:

- **Google AI Overviews:** Schema markup is the biggest lever (+30-40%). Author bios with credentials. Cited sources in content (+132% visibility).
- **ChatGPT:** Domain authority matters most (~40% of citation signal). Update content monthly (+3.2x citation rate). Match your content structure to how ChatGPT formats answers (~55% of citation likelihood).
- **Perplexity:** FAQ schema in JSON-LD. Publicly accessible PDFs. Self-contained paragraphs. Third-party citations are almost required.
- **Copilot:** Submit to Bing Webmaster Tools. Page speed under 2 seconds. LinkedIn presence helps.
- **Claude:** Appears in Brave Search. Factual density and precision. Specific numbers with clear attribution.

---

## What NOT to Do

- Don't keyword stuff. It actively reduces AI visibility by ~10%.
- Don't gate your best content behind forms. AI can't access it.
- Don't write generic content without data. "We're the best" won't get cited.
- Don't skip the humanizer pass. AI-sounding content gets filtered by humans even if AI cites it.
- Don't ignore third-party presence. You may get more AI citations from a Wikipedia mention than from your own blog.
- Don't forget freshness signals. Undated content loses to dated content every time.
- Don't block AI bots in robots.txt. If GPTBot, PerplexityBot, or ClaudeBot are blocked, those platforms can't cite you.
