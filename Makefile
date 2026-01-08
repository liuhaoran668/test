.PHONY: help install format lint type-check test security clean all

help:  ## 显示帮助信息
	@echo "可用的命令："
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## 安装开发依赖
	pip install --upgrade pip
	pip install -r requirements-dev.txt

format:  ## 格式化代码（Black + isort）
	black .
	isort .

format-check:  ## 检查代码格式
	black --check --diff .
	isort --check-only --diff .

lint:  ## 运行代码检查（Flake8 + Ruff）
	flake8 .
	ruff check .

lint-fix:  ## 自动修复代码问题
	ruff check --fix .

type-check:  ## 运行类型检查（MyPy）
	mypy .

test:  ## 运行测试
	pytest -v

test-cov:  ## 运行测试并生成覆盖率报告
	pytest --cov=. --cov-report=html --cov-report=term -v
	@echo "覆盖率报告已生成到 htmlcov/index.html"

security:  ## 运行安全扫描（Bandit）
	bandit -r . -f screen

clean:  ## 清理生成的文件
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf bandit-report.json

all: format lint type-check test  ## 运行所有检查（格式化、检查、类型检查、测试）

ci: format-check lint type-check test security  ## 模拟 CI 环境检查（不自动格式化）
