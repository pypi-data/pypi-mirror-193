# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rtorch']

package_data = \
{'': ['*']}

install_requires = \
['numpy']

setup_kwargs = {
    'name': 'rtorch',
    'version': '0.0.3',
    'description': '',
    'long_description': '# realtorch\n\n一个精简版的 Pytorch+cuda 框架\n\n## 安装\n\n```bash\npip install realtorch\n```\n\n## 使用\n\n和 Pytorch 的API完全相同, 如果您已有一个Pytorch版本的代码,您可以简单的通过 `import rtorch as torch` 来替换\n\n## 开发文档\n\nhttps://luzhixing12345.github.io/realtorch/\n\n## 参考\n\n- [Pytorch](https://github.com/pytorch/pytorch)\n\n',
    'author': 'luzhixing12345',
    'author_email': 'luzhixing12345@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
