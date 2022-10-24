#!/usr/bin/python
import discogs_client
import re
import json
import subprocess

d = discogs_client.Client('ExampleApplication/0.1', user_token="yourusertokenhere")

poo = subprocess.run(['mpc'], stdout=subprocess.PIPE)
poo = poo.stdout.decode('utf-8')
poo = re.sub(r'(?is) - .+', '', poo)
results = d.search(poo, type='artist')
artist = results[0]
clean = artist.profile.replace('[a=', '')
clean = clean.replace(']', '')
clean = re.sub(r'(?is)[\r\n]+', '', clean)

print(clean)