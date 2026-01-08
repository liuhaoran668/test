# Python CI/CD 测试项目

![Python CI](https://github.com/yourusername/yourrepo/workflows/Python%20CI/badge.svg)

你好，测试增加

## 📋 项目简介

这是一个配置了完整 CI/CD 流程的 Python 项目示例，包含代码格式化、代码检查、类型检查和测试。

## 🚀 特性

- ✅ **代码格式化**: 使用 Black 和 isort
- 🔍 **代码检查**: 使用 Flake8 和 Ruff
- 🔒 **类型检查**: 使用 MyPy
- 🧪 **单元测试**: 使用 Pytest
- 🛡️ **安全扫描**: 使用 Bandit
- 📊 **代码覆盖率**: 自动生成覆盖率报告
- 🔄 **多版本测试**: 支持 Python 3.9, 3.10, 3.11

## 📦 安装

### 1. 克隆仓库

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements-dev.txt
```

## 🛠️ 开发工具使用

### 代码格式化

```bash
# 检查代码格式
black --check .

# 自动格式化代码
black .

# 排序 imports
isort .
```

### 代码检查

```bash
# Flake8 检查
flake8 .

# Ruff 检查（更快）
ruff check .

# 自动修复部分问题
ruff check --fix .
```

### 类型检查

```bash
mypy .
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行测试并生成覆盖率报告
pytest --cov=. --cov-report=html

# 查看覆盖率报告
open htmlcov/index.html  # Mac
# 或
start htmlcov/index.html  # Windows
```

### 安全扫描

```bash
bandit -r .
```

### 一键运行所有检查

```bash
# 可以创建一个脚本来运行所有检查
black . && isort . && ruff check --fix . && mypy . && pytest
```

## 🔄 CI/CD 工作流

项目配置了 GitHub Actions 自动化工作流（`.github/workflows/python-ci.yml`），每次推送或 PR 时会自动执行：

1. **代码质量检查** - 在多个 Python 版本上运行
   - Black 格式检查
   - isort import 排序检查
   - Flake8 代码风格检查
   - Ruff 现代 linter 检查
   - MyPy 类型检查
   - Pytest 单元测试
   - 代码覆盖率报告

2. **安全检查**
   - Bandit 安全漏洞扫描

## 📁 项目结构

```
.
├── .github/
│   └── workflows/
│       └── python-ci.yml      # GitHub Actions 工作流配置
├── src/                        # 源代码目录
│   ├── __init__.py
│   └── calculator.py          # 示例模块
├── tests/                      # 测试目录
│   ├── __init__.py
│   └── test_calculator.py     # 示例测试
├── .gitignore                  # Git 忽略文件
├── pyproject.toml              # 项目配置和工具设置
├── requirements-dev.txt        # 开发依赖
├── LICENSE                     # 许可证
└── README.md                   # 项目说明
```

## ⚙️ 配置说明

所有工具的配置都在 `pyproject.toml` 文件中统一管理：

- **Black**: 行长度 88，支持 Python 3.9+
- **isort**: 兼容 Black 的配置
- **Flake8**: 最大行长度 88，复杂度限制 10
- **Ruff**: 启用多个规则集（pycodestyle、pyflakes、isort 等）
- **MyPy**: 启用严格类型检查
- **Pytest**: 配置测试路径和选项
- **Coverage**: 配置覆盖率报告
- **Bandit**: 配置安全扫描排除项

## 🤝 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

**注意**: 所有 PR 必须通过 CI 检查才能合并！

## 📝 开发建议

### Git Hooks (可选)

你可以使用 pre-commit 来在提交前自动运行检查：

```bash
pip install pre-commit
pre-commit install
```

创建 `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.9
    hooks:
      - id: ruff
        args: [--fix]
```

### IDE 集成

#### VS Code

安装推荐的扩展：
- Python
- Pylance
- Black Formatter
- isort
- Ruff

在 `.vscode/settings.json` 中配置：

```json
{
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  }
}
```

#### PyCharm

在设置中配置：
- File Watchers: 配置 Black 和 isort
- External Tools: 配置 Flake8、Ruff、MyPy
- Python Integrated Tools: 选择 Pytest 作为测试运行器

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 📮 联系方式

如有问题或建议，请提交 Issue 或 Pull Request。
