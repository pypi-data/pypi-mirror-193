# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netscanner']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=22.1.0,<23.0.0',
 'aiosignal>=1.3.1,<2.0.0',
 'async-timeout>=4.0.2,<5.0.0',
 'attrs>=22.2.0,<23.0.0',
 'certifi>=2022.12.7,<2023.0.0',
 'charset-normalizer>=3.0.1,<4.0.0',
 'frozenlist>=1.3.3,<2.0.0',
 'idna>=3.4,<4.0',
 'mac-vendor-lookup>=0.1.12,<0.2.0',
 'multidict>=6.0.4,<7.0.0',
 'netscanner>=0.0.1,<0.0.2',
 'pip>=22.3.1,<23.0.0',
 'requests>=2.28.1,<3.0.0',
 'setuptools>=65.6.3,<66.0.0',
 'urllib3>=1.26.14,<2.0.0',
 'wheel>=0.38.4,<0.39.0',
 'yarl>=1.8.2,<2.0.0']

setup_kwargs = {
    'name': 'netscanner',
    'version': '0.0.4',
    'description': 'A comprehensive network reconnaissance tool',
    'long_description': '\n# NETSCANNER\n\nThis project was created as part of my final year undergraduate development project for my Bachelor of Science degree. \n\nThis program will conduct a comprehensive scan of the local network and surrounding wireless networks using basic OS utilities, Nmap and airodump-ng.\n\n## Demo\n\n\n\n## Requirements\n\n* `python3`: NETSCANNER was designed to work with Python 3.10.\n* [`ifconfig`](https://linux.die.net/man/8/ifconfig): For gathering statistical data on local interfaces.\n* [`ethtool`](https://linux.die.net/man/8/ethtool): For gathering statistical data on local interfaces\n* [`iwconfig`](https://linux.die.net/man/8/iwconfig): For gathering statistical data on local wireless-capable interfaces.\n* [`airmon-ng`](https://www.aircrack-ng.org/doku.php?id=airmon-ng): For enabling monitor mode on capable interfaces.\n* [`airodump-ng`](https://www.aircrack-ng.org/doku.php?id=airodump-ng): For capturing 802.11 beacon frames.\n* [`Nmap`](https://nmap.org/): For conducting local network reconnaissance.\n\nA monitor-mode capable wireless interface is also required if you wish to use the wireless network discovery feature. See [here](http://www.aircrack-ng.org/doku.php?id=compatible_cards) for more information on this.\n## Execution\n\n### Using PyPi\nThe preferred method of running the program is installing the Python package from PyPi directly.\n\n```bash\n  pip install netscanner\n```\n\nThen running the program:\n\n```bash\n  python3 netscanner\n```\n\n### Manually\nYou can also run the module itself by downloading the NetScanner.py module and running it.\n\n```bash\n  python3 NetScanner.py\n```\n\n## Modes and Options\n\n### Modes \n* Mode 1 \n    * This mode will execute all functions of the program. If no flags are specified this will be the mode of operation.\n* Mode 2 (-nP)\n    * This flag will execute Mode 2, NO PORT SCAN, which will execute the Host Discovery and 802.11 WLAN Discovery processes.\n* Mode 3 (-w)\n    * This flag will execute Mode 3, WIRELESS ONLY, which will execute the 802.11 WLAN Discovery process exclusively.\n* Mode 4 (-l)\n    * This flag will execute Mode 4, LOCAL SCAN ONLY, which will execute the Host Discovery and Port Scan processes.\n* Mode 5 (-hD)\n    * This flag will execute Mode 5, HOST DISCOVERY ONLY, which will execute the Host Discovery Process exclusively.\n\n### Options\n* Wireless Scan Period (--wP)\n    * This option allows you to specify a scan period for the 802.11 WLAN Discovery process. The default is 60. This value is ignored if the mode of operation is not Mode 1, 2 or 3. Large values will result in longer scan times but greater verbosity.\n* Port Scan Period (--pP)\n    * This option allows you to specify a scan period for the Port Scan process. The default is 60. This value is ignored if the mode of operation is not Mode 1 or 4. Large values will result in longer scan times but greater verbosity. \n* Port Range (--pR)\n    * This option allows you to specify a port range for the Port Scan process. The default is the 100 most common ports determined by Nmap (-F). Large values will result in longer scan times but greater verbosity. It is useful to combine this option with the --pP option to avoid scan timeouts when scanning large ranges. \n## Processes\n\nThis section provides a brief synopsis of each process used in the program. There are three processes that are used.\n\n### Host Discovery\nThis process gathers characteristics about the local network and hosts on the local network using ifconfig, iwconfig, ethtool and the ARP Request Ping Flood and rDNS query flood in Nmap, host discovery techniques.\n\n### Port Scan\nBy default, this process uses Nmap to determine the state of the 100 most used TCP and UDP ports, determined by Nmap, on all active hosts on the local network using the TCP Half-Open Scan and the UDP Scan, port scanning techniques. The ports that are scanned can be changed using the --pR flag, in the command line, to indicate a port range.\n\nThis process also has a default timeout period of 60 seconds which can be changed using the --pP flag.\n\n### Remote WLAN Discovery\nThis process determines the characteristics of remote wireless networks in the vicinity of the host machine if a wireless interface is present and available using the 802.11 packet capture technique with airodump-ng.\n\nThis process has a default timeout period of 60 seconds which can be changed using the --wP flag.',
    'author': 'Adam Dawood',
    'author_email': 'ADD0242@MY.LONDONMET.AC.UK',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/add0242/NETSCANNER',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
