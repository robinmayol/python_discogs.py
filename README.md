`python_discogs.py` automagically fetches the biography of the artist you are currently listening to (if you use MPD). Originally coded to add to my `conky` setup.

# Requirements:

## Music Player Daemon
If you do not know MPD go read about it right now and install it. The package for your distribution should be called `mpd` and you will need its command line client `mpc`

## Python
`python3`

## Python Discogs API Client
`python_discogs` (install with pip:
`python3 -m pip install python_discogs`)

## A discogs API token key
Link to get one (you just need a Discogs account) and API Manual [here](https://python3-discogs-client.readthedocs.io/en/latest/authentication.html#user-token-authentication)

Copy and paste you token into the file `python_discogs.py` in place of yourusertokenhere.

```
#!/usr/bin/python
import discogs_client
import re
import json
import subprocess

d = discogs_client.Client('ExampleApplication/0.1', user_token="yourusertokenhere")
```

# Usage:
Play a song via mpd and execute:

`$ python3 python_discogs.py`