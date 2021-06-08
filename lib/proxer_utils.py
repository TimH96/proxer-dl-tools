"""
    lib/proxer_utils.py

    lib for utility functions to scrape data from proxer.me
"""

from requests       import Response, get
from clint.textui   import progress


class TargetNotFoundError(Exception):
    """Error thrown when target element of scrape could not be found"""


def get_embed_url(url: str, token: list) -> str:
    """
    Returns URL of proxer embed

    :param url: url of base episode page
    :param token: (key, value) tuple of auth-token cookie
    :returns: url of embed
    :raises TargetNotFoundError: when embed could not be found
    """
    SEARCH_TOKEN : str = '"code":"'
    # get page
    content : str = get(
        url,
        cookies={
            token[0]:token[1],
            'stream_choose':'proxer-stream'
        },
        headers={'User-Agent': 'Mozilla/5.0'}
    ).text
    # get position of embed code
    code_index : int = content.find(SEARCH_TOKEN) + len(SEARCH_TOKEN)
    if code_index < len(SEARCH_TOKEN):
        raise TargetNotFoundError
    # parse code
    code : str = content[code_index:].partition('"')[0]
    # build and return url
    return f'https://stream.proxer.me/embed-{str(code)}-728x504.html'


def get_mp4_url(url: str) -> str:
    """
    Returns URL of direct link to mp4

    :param url: url of proxer embed player
    :returns: url of mp4
    :raises TargetNotFoundError: when mp4 url could not be found
    """
    SEARCH_TOKEN : str = 'source type="video/mp4" src="'
    # get page
    content : str = get(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    ).text
    # get position of embed code
    link_index : int = content.find(SEARCH_TOKEN) + len(SEARCH_TOKEN)
    if link_index < len(SEARCH_TOKEN):
        raise TargetNotFoundError
    # find and return target url
    return content[link_index:].partition('"')[0]


def download_mp4(url: str, filepath: str, label: str = '') -> None:
    """
    Downloads mp4 from url and posts to file, prints progress to stdout

    :param url: url of mp4
    :param filepath: filepath to output
    :param label: optional label for stdout progress bar, max length 32
    """
    CHUNK_SIZE : int = 255
    LABEL_SIZE : int = 32
    # parse label
    if label == '':
        pass
    elif len(label) >= LABEL_SIZE:
        label = label[:LABEL_SIZE-4] + '... '
    else:
        label = label.ljust(LABEL_SIZE, ' ')
    # get page
    content : Response = get(url, stream=True)
    t_leng  : int      = int(content.headers.get('content-length'))
    # dl to file
    with open(filepath, 'wb') as file:
        if t_leng:
            for chunk in progress.bar(content.iter_content(chunk_size=255), expected_size=t_leng/CHUNK_SIZE, label=label):
                if chunk:  # filter out keep-alive new chunks
                    file.write(chunk)
        else:
            file.write(content)
