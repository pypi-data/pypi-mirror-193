# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oda_data',
 'oda_data.classes',
 'oda_data.clean_data',
 'oda_data.get_data',
 'oda_data.indicators',
 'oda_data.read_data',
 'oda_data.tools']

package_data = \
{'': ['*'], 'oda_data': ['.raw_data/*', 'settings/*']}

install_requires = \
['bblocks>=1,<2',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'lxml>=4.9.2,<5.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pydeflate>=1.3.1,<2.0.0',
 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'oda-data',
    'version': '1.0.0',
    'description': 'A python package to work with Official Development Assistance data from the OECD DAC.',
    'long_description': '[![pypi](https://img.shields.io/pypi/v/oda_data.svg)](https://pypi.org/project/oda_data/)\n[![python](https://img.shields.io/pypi/pyversions/oda_data.svg)](https://pypi.org/project/oda_data/)\n[![codecov](https://codecov.io/gh/ONEcampaign/oda_data_package/branch/main/graph/badge.svg?token=G8N8BWWPL8)](https://codecov.io/gh/ONEcampaign/oda_data_package)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n# The ODA Data Package\nThis package contains key tools used by The ONE Campaign to analyse Official Development Assistance (ODA) data from\nthe OECD [DAC](https://www.oecd.org/dac/stats/) databases.\n\nInteracting with the DAC databases can be a complex task. There are many databases, tables, and web interfaces which\ncan be used to get the data you need. This means that getting the right ODA data can require expert knowledge not only\nof ODA, but also of how the DAC databases and tools are organised.\n\nThis package aims to simplify this process and make it easier for users to get the data they need.\n\nPlease submit questions, feedback or requests via \nthe [issues page](https://github.com/ONEcampaign/oda_data_package/issues).\n\n## Getting started\n\n### Installation\nThe package can be installed using pip:\n\n```bash\npip install oda-data --upgrade\n```\n\nThe package is compatible with Python 3.10 and above.\n\n### Basic usage\n\nMost users can get the data they need by using the `ODAData` class.\n\nAn object of this class can handle:\n- getting data for specific indicators (one or more)\n- filtering the data for specific donors, recipients(if relevant), years.\n- returning the data in a variety of currency/prices combinations.\n\nFor example, to get Total ODA in net flows and grant equivalents, in constant 2021 Euros, for 2018-2021.\n\n```python\nfrom oda_data import ODAData, set_data_path\n\n# set the path to the folder where the data should be stored\nset_data_path("path/to/data/folder")\n\n# create object, specifying key details of the desired output\ndata = ODAData(years=range(2018,2022), currency="EUR", prices="constant", base_year=2021)\n\n# load the desired indicators\ndata.load_indicator(indicators = ["total_oda_flow_net", "total_oda_ge"])\n\n# get the data\ndf = data.get_data()\n\nprint(df.head(6))\n```\nThis would result in the following dataframe:\n\n|   donor_code | donor_name   |   year |   value | indicator          | currency   | prices   |\n|-------------:|:-------------|-------:|--------:|:-------------------|:-----------|:---------|\n|            1 | Austria      |   2021 | 1261.76 | total_oda_flow_net | EUR        | constant |\n|            1 | Austria      |   2021 | 1240.31 | total_oda_ge       | EUR        | constant |\n|            2 | Belgium      |   2021 | 2176.38 | total_oda_flow_net | EUR        | constant |\n|            2 | Belgium      |   2021 | 2174.38 | total_oda_ge       | EUR        | constant |\n|            3 | Denmark      |   2021 | 2424.51 | total_oda_flow_net | EUR        | constant |\n|            3 | Denmark      |   2021 | 2430.65 | total_oda_ge       | EUR        | constant |\n\n\nTo print the full list of available indicators, you can call `.get_available_indicators()`.\n\nFor full details on the available indicators and how we calculate them,\nsee the indicators [documentation](oda_data/settings/Available indicators.md)\n\n## Tutorials\nFor more detailed examples of how to use the package, see the [tutorials](tutorials).\n- A [tutorial notebook](tutorials/1.%20total_donor_oda.ipynb) on loading the package and getting total oda data\n- A [tutorial notebook](tutorials/2.%20total_recipient_oda_by_donor.ipynb) on getting ODA by donor and recipient\n  (including both bilateral and imputed multilateral data)\n- A [tutorial notebook](tutorials/3.%20sector_analysis_by_donor_and_recipient.ipynb) on getting ODA by sectors\n  (including both bilateral and imputed multilateral data)\n\nPlease reach out if you have questions or need help with using the package for your analysis.\n\n## Key features\n\n- **Speed up analysis** - The package handles downloading, cleaning and loading all the data, so you can focus on the \nanalysis. The data is downloaded from the bulk download service of the OECD, and once it is stored locally, producing\nthe output is extremely fast.\n- **Access all of our analysis** - Besides the classic OECD DAC indicators, the package also provides access to the\ndata and analysis produced by ONE. This includes gender or climate data in gross disbursement terms (instead of\ncommitments) and our multilateral sectors imputations.\n- **Get data in the currency and prices you need** - ODA data is only available in US dollars (current or constant \nprices) and local currency units (current prices). The package allows you to view the data in US dollars, Euros,\nBritish Pounds and Canadian dollars, in both current and constant prices. We can add any other DAC currency if you\nrequest it via the [issues page](https://github.com/ONEcampaign/oda_data_package/issues)\n\n## Contributing\nInterested in contributing to the package? Please reach out.\n',
    'author': 'Jorge Rivera',
    'author_email': 'jorge.rivera@one.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
