"""
    proxer-dl-video.py

    command line script to download a single video from proxer.me
"""

import sys
from argparse           import ArgumentParser, Namespace
from lib.proxer_utils   import download_mp4, get_embed_url, get_mp4_url

# argument parsing
parser : ArgumentParser = ArgumentParser(
    description='Download single video from proxer.me',
    allow_abbrev=True
)
parser.add_argument(
    '-u', '--url',
    help='url to proxer.me video view url',
    required=True
)
parser.add_argument(
    '-o', '--outfile',
    help='path to output file, include .mp4 extensions',
    required=True
)
parser.add_argument(
    '-t', '--token',
    help='auth token cookie, seperated by =, example: 4lpHaNuM57r=An0th3r5tr',
    required=True
)
args : Namespace = parser.parse_args()
# input guarding
try:
    args.token = args.token.split('=')
    if len(args.token[0]) <= 0 or len(args.token[1]) <= 0:
        raise Exception
except Exception:
    print('exit with error: auth token could not be parsed')
try:
    with open(args.outfile, 'wb') as f:
        pass
except Exception:
    print(f'exit with error: file {args.outfile} could not be opened')
# script execution
try:
    embed_url = get_embed_url(
        'https://proxer.me/watch/18686/4/engsub',
        ('e0da4f913f5f05ed7a3f6dc5f0488c7b','7ebv928opvp5o6vu82fu81bh5n')
    )

mp4_url = get_mp4_url(embed_url)

print(mp4_url)

download_mp4(
    mp4_url,
    './test.mp4',
    "asdasdasdasddddddddddddddddddaaa"
)
"""