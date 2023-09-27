#!/usr/bin/env python3
import json
import os
import hashlib

# Function to generate a hashed ID
def generate_id(title):
    hashed = hashlib.sha256(title.encode()).hexdigest()
    return hashed[:63]

# Initialize an empty list to store metadata
metadata_list = []

# Loop through each HTML file in the directory
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        # Create metadata for each HTML file
        metadata = {
            "id": generate_id(filename),  # Unique identifier, using hashed filename
            "content": {
                "mimeType": "text/html",
                "uri": f"gs://your-cloud-storage-bucket/{filename}"  # Replace with your actual Cloud Storage path
            },
            "jsonData": json.dumps({
                "title": filename.split('.')[0].replace('_', ' '),  # Convert underscores back to spaces for the title
                "url": f"https://your-website.com/{filename}"  # Replace with the actual URL where this content can be found, if applicable
            })
        }
        
        # Append metadata to list
        metadata_list.append(metadata)

# Write metadata to a JSON Lines file
with open('metadata.jsonl', 'w') as f:
    for entry in metadata_list:
        f.write(json.dumps(entry) + '\n')
