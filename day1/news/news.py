import urllib.request
import re

url = "https://www.farsnews.ir/"
fp = urllib.request.urlopen(url)
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

# print(mystr)


pattern = r"<h3 class=\"title\"[^>]*>(.*)</h3>"
groups = re.findall(pattern, mystr)
# print(groups)
with open("fars.html", "w") as fars_file:
    for group in groups:
        group = re.sub(r'href="','href="https://farsnews.ir', group)
        fars_file.write("<h3>" + group + "</h3>" + "\n")
