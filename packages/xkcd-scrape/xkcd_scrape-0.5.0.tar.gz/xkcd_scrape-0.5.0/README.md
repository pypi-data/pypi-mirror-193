# XKCD Scrape

`xkcd-scrape` is a Python module to dump the XKCD.com archive and get comic info using BS4. Honestly, it's a very basic module with one premise - easily get information about comics.

[![status-badge](https://ci.codeberg.org/api/badges/calamity/xkcd-scrape/status.svg)](https://ci.codeberg.org/calamity/xkcd-scrape)
![PyPI](https://img.shields.io/pypi/v/xkcd-scrape?color=blue)

## Examples
Basic usage:
```py
from xkcdscrape import xkcd

# Load the archive of comics into a variable
# Allows to get the publication date by passing into getComicInfo and getRandomComic
archive = xkcd.parseArchive()

# Get info about latest comic
info = xkcd.getComicInfo(archive=archive) # w/ date
info = xkcd.getComicInfo() # w/o date

# Get info about specific comic
# The comic can either be an int (2000), a str ("2000"|"/2000/"), or a link ("https://xkcd.com/2000")
info = xkcd.getComicInfo(2000, archive) # w/ date
info = xkcd.getComicInfo(2000) # w/o date

# Get info about a random comic
# Passing the second paramenter as True makes the module only fetch comics that are present in the archive
info = xkcd.getRandomComic(archive, True) # w/ date
info = xkcd.getRandomComic() # w/o date

# Dump archive to file
xkcd.dumpToFile(archive, "dump.json")

# Get info using the archive dump.
info = xkcd.getComicInfo("dump.json") # latest
info = xkcd.getComicInfo("dump.json", 2000) # specific
info = xkcd.getRandomComic("dump.json", True) # random

# Get latest entry from the RSS feed
# Currently VERY raw, just returns the first <item> tag as a string
lastentry = xkcd.getLastRSS()
```

The `getComicInfo` function (also called inside of `getRandomComic`) returns a dict with following keys:
```py
# xkcd.getComicInfo(2000, archive)
{
    'date': '2018-5-30', 
    'num': '2000', 
    'link': 'https://xkcd.com/2000/', 
    'name': 'xkcd Phone 2000', 
    'image': 'https://imgs.xkcd.com/comics/xkcd_phone_2000.png', 
    'title': 'Our retina display features hundreds of pixels per inch in the central fovea region.'
}
```
As you can see, it returns the following list of keys:
- `num` - comic number
- `link` - hyperlink to comic
- `name` - the name of the comic
- `date` - YYYY-MM-DD formatted date of when the comic was posted (not returned if archive is None)
- `image` - hyperlink to image used in the comic
- `title` - title (hover) text of the comic

## Archive
The [XKCD archive](https://xkcd.com/archive/) is where we get the list of comics, as well as their names and date of posting. This is the only place where we can get the date of posting, so it's required if you need the date.

The archive is a dict containing various dicts with keys of `/num/`. Example:
```py
{
    ...,
    "/2000/": {
        "date": "2018-5-30", 
        "name": "xkcd Phone 2000"
    },
    ...
}
```

## Tests
Tests can be run from the project's shell after installing and activating the venv using `poetry run pytest`.
Use Python's included `unittest` module for creating tests (examples are in `tests/`).

## TODO
- Improve RSS feed output
- API and homepage (on one domain?)
