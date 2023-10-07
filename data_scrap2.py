import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def retrieve_name(url, position, count):
    while count > 0:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")

        # Retrieve all of the anchor tags
        tags = soup("a")

        url = tags[position - 1].get("href", None)  # New URL to navigate to
        count -= 1

    return tags[position - 1].string




# For actual problem
url_actual = "http://py4e-data.dr-chuck.net/known_by_Abigail.html"
position_actual = 18
count_actual = 7
print(
    "Last name in the actual sequence:",
    retrieve_name(url_actual, position_actual, count_actual),
)
