# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nonebot_plugin_sqlalchemy']

package_data = \
{'': ['*']}

install_requires = \
['nonebot2>=2.0.0-rc.2,<3.0.0', 'sqlalchemy[asyncio]>=1.4.41,<2.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-sqlalchemy',
    'version': '0.1.7',
    'description': '',
    'long_description': '<!-- markdownlint-disable MD033 MD036 MD041 -->\n\n<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\nnonebot-plugin-sqlalchemy\n============\n\n_✨ NoneBot SQLAlchemy 封装插件 ✨_\n\n</div>\n\n<p align="center">\n  <a href="https://raw.githubusercontent.com/ssttkkl/nonebot-plugin-sqlalchemy/master/LICENSE">\n    <img src="https://img.shields.io/github/license/ssttkkl/nonebot-plugin-sqlalchemy.svg" alt="license">\n  </a>\n  <a href="https://pypi.python.org/pypi/nonebot-plugin-sqlalchemy">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-sqlalchemy.svg" alt="pypi">\n  </a>\n  <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">\n</p>\n\n## Get Started\n\n### 1、定义data_source\n\n```python\nfrom nonebot import get_driver, require\n\n# 注意必须先require再import\nrequire("nonebot_plugin_sqlalchemy")\nfrom nonebot_plugin_sqlalchemy import DataSource\n\n# 必须使用支持asyncio的驱动器\ndb_conn_url = "postgresql+asyncpg://username:password@localhost:5432/database"\ndata_source = DataSource(get_driver(), db_conn_url)\n```\n\n### 2、定义映射\n```python\nfrom sqlalchemy import Column, String, Integer\n\n@data_source.registry.mapped\nclass UserOrm:\n    __tablename__ = \'users\'\n\n    id: int = Column(Integer, primary_key=True, autoincrement=True)\n    username: str = Column(String)\n    password: str = Column(String)\n    nickname: str = Column(String)\n```\n\n### 3、在Matcher中使用\n\n```python\nfrom nonebot import on_command\nfrom nonebot.adapters.onebot.v11 import MessageEvent\nfrom nonebot.internal.matcher import Matcher\nfrom sqlalchemy import select\n\nlogin_matcher = on_command("login")\n\n\n@login_matcher.handle()\nasync def handler(event: MessageEvent, matcher: Matcher):\n    username, password = event.get_plaintext().split(" ")\n\n    session = data_source.session()\n    \n    stmt = select(UserOrm).where(UserOrm.username == username, UserOrm.password == password)\n    result = await session.execute(stmt)\n    user = result.scalar_one_or_none()\n\n    if user is not None:\n        await matcher.send(f"Hello, {user.nickname}")\n```\n\n通过`data_source.session()`获取AsyncSession对象，此处获取的session实际上是async_scoped_session。\n\n在Matcher的一次执行过程中，多次调用`data_source.session()`获得的是同一个session，并且会在Matcher执行完毕后自动关闭。也就是说我们可以像下面这样使用：\n\n```python\nfrom nonebot import on_command\nfrom nonebot.adapters.onebot.v11 import MessageEvent\nfrom nonebot.internal.matcher import Matcher\nfrom sqlalchemy import select\nfrom typing import Optional\n\nasync def login(username: str, password: str) -> Optional[User]:\n    session = data_source.session()\n    \n    stmt = select(UserOrm).where(UserOrm.username == username, UserOrm.password == password)\n    result = await session.execute(stmt)\n    user = result.scalar_one_or_none()\n\n    return user\n\n\nlogin_matcher = on_command("login")\n\n\n@login_matcher.handle()\nasync def handler(event: MessageEvent, matcher: Matcher):\n    username, password = event.get_plaintext().split(" ")\n    user = await login(username, password)\n    if user is not None:\n        await matcher.send(f"Hello, {user.nickname}")\n```\n\n参考：https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#using-asyncio-scoped-session\n\n注意：务必保证一次Matcher执行过程不会在不同的Task中调用`data_source.session()`获取session（即不要使用`create_task()`或`ensure_future()`创建Task），否则可能出现错误。若有这样的需求，请参考下文的方法手动创建并管理session。\n\n\n### 4、在Matcher之外使用\n\n在Matcher之外（如on_bot_connect等钩子函数中，或者是APScheduler的定时任务中）则必须通过`AsyncSession(data_source.engine)`创建session。\n\n```python\nasync def do_something():\n    async with AsyncSession(data_source.engine) as session:\n        # ...\n```\n',
    'author': 'ssttkkl',
    'author_email': 'huang.wen.long@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ssttkkl/nonebot-plugin-sqlalchemy',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
