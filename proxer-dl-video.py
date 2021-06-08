"""
    proxer-dl-video.py

    command line script to download a single video from proxer.me
"""

from lib.script_utils   import script_exit, check_validity_token
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
        help='path to output file, include .mp4 extensions'
    )
    parser.add_argument(
        '-t', '--token',
        help='auth token cookie, seperated by =, example: --token 4lpHaNuM57r=An0th3r5tr',
        required=True
    )
    parser.add_argument(
        '-g', '--get_mode',
        action='store_true',
        help="get url mode, collects direct mp4 link and posts it to stdout but doesn't download them",
    )
    args : Namespace = parser.parse_args()
    # input check
    args.token = check_validity_token(args.token)
    if not args.get_mode:
        if not args.outfile:
            script_exit('--outfile required unless in --get_mode')
    # script execution
    try:
        embed_url = get_embed_url(
            args.url,
            args.token
        )
    except TargetNotFoundError:
        script_exit('could not find embed, this is most likely due to an invalid auth token or because there is no proxer upload for this video or DDOS protection')
    mp4_url = get_mp4_url(embed_url)
    # log collected mp4s if in get_mode
    if args.get_mode:
        print(mp4_url)
    # download in normal mode
    else:
        try:
            download_mp4(
                mp4_url,
                args.outfile,
                args.outfile
            )
            print(f'successfully downloaded {args.url}')
        except KeyboardInterrupt:
            script_exit('keyboard interrupt, download stopped')
