# Humanizer Checklist

Run every piece of content through this checklist before delivering. Based on Wikipedia's "Signs of AI writing" guide. The goal: content that is structured for AI extraction but reads like a human with opinions wrote it.

---

## Contents
- [The Two-Pass Process](#the-two-pass-process)
- [Content Patterns to Kill](#content-patterns-to-kill)
- [Language Patterns to Kill](#language-patterns-to-kill)
- [Style Patterns to Kill](#style-patterns-to-kill)
- [Filler and Hedging to Kill](#filler-and-hedging-to-kill)
- [Adding Voice](#adding-voice)
- [AI Vocabulary Blacklist](#ai-vocabulary-blacklist)

---

## The Two-Pass Process

After writing any draft:

**Pass 1:** Scan for every pattern in this document. Fix each one.

**Pass 2:** Ask yourself "What makes this obviously AI-generated?" Answer honestly with the remaining tells. Fix those too.

Only deliver after both passes. No exceptions.

---

## Content Patterns to Kill

### Significance inflation
AI puffs up importance with phrases about how things "represent broader trends" or "mark pivotal moments."

Kill: "stands/serves as", "is a testament to", "a vital/crucial/pivotal role", "underscores/highlights its importance", "reflects broader", "symbolizing its ongoing", "setting the stage for", "represents a shift", "evolving landscape"

Before: "The new policy marks a pivotal moment in the evolution of regional data privacy, reflecting broader global trends."
After: "The new policy requires companies to delete user data within 30 days of request."

### Fake depth with -ing phrases
AI tacks present participle phrases onto sentences to sound analytical.

Kill: "highlighting...", "underscoring...", "emphasizing...", "reflecting...", "symbolizing...", "contributing to...", "showcasing...", "fostering...", "ensuring..."

Before: "The platform uses end-to-end encryption, ensuring user privacy while showcasing their commitment to security."
After: "The platform uses end-to-end encryption."

### Promotional language
AI can't keep a neutral tone, especially for products and places.

Kill: "boasts a", "vibrant", "rich" (figurative), "profound", "nestled", "in the heart of", "groundbreaking", "renowned", "breathtaking", "stunning", "cutting-edge", "game-changing", "revolutionary"

Before: "Nestled in the heart of Austin's vibrant tech scene, this groundbreaking platform boasts a rich feature set."
After: "The platform launched in Austin in 2023 and has 40,000 active users."

### Vague attributions
AI attributes claims to unnamed authorities.

Kill: "Industry reports suggest", "Experts argue", "Observers have cited", "Some critics argue", "Studies show"

Replace with specific sources: "A 2024 Stanford study found..." or "According to Gartner's Q3 2024 report..."

### Formulaic "challenges and future" sections
AI always adds a "Despite challenges... the future looks bright" section.

Kill any section that follows the pattern: despite [problems] → but → optimistic conclusion. Replace with specific, dated facts about what actually happened or is planned.

---

## Language Patterns to Kill

### Copula avoidance
AI substitutes elaborate constructions for simple "is" and "are."

Kill: "serves as", "stands as", "functions as", "represents", "marks"
Replace with: "is", "are", "has"

Before: "The dashboard serves as the primary interface for data visualization."
After: "The dashboard is the primary interface for data visualization."

### Negative parallelisms
"It's not just X; it's Y" and "Not only... but also..."

Before: "It's not just about the features; it's about the experience."
After: Just state what it is. Drop the rhetorical construction entirely.

### Rule of three
AI forces ideas into groups of three.

Before: "The event features innovation, inspiration, and industry insights."
After: Pick the one or two that actually matter and say something specific about them.

### Elegant variation (synonym cycling)
AI has repetition penalties that cause excessive synonym substitution. The protagonist becomes the main character becomes the central figure becomes the hero.

Fix: Pick one term and use it consistently. Repetition is fine.

### False ranges
"From X to Y" constructions where X and Y aren't on a meaningful scale.

Before: "From startups to enterprises, from marketing to engineering..."
After: Just list the specific things without the rhetorical framing.

---

## Style Patterns to Kill

### Em dash overuse
AI uses em dashes (—) far more than humans. One per article maximum. Replace most with commas, periods, or parentheses.

### Bold overuse
AI mechanically bolds phrases. Use bold sparingly — only for terms being defined or genuine emphasis, not for every noun phrase.

### Inline-header vertical lists
AI writes lists where every item starts with a bolded header and colon. Convert to prose when the list has 3 or fewer items. For longer lists, vary the format.

### Title Case headings
AI capitalizes all main words. Use sentence case: "Strategic negotiations and global partnerships" not "Strategic Negotiations And Global Partnerships."

### Emojis
Never decorate headings or bullet points with emojis unless the user explicitly requests them.

### Curly quotation marks
Use straight quotes ("...") not curly quotes ("...").

---

## Filler and Hedging to Kill

### Filler phrases
- "In order to" → "To"
- "Due to the fact that" → "Because"
- "At this point in time" → "Now"
- "In the event that" → "If"
- "Has the ability to" → "Can"
- "It is important to note that" → (delete, just state the thing)
- "It is worth mentioning that" → (delete)
- "When it comes to" → (delete or rephrase)

### Excessive hedging
Before: "It could potentially possibly be argued that the policy might have some effect."
After: "The policy may affect outcomes."

### Generic positive conclusions
Kill: "The future looks bright", "Exciting times lie ahead", "This represents a major step", "continues their journey toward excellence."

Replace with a specific fact: "The company plans to open two more locations next year."

### Chatbot artifacts
Kill anything that sounds like a chatbot talking to you: "Great question!", "I hope this helps!", "Let me know if you'd like me to expand on any section", "Here is an overview of...", "Certainly!", "Of course!"

These should never appear in published content.

---

## Adding Voice

Removing AI patterns is half the job. The other half is making it sound like a person wrote it.

### Signs of soulless writing (even if "clean"):
- Every sentence is the same length
- No opinions, just neutral reporting
- No uncertainty or mixed feelings
- No first person
- No humor, no edge
- Reads like a Wikipedia article or press release

### How to fix it:

**Have opinions.** React to the facts you're presenting. "I don't know how to feel about this" is more human than a neutral pros/cons list.

**Vary rhythm.** Short sentences. Then longer ones. Mix it up. A paragraph of identically structured sentences is a tell.

**Acknowledge complexity.** Real people have mixed feelings. "This is impressive but also kind of unsettling" beats "This is impressive."

**Use "I" when it fits.** First person isn't unprofessional. "Here's what gets me..." signals a real person.

**Be specific about feelings.** Not "this is concerning" but "there's something unsettling about running tests against a live database at 3am."

**Let some mess in.** Perfect structure feels algorithmic. An aside or half-formed thought is human.

### Important caveat for AI SEO content:
You're balancing two things: AI-extractable structure (clean, predictable, self-contained paragraphs) and human voice. The structure IS important — don't sacrifice extractability for personality. Instead, inject voice WITHIN the structured format. Each self-contained paragraph can still have personality. The FAQ answers can still sound like a person. The comparison table stays a table, but the "bottom line" sentence can have an opinion.

---

## AI Vocabulary Blacklist

These words appear far more frequently in AI-generated text than in human writing. Avoid or replace:

additionally, align with, arguably, at its core, catalyst, commendable, comprehensive, crucial, cutting-edge, delve, elevate, embark, emphasizing, empower, encompassing, enduring, enhance, ensure, evolving, exemplifies, explore, facilitate, foster, furthermore, garner, groundbreaking, harness, highlight (as verb), holistic, illuminate, impact (as verb meaning "affect"), in conclusion, in summary, in today's [X], innovative, instrumental, interplay, intricate/intricacies, it's important to note, it's worth noting, journey (abstract), key (as adjective), landscape (abstract), leverage, Moreover, multifaceted, navigate (abstract), notably, nuance/nuanced, optimize, overarching, paramount, pivotal, poised, profound, realm, reshape, robust, seamless, shed light on, showcase, streamline, synergy, tapestry (abstract), testament, transformative, treasure trove, underscore, unique (when meaning "good"), unlock, unpack, valuable, vibrant, vital

Not every use of these words is wrong. "Additionally" in a list of genuine additions is fine. But if you see three or more of these words clustered together, rewrite the passage.
