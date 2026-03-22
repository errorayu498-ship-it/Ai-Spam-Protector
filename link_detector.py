import re
from config import CONFIG

url_pattern = r'https?://\S+'

def extract_links(text):
    return re.findall(url_pattern, text)

def is_allowed(link):

    for site in CONFIG["allowed_socials"]:
        if site in link:
            return True

    return False
