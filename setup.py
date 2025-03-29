from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="env-key-manager",
    version="0.1.0",
    author="ROOKIE-AI",
    author_email="support@rookie-ai.com",
    description="A secure environment variable key manager with encryption support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ROOKIE-AI/env-key-manager",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "cryptography>=3.4.7",
    ],
    entry_points={
        "console_scripts": [
            "env-key-manager=env_key_manager.cli:main",
        ],
    },
) 