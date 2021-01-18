#!/usr/bin/env python3
import requests
import webbrowser
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--sech", help="trap nsfw", action="store_true")
parser.add_argument("--url", help="daj urla", action="store_true")
args = parser.parse_args()

trapy = ['astolfo_(fate)','astolfo','','felix_argyle']

r = requests.get('https://cure.ninja/booru/api/json?q={}+trap&f={}&o=r&s=1'.format(random.choice(trapy), 'e' if args.sech else 's'))
url = r.json()['results'][0]['page']
if args.url:
    print(url)
else:
    webbrowser.open(url)