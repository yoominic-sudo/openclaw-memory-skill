#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/Users/yoominic/.openclaw/workspace/MEMORY.md')
MAX_LINES = 120

text = TARGET.read_text(encoding='utf-8') if TARGET.exists() else ''
lines = len(text.splitlines())
if lines > MAX_LINES:
    print(f'WARN: MEMORY.md too long ({lines} lines > {MAX_LINES})')
else:
    print(f'OK: MEMORY.md {lines} lines')
