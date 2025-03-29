import argparse
from .manager import APIKeyManager

def main():
    parser = argparse.ArgumentParser(description="环境变量密钥管理器")
    parser.add_argument(
        "--env-names",
        nargs="+",
        help="要设置的环境变量名称列表",
    )
    parser.add_argument(
        "--config-file",
        help="配置文件路径",
    )
    
    args = parser.parse_args()
    
    key_manager = APIKeyManager(config_file=args.config_file)
    key_manager.setup_api_key(args.env_names)

if __name__ == "__main__":
    main() 