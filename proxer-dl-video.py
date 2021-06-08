"""
    proxer-dl-video.py

    command line script to download a single video from proxer.me
"""

from lib.script_utils   import script_exit
from lib.proxer_utils   import download_mp4, get_embed_url, get_mp4_url, TargetNotFoundError
from argparse           import ArgumentParser, Namespace

if __name__ == '__main__':
    # argument parsing
    parser : ArgumentParser = ArgumentParser(
        description='Download single video from proxer.me, only works for direct proxer uploads',
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
        help='auth token cookie, seperated by =, example: --token 4lpHaNuM57r=An0th3r5tr',
        required=True
    )
    args : Namespace = parser.parse_args()
    # input guarding
    try:
        args.token = args.token.split('=')
        if len(args.token[0]) <= 0 or len(args.token[1]) <= 0:
            raise Exception
    except Exception:
        script_exit('auth token could not be parsed')
    try:
        with open(args.outfile, 'wb') as f:
            pass
    except Exception:
        script_exit(f'file {args.outfile} could not be opened')
    # script execution
    try:
        embed_url = get_embed_url(
            args.url,
            args.token
        )
    except TargetNotFoundError:
        script_exit('could not find embed, this is most likely due to an invalid auth token or because there is no proxer upload for this video')
    mp4_url = get_mp4_url(embed_url)
    try:
        download_mp4(
            mp4_url,
            args.outfile,
            args.outfile
        )
        print(f'successfully downloaded {args.url}')
    except KeyboardInterrupt:
        script_exit('keyboard interrupt, download stopped')
