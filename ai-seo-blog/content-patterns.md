# AEO and GEO Content Patterns

Reusable content block patterns optimized for answer engines and AI citation. Use these templates when writing any content in the ai-seo-blog skill.

---

## Contents
- [AEO Block Patterns](#aeo-block-patterns) (Definition, Step-by-Step, Comparison Table, Pros/Cons, FAQ, Listicle)
- [GEO Authority Patterns](#geo-authority-patterns) (Statistic Citation, Expert Quote, Authoritative Claim, Self-Contained Answer, Evidence Sandwich)
- [Domain-Specific Tactics](#domain-specific-tactics)
- [Answer Hub TL;DR Formula](#answer-hub-tldr-formula)

---

## AEO Block Patterns

These patterns help content appear in featured snippets, AI Overviews, voice search results, and answer boxes.

### Definition Block

Use for "What is [X]?" queries. Lead with a single-sentence definition.

```
## What is [Term]?

[Term] is [concise 1-sentence definition]. [1-2 sentence expansion with key characteristics]. [Brief context on why it matters].
```

Keep the first sentence under 30 words. AI systems extract this sentence as the primary answer.

### Step-by-Step Block

Use for "How to [X]" queries. Numbered steps with bolded step names.

```
## How to [Action/Goal]

[1-sentence overview]

1. **[Step Name]**: [Clear action in 1-2 sentences]
2. **[Step Name]**: [Clear action in 1-2 sentences]
3. **[Step Name]**: [Clear action in 1-2 sentences]

[Optional: expected outcome or time estimate]
```

Implement `HowTo` schema alongside this block.

### Comparison Table Block

Use for "[X] vs [Y]" queries. Tables get extracted more reliably than prose.

```
## [Option A] vs [Option B]: [Brief Descriptor]

| Feature | [Option A] | [Option B] |
|---------|------------|------------|
| [Criteria 1] | [Value] | [Value] |
| [Criteria 2] | [Value] | [Value] |
| [Criteria 3] | [Value] | [Value] |
| Best For | [Use case] | [Use case] |

**Bottom line**: [1-2 sentence recommendation based on different needs]
```

Always include a "Best For" row. AI systems use this to match recommendations to user intent.

### Pros and Cons Block

Use for "Is [X] worth it?" and "Should I [X]?" queries.

```
## Advantages and Disadvantages of [Topic]

[1-sentence context]

### Pros
- **[Benefit]**: [Specific explanation with data if possible]
- **[Benefit]**: [Specific explanation]
- **[Benefit]**: [Specific explanation]

### Cons
- **[Drawback]**: [Specific explanation]
- **[Drawback]**: [Specific explanation]

**Verdict**: [1-2 sentence balanced conclusion]
```

### FAQ Block

Essential for FAQPage schema. Use exact phrasing people type into AI.

```
## Frequently Asked Questions

### [Question as people actually ask it]?
[Direct answer in first sentence]. [2-3 supporting sentences with specifics].

### [Question as people actually ask it]?
[Direct answer in first sentence]. [2-3 supporting sentences with specifics].
```

Tips:
- Use "How do I..." not "How does one..."
- Match "People Also Ask" and AI query patterns
- Keep answers 50-100 words
- First sentence must answer the question completely on its own

### Listicle Block

Use for "Best [X]", "Top [X]" queries. Each item needs a justification, not just a name.

```
## [Number] Best [Items] for [Goal/Purpose]

[1-2 sentence intro with selection criteria]

### 1. [Item Name]
[2-3 sentences: why it's included, specific benefit, a real spec or data point]

### 2. [Item Name]
[2-3 sentences with specifics]

### 3. [Item Name]
[2-3 sentences with specifics]
```

Implement `ItemList` schema alongside this block.

---

## GEO Authority Patterns

These patterns increase the likelihood of citation by AI assistants. Based on the Princeton GEO study (KDD 2024):

| Method | Visibility Boost |
|--------|:---:|
| Cite sources | +40% |
| Add statistics | +37% |
| Add expert quotes | +30% |
| Authoritative tone | +25% |
| Improve clarity | +20% |
| Technical terms | +18% |
| Fluency optimization | +15-30% |
| Keyword stuffing | **-10%** (hurts) |

Best combination: Fluency + Statistics = maximum boost.

### Statistic Citation Block

Statistics increase AI citation rates by 15-30%. Always include the source.

```
[Claim]. According to [Source/Organization], [specific statistic with number and timeframe]. [Why this matters].
```

Example: "Mobile optimization directly impacts rankings. According to Google's 2024 Core Web Vitals report, 70% of web traffic comes from mobile devices, and pages failing mobile usability see 24% higher bounce rates."

Rules:
- Cite the original research, not a summary of research
- Include dates on all statistics
- Named organizations beat "studies show"

### Expert Quote Block

Named attribution adds credibility. AI systems can verify named experts.

```
"[Direct quote]," says [Expert Name], [Title] at [Organization]. [1 sentence of context].
```

Rules:
- Real people with verifiable credentials
- Title and organization are required, not optional
- The surrounding sentence should add context, not just repeat the quote

### Authoritative Claim Block

Structure claims so AI can extract them cleanly.

```
[Topic] [is/has/requires] [clear, specific claim]. [Source] [confirms/found] that [supporting evidence]. This [means/suggests] [implication or action].
```

Three-sentence structure: claim → evidence → implication. Each sentence works on its own.

### Self-Contained Answer Block

The most important pattern for AI extraction. Create standalone statements that work without surrounding context.

```
**[Topic/Question]**: [Complete answer in 2-3 sentences with specific details, numbers, or examples.]
```

Test: if you copied just this paragraph into a different document, would it still make sense and be useful? If yes, it's self-contained.

### Evidence Sandwich Block

For building a case with multiple data points.

```
[Opening claim].

Evidence:
- [Data point 1 with source]
- [Data point 2 with source]
- [Data point 3 with source]

[Concluding statement connecting evidence to action].
```

---

## Domain-Specific Tactics

### Health / Supplement Content
- Cite peer-reviewed studies with publication name and year
- Include dosage specifics (mg, form, servings)
- Note third-party testing status and certifying body
- Add "last reviewed" dates
- Reference specific clinical outcomes, not vague "supports health"

### Technology / SaaS Content
- Version numbers and dates for all software mentions
- Reference official documentation
- Code examples where relevant
- Specific performance metrics ("processes 10K requests/sec" not "blazing fast")

### Financial Content
- Reference regulatory bodies (SEC, FTC)
- Specific numbers with timeframes
- Note that content is educational, not advice
- Cite recognized institutions

### Local Business Content
- Frame as "[Year] [City] [Industry] Report"
- Include comparison tables with local competitors
- Real ratings, service areas, pricing tiers
- Structured data that reads as "research" not "advertisement"

### E-commerce / Product Content
- Exact specs: price, quantity, serving size, dimensions
- Third-party testing status with certifying body name
- Review count and average rating (specific numbers)
- Comparison against named competitors with real specs
- GTIN or MPN identifiers for shopping features

---

## Answer Hub TL;DR Formula

This is the most important paragraph on any Answer Hub page. AI will quote it directly. Write it using this formula:

```
For [use case] in [year], [specific recommendation] at [exact spec] is [claim based on evidence].
[Brand Name] [Product] offers [spec 1] with [spec 2] at [price/value].
For [alternative use case], [alternative option] offers [benefit] at [tradeoff].
Compare [decision criteria 1], [criteria 2], and [criteria 3] before choosing.
```

Rules for the TL;DR:
- 60-90 words, no more
- Neutral, factual tone (not promotional)
- Include specific numbers: dosage, price, supply duration
- Name the top pick but acknowledge alternatives
- End with decision criteria the reader should evaluate
- Write it the way you'd want an AI assistant to say it out loud

This single paragraph is responsible for the majority of AI citations from Answer Hub pages. Spend more time on it than any other section.
