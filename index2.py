# Import necessary libraries
import urllib.request
import xml.etree.ElementTree as ET

# Prompt the user to enter a URL and store it in the variable 'url'
url = input("Enter URL: ")

# Use urllib to fetch the XML data from the specified URL
response = urllib.request.urlopen(url)
xml_data = response.read().decode()

# Print out the number of characters retrieved from the URL
print(f"Retrieved {len(xml_data)} characters")

# Parse the fetched XML data using ElementTree
tree = ET.fromstring(xml_data)

# Search and find all the 'count' elements in the parsed XML tree
counts = tree.findall(".//count")

# Calculate the total sum of all numbers inside the 'count' elements
total_sum = sum(int(count.text) for count in counts)

# Calculate the number of 'count' elements found
comment_count = len(counts)

# Display the number of 'count' elements and their total sum
print(f"Count: {comment_count}")
print(f"Sum: {total_sum}")
