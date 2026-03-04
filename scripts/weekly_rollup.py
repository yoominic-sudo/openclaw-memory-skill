#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timedelta

ROOT = Path('/Users/yoominic/.openclaw/workspace')


def main():
    today = datetime.now()
    year, week, _ = today.isocalendar()
    out = ROOT / 'memory' / 'weekly' / f'{year}-W{week:02d}.md'

    days = []
    for i in range(7):
        d = today - timedelta(days=i)
        p = ROOT / 'memory' / f"{d.strftime('%Y-%m-%d')}.md"
        if p.exists():
            days.append(p)
    days.reverse()

    lines = [f'# Weekly Summary {year}-W{week:02d}', '']
    for p in days:
        text = p.read_text(encoding='utf-8')
        key = []
        capture = False
        for ln in text.splitlines():
            if ln.strip().startswith('## 今日要点（自动压缩）'):
                capture = True
                continue
            if capture and ln.strip().startswith('## '):
                break
            if capture and ln.strip().startswith('- '):
                key.append(ln.strip())
        if key:
            lines.append(f'## {p.stem}')
            lines.extend(key[:10])
            lines.append('')

    out.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')
    print(f'generated: {out}')


if __name__ == '__main__':
    main()
