"""
    proxer-dl-series.py

    command line script to download an entire series from proxer.me
"""

from os                 import makedirs
from os.path            import exists, realpath, join
from lib.script_utils   import script_exit, check_validity_token, check_validity_episodes
from lib.proxer_utils   import download_mp4, get_embed_url, get_mp4_url, TargetNotFoundError, LanguageTypes
from argparse           import ArgumentParser, Namespace

if __name__ == '__main__':
    # argument parsing
    parser : ArgumentParser = ArgumentParser(
        description='Download anime series from proxer.me, only works for direct proxer uploads',
        allow_abbrev=True
    )
    parser.add_argument(
        '-i', '--id',
        help='proxer anime id, found in the url as so: https://proxer.me/info/{anime_id}/details',
        required=True
    )
    parser.add_argument(
        '-l', '--lang',
        help='language type',
        required=True,
        choices=[lang.name.lower() for lang in LanguageTypes]
    )
    parser.add_argument(
        '-o', '--outdir',
        help='path to output dir'
    )
    parser.add_argument(
        '-t', '--token',
        help='auth token cookie, seperated by =, example: --token 4lpHaNuM57r=An0th3r5tr',
        required=True
    )
    parser.add_argument(
        '-e', '--episodes',
        help='which episodes to download, given as {start_ep}-{end-ep}, example: -e 1-12',
        required=True
    )
    parser.add_argument(
        '-g', '--get_mode',
        action='store_true',
        help="get url mode, collects direct mp4 links and posts them to stdout but doesn't download them",
    )
    args : Namespace = parser.parse_args()
    # input check
    if not args.get_mode:
        if not args.outdir:
            script_exit('--outdir required unless in --get_mode')
    args.token = check_validity_token(args.token)
    args.episodes = check_validity_episodes(args.episodes)
    # collect mp4 urls
    found_episodes : list = []  # schema: {'ep': int, 'url': str}
    print('Collecting direct mp4 links ...')
    for ep_count in range(args.episodes[0], args.episodes[1]+1):
        try:
            page_url  : str = f'https://proxer.me/watch/{args.id}/{ep_count}/{args.lang}'
            embed_url : str = get_embed_url(
                page_url,
                args.token
            )
            mp4_url : str = get_mp4_url(embed_url)
            found_episodes.append({
                'ep'  : ep_count,
                'url' : mp4_url
            })
        except TargetNotFoundError:
            print(f'error: could not find mp4 for {page_url}, most likely because auth token was rejected or there is no proxer upload for this episode or DDOS protection')
            print(f'  skipping episode {ep_count}')
            continue
        except Exception:
            print(f'error: unforeseen error with getting mp4 from {page_url}')
            print(f'  skipping episode {ep_count}')
    # log collected mp4s if in get_mode
    if args.get_mode:
        print('Launched in get_mode, printing found urls')
        for episode in found_episodes:
            print(episode['ep'], episode['url'])
    # download in normal mode
    else:
        args.outdir = realpath(args.outdir)
        if not exists(args.outdir):
            makedirs(args.outdir)
            print(f'Created {args.outdir}')
        for episode in found_episodes:
            download_mp4(
                episode['url'],
                join(args.outdir, f'ep_{episode["ep"]}'),
                f'{args.id} {args.lang} ep.{episode["ep"]}'
            )
