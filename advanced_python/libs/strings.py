"""
libs.strings

By default, uses `en-gb.json` file inside the `strings` top-level folder.

If language changes, set `libs.strings.default_locale` and run `libs.strings.refresh()`.
"""
import json

default_locale = "en-gb"
cached_strings = {}


def refresh():
    print("Refreshing...")
    global cached_strings
    with open(f"strings/{default_locale}.json") as f: #loads the traslations texxt from the strigs library
        cached_strings = json.load(f) # loads it as a json that is saved to cached strings


def gettext(name):
    return cached_strings[name]


#when python imports a file it runs this function

def set_default_locale(locale):
    global  default_locale
    default_locale = locale
refresh()
