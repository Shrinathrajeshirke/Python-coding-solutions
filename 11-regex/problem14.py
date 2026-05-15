# Write a function that parses URLs and extracts their components.

# Given this text:

# Write a function parse_urls(urls) that returns a list of 
# dictionaries for valid URLs only, each containing:
# - "protocol": the protocol (https, http, ftp)
# - "domain": the domain (e.g. www.example.com)
# - "path": the path (e.g. /path/to/page) or "" if none
# - "query": the query string (e.g. name=john&age=25) or "" if none

urls = [
    "https://www.example.com/path/to/page?name=john&age=25",
    "http://blog.site.org/articles/python-regex",
    "https://shop.store.net/products?id=123&category=electronics",
    "ftp://files.server.com/downloads",
    "invalid-url",
    "https://simple.com"
]

import re

def url_parser(urls):
    pattern = r"(?P<protocol>ftp|https?)://(?P<domain>[a-zA-Z0-9.-]+)(?P<path>/[a-zA-Z0-9/_-]*)?(\?(?P<query>.+))?"

    parsed_urls = []

    for url in urls:
        match = re.search(pattern, url)
        if match:
            protocol = match.group('protocol')
            domain = match.group('domain')
            path = match.group('path')
            path = "" if path==None else path
            query = match.group('query')
            query = "" if query==None else query
            parsed_urls.append({"protocol":protocol, "domain": domain, "path": path, "query": query})
    
    return parsed_urls

print(url_parser(urls))
