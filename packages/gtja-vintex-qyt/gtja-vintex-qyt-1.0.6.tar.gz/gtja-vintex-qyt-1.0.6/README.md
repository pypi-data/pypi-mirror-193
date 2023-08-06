# 国泰君安道合券源通 Python SDK

国泰君安道合券源通 Python SDK 为国泰君安道合注册用户提供通过使用 Python 访问国泰君安券源通券池券单查询的封装。

## 操作系统
Windows / Linux

## Python 版本
Python 3.7+

## 安装

用户可以通过在命令行执行命令，使用 `pip` 包管理工具进行安装
```shell
$ python -m pip install gtja-vintex-qyt
```

## 使用方法

在 Python 代码中引入国泰君安道合券源通 Python 库，使用国泰君安道合注册用户的用户名及密码初始化客户端后，结合阅读国泰君安券源通相关文档，调用接口进行券池券单的查询操作。

```python
from gtja_vintex_qyt import GtjaVintexQyt

# 使用国泰君安道合注册用户的用户名及密码初始化客户端
vintex_qyt_client = GtjaVintexQyt("vintex_username", "vintex_password")

# 调用 qc0020 接口进行券池券单查询，具体业务含义请查阅国泰君安券源通相关文档
result1 = vintex_qyt_client.qc0020(pooltype="1")

# 调用 qc0021 接口进行券汇总单查询，具体业务含义请查阅国泰君安券源通相关文档
result2 = vintex_qyt_client.qc0021()
```


