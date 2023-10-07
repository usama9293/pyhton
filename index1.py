import urllib.request, urllib.error
import xml.etree.ElementTree as ET


def extract_data_from_url(url):
    # Use urllib to fetch the content of the URL
    response = urllib.request.urlopen(url)
    data = response.read().decode()
    return data


def compute_sum_from_xml(data):
    # Parse the XML data
    tree = ET.fromstring(data)

    # Find all 'count' elements
    counts = tree.findall(".//count")

    # Extract the numbers and compute their sum
    total = sum(int(count.text) for count in counts)
    return total, len(counts)


def main():
    url = input("Enter URL: ")
    xml_data = extract_data_from_url(url)

    # Display the number of characters retrieved
    print(f"Retrieved {len(xml_data)} characters")

    total_sum, comment_count = compute_sum_from_xml(xml_data)

    # Display the count of 'comment' entries and their sum
    print(f"Count: {comment_count}")
    print(f"Sum: {total_sum}")


if __name__ == "__main__":
    main()
