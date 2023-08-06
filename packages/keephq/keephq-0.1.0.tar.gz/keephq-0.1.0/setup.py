# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['keephq',
 'keephq.action',
 'keephq.alert',
 'keephq.alertmanager',
 'keephq.cli',
 'keephq.conditions',
 'keephq.contextmanager',
 'keephq.exceptions',
 'keephq.functions',
 'keephq.iohandler',
 'keephq.parser',
 'keephq.providers',
 'keephq.providers.base',
 'keephq.providers.cloudwatch_provider',
 'keephq.providers.console_provider',
 'keephq.providers.elastic_provider',
 'keephq.providers.http_provider',
 'keephq.providers.logfile_provider',
 'keephq.providers.mock_provider',
 'keephq.providers.models',
 'keephq.providers.mysql_provider',
 'keephq.providers.newrelic_provider',
 'keephq.providers.pagerduty_provider',
 'keephq.providers.pushover_provider',
 'keephq.providers.sentry_provider',
 'keephq.providers.slack_provider',
 'keephq.providers.snowflake_provider',
 'keephq.providers.ssh_provider',
 'keephq.providers.zenduty_provider',
 'keephq.step']

package_data = \
{'': ['*']}

install_requires = \
['astunparse>=1.6.3,<2.0.0',
 'boto3>=1.26.72,<2.0.0',
 'chevron>=0.14.0,<0.15.0',
 'click>=8.1.3,<9.0.0',
 'datefinder>=0.7.3,<0.8.0',
 'elasticsearch>=8.6.1,<9.0.0',
 'logmine>=0.4.1,<0.5.0',
 'mysql-connector-python>=8.0.32,<9.0.0',
 'paramiko>=3.0.0,<4.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'pygithub>=1.57,<2.0',
 'python-dotenv>=0.21.1,<0.22.0',
 'python-json-logger>=2.0.6,<3.0.0',
 'pyyaml>=6.0,<7.0',
 'requests>=2.28.2,<3.0.0',
 'sentry-sdk>=1.15.0,<2.0.0',
 'snowflake-connector-python>=3.0.0,<4.0.0',
 'validators>=0.20.0,<0.21.0',
 'zenduty-api>=0.2,<0.3']

entry_points = \
{'console_scripts': ['keep = keep.cli.cli:cli']}

