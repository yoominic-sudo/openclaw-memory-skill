# Memory Automation

## 脚本
- `scripts/memory_automation/daily_summary.py`：每天给 `memory/YYYY-MM-DD.md` 追加“今日要点”
- `scripts/memory_automation/weekly_rollup.py`：生成本周 `memory/weekly/YYYY-Www.md`
- `scripts/memory_automation/check_memory_size.py`：检查 `MEMORY.md` 是否超长

## 本地 cron 示例

```cron
# 每天 23:40 生成当日压缩要点
40 23 * * * /usr/bin/python3 /Users/yoominic/.openclaw/workspace/scripts/memory_automation/daily_summary.py

# 每周日 23:50 生成周摘要
50 23 * * 0 /usr/bin/python3 /Users/yoominic/.openclaw/workspace/scripts/memory_automation/weekly_rollup.py

# 每天 10:00 检查 MEMORY.md 长度
0 10 * * * /usr/bin/python3 /Users/yoominic/.openclaw/workspace/scripts/memory_automation/check_memory_size.py
```

## 手动执行

```bash
python3 scripts/memory_automation/daily_summary.py
python3 scripts/memory_automation/weekly_rollup.py
python3 scripts/memory_automation/check_memory_size.py
```
