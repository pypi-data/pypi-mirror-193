# service-bootstrap

Helper for starting up a service in python

## Function `start_service()`

Usage:
```python
from bootstrap.bootstrap import start_service

config, logger, timezone = start_service()
```

### Configuration
`start_service()` will look for a config YAML file and load it into a dict,
using the following algorithm:

* if the env variable `CONFIG` is defined, it will be used to determine the location of the config file
* otherwise a file `./config.yaml` is expected to be present

The file will be parsed and returned as a first returned variable

### Logging

`start_service()` will configure the logger will in the following way:
1. if `./logging.yaml` exists, it will be loaded into a dict and used to configure logging (using [dictConfig](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig))
2. otherwise the default logging format will be applied, which is defined as writing logs on INFO level to stdout

Additionally, `start_service()` will look for `./loglevels.yaml` file with the following structure:
```yaml
'apscheduler.scheduler': 'ERROR',
'apscheduler.executors.default': 'WARN'
```
and use this file to configure per-logger log levels. Note that the settings two mentioned above
(`'apscheduler.scheduler': 'ERROR'` and `'apscheduler.executors.default': 'WARN'`) will be used as a 
default.

Finally, `start_service()` will create a logger called `main`, log two messages
```python
logger.info("Starting application!")
logger.info("Your timezone is %s" % timezone)
```
and return this logger as a second returned variable

### Timezone

The third returned variable will contain the local timezone as a string (f.ex `Europe/Warsaw`), detected using
the following algorithm:

 * if the env variable `TIMEZONE` is defined, it will be used
 * otherwise timezone will be autodetected using [tzlocal](https://pypi.org/project/tzlocal/)

### Note on YAML loading

All yaml files are loaded using `load_yaml()` and may contain env variables!

## Function `load_yaml()`
Usage:
```python
from bootstrap.utils import load_yaml

content = load_yaml("file.yaml")
```
It will load the content of `file.yaml` into a dict resolving ENV variables