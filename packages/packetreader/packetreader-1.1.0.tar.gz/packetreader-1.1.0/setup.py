# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['PacketReader']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'packetreader',
    'version': '1.1.0',
    'description': 'A pcap file parser',
    'long_description': "PacketReader\n============\n\nA ``pcap`` file parser implemented by Python. Only supports TCP and UDP packet.\n\nInstallation\n------------\n\n::\n\n  pip install PacketReader\n\nUsage\n-----\n\n1. Import module.\n::\n\n  import PacketReader\n\n2. Read from a pcap file. ``read_pcap`` return a list of packets.\n::\n\n  packets = PacketReader.read_pcap(pcap_file)\n\n3. You can print the information of each packet.\n::\n\n  print(packets[0])\n\n4. PacketReader supports IP/TCP/UDP. You can get the MAC address, IP address or flags of packets.\n::\n\n    print(packets[0].src_mac_address)\n    print(packets[0].tcp_header['SYN'])\n\n\nExample\n-------\n::\n\n    >>> import PacketReader\n    >>> pl=PacketReader.read_pcap('test.pcap')\n    >>> print(len(pl))\n    179\n    >>> print(pl[0])\n    Packet 1 Information:\n    [1] Epoch Time: 1448157839.796592 seconds\n    [2] Frame Length: 85 bytes\n    [3] Destination Mac Address: 28:C2:DD:1D:75:C1\n    [4] Source Mac Address: 88:25:93:37:60:84\n    [5] Destination IP Address: 192.168.1.183\n    [6] Source IP Address: 192.30.252.88\n    [7] Destination Port: 57747\n    [8] Source Port :443\n    [9] Protocol: 6\n",
    'author': 'yuellin',
    'author_email': 'linyue92@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
