# How Each AI Platform Picks Sources

Each AI search platform has its own index, ranking logic, and content preferences. Use this reference when optimizing content for a specific platform or when a user asks about platform-specific strategy.

---

## Contents
- [Shared Fundamentals](#shared-fundamentals)
- [Google AI Overviews](#google-ai-overviews)
- [ChatGPT](#chatgpt)
- [Perplexity](#perplexity)
- [Microsoft Copilot](#microsoft-copilot)
- [Claude](#claude)
- [Robots.txt Configuration](#robotstxt-configuration)
- [Priority Order](#priority-order)

---

## Shared Fundamentals

Every AI platform requires these three things:

1. **Your content must be in their index.** Each uses a different search backend (Google, Bing, Brave, or their own). No index = no citation.
2. **Your content must be crawlable.** AI bots need access via robots.txt.
3. **Your content must be extractable.** AI systems pull passages, not pages. Self-contained paragraphs and clear structure win.

---

## Google AI Overviews

**Search backend:** Google's own index
**Appears in:** ~45% of Google searches
**Reduces clicks to websites by:** up to 58%

### What makes it different
Already has your traditional SEO signals (backlinks, page authority, topical relevance). The AI layer adds preference for cited sources and structured data. Only ~15% of AI Overview sources overlap with conventional top-10 organic results — pages outside page 1 can still get cited.

### Key ranking signals
- **Schema markup** is the single biggest lever: +30-40% visibility boost. Use Article, FAQPage, HowTo, Product schemas.
- **Cited sources in content**: +132% visibility boost. Not just making claims — linking to the evidence.
- **Authoritative tone** (not salesy): +89% visibility boost.
- **E-E-A-T signals**: Author bios with real credentials, first-hand experience, transparent sourcing.
- **Topical authority**: Content clusters with strong internal linking.
- **Google Knowledge Graph presence**: An accurate Wikipedia entry helps significantly.

### Queries that trigger AI Overviews most often
- "How to [X]" patterns
- "What is [X]" patterns
- Informational queries with clear answer intent

---

## ChatGPT

**Search backend:** Bing-based index + training knowledge
**Key stat:** 5+ billion visits/month

### What makes it different
Domain authority matters more here than other platforms. An SE Ranking study of 129,000 domains found authority/credibility signals account for ~40% of citation determination, content quality ~35%, platform trust ~25%.

High referring domain counts (350K+) average 8.4 citations per response. Even slight drops in trust scores (91-96 vs 97-100) cut citations from 8.4 to 6.

### Key ranking signals
- **Domain authority**: The strongest baseline signal. Invest in backlinks.
- **Freshness**: Content updated within 30 days gets cited ~3.2x more often. Update competitive content monthly.
- **Content-answer fit**: A ZipTie analysis of 400K pages found that matching ChatGPT's response style accounts for ~55% of citation likelihood. Far more important than domain authority (12%) or on-page structure (14%) alone. Write the way ChatGPT would answer the question.
- **Clean heading hierarchy**: H1 > H2 > H3 with descriptive headings.
- **Verifiable statistics with named sources**.

### Where ChatGPT looks beyond your site
- Wikipedia: 7.8% of all citations
- Reddit: 1.8%
- Forbes: 1.1%
- Brand official sites are cited frequently but third-party mentions carry significant weight

### ChatGPT Shopping
Pulls from Google Merchant Center data. Requirements:
- GTIN (barcode) for every variant, or MPN + brand name
- Front-loaded titles with specs: "Magnesium Glycinate 400mg Sleep Support, 60 Servings, Third-Party Tested"
- All relevant product attributes filled in
- Images: 1200px+, clean backgrounds, no watermarks
- Reviews mapped to SKUs: aim for 50+ verified, 4.2+ stars
- Zero critical Merchant Center errors

---

## Perplexity

**Search backend:** Own index + Google's index, multiple reranking passes
**Key stat:** 500+ million queries/month
**Unique feature:** Always cites sources with clickable links (most transparent AI search)

### What makes it different
Most "research-oriented" AI search. Uses curated authoritative domain lists (Amazon, GitHub, academic sites) with inherent ranking boosts. Time-decay algorithm evaluates new content quickly — fresh publishers get a real shot.

### Key ranking signals
- **FAQ Schema (JSON-LD)**: Pages with FAQ structured data get cited noticeably more.
- **PDF documents**: Publicly accessible whitepapers and research reports are prioritized. If you have gated PDFs, make a version public.
- **Publishing velocity**: How frequently you publish matters more than keyword targeting.
- **Self-contained paragraphs**: Perplexity extracts atomic, semantically complete paragraphs. Each paragraph = one clean idea.
- **Third-party citations**: Almost exclusively recommends brands with external validation. This is the platform where third-party mentions matter most.
- **Article schema** with publication and modification timestamps.

### Perplexity bot
Allow `PerplexityBot` in robots.txt.

---

## Microsoft Copilot

**Search backend:** Bing's index (entirely)
**Embedded in:** Edge, Windows, Microsoft 365, Bing Search

### What makes it different
Microsoft ecosystem connection creates unique opportunities. LinkedIn and GitHub presence provides ranking boosts other platforms don't offer. Page speed threshold is stricter: sub-2-second load times are a clear signal.

### Key ranking signals
- **Bing Webmaster Tools**: Submit your site. Many sites only submit to Google Search Console.
- **IndexNow protocol**: Faster indexing of new/updated content.
- **Page speed**: Under 2 seconds.
- **Entity definitions**: When your content defines a term, make the definition explicit and extractable.
- **LinkedIn presence**: Publish articles, maintain company page.
- **GitHub presence** (if relevant to your domain).
- **Bingbot access**: Full crawl access required.

---

## Claude

**Search backend:** Brave Search (not Google, not Bing)
**Key difference:** Completely different index from other platforms

### What makes it different
Extremely selective about citations. Very low citation rate — looks for the most factually accurate, well-sourced content on a topic. Data-rich content with specific numbers and clear attribution performs significantly better than general-purpose content.

### Key ranking signals
- **Brave Search visibility**: Verify at search.brave.com. If you don't appear there, Claude can't find you.
- **Factual density**: Specific numbers, named sources, dated statistics. Precision is rewarded.
- **Clear extractable structure** with descriptive headings.
- **Authoritative source citations** within your content.
- **Accuracy**: Claude rewards being the most factually accurate source on a topic.

### Claude bots
Allow both `ClaudeBot` and `anthropic-ai` user agents in robots.txt.

---

## Robots.txt Configuration

Allow all AI bots. If any are blocked, that platform can't cite you.

```
User-agent: GPTBot
User-agent: ChatGPT-User
User-agent: PerplexityBot
User-agent: ClaudeBot
User-agent: anthropic-ai
User-agent: Google-Extended
User-agent: Bingbot
Allow: /
```

You can safely block `CCBot` (Common Crawl) without affecting AI search citations — it's only used for training dataset collection.

---

## Priority Order

If optimizing for one platform at a time:

1. **Google AI Overviews** — Largest reach (45%+ of Google searches). You likely have Google SEO foundations already. Add schema, cited sources, E-E-A-T.
2. **ChatGPT** — Most-used standalone AI search. Focus on freshness, domain authority, content-answer fit.
3. **Perplexity** — Valuable for researchers, early adopters, tech audiences. FAQ schema, public PDFs, self-contained paragraphs.
4. **Copilot** — If audience skews enterprise/Microsoft.
5. **Claude** — If audience skews developer/analyst.

### Actions that help on every platform
1. Allow all AI bots in robots.txt
2. Implement schema markup (FAQPage, Article, Organization minimum)
3. Include statistics with named sources
4. Update content monthly for competitive topics
5. Clear heading structure (H1 > H2 > H3)
6. Page load under 2 seconds
7. Author bios with credentials
