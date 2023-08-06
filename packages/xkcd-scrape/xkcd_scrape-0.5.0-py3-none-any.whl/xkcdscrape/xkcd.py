from bs4 import BeautifulSoup as BS
from importlib.metadata import version
import requests, json, re, random


class Macros:
    def transformArchive(archive: str | dict | None) -> dict | None:
        if isinstance(archive, str):
            try:
                with open(archive) as afile:
                    archive: dict = json.load(afile)
            except FileNotFoundError:
                raise FileNotFoundError("Archive file not found") from None
            else:
                return archive
        else:
            return archive

    def getComicDate(archive: dict, num: str) -> str:
        date = None
        try:
            date = archive[num]["date"]
        except KeyError:
            raise KeyError("Comic not in archive, unable to get date") from None
        else:
            return date

    def getHeaders() -> dict:
        return {"User-Agent": f"xkcd-scrape/{version('xkcd-scrape')}"}


def parseArchive() -> dict:
    """Parse the xkcd.com archive for simple comic info."""
    archive: dict = {}
    archiveDoc = requests.get(
        "https://xkcd.com/archive/", headers=Macros.getHeaders()
    ).text
    soup = BS(archiveDoc, "html.parser")
    comicContainer = soup.find(id="middleContainer")
    for comicTag in comicContainer.children:
        if comicTag.name == "a":
            archive[comicTag["href"]] = {
                "date": comicTag["title"],
                "name": comicTag.string,
            }
    return archive


def dumpToFile(
    archiveDict: dict, fp: str = "xkcd.json", indent: int | None = None
) -> None:
    """Dump an archive dict into a file."""
    try:
        with open(fp, "x") as file:
            json.dump(archiveDict, file, indent=indent)
    except FileExistsError:
        with open(fp, "w") as file:
            json.dump(archiveDict, file, indent=indent)
    return None


def getComicInfo(
    comic: int | str = "xkcd.com", archive: dict | str | None = None
) -> dict:
    """Return object with complete comic info."""

    # Transform archive into a dict
    archive = Macros.transformArchive(archive)

    # Construct link from comic input
    if isinstance(comic, str):
        m = re.match(r"((https?:\/\/)?(xkcd\.com)(\/\d+\/?)?)|(\/\d+\/)|(\d+)", comic)
        if m == None:
            raise ValueError("Comic doesn't match proper formatting")
        m = m[0]
        if m.startswith("http"):
            link = comic
        elif m.startswith("xkcd.com"):
            link = f"https://{m}"
        elif m.startswith("/"):
            link = f"https://xkcd.com{m}"
        elif m[0].isdigit():
            link = f"https://xkcd.com/{m}"
        else:
            raise RuntimeError("How did you get here?")
    elif isinstance(comic, int):
        link = f"https://xkcd.com/{comic}/"

    # Get information from comic's page
    # This looks like a bit of a mess...
    comicInfo = {}
    comicDoc = requests.get(link, headers=Macros.getHeaders()).text
    cc = BS(comicDoc, "html.parser").find(id="middleContainer")
    if cc == None:
        raise ValueError("Comic not found") from None
    ntag = cc.find("a", {"href": re.compile(r"https://xkcd.com/")})
    num = "/" + re.search(r"(\d+)", ntag.string)[0] + "/"
    if isinstance(archive, dict):
        try:
            date = Macros.getComicDate(archive, num)
            comicInfo["date"] = date
        except KeyError:
            pass

    # Build the comicInfo dict
    comicInfo["num"] = num.strip("/")
    comicInfo["link"] = ntag.string
    comicInfo["name"] = cc.find("div", {"id": "ctitle"}).string
    comicInfo["image"] = "https:" + cc.find("img")["src"]
    comicInfo["title"] = cc.find("img")["title"]
    return comicInfo


def getRandomComic(archive: dict | str | None = None, fromArchive: bool = False) -> dict:
    """Return random comic's info. Calls getComicInfo internally.\n
    fromArchive defines if comic is received from online or from the archive dict."""

    # Transform archive into a dict
    archive = Macros.transformArchive(archive)
    if archive == None:
        fromArchive = False

    # Get the comic info using getComicInfo()
    if fromArchive:
        c = random.choice(list(archive.keys()))
        return getComicInfo(c, archive)
    else:
        c = requests.get("https://c.xkcd.com/random/comic/").url
        if archive is not None:
            return getComicInfo(c, archive)
        else:
            return getComicInfo(c, archive)

def getLastRSS() -> str:
    """Get the latest entry from from xkcd.com/rss.xml.\n
    Very very raw, absolutely uncleaned. You could cache and compare, I guess?"""
    feed = requests.get(
        "https://xkcd.com/rss.xml", headers=Macros.getHeaders()
    ).text
    soup = BS(feed, 'xml').find('item')
    return str(soup)