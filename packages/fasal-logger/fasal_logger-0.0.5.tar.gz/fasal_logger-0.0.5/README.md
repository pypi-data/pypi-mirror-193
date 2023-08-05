
### Installation
Install the package [fasal-logger](https://pypi.org/project/fasal-logger/) using the following command
```bash
pip install --upgrade fasal-logger
```

--------------
### Configuration
- Create a file `logger.yml`. Copy the contents from the repository and make the necessary changes (If needed)
```yaml
version: 1
disable_existing_loggers: no
formatters:
  simple:
    format: "%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s"
    datefmt: '%Y-%m-%d %H:%M:%S'
  fasalFormat:
    (): fasal_logger.FasalStdlibFormatter
    datefmt: '%Y-%m-%d %H:%M:%S'
    extra: {"author": "${USER}"}
    exclude_fields: [ecs, log.original]

handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: fasalFormat
    stream: ext://sys.stdout
  file:
    class : logging.handlers.RotatingFileHandler
    level: DEBUG
    formatter: fasalFormat
    filename: 'logging.example.log'
    mode: a
    maxBytes: 1000000  # 1 MB
    backupCount: 2
    encoding: utf8

root:
  level: DEBUG
  handlers: [console]
  propogate: no

loggers:
  fasalLogger:
    level: DEBUG
    handlers: [console]
    propagate: no
```

- The `logger.yml` defined here defaults to console. In order to log the contents into a file, make the required changes to the `logger.yml`.
``` yaml
root:
  handlers: [console, file]

loggers:
  fasalLogger:
    handlers: [console, file]

```

And change the filename and location.
```yaml
handler:
    file:
        filename: 'logging.example.log'
```

### Usage
In order to use the logger in your code, add the following piece of code at the top of your .py file

**Note:** `Get the webhook from the infra team to able to send messages to slack to any other channel. (By default using #fasal-ai-infra)`

```python
import logging
import logging.config
import os
from fasal_logger import LoggerInitializer, SlackNotification

logging.captureWarnings(True)
logger = logging.getLogger(__name__)
logger_init = LoggerInitializer()
logger_init(logger=logger, config='path_to_logger.yml')
slk = SlackNotification() # set parameter for webhook, DEV (if needed)

# Use logger now
logger.info("Logger set")

# Send a message to slack channel
slk.notify(message="testing")

```
----------

### Variables taken from environment are:
Set these variables as required in the file used to read environment variable.

*Note: You can keep env variables in an yaml file `local.yml` and use [python-dotenv-yaml](https://pypi.org/project/python-dotenv-yaml/) library to read it*

  - `SLACK_WEBHOOK`: Channel webhook trigger, defaults to slack channel #fasal-ai-infra
  - `DEV`: If True, no message is send to slack
  - `ENV`: logger environment (staging/production/development)

------------
### Another example usage:
```python
import logging
import logging.config
import os

from functools import reduce
from fasal_logger import LoggerInitializer, SlackNotification

logging.captureWarnings(True)
logger = logging.getLogger(__name__)
logger_init = LoggerInitializer()
logger_init(logger=logger, config='logger.yml')
slk = SlackNotification(DEV=True)
high_level_stuff = {'custom_tag': 'tagged-at-line'}


logger.info("Starting the function", extra={'tag': 'xxx'})
def my_sum(a,b):
    if isinstance(a, str):
        logger.warning("This is not int")
    logger.info(f'performing addition of {a}, {b}')
    try:
        result = a+b
        logger.info(f'result: {result}')
    except Exception as err:
        logger.error(err)
        raise err
    return result

def run_request():
    import requests
    logger.info("request")
    ploads = {'things':2,'total':25}
    r = requests.get('https://httpbin.org/get',params=ploads)


param = [1,2,3]
result = reduce(my_sum, param)
logger.info(f"final: {result}", extra=high_level_stuff)
run_request()
slk.notify(message="this is test")
```
**Note:**
1. Use logger.info() with first argument as string
2. In order to pass another set of key: value pairs to logger.info / logger.warnings / logger.debug
  - Pass the key: value pair to logger.yaml
  ```yaml
  formatters:
  fasalFormat:
    (): fasal_logger.FasalStdlibFormatter
    datefmt: '%Y-%m-%d %H:%M:%S'
    extra: {"author": "${USER}", "key-1": "value-1", "key-2": "value-2"}
  ```
  - Pass a dictionary to argument `extra` inside logger.info(). However, doing so will only effect the logger's log where its added and adding in `logger.yaml` will effect it globally
  ```python
  logger.info("my message", extra = {'key-1': 'value-1'})
  ```

-----------
Build and Published using (`poetry`)[https://python-poetry.org/docs/cli/#publish]