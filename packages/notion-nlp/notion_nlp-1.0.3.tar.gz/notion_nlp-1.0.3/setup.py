# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['notion_nlp', 'notion_nlp.core', 'notion_nlp.parameter']

package_data = \
{'': ['*']}

install_requires = \
['arrow==1.2.3',
 'jieba==0.42.1',
 'pandas==1.5.3',
 'pydantic==1.10.5',
 'pyfunctional==1.4.3',
 'requests==2.28.2',
 'ruamel-yaml==0.17.21',
 'scikit-learn==1.2.1',
 'tabulate==0.9.0',
 'tqdm==4.64.1',
 'typer==0.7.0',
 'wcwidth==0.2.6']

setup_kwargs = {
    'name': 'notion-nlp',
    'version': '1.0.3',
    'description': 'Reading rich text information from a Notion database and performing simple NLP analysis.',
    'long_description': '<p align="center">\n  <img width="100px" src="https://img.icons8.com/ios/250/FFFFFF/share-2.png" align="center" alt="Notion Rich Text Data Analysis" />\n  <h1 align="center">\n    Notion NLP\n  </h1>\n  <p align="center">\n    To read text from a Notion database and perform natural language processing analysis.\n  </p>\n</p>\n\n  <p align="center">\n    <a href="https://github.com/dario-github/notion-nlp/actions">\n      <img alt="Tests Passing" src="https://github.com/dario-github/notion-nlp/actions/workflows/main.yml/badge.svg" />\n    </a>\n    <a href="https://codecov.io/gh/dario-github/notion-nlp">\n      <img alt="codecov" src="https://codecov.io/gh/dario-github/notion-nlp/branch/main/graph/badge.svg?token=ehzYhousD3" />\n    </a>\n    <a href="https://github.com/dario-github/notion-nlp/graphs/contributors">\n      <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/dario-github/notion-nlp" />\n    </a>\n    <a href="https://github.com/dario-github/notion-nlp">\n      <img alt="visitors" src="https://visitor-badge.glitch.me/badge?page_id=dario-github.notion_nlp&left_color=gray&right_color=green" />\n    </a>\n  </p>\n  \n  <p align="center">\n    <a href="README.md">English</a>\n    /\n    <a href="README.zh.md">简体中文</a>\n  </p>\n\n## Introduction\n\nWhen flomo first came out, a database was built in notion to implement similar functionality. It has been a few years since I recorded my thoughts and summaries, and I have accumulated some corpus. flomo\'s roaming function is not very suitable for my needs, so I wanted to write my own small tool to access the notion API and do NLP analysis.\n\nLast year I wrote a demo using a notebook, but I put it on hold for a while and then improved it. Currently, it supports batch analysis tasks, you can add multiple databases and properties in the configuration file to filter the sorting criteria, and then output the keywords and the corresponding statement paragraph markdown by TF-IDF.\n\nFor example, I have added the following task myself.\n\n- Reflections from the last year\n- Summary optimisation for the year\n- Self-caution for all periods\n- List for the week\n\n## Pipline\n\n<div style="text-align:center;">\n\n```mermaid\nflowchart TB\n\nA[(Notion Database)] --> B([read rich text via API]) --> C([split word / cleaning / word-phrase mapping]) --> D[/calculate TF-IDF/] --> E[[Output the top-n keywords and their corresponding sentences in markdown format]]\n```\n\n</div>\n\n## Installation\n\n```shell\npython3.8 -m pip install notion-nlp\n```\n\n## Quick use\n\nConfiguration file reference ``configs/config.sample.yaml`` (hereinafter config, please rename to ``config.yaml`` as your own configuration file)\n\n### Get the integration token\n\nIn [notion integrations](https://www.notion.so/my-integrations/) create a new integration, get your own token and fill in the token in the config.yaml file afterwards.\n\n> [graphic tutorial in tango website](https://app.tango.us/app/workflow/6e53c348-79b6-4ed3-8c75-46f5ddb996da?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links) / [graphic tutorial in markdown format](./docs/tango/get_the_integration_token.md)\n\n### Add integration to database/get database ID\n\nIf you open the notion database page in your browser or click on the share copy link, you will see the database id in the address link (similar to a string of jumbles) and fill in the database_id under the task of config.\n\n> [graphic tutorial in tango website](https://app.tango.us/app/workflow/7e95c7df-af73-4748-9bf7-11efc8e24f2a?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links) / [graphic tutorial in markdown format](./docs/tango/add_integration_to_database.md)\n\n### Configure the filter sort database entry extra parameter\n\nThe task\'s extra is used to filter and sort the database, see [notion filter API](https://developers.notion.com/reference/post-database-query-filter#property-filter-object) for format and content, the [config.sample.yaml](./configs/config.sample.yaml) file already provides 2 configurations.\n\n### Run all tasks\n\n```shell\npython3.8 -m notion-nlp run-all-task --config-file ${Your Config file Path}\n```\n\n## Development\n\nWelcome to fork and add new features/fix bugs.\n\n- After cloning the project, use the `create_python_env_in_new_machine.sh` script to create a Poetry virtual environment.\n\n- After completing the code development, use the invoke command to perform a series of formatting tasks, including black/isort tasks added in task.py.\n  \n    ```shell\n    invoke check\n    ```\n\n- After submitting the formatted changes, run unit tests to check coverage.\n\n    ```shell\n    poetry run tox\n\n    ```\n\n## Note\n\n- The word segmentation tool has two built-in options: jieba/pkuseg. (Considering adding language analysis to automatically select the most suitable word segmentation tool for that language.)\n\n  - jieba is used by default.\n  - pkuseg cannot be installed with poetry and needs to be installed manually with pip. In addition, this library is slow and requires high memory usage. It has been tested that a VPS with less than 1G memory needs to load virtual memory to use it.\n\n- The analysis method using tf-idf is too simple. Consider integrating the API of LLM (such as chatGPT) for further analysis.\n\n## Contributions\n\n- scikit-learn - [https://github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)\n\n## License and Copyright\n\n- [MIT License](./LICENSE)\n  - The MIT License is a permissive open-source software license. This means that anyone is free to use, copy, modify, and distribute your software, as long as they include the original copyright notice and license in their derivative works.\n\n  - However, the MIT License comes with no warranty or liability, meaning that you cannot be held liable for any damages or losses arising from the use or distribution of your software.\n\n  - By using this software, you agree to the terms and conditions of the MIT License.\n\n## Contact information\n\n- See more at my [HomePage](https://github.com/dario-github)\n',
    'author': 'Dario Zhang',
    'author_email': 'zdclink@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.10,<3.9.0',
}


setup(**setup_kwargs)
