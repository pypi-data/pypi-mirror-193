# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['neptune_compatibility_package']

package_data = \
{'': ['*']}

install_requires = \
['neptune']

setup_kwargs = {
    'name': 'neptune-client',
    'version': '1.0.0',
    'description': 'Neptune Client',
    'long_description': '<div align="center">\n    <img src="https://raw.githubusercontent.com/neptune-ai/neptune-client/assets/readme/github-banner.jpeg" width="1500" />\n    &nbsp;\n <h1>neptune.ai</h1>\n</div>\n\n<div align="center">\n  <a href="https://docs.neptune.ai/usage/quickstart/">Quickstart</a>\n  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>\n  <a href="https://neptune.ai/">Website</a>\n  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>\n  <a href="https://docs.neptune.ai/">Docs</a>\n  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>\n  <a href="https://github.com/neptune-ai/examples">Examples</a>\n  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>\n  <a href="https://neptune.ai/resources">Resource center</a>\n  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>\n  <a href="https://neptune.ai/blog">Blog</a>\n  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>\n  <a href="https://neptune.ai/events">Podcast</a>\n&nbsp;\n  <hr />\n</div>\n\n## ⚠️ This package has been renamed to [`neptune`](https://pypi.org/project/neptune)\n\nWith the `1.0` release of the Neptune client library, we changed the package name from `neptune-client` to `neptune`.\n\nTo upgrade your Neptune client from `0.x` to `1.x`:\n\n```\npip uninstall neptune-client\n```\n\n```\npip install neptune\n```\n\nThe neptune `1.0.0` release comes with numerous updates, notably:\n\n- The `neptune.new` package is now just `neptune`.\n- We tweaked the monitoring of system metrics and hardware consumption:\n    - Better support for multi-process jobs.\n    - Disabled by default if you start Neptune in an interactive session.\n- Initialization and project management functions take keyword arguments instead of positional ones.\n- Run states are changed to `"inactive"` and `"active"` instead of `"idle"` and `"running"`.\n- If you attempt to log unsupported types, they\'re no longer implicitly cast to `string`. We offer utilities and workarounds for types that are not yet directly supported.\n\nFor the full list of changes, see the [neptune 1.0.0 upgrade guide](https://docs.neptune.ai/setup/neptune-client_1-0_release_changes).\n',
    'author': 'neptune.ai',
    'author_email': 'contact@neptune.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://neptune.ai/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
