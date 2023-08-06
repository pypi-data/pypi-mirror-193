# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xkcdscrape']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'lxml>=4.9.2,<5.0.0',
 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'xkcd-scrape',
    'version': '0.5.0',
    'description': 'Scrape the XKCD comic archive',
    'long_description': '# XKCD Scrape\n\n`xkcd-scrape` is a Python module to dump the XKCD.com archive and get comic info using BS4. Honestly, it\'s a very basic module with one premise - easily get information about comics.\n\n[![status-badge](https://ci.codeberg.org/api/badges/calamity/xkcd-scrape/status.svg)](https://ci.codeberg.org/calamity/xkcd-scrape)\n![PyPI](https://img.shields.io/pypi/v/xkcd-scrape?color=blue)\n\n## Examples\nBasic usage:\n```py\nfrom xkcdscrape import xkcd\n\n# Load the archive of comics into a variable\n# Allows to get the publication date by passing into getComicInfo and getRandomComic\narchive = xkcd.parseArchive()\n\n# Get info about latest comic\ninfo = xkcd.getComicInfo(archive=archive) # w/ date\ninfo = xkcd.getComicInfo() # w/o date\n\n# Get info about specific comic\n# The comic can either be an int (2000), a str ("2000"|"/2000/"), or a link ("https://xkcd.com/2000")\ninfo = xkcd.getComicInfo(2000, archive) # w/ date\ninfo = xkcd.getComicInfo(2000) # w/o date\n\n# Get info about a random comic\n# Passing the second paramenter as True makes the module only fetch comics that are present in the archive\ninfo = xkcd.getRandomComic(archive, True) # w/ date\ninfo = xkcd.getRandomComic() # w/o date\n\n# Dump archive to file\nxkcd.dumpToFile(archive, "dump.json")\n\n# Get info using the archive dump.\ninfo = xkcd.getComicInfo("dump.json") # latest\ninfo = xkcd.getComicInfo("dump.json", 2000) # specific\ninfo = xkcd.getRandomComic("dump.json", True) # random\n\n# Get latest entry from the RSS feed\n# Currently VERY raw, just returns the first <item> tag as a string\nlastentry = xkcd.getLastRSS()\n```\n\nThe `getComicInfo` function (also called inside of `getRandomComic`) returns a dict with following keys:\n```py\n# xkcd.getComicInfo(2000, archive)\n{\n    \'date\': \'2018-5-30\', \n    \'num\': \'2000\', \n    \'link\': \'https://xkcd.com/2000/\', \n    \'name\': \'xkcd Phone 2000\', \n    \'image\': \'https://imgs.xkcd.com/comics/xkcd_phone_2000.png\', \n    \'title\': \'Our retina display features hundreds of pixels per inch in the central fovea region.\'\n}\n```\nAs you can see, it returns the following list of keys:\n- `num` - comic number\n- `link` - hyperlink to comic\n- `name` - the name of the comic\n- `date` - YYYY-MM-DD formatted date of when the comic was posted (not returned if archive is None)\n- `image` - hyperlink to image used in the comic\n- `title` - title (hover) text of the comic\n\n## Archive\nThe [XKCD archive](https://xkcd.com/archive/) is where we get the list of comics, as well as their names and date of posting. This is the only place where we can get the date of posting, so it\'s required if you need the date.\n\nThe archive is a dict containing various dicts with keys of `/num/`. Example:\n```py\n{\n    ...,\n    "/2000/": {\n        "date": "2018-5-30", \n        "name": "xkcd Phone 2000"\n    },\n    ...\n}\n```\n\n## Tests\nTests can be run from the project\'s shell after installing and activating the venv using `poetry run pytest`.\nUse Python\'s included `unittest` module for creating tests (examples are in `tests/`).\n\n## TODO\n- Improve RSS feed output\n- API and homepage (on one domain?)\n',
    'author': 'calamity',
    'author_email': 'clmty@vk.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://codeberg.org/calamity/xkcd-scrape',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
