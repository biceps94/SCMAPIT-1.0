#------- Project: MAPIT.PY with webbrowser Module-------#

#! python3
# scmapit.py

import webbrowser, sys,pyperclip


if len(sys.argv)>1:
    # Get address from command line.
    address = ''.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' +address)
# webbrowser.open('https://www.google.com/search?sxsrf=ALeKk004iaY40_0cb-S_J0qwCsJ6LNtfvg%3A1588895008932&source=hp&ei=IJ20Xr-oNomLlwSSn7_wBA&q=' +address)

