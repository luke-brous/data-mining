import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# The course schedule URL
base_url = "https://scarl.sewanee.edu/CS428/schedule.html"
output_dir = "CS428"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

print(f"Fetching course page: {base_url}")
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all links
links = soup.find_all("a")

for link in links:
    href = link.get("href")
    if not href:
        continue

    # Filter: We only want relative links to course materials
    # This targets the folders visible on the site: Lecture, Homework, Labs, Resources
    # It also grabs loose files like .tgz (code) or .pdf
    if any(marker in href for marker in ["Lecture/", "Homework/", "Labs/", "Resources/", ".pdf", ".tgz", ".c"]):
        
        # Construct full URL (handles relative links automatically)
        file_url = urljoin(base_url, href)
        
        # Keep the filename clean
        filename = os.path.basename(href)
        save_path = os.path.join(output_dir, filename)

        # Skip external links (like Wikipedia or other universities)
        if "sewanee.edu" not in file_url and "Lecture" not in href: 
            continue

        print(f"Downloading {filename}...")
        
        try:
            file_resp = requests.get(file_url)
            with open(save_path, 'wb') as f:
                f.write(file_resp.content)
        except Exception as e:
            print(f"Failed to download {file_url}: {e}")

print("Download complete!")