"""
    proxer-dl-video.py

    command line script to download a single video from proxer.me
"""

from sys                import exit
from lib.proxer_utils   import download_mp4, get_embed_url, get_mp4_url, TargetNotFoundError
from argparse           import ArgumentParser, Namespace


def _script_exit(reason: str) -> None:
    """Wrapper for script exit on error"""
    print(f'exit with error: {reason}')
    exit()


if __name__ == '__main__':
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
        _script_exit('auth token could not be parsed')
    try:
        with open(args.outfile, 'wb') as f:
            pass
    except Exception:
        _script_exit(f'file {args.outfile} could not be opened')
    # script execution
    try:
        embed_url = get_embed_url(
            args.url,
            args.token
        )
    except TargetNotFoundError:
        _script_exit('could not find embed, this is most likely due to an invalid auth token or because there is no proxer upload for this video')
    mp4_url = get_mp4_url(embed_url)
    try:
        download_mp4(
            mp4_url,
            args.outfile,
            args.outfile
        )
        print(f'successfully downloaded {args.url}')
    except KeyboardInterrupt:
        _script_exit('keyboard interrupt, download stopped')
