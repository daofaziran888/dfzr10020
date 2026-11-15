# 道法自然非遗手工艺传习工坊管理平台

面向非遗手工艺传承的师徒带教、材料采备、工序流转、作品评审与工坊展销的一体化传习管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 传承项目 | `inheritance` | 技艺项目 | 项目编号、技艺名称、所属名录 |
| 传承人档案 | `master` | 传承人 | 传承人编号、姓名、技艺门类 |
| 学徒管理 | `apprentice` | 学徒 | 学徒编号、姓名、师从何人 |
| 材料采备 | `material` | 原材料 | 材料编号、材料名称、材料类别 |
| 工具管理 | `tool` | 手工工具 | 工具编号、工具名称、工具类别 |
| 作品工序 | `workpiece` | 在制作品 | 作品编号、作品名称、技艺门类 |
| 工序标准 | `procedure` | 工序步骤 | 工序编号、工序名称、所属技艺 |
| 作品评审 | `review` | 评审记录 | 评审编号、评审作品、评审日期 |
| 展销活动 | `exhibition` | 展销活动 | 活动编号、活动名称、活动类型 |
| 奖项荣誉 | `award` | 获奖记录 | 奖项编号、奖项名称、获奖作品 |
| 培训课程 | `training` | 传习课程 | 课程编号、课程名称、授课传承人 |
| 捐赠收藏 | `donation` | 捐赠记录 | 捐赠编号、捐赠人、捐赠物品 |
| 合作机构 | `partner` | 合作单位 | 机构编号、机构名称、合作方向 |
| 项目经费 | `fund` | 经费项目 | 项目编号、经费来源、批准金额 |
| 文献资料 | `document` | 技艺文献 | 文献编号、文献名称、文献类型 |
| 参观接待 | `visit` | 来访记录 | 记录编号、来访单位、来访人数 |
| 品质抽检 | `quality` | 抽检记录 | 抽检编号、抽检对象、抽检日期 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
