# Extract components from URLs
# Components: protocol, domain, path, query parameters
# Use regex groups

urls = [
    "https://www.example.com/path/page?id=123&name=test",
    "http://site.org/about",
    "https://shop.com/products?category=books&sort=price"
]

import re

def extract_urls(url):
    pattern = r"(?P<protocol>https?)://(?P<domain>[a-zA-Z0-9.-]+)(?P<path>/[a-zA-Z0-9/_-]*)?(\?(?P<query>.+))?"

    match = re.search(pattern, url)
    
    if match:
        print(f"{url}:")
        print(f"Protocol: {match.group('protocol')}")
        print(f"Domain: {match.group('domain')}")
        print(f"Path: {match.group('path')}")
        print(f"Query: {match.group('query')}\n")

for url in urls:
    extract_urls(url)