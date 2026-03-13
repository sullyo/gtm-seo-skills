# GTM SEO Skills

A collection of Claude Code skills for automated SEO content marketing. Three skills that work together to research keywords, write AI-optimized blog posts, and run a full content pipeline at scale.

## Skills

### 1. `ai-seo-blog` — AI SEO Blog Writer
Write blog posts and web content optimized for AI search engines (ChatGPT, Perplexity, Google AI Overviews, Claude, Copilot). Handles structure, schema markup, and humanization so content gets cited by AI assistants and reads like a human wrote it.

### 2. `gtm-content-engine` — GTM Content Engine
Automated content pipeline: keyword research, SERP analysis, content calendar, and article generation at scale (3/day). Combines SERP intelligence with founder transcripts to produce differentiated content. Uses `ai-seo-blog` for writing quality standards.

### 3. `keywords-everywhere` — Keywords Everywhere API
SEO/SEM data retrieval via the Keywords Everywhere REST API. Search volume, CPC, competition, related keywords, backlinks, and domain analysis — all from the command line.

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-org/gtm-seo-skills.git
```

### 2. Install as Claude Code skills

Each subfolder is a standalone skill. Add them to Claude Code by running:

```bash
claude skill add /path/to/gtm-seo-skills/ai-seo-blog
claude skill add /path/to/gtm-seo-skills/gtm-content-engine
claude skill add /path/to/gtm-seo-skills/keywords-everywhere
```

Or add all three at once from the repo root:

```bash
for skill in ai-seo-blog gtm-content-engine keywords-everywhere; do
  claude skill add "$(pwd)/$skill"
done
```

### 3. Set up credentials

The `keywords-everywhere` skill requires an API key:

```bash
export KEYWORDS_EVERYWHERE_API_KEY='your-api-key-here'
```

**Where to get the API key:**
1. Create an account at [keywordseverywhere.com](https://keywordseverywhere.com)
2. Purchase API credits (starts at $1 for 100,000 credits)
3. Go to **API** > **API Settings** at [keywordseverywhere.com/api-settings.html](https://keywordseverywhere.com/api-settings.html)
4. Copy your API key

Add the export to your shell profile (`~/.zshrc` or `~/.bashrc`) to make it persistent.

### 4. Install Python dependency (for keywords-everywhere)

```bash
pip install requests --break-system-packages
```

### 5. Configure your product (for gtm-content-engine)

The content engine needs to know about your product to generate relevant content. Edit the product file:

```
gtm-content-engine/references/product.md
```

Replace all `[placeholder]` values with your actual product details — name, features, competitors, target audience, differentiators, etc. A template is also available at `references/product-template.md`.

If you skip this step, the engine will prompt you to fill it in when you first use it.

## How the skills work together

```
keywords-everywhere          ai-seo-blog
   (SEO data)               (writing quality)
        \                       /
         \                     /
          v                   v
       gtm-content-engine
       (orchestration pipeline)
              |
              v
         Blog articles
       (MDX for Fumadocs)
```

- **keywords-everywhere** provides the data: search volume, CPC, competition, related keywords, backlinks
- **ai-seo-blog** provides the writing standards: AI-optimized structure, humanization, schema markup
- **gtm-content-engine** orchestrates the pipeline: keyword research -> content calendar -> SERP analysis -> article generation

You can use each skill independently, but they're designed to complement each other.

## Usage examples

**Keyword research:**
> "Find keywords related to AI video editing"

**Content calendar:**
> "Build a content calendar for the next week"

**Write a single article:**
> "Write a blog post targeting 'best AI ad makers 2026'"

**Run the full pipeline:**
> "Run today's batch" or "Generate today's articles"

**Check SEO data:**
> "What keywords does competitor.com rank for?"

**Backlink analysis:**
> "Show me backlinks pointing to competitor.com/blog"

## Skill structure

```
gtm-seo-skills/
├── README.md
├── ai-seo-blog/
│   ├── SKILL.md                      # Skill definition
│   ├── content-patterns.md           # AEO/GEO content block patterns
│   ├── humanizer-checklist.md        # AI writing detection & removal
│   └── platform-ranking-factors.md   # AI platform optimization guide
├── gtm-content-engine/
│   ├── SKILL.md                      # Skill definition
│   └── references/
│       ├── product.md                # YOUR product details (fill this in)
│       ├── product-template.md       # Template for the product file
│       ├── keyword-research.md       # Keyword research workflow
│       └── content-pipeline.md       # SERP analysis to publishing
└── keywords-everywhere/
    ├── SKILL.md                      # Skill definition
    └── scripts/
        └── ke_client.py              # Python CLI for Keywords Everywhere API
```

## Credentials summary

| Skill | Environment Variable | Where to get it |
|---|---|---|
| `keywords-everywhere` | `KEYWORDS_EVERYWHERE_API_KEY` | [keywordseverywhere.com/api-settings.html](https://keywordseverywhere.com/api-settings.html) |
