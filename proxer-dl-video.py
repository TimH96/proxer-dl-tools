from proxer_utils import download_mp4, get_embed_url, get_mp4_url

embed_url = get_embed_url(
    'https://proxer.me/watch/18686/4/engsub',
    ('e0da4f913f5f05ed7a3f6dc5f0488c7b', '70qn7q3uri1nsqfef9c6jpb03m')
)

mp4_url = get_mp4_url(embed_url)

print(mp4_url)

download_mp4(
    mp4_url,
    './test.mp4',
    "asdasdasdasddddddddddddddddddaaa"
)