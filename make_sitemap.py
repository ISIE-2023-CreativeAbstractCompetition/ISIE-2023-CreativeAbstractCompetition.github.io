import os
import datetime
import xml.etree.ElementTree as ET

# Set the base URL of your website
base_url = "https://isie-2023-creativeabstractcompetition.github.io/"

# Set the directory to crawl for URLs
directory = os.getcwd()

# Set the output file name for the sitemap
output_file = "sitemap.xml"

# Set the date format for the last modified date
date_format = "%Y-%m-%d"

# Create the root element of the sitemap
root = ET.Element("urlset")
root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

# Loop through the files in the directory and add URLs to the sitemap
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        # Only include HTML files in the sitemap
        if filename.endswith(".html"):
            # Get the full path of the file
            file_path = os.path.join(dirpath, filename)
            # Get the last modified date of the file
            last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime(date_format)
            # Create the URL element and add it to the sitemap
            url = ET.SubElement(root, "url")
            loc = ET.SubElement(url, "loc")
            loc.text = base_url + os.path.relpath(file_path, directory)
            lastmod = ET.SubElement(url, "lastmod")
            lastmod.text = last_modified
            priority = ET.SubElement(url, "priority")
            # Set the priority based on the directory depth
            priority.text = str(1.0 - float(os.path.relpath(file_path, directory).count(os.sep)) * 0.1)

# Write the sitemap to a file
tree = ET.ElementTree(root)
tree.write(output_file, encoding="UTF-8", xml_declaration=True)