# BlogDataAutomation
Python scripts for automating blog data management and content preparation. Created as part of my journey in Google's IT Automation with Python course. Ideal for bloggers and content creators looking to streamline their workflow.
# Scripts
# WP_XML_to_Clean_HTML.py
Purpose: Cleans HTML content from XML blog posts, making them easier to manage and read.
Usage: Run the script and provide the path to your XML file containing blog posts.

# Generate_JSON_Lines_Metadata.py
Purpose: Generates metadata for each HTML file, useful for tasks like training Large Language Models or SEO optimization.
Usage: Run the script in the directory containing your HTML files.
Note: Before running the script, make sure to replace the placeholders in the following lines with your actual information:
- gs://your-cloud-storage-bucket/{filename}: Replace with your actual Cloud Storage path.
- https://your-website.com/{filename}: Replace with the actual URL where this content can be found, if applicable.

# Acknowledgments
These scripts were generated with the assistance of ChatGPT, a large language model by OpenAI. The project serves as a practical application of what I've learned in the Google IT Automation with Python course.
