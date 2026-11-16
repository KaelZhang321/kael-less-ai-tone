#!/usr/bin/env bash
# 中文 AI 味词 + 合规红线快速扫描。
# 用法: ./check-ai-isms.sh <文件或目录>   （目录递归扫 *.md）
# 退出码: 0 = 干净；1 = 有命中（命中可能是"合规说明文字"本身，人工复核上下文即可）
TARGET="${1:-.}"
if [ -d "$TARGET" ]; then
  FILES=$(find "$TARGET" -name "*.md")
else
  FILES="$TARGET"
fi
PAT='赋能|闭环|抓手|颗粒度|底层逻辑|助力|打造|点亮|深耕|赛道|私域|心智|链路|破圈|躬身入局|升维|降维|思维模型|跑通|重构|一站式|天花板|YYDS|干货满满|保姆级|手把手|不仅.*更|让我们|总而言之|综上所述|值得注意的是|包过|保过|考了就涨薪|拿证即就业|提分|保送|代考|代做'
HIT=0
for f in $FILES; do
  M=$(grep -n -E "$PAT" "$f" 2>/dev/null)
  if [ -n "$M" ]; then
    echo "⚠️ $f:"
    echo "$M"
    HIT=1
  fi
done
[ $HIT -eq 0 ] && echo "✅ 无 AI 味词、无违规承诺"
exit $HIT
