# Author:码思客-木森
# WeChart:musen9111

from setuptools import setup, find_packages

with open("readme.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name='musktest',
    version='1.0.1',
    author='MuSen',
    author_email='mskjy@qq.com',
    url='https://github.com/musen123/MuskTest',
    description="MuskTest 码思客教育出品的测试框架",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["Jinja2==3.0.3",
                      'PyYAML==5.3.1',
                      'requests==2.24.0',
                      'requests-toolbelt==0.9.1',
                      'PyMySQL==1.0.2',
                      'rsa==4.7.2',
                      'jsonpath==0.82',
                      'pyasn1==0.4.8',
                      'colorama==0.4.4',
                      'faker==8.11.0'],

    packages=find_packages(),
    package_data={
        "": ["*.html", "*.md", "*.py", '*.json', "*.yaml"],
    },
    # 指定python版本
    python_requires='>=3.6',

    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    # 安装时生成脚本命令行脚本文件
    entry_points={
        "console_scripts": [
            "mst = musktest.manage:main",
        ],
    }
)
