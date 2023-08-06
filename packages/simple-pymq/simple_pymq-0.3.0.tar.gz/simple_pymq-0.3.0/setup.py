# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_pymq',
 'simple_pymq.broker',
 'simple_pymq.consumer',
 'simple_pymq.exceptions',
 'simple_pymq.pipeline',
 'simple_pymq.producer',
 'simple_pymq.utils']

package_data = \
{'': ['*']}

install_requires = \
['pytz', 'rich']

extras_require = \
{':extra == "all"': ['redis[redis]>=4.2'],
 ':extra == "all" or extra == "cron"': ['croniter[cron]'],
 ':extra == "all" or extra == "fs"': ['aiofiles[fs]']}

setup_kwargs = {
    'name': 'simple-pymq',
    'version': '0.3.0',
    'description': 'Simple python message queue framework is ready to serve.',
    'long_description': '# simple-pymq #\n\n[![dockhardman](https://circleci.com/gh/dockhardman/simple-pymq.svg?style=shield)](https://app.circleci.com/pipelines/github/dockhardman/simple-pymq)\n\nSimple python message queue framework is ready to serve.\n\n## Installation ##\n\n```bash\npip install simple-pymq\n```\n\n## Usage ##\n\nSimple message queue pipeline in memory:\n\n```python\nimport asyncio\nfrom simple_pymq import (\n    PrintConsumer,\n    QueueBroker,\n    SimpleMessageQueue,\n    TimeCounterProducer,\n)\n\n\nasync def main():\n    q = QueueBroker(maxsize=32)\n    p = TimeCounterProducer(\n        count_seconds=1.0, max_produce_count=3, put_value="Message here."\n    )\n    c = PrintConsumer(max_consume_count=3)\n    mq = SimpleMessageQueue()\n\n    await mq.run(broker=q, producers=p, consumers=c)\n    print("All tasks done!")\n\n\nasyncio.run(main())\n```\n',
    'author': 'Allen Chou',
    'author_email': 'f1470891079@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8.0,<3.11.0',
}


setup(**setup_kwargs)
