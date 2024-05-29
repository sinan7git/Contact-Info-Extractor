import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re
import spacy
from.helper import find_company_name,find_phone_number,find_emails

nlp = spacy.load("en_core_web_sm")
nlp.max_length = 2000000
def google_search(query):
    api_key = "{api_key}"
    search_engine_id = "{serch_engine_id}"
    base_url = "https://www.googleapis.com/customsearch/v1"

    query_params = {
        'q': query,
        'cx': search_engine_id,
        'key': api_key
    }

    response = requests.get(base_url, params=urlencode(query_params))

    if response.status_code == 200:
        return response.json()['items']
    else:
        return None


def extract_contact_info(website_url):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.content, 'html.parser')


    contact_link = None
    for link in soup.find_all('a', href=True):
        if re.search(r'contact', link.text, re.IGNORECASE):
            contact_link = link['href']
            break


    doc = nlp(soup.get_text())
    company_name = find_company_name(soup)
    phone_number = find_phone_number(soup)
    emails = find_emails(soup)

    return contact_link, emails, company_name , phone_number
