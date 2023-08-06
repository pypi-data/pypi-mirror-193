# coding: utf-8
# author: shiqiangliang


from setuptools import setup, find_packages

setup(
    name="django-pooldb",
    version="1.1",
    description='基于DBUtils.PooledDB封装的Django数据库连接引擎',
    long_description="file: README.md",
    author="shiqiangliang",
    author_email="lsq54264@vip.qq.com",
    url='https://github.com/liangalien/django-pooldb',
    packages=find_packages(),
    install_requires=['django==3.2.18', 'DBUtils', 'pymysql', 'psycopg2'],
    python_requires=">=3.6,<3.11",
    keywords=['django db pool', 'django mysql pool', 'django postgres pool'],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
