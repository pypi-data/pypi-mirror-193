# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ng_bot']

package_data = \
{'': ['*']}

install_requires = \
['prettytable>=3.6.0,<4.0.0',
 'pyngrok>=5.2.1,<6.0.0',
 'pytelegrambotapi>=4.10.0,<5.0.0',
 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'ng-bot',
    'version': '1.0.0',
    'description': 'Bot Integrations with various platforms to send latest ngork links',
    'long_description': "# Tele-Ng-Bot\n\nTelegram Ngrok Bot (Tele-Ng-Bot) publishes updated ngrok URLs to telegram chat ids and restricts other users to access the bot.\n\n> `Note`: This bot may be used for malicious purposes too. Its upto users how they use this tool/bot. Author is not responsible for user's action in any manner.\n\n## Installation\n\n- Clone repo\n\n  ```bash\n  git clone --depth=1 https://github.com/dmdhrumilmistry/ng_bot.git\n  ```\n\n- Change directory\n\n  ```bash\n  cd ng_bot\n  ```\n\n- Install requirements\n\n  ```bash\n  python3 -m pip install -r requirements.txt\n  ```\n\n## Usage\n\n- Create Ngrok account\n\n- Complete Sign Up process\n\n- Add new AUTH TOKEN from [dashboard](https://dashboard.ngrok.com/get-started/your-authtoken)\n\n- Store variables in `.env` file\n\n  ```bash\n  NGROK_AUTH_TOKEN='your_auth_token'\n  TELE_BOT_TOKEN='telegram_bot_token'\n  ALLOWED_USER_IDS=tele_user_id1, tele_user_id2, tele_user_id3\n  DISCORD_WEBHOOK_URL='webhook-url' \n  ```\n\n  > Above variables can also be stored in environment variables\n\n- Start application\n\n  ```bash\n  # for telegram\n  python3 -m ng_bot --http 8080 --tcp 22 4444 --platform telegram\n\n  # for discord\n  python3 -m ng_bot --tcp 22 --platform discord\n  ```\n",
    'author': 'Dhrumil Mistry',
    'author_email': '56185972+dmdhrumilmistry@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
