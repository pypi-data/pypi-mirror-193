# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mobilecoin', 'mobilecoin.util']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0',
 'base58>=2.1.1,<3.0.0',
 'protobuf>=4.21.12,<5.0.0',
 'segno>=1.5.2,<2.0.0']

entry_points = \
{'console_scripts': ['mob = mobilecoin.cli:main']}

setup_kwargs = {
    'name': 'mobilecoin',
    'version': '2.3.1',
    'description': '',
    'long_description': "# Python API and CLI for MobileCoin Full-Service Wallet\n\n## Installation\n\n`$ pip install mobilecoin`\n\n\n## CLI usage\n\nFirst, you should have an instance of the full-service wallet running on your local machine. Setup instructions are at https://github.com/mobilecoinofficial/full-service.\n\n```\n$ cd full-service\n$ ./tools/run-fs.sh test\n```\nSee the full-service README for more details.\n\nCheck that your CLI is correctly configured by running the status command:\n```\n$ mob status\nConnected to MobileCoin network.\nAll accounts synced, 1421264 blocks.\n\nTotal balance for all accounts:\n  0 MOB\n\nTransaction Fees:\n  0.0004 MOB\n  0.00256 eUSD\n```\n\nCreate an account.\n```\n$ mob create\nCreated a new account.\nd7efc1\n\n```\n\nSee it in the account list.\n```\n$ mob list\n\nd7efc1 (synced)\n  address 6eRwLkggafsMs8Mef3JPLExksDpG7BRdYtaDhLkNn1c3AkcdZegJXxsxaPGnZZjR8nuz9SmhYHPrZ3yxqfjmbxfefCK6RqXqNfD9w4T9Hb7\n  0 MOB\n```\n\nGet at least 1 MOB on testnet in order to run unitests, then export your wallet so the\nunittests can use it. Store this file in a safe location.\n\n```\n$ mob export d7\nYou are about to export the secret entropy mnemonic for this account:\n\nd7efc1 (synced)\n  address 6eRwLkggafsMs8Mef3JPLExksDpG7BRdYtaDhLkNn1c3AkcdZegJXxsxaPGnZZjR8nuz9SmhYHPrZ3yxqfjmbxfefCK6RqXqNfD9w4T9Hb7\n  1.0000 MOB\n\nKeep the exported entropy file safe and private!\nAnyone who has access to the entropy can spend all the funds in the account.\nReally write account entropy mnemonic to a file? (Y/N) Y\nWrote mobilecoin_secret_mnemonic_d7efc1.json.\n\n$ mv mobilecoin_secret_mnemonic_d7efc1.json /path/to/safe/location\n```\n\n\n## Run unittests and integration tests.\n\nSet an environment variable to tell the unittests where your wallet export file is.\n```\n$ export MC_WALLET_FILE='/path/to/safe/location/mobilecoin_secret_mnemonic_d7efc1.json'\n```\n\nOptionally set environment variables to run fog tests.\n```\n$ export MC_FOG_REPORT_URL='fog://fog.test.mobilecoin.com'\n$ export MC_FOG_AUTHORITY_SPKI='MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvnB9wTbTOT5uoizRYaYbw7XIEkInl8E7MGOAQj+xnC+F1rIXiCnc/t1+5IIWjbRGhWzo7RAwI5sRajn2sT4rRn9NXbOzZMvIqE4hmhmEzy1YQNDnfALAWNQ+WBbYGW+Vqm3IlQvAFFjVN1YYIdYhbLjAPdkgeVsWfcLDforHn6rR3QBZYZIlSBQSKRMY/tywTxeTCvK2zWcS0kbbFPtBcVth7VFFVPAZXhPi9yy1AvnldO6n7KLiupVmojlEMtv4FQkk604nal+j/dOplTATV8a9AJBbPRBZ/yQg57EG2Y2MRiHOQifJx0S5VbNyMm9bkS8TD7Goi59aCW6OT1gyeotWwLg60JRZTfyJ7lYWBSOzh0OnaCytRpSWtNZ6barPUeOnftbnJtE8rFhF7M4F66et0LI/cuvXYecwVwykovEVBKRF4HOK9GgSm17mQMtzrD7c558TbaucOWabYR04uhdAc3s10MkuONWG0wIQhgIChYVAGnFLvSpp2/aQEq3xrRSETxsixUIjsZyWWROkuA0IFnc8d7AmcnUBvRW7FT/5thWyk5agdYUGZ+7C1o69ihR1YxmoGh69fLMPIEOhYh572+3ckgl2SaV4uo9Gvkz8MMGRBcMIMlRirSwhCfozV2RyT5Wn1NgPpyc8zJL7QdOhL7Qxb+5WjnCVrQYHI2cCAwEAAQ=='\n```\n\nWith full-service running, start the integration tests.\n```\n$ poetry run pytest -v\n```\n",
    'author': 'Christian Oudard',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://mobilecoin.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
