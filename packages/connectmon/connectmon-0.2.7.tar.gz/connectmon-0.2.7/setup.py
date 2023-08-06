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
    'version': '0.2.7',
    'description': 'A tool for monitoring tasks and connectors in Kafka Connect.',
    'long_description': '# ConnectMon\n\nA tool for monitoring tasks and connectors in Kafka Connect. \n\n## Installation\n\nWith pip\n```\npip install connectmon\n```\n\nWith poetry\n```\npoetry add connectmon\n```\n\n## Usage\n\n```py\nfrom connectmon import env, API\nfrom connectmon.messaging import TeamsService\n\n\n## Setup Kafka Connect Rest API client and check if cluster is reachable\nconnect = API(env.CONNECT_URL)\n\n## Get all connectors and check if any are in a failed state\nconnectors = connect.get_all_connectors()\n\n## Loop through all channels and send messages\nfor channel in env.CHANNELS.channels:\n    if channel.type == "teams":\n        service = TeamsService(connect, channel)\n        service.process_channel_connectors(connectors)\n        service.send_message()\n```\n\n## Configuration\n\nBase configuration for ConnectMon is handled through Environment Variables. \n\n### Environment Variables\n\n| Name | Type | Description | Default |\n|------|------|-------------| ------- | \n| **CONFIG_PATH** | Optional string | The path to the channel configuration file | `""` |\n| **CONNECT_URL** | string | The URL of the Connect cluster | `"http://localhost:8083"` |\n| SKIP_TLS_VERIFY | boolean | Whether to skip TLS verification | `False` |\n| ENVIRONMENT | string | The environment the application is running in | `"dev"` |\n| LOG_LEVEL | string | The log level for the application | `"INFO"` |\n| LOG_FORMAT | string | The log format for the application | `"(asctime)s - ..."` |\n\n> *Name in bold are required!*\n\nIf `CONFIG_PATH` is provided, the application will attempt to load\nconfiguration from the file, which will set `settings.CHANNELS` with the\nchannels configured in the supplied configuration file.\n\n### Channel Configuration\n\nYou can configure specific channels to receive notifications when connectors or tasks are paused or failed.\n\nA config file could look like this\n\n```yaml\nchannels:\n  - name: my-teams-team-name\n    type: teams\n    url: https://my-org.webhook.office.com/webhookb2/...\n    actions:\n      - RESTART_FAILED\n    include:\n      - i-want-to-monitor-this-connector\n      - this-too\n    exclude:\n      - who-cares-about-this-connector\n      - this-is-someone-elses-problem\n```\n\nSupported fields for channels are:\n\n| Name | Type | Description | Default |\n| ---- | ---- | ----------- | ------- |\n| **name** | string | Name of the channel | `""` |\n| **type** | string | Type of channel | `""` |\n| **url**  | string | Url to send payload to | `""` |\n| actions | list of strings | Can be any of `RESTART_FAILED`, `RESTART_FAILED_CONNECTORS`, `RESTART_FAILED_TASKS`, `RESUME_PAUSED_CONNECTORS` | `RESTART_FAILED` |\n| include | list of strings | Names of connectors to include for this channel | `["*"]` |\n| exclude | list of strings | Names of connectors to *exclude* for this channel | `[]` |\n\n> Current only Microsoft Teams or `type: "teams"` is supported.',
    'author': 'Jens Peder Meldgaard',
    'author_email': 'jenspederm@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JenspederM/ConnectMon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
