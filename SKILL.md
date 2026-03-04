# OpenClaw 记忆策略技能

> 自动化记忆管理与 Token 优化方案

## 功能

本技能提供一套完整的 OpenClaw 记忆管理方案，帮助：
- 减少上下文 Token 消耗
- 建立长期/短期记忆分层
- 自动化记忆压缩与归档
- 快速检索记忆

## 文件结构

```
skills/openclaw-memory-strategy/
├── SKILL.md                 # 本文件
├── scripts/
│   ├── daily_summary.py     # 每日记忆压缩
│   ├── weekly_rollup.py     # 周摘要生成
│   └── check_memory_size.py # 检查 MEMORY.md 长度
└── docs/
    ├── MEMORY_STRATEGY.md   # 完整策略文档
    └── AUTOMATION.md        # 自动化配置说明
```

## 快速开始

### 1. 安装技能

```bash
# 克隆或复制到 workspace/skills/
cp -r skills/openclaw-memory-strategy ~/.openclaw/workspace/skills/
```

### 2. 配置 cron（推荐）

```bash
# 添加到 crontab
crontab -e

# 每天 23:40 压缩当日要点
40 23 * * * /path/to/workspace/skills/openclaw-memory-strategy/scripts/daily_summary.py

# 每周日 23:50 生成周摘要
50 23 * * 0 /path/to/workspace/skills/openclaw-memory-strategy/scripts/weekly_rollup.py

# 每天 10:00 检查 MEMORY.md 长度
0 10 * * * /path/to/workspace/skills/openclaw-memory-strategy/scripts/check_memory_size.py
```

### 3. 初始化记忆结构

```bash
# 创建 memory 目录结构
mkdir -p workspace/memory/weekly

# 创建索引文件
cat > workspace/memory/index.md << 'EOF'
# Memory Index

## 用户偏好
- 长期记忆：workspace/MEMORY.md

## 项目（按主题分）
- 日志：workspace/memory/YYYY-MM-DD.md
- 周摘要：workspace/memory/weekly/YYYY-Www.md
EOF
```

## 核心策略

### 分层架构

```
MEMORY.md (热缓存, ≤100行)
    ↑
    │ ← 先查这里，90%场景直接命中
    │
memory/index.md (索引)
    ↑
    │ ← 按主题快速路由
    │
memory/YYYY-MM-DD.md (日记忆)
memory/weekly/YYYY-Www.md (周摘要)
```

### 写入规则

写入 MEMORY.md 的标准：
- 会被反复用到（偏好、固定流程、项目核心约束）
- 决策性信息（已拍板方案、禁止事项）
- 高代价信息（踩坑结论、线上故障根因）

**不要写入：**
- 一次性聊天内容
- 可随时外查的信息
- 已过期/未确认结论

### 检索流程

1. 先查 `MEMORY.md`（热缓存）
2. 再查 `memory/index.md`（索引）
3. 最后查具体日/周文件

## 验收指标

- 平均会话上下文长度下降
- memory_search 命中相关性上升
- 复杂任务中断率下降

## 相关文件

- `MEMORY_STRATEGY.md` - 完整策略文档
- `AUTOMATION.md` - 自动化配置说明
