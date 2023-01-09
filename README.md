# 电影知识问答

基于知识图谱的电影知识问答系统。

[![预览](assets/preview.webp)](https://kgqa.mrcai.dev)

## ✨ 项目介绍

- 训练 TF-IDF 向量算法和朴素贝叶斯分类器，预测用户文本所属的问题类别
- 使用分词库解析用户文本词性，提取关键词
- 结合关键词与问题类别，在 Neo4j 中查询问题的答案
- 通过 Flask 对外提供 RESTful API
- 前端交互与答案展示

## 🚀 项目使用

在 `backend` 目录下添加环境变量文件 `.env`。

```
# Neo4j 数据库地址
DATABASE_URI=

# Neo4j 用户名
DATABASE_USER=

# Neo4j 密码
DATABASE_PASSWORD=
```

启动后端服务。

```
cd backend
gunicorn app:app
```

在 `frontend` 目录下添加环境变量文件 `.env`。

```
# 后端服务地址
VITE_API_BASE_URL=
```

启动前端服务。

```
cd frontend
npm build
npm preview
```

## 🗃️ 技术栈

### 数据库

[![Neo4j](https://img.shields.io/badge/neo4j-006fd6?style=for-the-badge&logo=neo4j&logoColor=ffffff)](https://neo4j.com/)

### 核心 QA 模块

[![Python](https://img.shields.io/badge/python-3776ab?style=for-the-badge&logo=python&logoColor=ffd343)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/sklearn-ff9c34?style=for-the-badge&logo=scikit-learn&logoColor=ffffff)](https://scikit-learn.org/stable/index.html)
[![Jieba](https://img.shields.io/badge/jieba-3776ab?style=for-the-badge&logo=python&logoColor=ffd343)](https://github.com/fxsjy/jieba)

### 后端

[![Python](https://img.shields.io/badge/python-3776ab?style=for-the-badge&logo=python&logoColor=ffd343)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3e4349?style=for-the-badge&logo=flask&logoColor=ffffff)](https://www.python.org/)
[![Render](https://img.shields.io/badge/render-eef2f5?style=for-the-badge&logo=render)](https://render.com/)

### 前端

[![TypeScript](https://img.shields.io/badge/typescript-3178c6?style=for-the-badge&logo=typescript&logoColor=ffffff)](https://www.typescriptlang.org/)
[![Preact](https://img.shields.io/badge/preact-673ab8?style=for-the-badge&logo=preact&logoColor=ffffff)](https://preactjs.com/)
[![Tailwind CSS](https://shields.io/badge/tailwind%20css-38bdf8?style=for-the-badge&logo=tailwindcss&logoColor=ffffff)](https://tailwindcss.com/)
[![pnpm](https://img.shields.io/badge/pnpm-f69220?style=for-the-badge&logo=pnpm&logoColor=ffffff)](https://pnpm.io/)
[![Vite](https://img.shields.io/badge/vite-646cff?style=for-the-badge&logo=vite&logoColor=ffffff)](https://vitejs.dev/)
[![ESLint](https://shields.io/badge/eslint-4b32c3?style=for-the-badge&logo=eslint&logoColor=ffffff)](https://eslint.org/)
[![Prettier](https://shields.io/badge/prettier-24292e?style=for-the-badge&logo=prettier)](https://prettier.io/)

## 📜 许可证

[MIT](LICENSE)
