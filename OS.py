import webbrowser

site = input()

if 'https://' in site:
    webbrowser.open(site)
    print("Browser opening...")

elif 'www.' in site:
    site = 'https://' + site
    webbrowser.open(site)
    print("Browser opening again...")

else:
    site = 'https://www.' + site
    webbrowser.open(site)
    print("Browser still opening...")