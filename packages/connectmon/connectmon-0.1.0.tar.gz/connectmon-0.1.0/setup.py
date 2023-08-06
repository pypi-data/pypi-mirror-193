# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['connectmon']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.5,<2.0.0',
 'pymsteams>=0.2.2,<0.3.0',
 'python-dotenv>=0.21.1,<0.22.0',
 'pyyaml>=6.0,<7.0',
 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'connectmon',
    'version': '0.1.0',
    'description': 'A tool for monitoring tasks and connectors in Kafka Connect.',
    'long_description': '# ConnectMon\n\nA tool for monitoring tasks and connectors in Kafka Connect. \n\n## Installation\n\nWith pip\n```\npip install connectmon\n```\n\nWith poetry\n```\npoetry add connectmon\n```\n\n## Usage\n\n```py\nfrom connectmon.config import settings\nfrom connectmon.api import API\n\nfrom pprint import pprint\n\n## Setup your API you can get your environment variables from connectmon.config.settings\nconnect = API(settings.CONNECT_URL)\n\nif not connect.is_reachable():\n    raise Exception("Cluster is not reachable")\n\n## Get a list of connectors and their status\nconnectors = connect.get_all_connector_status()\n\n## Restart any failed or paused connectors and collect messages along the way\nerrors_and_warning = connect.restart_failed_connectors_if_any(connectors)\n\n## If any channels have been registered in the configuration supplied through CONFIG_PATH \n## And there were any connectors or tasks to reset\n## Then process each channel\nif settings.CHANNELS and len(errors_and_warnings) > 0:\n    for channel in settings.CHANNELS.channels:\n        \n        if channel.type == "teams":\n            print(f"Sending message to {channel.name}...")\n            teams_msg = build_teams_message(channel.url, errors_and_warnings)\n            teams_msg.send()\n\n```\n\n## Configuration\n| Name | Type | Description |\n|------|------|-------------|\n| CONNECT_URL | string | The URL of the Connect cluster |\n| ENVIRONMENT | string | The environment the application is running in |\n| LOG_LEVEL | string | The log level for the application |\n| LOG_FORMAT | string | The log format for the application |\n| CONFIG_PATH | Optional string | The path to the configuration file |\n\nIf `CONFIG_PATH` is provided, the application will attempt to load\nconfiguration from the file, which will set `settings.CHANNELS` with the\nchannels configured in the supplied configuration file.\n\nA config file could look like this\n```yaml\nchannels:\n  - name: my-teams-team-name\n    type: teams\n    url: https://my-org.webhook.office.com/webhookb2/...\n    include:\n        - i-want-to-monitor-this-connector\n        - this-too\n    exclude:\n        - who-cares-about-this-connector\n        - this-is-someone-elses-problem\n```\n\n> Current only Microsoft Teams is supported. More will come if requested.',
    'author': 'Jens Peder Meldgaard',
    'author_email': 'jenspederm@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
