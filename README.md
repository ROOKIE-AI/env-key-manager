# Env Key Manager

一个安全的环境变量密钥管理器，支持加密存储和加载环境变量。

## 功能特点

- 安全加密存储环境变量
- 支持自定义环境变量名称
- 交互式命令行界面
- 自动保存和加载已配置的密钥
- 使用 Fernet 对称加密算法
- 支持自定义配置文件路径

## 安装

```bash
pip install env-key-manager
```

## 使用方法

### 命令行使用

```bash
# 启动交互式配置
env-key-manager

# 或者直接指定环境变量名称
env-key-manager --env-names "API_KEY1" "API_KEY2"

# 使用自定义配置文件
env-key-manager --config-file "/path/to/config.json"
```

### Python 代码中使用

```python
from env_key_manager import APIKeyManager

# 创建实例
key_manager = APIKeyManager()

# 设置环境变量
key_manager.setup_api_key(["OPENAI_API_KEY", "API_KEY2"])

# 使用自定义配置文件
key_manager = APIKeyManager(config_file="/path/to/config.json")
```

## 配置说明

- 配置文件默认保存在用户主目录下的 `.env_config.json`
- 所有密钥都经过加密存储
- 支持自定义配置文件路径
- 使用 Fernet 对称加密算法确保安全性

## 开发

```bash
# 克隆仓库
git clone https://github.com/ROOKIE-AI/env-key-manager.git
cd env-key-manager

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest
```

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 作者

ROOKIE