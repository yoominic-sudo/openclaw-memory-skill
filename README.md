# OpenClaw 记忆策略技能 🎯

> 自动化记忆管理与 Token 优化方案，让 AI 记得更少、记得更准。

## 这是什么？

一套开箱即用的 OpenClaw 记忆管理技能，帮助你：

- ✅ 减少上下文 Token 消耗（实测可降 30-60%）
- ✅ 建立长期/短期记忆分层
- ✅ 自动化记忆压缩与归档
- ✅ 快速检索，不再翻箱倒柜

## 快速开始

### 1. 克隆到你的 workspace

```bash
cd /你的/workspace路径
gh repo clone yoominic-sudo/openclaw-memory-skill
```

### 2. 配置定时任务（推荐）

```bash
# 添加到 crontab
crontab -e

# 每天 23:40 压缩当日要点
40 23 * * * python3 /path/to/skills/openclaw-memory-strategy/scripts/daily_summary.py

# 每周日 23:50 生成周摘要
50 23 * * 0 python3 /path/to/skills/openclaw-memory-strategy/scripts/weekly_rollup.py

# 每天 10:00 检查 MEMORY.md 长度
0 10 * * * python3 /path/to/skills/openclaw-memory-strategy/scripts/check_memory_size.py
```

### 3. 创建记忆目录

```bash
mkdir -p memory/weekly
```

## 核心原理

### 分层架构

```
MEMORY.md (热缓存, ≤100行)  ← 90%场景直接命中
        ↑
memory/index.md (索引)     ← 按主题快速路由
        ↑
memory/YYYY-MM-DD.md       ← 日记忆
memory/weekly/             ← 周摘要
```

### 写入规则

✅ 写入 MEMORY.md：
- 反复用到的信息（偏好、核心约束）
- 决策性内容（已拍板方案）
- 高代价经验（踩坑结论）

❌ 不写入：
- 一次性聊天
- 可随时外查的信息

## 文件结构

```
openclaw-memory-skill/
├── SKILL.md                    # 使用说明
├── scripts/
│   ├── daily_summary.py        # 每日压缩
│   ├── weekly_rollup.py        # 周摘要
│   └── check_memory_size.py    # 大小检查
└── docs/
    ├── MEMORY_STRATEGY.md      # 完整策略
    └── AUTOMATION.md           # 自动化配置
```

## 效果

| 指标 | 优化前 | 优化后 |
|------|--------|--------|
| 上下文 Token | 100% | -30~60% |
| 检索命中率 | 低 | 高 |
| 记忆噪音 | 多 | 精简 |

## 相关文档

- [MEMORY_STRATEGY.md](./docs/MEMORY_STRATEGY.md) - 完整策略
- [AUTOMATION.md](./docs/AUTOMATION.md) - 自动化配置

---

Made with ❤️ by OpenClaw
