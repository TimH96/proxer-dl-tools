This is a collection of lightweight command line scripts to directly download videos from the anime host [proxer.me](https://proxer.me/), using Python. Backup your favorite show with just one line.
```bash
$ python .\proxer-dl-series.py -i 8225 -l engsub -t Y0uR5oken=4lphNuM5tr -o H:\anime\Ping_Pong\ -e 1-11
```

-------------------------------------------

### Usage

#### Install

If you have Python 3.9^, you can just clone the repo and install its dependencies. Alternatively, you can download the packaged exectuables from the [releases page](https://github.com/TimH96/proxer-dl-tools/releases). Note that ``python .\proxer-dl-series.py`` is equivalent to ``.\proxer-dl-series.exe`` for the following documentation.

#### Getting your authentication cookie

As proxer will only allow registered users to view videos, you will have to get the authentication cookie and pass it to the scripts. This will allow the script to open websites as if it was logged in as your account. In the interest of keeping these tools as lightweight as possible, there is no automation for getting this token, as it would require a chromedriver or similiar tools. Fortunately, it is very easy to get manually.

1. Open any proxer video page in your preferred browser while logged in
2. Open developer tools (usually ``F12``) and navigate to the network tab, then reload the page
3. Click on the first entry in the table of network requests, it is usually named after your language option, i.e. ``engsub``
4. Navigate to the Request Headers section of this request and find the Cookie field
5. There will be multiple cookies there, you can find the authentication token by method of elimination - all the other cookies will be humanly readable to some degree, look for the one that looks like two random alphanumerical strings seperated by a ``=``
6. Copy this token and use it for the ``--token`` parameter when using the scrips, i.e. ``--token r4nD0m57rng=4lpHaNuMsTr1ng``

Note that the token expires eventually, so you will have to repeat these steps between download sessions. The scripts might also be caught by the DDOS protection. You can circumvent this by opening any video page in your browser and completing the Captcha verification, then running the script again.

#### Download a video

Run the ``proxer-dl-video`` script, passing in the video URL, auth token and the file to output it to. Use ``.\proxer-dl-video.exe -h`` for more information.

#### Download a series

Run the ``proxer-dl-series`` script, passing in the anime ID, auth token, output directory, episode range and language option. You can also retrieve all the download links instead with the ``--get_mode`` parameter, which might be useful if you want more control over when and how to download the series, i.e. from your browser. Use ``.\proxer-dl-series.exe -h`` for more information.

### Dependencies

These tools use the ``clint`` module to parse the download progress bar. It can be easily installed using ``pip``:

```bash
$ pip install clint
```

### Note of Intent

I wrote these tools with the following purpose in mind:
+ Backing up potentially volatile data.
+ Watching anime on demand. Proxer hosts anime in excellent quality (better than any host I am aware of), but their servers can be understandbly slow given that their service is free. This however can make streaming shows nigh unwatchably at times.

However, these tools are prone to abuse, further straining the already overloaded serves, and I'm also advertising techniques such as circumventing their DDOS protection. I therefore want to state that I appreciate the free service proxer.me is hosting and in no way encourage bad actors. Please be sensible when downloading.