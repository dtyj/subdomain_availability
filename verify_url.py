import sys
import requests
import re
from requests.exceptions import ConnectionError

print "Subdomain Availability Tool"
print "Author: Dennis T"
print "https://github.com/dtyj/subdomain_availability"
print ""

output_stream = sys.stdout
py_regex = "(http|https)://[\w\-]+(\.[\w\-]+)+\S*"
prepend_list = ["https://", "http://"]
total_line = 0
current_line = 0

if len(sys.argv) > 1:
    file_input = str(sys.argv[1])
    for count in open(file_input, "r"):
        total_line += 1
    for url in open(file_input, "r"):
        current_line += 1
        output_stream.write('Working on Line %s of %s..\r' % (current_line, total_line))
        output_stream.flush()
        if re.match(py_regex, url) is None:
            for list in prepend_list:
                prepend_url = list + url
                prepend_url = prepend_url.rstrip('\n')
                try:
                    r = requests.get(prepend_url)
                    if r.status_code == 200:
                        print prepend_url
                except ConnectionError as e:
                    pass
    output_stream.write('\n')
else:
    print "Example: python verify_url http://www.google.com"
