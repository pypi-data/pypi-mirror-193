# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_heweather']

package_data = \
{'': ['*'],
 'nonebot_plugin_heweather': ['templates/*',
                              'templates/css/*',
                              'templates/css/fonts/*']}

install_requires = \
['httpx>=0.18.0,<1.0.0',
 'nonebot-adapter-onebot>=2.0.0-beta.1',
 'nonebot-plugin-htmlrender>=0.0.4.3',
 'nonebot2[fastapi]>=2.0.0rc1',
 'pydantic>=1.5.0']

setup_kwargs = {
    'name': 'nonebot-plugin-heweather',
    'version': '0.6.2',
    'description': 'Get Heweather information and convert to pictures',
    'long_description': '# nonebot-plugin-heweather\n\n获取和风天气信息并转换为图片\n\n# 使用html+playwright来渲染好看的！\n\n- 使用了~~自产自销的~~[nonebot-plugin-htmlrender](https://github.com/kexue-z/nonebot-plugin-htmlrender)\n- **需要先保证playwright可以正常运行并在系统（或容器中）存在中文字体**\n\n\n# 安装\n\n直接使用 `pip install nonebot-plugin-heweather` 进行安装\n\n在 `bot.py` 中 写入 `nonebot.load_plugin("nonebot_plugin_heweather")`\n\n# 指令\n\n`天气+地区` 或 `地区+天气`  \n例如：`上海天气` 或 `天气广州`\n\n# 配置\n\n## apikey 必须配置 环境配置\n\n```\nQWEATHER_APIKEY = xxx\n```\n\n## api类型 必须配置 环境配置\n\n0 = 普通版(3天天气预报)\n1 = 个人开发版(7天天气预报)\n2 = 商业版 (7天天气预报)\n\n\n```\nQWEATHER_APITYPE = 0\n```\n\n## APIKEY获取方式\n\n**1、注册和风天气账号**  \n进入官网注册[https://id.qweather.com/#/login](https://id.qweather.com/#/login)  \n**2、进入控制台**  \n登录后，点击 “和风天气开发者控制台”  \n**3、创建项目**  \n点击控制台左侧 “项目管理”，然后点击 “创建项目”，根据提示自行填写  \n“选择订阅” -> “免费订阅”，“设置KEY” -> “Web API”，都填好后“创建”  \n**4、获取key并配置.env.xx**  \n返回 “项目管理”，可以看到创建的项目，点击KEY下面的 “查看”，复制KEY到你的.env.xx即可。  \n \n\n',
    'author': 'kexue',
    'author_email': 'x@kexue.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0.0',
}


setup(**setup_kwargs)
