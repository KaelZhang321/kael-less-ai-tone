# Kael Less AI Tone

Version 2.0: Chinese editorial revision with fact preservation, protected Markdown and author voice. The legacy whitelist remains available in strict mode.

## Core promise

This is a whitelist-based post-editing workflow:

- Four scopes: audit, polish, editorial (default for humanizing), and strict legacy whitelist.
- Editorial mode reviews paragraph purpose and repeated information, not just banned words.
- Facts, numbers, dates, citations, quotations, links and caveats are protected. Headings and column structure stay fixed unless explicitly authorized.
- Paragraphs may be merged inside a section without losing independent information.
- Code blocks, foreign-language passages, quotations, dialogue, and normal question sentences are protected.
- When a possible change is ambiguous, keep the original.

## V2 workflow

Read the complete draft, freeze the information ledger, review paragraph purpose, edit once, compare facts and protected content, then perform one bounded fresh-read pass. Never add fake experience or slang to manufacture personality.

Run `python3 scripts/editorial_qa.py source.md revision.md --json` for offline mechanical checks. These checks cannot prove semantic equivalence or identify AI authorship.

Run tests: `python3 -m unittest discover -s tests -v`.

Research scope and source-review decisions are in `references/research-review.md`; this is not an exhaustive Internet inventory.

## Included checks

- `scripts/check-translationese.py` — checks the supported translationese patterns.
- `scripts/check-structure.py` — measures sentence/paragraph structure patterns; it does not compare draft versions or prove structural preservation.
- `scripts/check-ai-isms.sh` — local literal-pattern lint; findings require contextual review.
- `scripts/compare-human-ai.py` — research/measurement helper.

## Install as a Hermes skill

```bash
git clone https://github.com/KaelZhang321/kael-less-ai-tone.git
cp -R kael-less-ai-tone ~/.hermes/skills/content/
```

Review `SKILL.md` before use. It is intentionally strict: this skill is not a general “make it sound human” rewriter.

## License

The inherited core is MIT-licensed, copyright shiujan; the original notice is preserved in `LICENSE`. This package is a local adaptation, not a claim of original authorship of the inherited rules or research. The bundled word-list lint is a local supplementary script; inspect its rules before use.

Research measurements in `RESEARCH.md` are inherited reports, not new experiments reproduced by this repository. No detector-score, authorship-detection, or plagiarism-evasion guarantees are made. The account-specific override file is optional and must not override factual accuracy or quotation preservation.
