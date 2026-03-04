#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime

ROOT = Path('/Users/yoominic/.openclaw/workspace')

def extract_points(text: str, limit=8):
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    picks = []
    for l in lines:
        if any(k in l for k in ['修复', '部署', '完成', '新增', '更新', '问题', '风险', '待办', '决定']):
            picks.append(l[:140])
        if len(picks) >= limit:
            break
    if not picks:
        picks = [l[:140] for l in lines[:min(5, len(lines))]]
    return picks

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    f = ROOT / 'memory' / f'{today}.md'
    if not f.exists():
        print(f'skip: {f} not found')
        return
    raw = f.read_text(encoding='utf-8')
    if '## 今日要点（自动压缩）' in raw:
        print('skip: summary already exists')
        return

    points = extract_points(raw)
    block = '\n\n## 今日要点（自动压缩）\n' + '\n'.join([f'- {p}' for p in points]) + '\n'
    f.write_text(raw.rstrip() + block, encoding='utf-8')
    print(f'updated: {f}')

if __name__ == '__main__':
    main()
