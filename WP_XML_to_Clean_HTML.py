#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def clean_html(html_content):
    # Initialize BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove script and style tags
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
        
    # Get text
    text = soup.get_text()
    
    # Break into lines and remove leading and trailing spaces
    lines = (line.strip() for line in text.splitlines())
    
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    
    # Remove blank lines
    clean_text = '\n'.join(chunk for chunk in chunks if chunk)
    
    return clean_text

# Parse the XML file
tree = ET.parse('blog_post.xml')
root = tree.getroot()

# Namespace for 'content' (replace with the actual namespace in your XML if different)
namespaces = {'content': 'http://purl.org/rss/1.0/modules/content/'}

# Loop through each post and extract HTML content
for item in root.findall(".//item"):
    post_title = item.find("title").text
    post_content = item.find("content:encoded", namespaces=namespaces).text
    
    # Clean the HTML content
    clean_content = clean_html(post_content)
    
    # Sanitize post_title to create a valid filename
    sanitized_title = post_title.replace(" ", "_").replace("/", "-").replace("(", "").replace(")", "")
    
    # Create an HTML file for each post
    with open(f"{sanitized_title}.html", "w", encoding="utf-8") as f:
        f.write(clean_content)
