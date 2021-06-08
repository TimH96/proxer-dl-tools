This is a collection of lightweight command line scripts to directly download videos from the anime host [proxer.me](https://proxer.me/), using Python. Backup your favorite show with just one line.
```bash
$ python .\proxer-dl-series.py -i 8225 -l engsub -t Y0uR5oken=4lphNuM5tr -o H:\anime\Ping_Pong\ -e 1-11
```

### Note of Intent

I wrote these tools with the following purpose in mind:
+ Backing up potentially volatile data.
+ Watching anime on demand. Proxer hosts anime in excellent quality (better than any host I am aware of), but their servers can be understandbly slow given that their service is free. This however can make streaming shows nigh unwatchably at times.

However, these tools are prone to abuse, further straining the already overloaded serves, and I will also be advertising techniques such as circumventing their DDOS protection. I therefore want to state that I appreciate the free service proxer.me is hosting and in no way encourage bad actors. Please be sensible when downloading.

### Dependencies

These tools use the ``clint`` module to parse the download progress bar. It can be easily installed using ``pip``:

```bash
$ pip install clint
```

### Usage

#### Install

If you have Python 3.9^, you can just clone the repo and install it's dependencies. Alternatively, you can download the packaged exectuables from the releases page.

#### Getting your authentication cookie

#### Download a video

#### Download a series