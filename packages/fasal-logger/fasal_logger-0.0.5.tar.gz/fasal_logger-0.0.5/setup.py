# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fasal_logger']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML==6.0', 'ecs-logging==2.0.0', 'slack-sdk==3.18.1']

setup_kwargs = {
    'name': 'fasal-logger',
    'version': '0.0.5',
    'description': 'json based python logger with support for slack notification',
    'long_description': '\n### Installation\nInstall the package [fasal-logger](https://pypi.org/project/fasal-logger/) using the following command\n```bash\npip install --upgrade fasal-logger\n```\n\n--------------\n### Configuration\n- Create a file `logger.yml`. Copy the contents from the repository and make the necessary changes (If needed)\n```yaml\nversion: 1\ndisable_existing_loggers: no\nformatters:\n  simple:\n    format: "%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s"\n    datefmt: \'%Y-%m-%d %H:%M:%S\'\n  fasalFormat:\n    (): fasal_logger.FasalStdlibFormatter\n    datefmt: \'%Y-%m-%d %H:%M:%S\'\n    extra: {"author": "${USER}"}\n    exclude_fields: [ecs, log.original]\n\nhandlers:\n  console:\n    class: logging.StreamHandler\n    level: DEBUG\n    formatter: fasalFormat\n    stream: ext://sys.stdout\n  file:\n    class : logging.handlers.RotatingFileHandler\n    level: DEBUG\n    formatter: fasalFormat\n    filename: \'logging.example.log\'\n    mode: a\n    maxBytes: 1000000  # 1 MB\n    backupCount: 2\n    encoding: utf8\n\nroot:\n  level: DEBUG\n  handlers: [console]\n  propogate: no\n\nloggers:\n  fasalLogger:\n    level: DEBUG\n    handlers: [console]\n    propagate: no\n```\n\n- The `logger.yml` defined here defaults to console. In order to log the contents into a file, make the required changes to the `logger.yml`.\n``` yaml\nroot:\n  handlers: [console, file]\n\nloggers:\n  fasalLogger:\n    handlers: [console, file]\n\n```\n\nAnd change the filename and location.\n```yaml\nhandler:\n    file:\n        filename: \'logging.example.log\'\n```\n\n### Usage\nIn order to use the logger in your code, add the following piece of code at the top of your .py file\n\n**Note:** `Get the webhook from the infra team to able to send messages to slack to any other channel. (By default using #fasal-ai-infra)`\n\n```python\nimport logging\nimport logging.config\nimport os\nfrom fasal_logger import LoggerInitializer, SlackNotification\n\nlogging.captureWarnings(True)\nlogger = logging.getLogger(__name__)\nlogger_init = LoggerInitializer()\nlogger_init(logger=logger, config=\'path_to_logger.yml\')\nslk = SlackNotification() # set parameter for webhook, DEV (if needed)\n\n# Use logger now\nlogger.info("Logger set")\n\n# Send a message to slack channel\nslk.notify(message="testing")\n\n```\n----------\n\n### Variables taken from environment are:\nSet these variables as required in the file used to read environment variable.\n\n*Note: You can keep env variables in an yaml file `local.yml` and use [python-dotenv-yaml](https://pypi.org/project/python-dotenv-yaml/) library to read it*\n\n  - `SLACK_WEBHOOK`: Channel webhook trigger, defaults to slack channel #fasal-ai-infra\n  - `DEV`: If True, no message is send to slack\n  - `ENV`: logger environment (staging/production/development)\n\n------------\n### Another example usage:\n```python\nimport logging\nimport logging.config\nimport os\n\nfrom functools import reduce\nfrom fasal_logger import LoggerInitializer, SlackNotification\n\nlogging.captureWarnings(True)\nlogger = logging.getLogger(__name__)\nlogger_init = LoggerInitializer()\nlogger_init(logger=logger, config=\'logger.yml\')\nslk = SlackNotification(DEV=True)\nhigh_level_stuff = {\'custom_tag\': \'tagged-at-line\'}\n\n\nlogger.info("Starting the function", extra={\'tag\': \'xxx\'})\ndef my_sum(a,b):\n    if isinstance(a, str):\n        logger.warning("This is not int")\n    logger.info(f\'performing addition of {a}, {b}\')\n    try:\n        result = a+b\n        logger.info(f\'result: {result}\')\n    except Exception as err:\n        logger.error(err)\n        raise err\n    return result\n\ndef run_request():\n    import requests\n    logger.info("request")\n    ploads = {\'things\':2,\'total\':25}\n    r = requests.get(\'https://httpbin.org/get\',params=ploads)\n\n\nparam = [1,2,3]\nresult = reduce(my_sum, param)\nlogger.info(f"final: {result}", extra=high_level_stuff)\nrun_request()\nslk.notify(message="this is test")\n```\n**Note:**\n1. Use logger.info() with first argument as string\n2. In order to pass another set of key: value pairs to logger.info / logger.warnings / logger.debug\n  - Pass the key: value pair to logger.yaml\n  ```yaml\n  formatters:\n  fasalFormat:\n    (): fasal_logger.FasalStdlibFormatter\n    datefmt: \'%Y-%m-%d %H:%M:%S\'\n    extra: {"author": "${USER}", "key-1": "value-1", "key-2": "value-2"}\n  ```\n  - Pass a dictionary to argument `extra` inside logger.info(). However, doing so will only effect the logger\'s log where its added and adding in `logger.yaml` will effect it globally\n  ```python\n  logger.info("my message", extra = {\'key-1\': \'value-1\'})\n  ```\n\n-----------\nBuild and Published using (`poetry`)[https://python-poetry.org/docs/cli/#publish]',
    'author': 'Binay Pradhan',
    'author_email': 'binay.pradhan@wolkus.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
