# Kael Less AI Tone

A conservative Chinese editing skill for removing explicitly defined AI-writing tells without rewriting the author’s voice.

## Core promise

This is a whitelist-based post-editing workflow:

- Only rules explicitly listed in `SKILL.md` may trigger a rewrite.
- Unmatched text remains unchanged.
- Article structure, facts, numbers, dates, citations, quotations, links, caveats, and paragraph order are preserved.
- Code blocks, foreign-language passages, quotations, dialogue, and normal question sentences are protected.
- When a possible change is ambiguous, keep the original.

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
