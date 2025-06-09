from setuptools import setup, find_packages

setup(
    name="personalWeb",  # 包名
    version="1.0.0",           # 版本号
    packages=find_packages(),  # 自动查找项目中的包
    install_requires=[         # 依赖（与 requirements.txt 一致）
        'Flask>=3.0.3',
        'gunicorn>=23.0.0',          # 部署用的 WSGI 服务器
        'uvicorn>=0.34.2',           # 如果用了 FastAPI 就需要它
        'lxml>=5.2.1',               # 如果处理 XML
        'PyMySQL>=1.1.1',            # 用于连接 MySQL
        'mysql-connector-python>=9.3.0',  # 也可能是连接 MySQL 的，但一般用不上两个
        'mysqlclient>=2.2.7',        # 这个更底层更高效（C 扩展），不推荐和 PyMySQL 一起用
        'matplotlib>=3.9.2',         # 如果项目里有图表绘制
        'jsonpointer>=2.1',          # 处理 JSON pointer 的
        'protobuf>=4.25.3',          # 如果有 Protocol Buffers 使用
        'psycopg>=3.2.6',            # 如果你还用到了 PostgreSQL（可选）


    ],
    author="duasong",
    author_email="2272168170@qq.com",
    description="A Flask project",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your_project",  # 项目主页（可选）
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>= 3.12.7',  # 指定 Python 版本
    entry_points={
        'console_scripts': [
            'run-your-project=your_package.app:main',  # 可执行脚本（可选）
        ],
    },
)