#!/usr/bin/env python3
"""Offline editorial hints and exact-token checks; not an authorship detector."""
import argparse
import collections
import json
import re
from pathlib import Path

PATTERNS = {
 'staging': r'接下来让我们|让我们深入|值得注意的是|先说结论|说白了',
 'inflation': r'新时代|无限可能|至关重要|重大意义|全新高度|赋能',
 'decorative_contrast': r'不仅.{0,35}(?:更是|而且)|不是.{0,35}而是',
 'generic_ending': r'拭目以待|未来可期|综上所述|总而言之',
 'performed_voice': r'说真的朋友们|我当时就惊呆了|你敢信|不是哥们',
}

def protected(text):
    # Conservative common Markdown fences, YAML, inline code, quotes and links.
    yaml = re.match(r'\A---\r?\n.*?\r?\n---(?:\r?\n|$)', text, re.S)
    spans = [yaml.group(0)] if yaml else []
    for pattern in [r'(?ms)^```[^\n]*\n.*?^```[^\n]*(?:\n|$)',r'(?ms)^~~~[^\n]*\n.*?^~~~[^\n]*(?:\n|$)',r'`[^`\n]+`',r'https?://[^\s<>\]\)]+',r'「[^」]*」|“[^”]*”',r'(?m)^\|.*\|\s*$']:
        spans += re.findall(pattern,text)
    return collections.Counter(spans)

def analyze(text):
    findings=[]
    for rule,pat in PATTERNS.items():
        for m in re.finditer(pat,text):
            findings.append({'rule':rule,'line':text.count('\n',0,m.start())+1,'excerpt':m.group(0),'action':'contextual_review'})
    return findings

def compare(source,target):
    issues=[]
    a=protected(source);b=protected(target)
    if a!=b:issues.append('protected_span_change')
    nums=lambda s:collections.Counter(re.findall(r'(?<![\w])\d+(?:[.,]\d+)*(?:%|％)?',s))
    if nums(source)!=nums(target):issues.append('numeric_token_change')
    headings=lambda s:re.findall(r'(?m)^#{1,6} .+$',s)
    if headings(source)!=headings(target):issues.append('heading_change')
    return {'mechanical_checks_pass':not issues,'issues':issues,'semantic_review_required':True,'authorship_claim':None}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('source');p.add_argument('target',nargs='?');p.add_argument('--json',action='store_true');args=p.parse_args()
    source=Path(args.source).read_text(encoding='utf-8');target=Path(args.target).read_text(encoding='utf-8') if args.target else None
    report={'source_findings':analyze(source),'meaning':'heuristic editorial hints; not probability of AI authorship'}
    if target is not None:report.update(compare(source,target));report['target_findings']=analyze(target)
    print(json.dumps(report,ensure_ascii=False,indent=2))
    raise SystemExit(1 if report.get('issues') else 0)

if __name__=='__main__':main()
