# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shoal']

package_data = \
{'': ['*']}

install_requires = \
['beartype>=0.12.0', 'invoke>=2.0.0', 'pydantic>=1.10.4', 'rich>=12.6.0']

setup_kwargs = {
    'name': 'shoal',
    'version': '1.0.0rc0',
    'description': 'Opinionated CLI Task Runner built on Invoke',
    'long_description': '# shoal\n\nOpinionated CLI Task Runner built on Invoke\n\n## Installation\n\n1. `poetry add `\n\n1. ...\n\n    ```sh\n    import\n\n    # < TODO: Add example code here >\n    ```\n\n1. ...\n\n## Usage\n\n<!-- < TODO: Show an example (screenshots, terminal recording, etc.) > -->\n\nFor more example code, see the [scripts] directory or the [tests].\n\n## Project Status\n\nSee the `Open Issues` and/or the [CODE_TAG_SUMMARY]. For release history, see the [CHANGELOG].\n\n## Contributing\n\nWe welcome pull requests! For your pull request to be accepted smoothly, we suggest that you first open a GitHub issue to discuss your idea. For resources on getting started with the code base, see the below documentation:\n\n- [DEVELOPER_GUIDE]\n- [STYLE_GUIDE]\n\n## Code of Conduct\n\nWe follow the [Contributor Covenant Code of Conduct][contributor-covenant].\n\n### Open Source Status\n\nWe try to reasonably meet most aspects of the "OpenSSF scorecard" from [Open Source Insights](https://deps.dev/pypi/shoal)\n\n## Responsible Disclosure\n\nIf you have any security issue to report, please contact the project maintainers privately. You can reach us at [dev.act.kyle@gmail.com](mailto:dev.act.kyle@gmail.com).\n\n## License\n\n[LICENSE]\n\n[changelog]: ./docs/CHANGELOG.md\n[code_tag_summary]: ./docs/CODE_TAG_SUMMARY.md\n[contributor-covenant]: https://www.contributor-covenant.org\n[developer_guide]: ./docs/DEVELOPER_GUIDE.md\n[license]: https://github.com/kyleking/shoal/LICENSE\n[scripts]: https://github.com/kyleking/shoal/scripts\n[style_guide]: ./docs/STYLE_GUIDE.md\n[tests]: https://github.com/kyleking/shoal/tests\n',
    'author': 'Kyle King',
    'author_email': 'dev.act.kyle@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyleking/shoal',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.12,<4.0.0',
}


setup(**setup_kwargs)
