from proxer_utils import download_mp4, get_embed_url, get_mp4_url

embed_url = get_embed_url(
    'https://proxer.me/watch/18686/4/engsub',
    ('e0da4f913f5f05ed7a3f6dc5f0488c7b', '70qn7q3uri1nsqfef9c6jpb03m')
)

mp4_url = get_mp4_url(embed_url)

print(mp4_url)

download_mp4(
    'https://cdn-cf-east.streamable.com/video/mp4/3sqnah.mp4?Expires=1623350100&Signature=lup8hrytkV7sOGMFbgJZ5MNjF66AFofo4lN170kx9MLNNusr63HfRUgvvg2405kWV~HO3PgA-Z~ORI7xl~mGDzSDiH5PArFLuoIA3~hbRfkIVU8F6Gi6kROBLTmqdW3RyLjVsK-Q1XiOZkGYWIlkgr4NfWJFj9UyL6My~rccf3u-dp5eK-emqN3YfIvQopw4hDj8-mkIaEgzEbZjZt6wIfXT-HEzxW-wyyGcjt2lw--dNj6Tj5S8DacL703gipndTX5S~BkZLvcTK5Zru~2lwfND~tSM-8uadoe8Q1da-qDv3Olm6zYnq-gOK-iHP4KxZBQQWN2~Wd6aQkbgkXXETA__&Key-Pair-Id=APKAIEYUVEN4EVB2OKEQ',
    './test.mp4'
)