setup_kwargs = {
    'name': 'keephq',
    'version': '0.1.0',
    'description': 'Alerting. for developers, by developers.',
    'long_description': '```diff\n+ Missing a specific use case? no worries, hit us up and we will implement it for you! just open an issue.\n```\n<br />\n<div align="center">\n    <img src="/docs/static/img/keep.png?raw=true">\n</div>\n\n<h1 align="center">Alerting. By developers, for developers.</h1>\n<br />\n<div align="center">\n    <a href="https://github.com/keephq/keep/blob/main/LICENSE">\n        <img src="https://img.shields.io/github/license/keephq/keep" />\n    </a>\n    <a href="https://keephq.dev/slack">\n        <img src="https://img.shields.io/badge/Chat-on%20Slack-blueviolet" alt="Slack community channel" />\n    </a>\n</div>\n\n<h4 align="center">\nSimple alerting tool, builtin providers (e.g. sentry/datadog or slack/pagerduty), 100% open sourced, free forever.\n</h4>\n<div align="center">\n\n- Simple and intuitive (GitHub actions-like) syntax.\n- Declarative alerting that can be easily managed and versioned in your version control and service repository.\n- Alerts from multiple data sources for added context and insights.\n- Freedom from vendor lock-in, making it easier to switch to a different observability tool if and when needed.\n\n</div>\n\n<p align="center">\n    <br />\n    <a href="https://keephq.wiki/" rel="dofollow"><strong>Get started »</strong></a>\n    <br />\n    <br />\n    <a href="https://github.com/orgs/keephq/projects/1">Roadmap</a>\n    ·\n    <a href="https://github.com/keephq/keep/tree/main/examples">Examples</a>\n    ·\n    <a href="https://github.com/keephq/keep/tree/main/keep/providers">Providers</a>\n    ·\n    <a href="https://keephq.wiki/">Docs</a>\n    ·\n    <a href="https://keephq.dev">Website</a>\n    ·\n    <a href="https://keephq.wiki/providers/new-provider">Add Providers</a>\n    ·\n    <a href="https://github.com/keephq/keep/issues/new?assignees=&labels=bug&template=bug_report.md&title=">Report Bug</a>\n    ·\n    <a href="https://keephq.dev/slack">Slack Community</a>\n</p>\n\n## 🗼 A glance of Keep\n\nKeep is a simple CLI tool that contains everything you need to start creating Alerts.\n\n- 10s of providers ready to use with your own data\n- Simple CLI tool to configure, trigger and test your alerts\n- Easily deployable via docker, vercel, github actions, etc.\n- Alerts are managed by simple yaml files that are human-readable\n\nBrought to you by developers, EASY to use and managable by code.\n\n## 🚨 Providers\n\n[Providers](https://keephq.wiki/providers/what-is-a-provider) are Keep\'s way of interacting with 3rd party products; Keep uses them either to query data or to send notifications.\n\nWe tried our best to cover all common providers, [missing any?](https://github.com/keephq/keep/issues/new?assignees=&labels=feature,provider&template=feature_request.md&title=Missing%20PROVIDER_NAME), providers include:\n\n- **Cloud**: AWS, GCP, Azure, etc.\n- **Monitoring**: Sentry, New Relic, Datadog, etc.\n- **Incident Management**: PagerDuty, OpsGenie, etc.\n- **Communication**: Email, Slack, Console, etc.\n- [and more...](https://github.com/keephq/keep/tree/main/keep/providers)\n\n## 🚀 Quickstart\n\n### Run locally\n\nTry our first mock alert and get it up and running in <5 minutes - Ready? Let\'s Go! ⏰\n\n<h5>First, clone Keep repository:</h5>\n\n```shell\ngit clone https://github.com/keephq/keep.git && cd keep\n```\n\n<h5>Install Keep CLI</h5>\n\n```shell\npip install .\n```\n\nor\n\n```shell\npoetry shell\npoetry install\n```\n\n<h5>From now on, Keep should be installed locally and accessible from your CLI, test it by executing:</h5>\n\n```\nkeep version\n```\n\nGet a Slack incoming webhook using [this tutorial](https://api.slack.com/messaging/webhooks) and use Keep to configure it:\n\n```\nkeep config provider --provider-type slack --provider-id slack-demo\n```\n\nPaste the Slack Incoming Webhook URL (e.g. <https://hooks.slack.com/services/...>) and you\'re good to go 👌\n\n<h5>Let\'s now execute our example "Paper DB has insufficient disk space" alert</h5>\n\n```bash\nkeep run --alerts-file examples/alerts/db_disk_space.yml\n```\n\n<div align="center">\n    Voilà 🥳\n    <br />\n    <img src="/docs/static/img/alert-example.png">\n    <br />\n    You should have received your first "Dunder Mifflin Paper Company" alert in Slack by now.\n    <br />\n</div>\n\n\n### Docker\n\nConfigure the Slack provider (See "[Run locally](https://github.com/keephq/keep#from-now-on-keep-should-be-installed-locally-and-accessible-from-your-cli-test-it-by-executing)" on how to obtain the webhook URL)\n\n```bash\ndocker run -v ${PWD}:/app -it keephq/cli config provider --provider-type slack --provider-id slack-demo\n```\n\nYou should now have a providers.yaml file created locally\n\nRun Keep and execute our example "Paper DB has insufficient disk space" alert\n\n```bash\ndocker run -v ${PWD}:/app -it keephq/cli -j run --alert-url https://raw.githubusercontent.com/keephq/keep/main/examples/alerts/db_disk_space.yml\n```\n\n### Render\nClick the Deploy to Render button to deploy Keep as a background worker running in [Render](https://www.render.com)\n\n[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)\n\nTo run Keep and execute our example "Paper DB has insufficient disk space" alert, you will need to configure you Slack provider.\n<br />\nWhen clicking the Deploy to Render button, you will be asked to provide the `KEEP_PROVIDER_SLACK_DEMO` environment variable, this is the expected format:\n\n```json\n{"authentication": {"webhook_url": "https://hooks.slack.com/services/..."}}\n```\n\n\\* Refer to [Run locally](https://github.com/keephq/keep#from-now-on-keep-should-be-installed-locally-and-accessible-from-your-cli-test-it-by-executing) on how to obtain the webhook URL\n\n##### Wanna have your alerts up and running in production? Go through our more detailed [Deployment Guide](https://keephq.wiki/deployment)\n\n## 🔍 Learn more\n\n- Share feedback/ask questions via our [Slack](https://keephq.dev/slack)\n- Explore [the full list of supported providers](https://github.com/keephq/keep/tree/main/keep/providers)\n- Explore the [documentation](https://keephq.wiki)\n- [Adding a new provider](https://keephq.wiki/providers/new-provider)\n- Check out our [website](https://www.keephq.dev)\n\n## 🫵 Keepers\n\nThank you for contributing and continuously making <b>Keep</b> better, <b>you\'re awesome</b> 🫶\n\n<a href="https://github.com/keephq/keep/graphs/contributors">\n  <img src="https://contrib.rocks/image?repo=keephq/keep" />\n</a>\n',
    'author': 'Paladin Data inc.',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
