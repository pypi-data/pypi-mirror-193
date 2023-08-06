# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rizthme',
 'rizthme.commands',
 'rizthme.events',
 'rizthme.models',
 'rizthme.models.factory',
 'rizthme.models.musics',
 'rizthme.models.musics.youtube',
 'rizthme.models.threads',
 'rizthme.setting']

package_data = \
{'': ['*']}

install_requires = \
['discord>=2.1.0,<3.0.0',
 'ffmpeg>=1.4,<2.0',
 'multipledispatch>=0.6.0,<0.7.0',
 'pynacl>=1.5.0,<2.0.0',
 'pytube>=12.1.2,<13.0.0',
 'tmktthreader>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'rizthme',
    'version': '2.1.2',
    'description': 'Discord Bot',
    'long_description': '# Rizthme\n\n## Requierement\n\nFirst step is to add in your environments variables,\na variables named "TOKEN" with in value, your discord application token.\n\ndo this with:\n\n```console\nfoo@bar:~$ export TOKEN=<your token>\n```\n\nnext, check that the ffmpeg module is installed on your device.\n\n```console\nfoo@bar:~$ ffmpeg -version\n```\n\nif not\n\n```console\nfoo@bar:~$ sudo apt install ffmpeg \n# or equivalent depending on your system\n```\n\n## To launch the discord client\n\n```console\nfoo@bar:~$ python3 client.py\n```\n\n### Automatical script launching\n\n#### For Linux user\n\nFor use automatically your virtual environment. (The virtual environment name need to be "venv/")\n\n```console\nfoo@bar:~$ source entrypoint.sh\n```\n\nif you don\'t want to use a virtual environment. juste use the script like this:\n\n```console\nfoo@bar:~$ bash entrypoint.sh\n```\nor \n\n```console\nfoo@bar:~$ sh entrypoint.sh\n```\n\n#### For Windows user\n\n> Not sure yet\n\nyou can do like this if you realy want to use that in Windows system\n\n```\nC:RizThme\\> entrypoint.bat\n```\n',
    'author': 'ladettanguy',
    'author_email': 'sti2dlab.ladettanguy@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
