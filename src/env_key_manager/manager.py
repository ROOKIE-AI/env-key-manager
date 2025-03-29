import os
import getpass
import json
import base64
from cryptography.fernet import Fernet
from pathlib import Path

class APIKeyManager:
    """API密钥管理器类，用于加密存储和加载API密钥"""
    
    def __init__(self, config_file=None):
        """初始化API密钥管理器
        
        Args:
            config_file: 配置文件路径，默认为用户主目录下的.env_config.json
        """
        self.config_file = Path(config_file) if config_file else Path.home() / ".env_config.json"
    
    def encrypt_api_key(self, api_key, encryption_key):
        """加密API密钥"""
        f = Fernet(encryption_key)
        encrypted_key = f.encrypt(api_key.encode())
        return base64.b64encode(encrypted_key).decode()
    
    def decrypt_api_key(self, encrypted_key, encryption_key):
        """解密API密钥"""
        f = Fernet(encryption_key)
        decoded_key = base64.b64decode(encrypted_key)
        return f.decrypt(decoded_key).decode()
    
    def save_custom_api_key(self, env_name, api_key):
        """保存加密的自定义API密钥到配置文件"""
        # 生成加密密钥
        encryption_key = Fernet.generate_key()
        
        # 加密API密钥
        encrypted_key = self.encrypt_api_key(api_key, encryption_key)
        
        # 如果配置文件已存在，读取现有配置
        config = {}
        if self.config_file.exists():
            try:
                with open(self.config_file, "r") as f:
                    config = json.load(f)
            except Exception:
                pass
        
        # 更新配置，使用环境变量名称作为键名前缀
        config.update({
            f"encrypted_{env_name}": encrypted_key,
            f"{env_name}_encryption_key": encryption_key.decode()
        })
        
        with open(self.config_file, "w") as f:
            json.dump(config, f)
    
    def load_custom_api_key(self, env_name):
        """从配置文件加载自定义API密钥"""
        if not self.config_file.exists():
            return None
        
        try:
            with open(self.config_file, "r") as f:
                config = json.load(f)
            
            encrypted_key_name = f"encrypted_{env_name}"
            encryption_key_name = f"{env_name}_encryption_key"
            
            if encrypted_key_name not in config or encryption_key_name not in config:
                return None
                
            encrypted_key = config[encrypted_key_name]
            encryption_key = config[encryption_key_name].encode()
            
            return self.decrypt_api_key(encrypted_key, encryption_key)
        except Exception as e:
            print(f"加载{env_name}密钥时出错: {e}")
            return None
    
    def setup_api_key(self, env_names=None):
        """设置API密钥并配置环境变量
        
        Args:
            env_names: 要加载的环境变量名称列表，如果为None则提示用户输入
        """
        if env_names is None:
            # 如果没有指定环境变量，提示用户输入
            env_names = []
            while True:
                env_name = input("请输入环境变量名称（直接回车结束）: ").strip()
                if not env_name:
                    break
                env_names.append(env_name)
        
        # 处理所有指定的环境变量
        for env_var in env_names:
            # 尝试从配置文件加载API密钥
            api_key = self.load_custom_api_key(env_var)
            
            # 如果没有保存的密钥，则请求用户输入
            if not api_key:
                api_key = getpass.getpass(f"请输入您的{env_var}密钥: ")
                if api_key:
                    save_choice = input(f"是否保存{env_var}密钥以便下次使用? (y/n): ").lower()
                    if save_choice == 'y':
                        self.save_custom_api_key(env_var, api_key)
                        print(f"{env_var}密钥已加密保存")
            
            # 设置环境变量
            if api_key:
                os.environ[env_var] = api_key
        
        return True 