from urllib import request, parse
import sys

myUrl = 'https://www.google.com/search?'
value = {'q': 'ANDESA Soft'}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

try:
    mydate = parse.urlencode(value)
    print(mydate)
    myUrl += mydate
    req = request.Request(myUrl, headers=myheader)
    answer = request.urlopen(req)
    answer = answer.readlines()
    for line in answer:
        print(line)
except Exception:
    print('Error occcured during web request!')
    print(sys.exc_info()[1])


myUrl2 = 'http://adv400.tripod.com/kartinka.jpg'
myFile = '/home/yauhen/Downloads/myimage.jpg'

try:
    print('Start downloading file from: ' + myUrl2)
    request.urlretrieve(myUrl2, myFile)
except Exception:
    print('Warning!!!')
    print(sys.exc_info())
    exit

print('File Downloaded and save at: ' + myFile)
