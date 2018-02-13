# Website Downloader

import requests # uses requests library as urllib isn't as fast
import sys

URL = sys.argv[1]
FILE = sys.argv[2]

result = requests.get(URL).text

open(FILE, 'w').write(result)
print(URL + " content saved to: " + FILE)