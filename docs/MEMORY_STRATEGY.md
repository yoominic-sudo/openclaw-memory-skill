# OpenClaw 记忆与降 Token 策略（可直接落地）

> 目标：让记忆更稳、更准，同时显著减少上下文 token 消耗。

## 1) 文件分层（先把结构固定）

- `MEMORY.md`：热缓存（Hot Cache）
  - 只放高频、关键、长期有效信息
  - 建议控制在 **50~100 行**
- `memory/YYYY-MM-DD.md`：日记忆（原始流水）
  - 记录当天发生的细节、讨论、临时结论
- `memory/weekly/YYYY-Www.md`：周摘要（压缩层）
  - 每周把日记忆压缩成 10~30 条可复用结论
- `memory/index.md`：索引（路由层）
  - 按主题列出“去哪查”

---

## 2) MEMORY.md 写入规则（只留“值钱信息”）

写入标准（满足任一条才写）：
- 会被反复用到（偏好、固定流程、项目核心约束）
- 决策性信息（已拍板方案、禁止事项）
- 高代价信息（踩坑结论、线上故障根因）

不要写入：
- 一次性聊天内容
- 可随时外查的信息
- 已过期/未确认结论

建议结构：
- User Preferences
- Ongoing Projects
- Do / Don’t
- Infra / Endpoint
- Lessons Learned

---

## 3) 检索路由（先判题，再查文件）

查询前先分类：
- 用户偏好类 → `MEMORY.md`
- 最近进展类 → `memory/近2天`
- 历史决策类 → `memory/weekly` + `MEMORY.md`
- 技术细节类 → `memory/index.md` 指向具体文件

原则：
- 先小范围查，命中不足再扩展
- 返回“最小必要片段”，不要整段喂给模型

---

## 4) 上下文剪枝（Context Pruning）

每轮只保留：
- 当前目标
- 未完成任务
- 关键约束（账号/路径/边界）
- 最近 1~3 轮必要上下文

主动清理：
- 大段网页原文
- 重复日志
- 已完成工具输出
- 与当前任务无关的历史枝节

---

## 5) 摘要节奏（防止记忆越堆越臃肿）

- 每天：把 `memory/YYYY-MM-DD.md` 末尾补一个“今日要点（3~10条）”
- 每周：生成 `memory/weekly/YYYY-Www.md`
- 每两周：清理 `MEMORY.md`（删旧、合并重复、上浮高频）

---

## 6) 成本优化（模型分工）

- 记忆整理/摘要：用便宜模型
- 复杂推理/最终输出：用强模型
- 高成本模型只在“必要步骤”调用

---

## 7) 可直接复制的模板

### memory/index.md

```md
# Memory Index

## 用户偏好
- 主文件：/Users/yoominic/.openclaw/workspace/MEMORY.md

## 项目：openclaw-model-console
- 日志：/Users/yoominic/.openclaw/workspace/memory/2026-03-04.md
- 周摘要：/Users/yoominic/.openclaw/workspace/memory/weekly/2026-W10.md

## 服务器与部署
- TOOLS: /Users/yoominic/.openclaw/workspace/TOOLS.md
```

### 日记忆末尾追加模板

```md
## 今日要点（自动压缩）
- [决策] xxx
- [变更] xxx
- [风险] xxx
- [待办] xxx
```

---

## 8) 最小执行清单（今天就能做）

1. 保持 `MEMORY.md` 在 100 行内
2. 新增 `memory/index.md`（主题索引）
3. 每晚把当日日志压缩成 3~10 条要点
4. 周末生成一份周摘要并回填 MEMORY.md

---

## 9) 验收指标（是否真的降 token）

- 平均会话上下文长度下降
- memory_search 的命中相关性上升
- 需要回溯全量历史的次数下降
- 复杂任务中断率下降（少“忘事”）

> 一句话：**记忆不是越多越好，而是“高命中 + 低噪声 + 可维护”。**
