import re
import spacy


nlp = spacy.load("en_core_web_sm")
nlp.max_length = 2000000# Load spaCy's language model
def find_company_name(soup):
    for tag in ['h1', 'h2', 'h3', 'h4', 'h5']:
        header = soup.find(tag)
        if header:
            return header.text.strip()

    title = soup.title
    if title:
        return title.text.strip()

    doc = nlp(soup.get_text())
    potential_names = [ent.text for ent in doc.ents if ent.label_ == 'ORG']
    if potential_names:
        return potential_names[0]

    print("Entities found:", doc.ents)
    return "Company Name Not Found"

def find_phone_number(soup):
    phone_regex = '|'.join([
        r'\+?\d[\d -]{8,12}\d',
        r'Tel: \(\d{3}\) \d{3}-\d{4}',
        r'\(\d{3}\) \d{3}-\d{4}',
        r'\d{3}-\d{3}-\d{4}',
        r'\d{3}.\d{3}.\d{4}',
        r'\d{3} \d{3} \d{4}'
    ])
    matches = re.findall(phone_regex, soup.get_text())
    if matches:
        phone_numbers = [re.sub(r'\D', '', match) for match in matches]
        return ", ".join(phone_numbers)
    else:
        return None


def find_emails(soup):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z]{2,}\b'

    email_anchors = soup.find_all('a', href=re.compile(r'^mailto:'))

    emails_from_anchors = [anchor['href'][7:] for anchor in email_anchors]

    text_content = soup.get_text()
    emails_from_text = re.findall(email_regex, text_content)

    all_emails = emails_from_anchors + emails_from_text

    if all_emails:
        return ", ".join(all_emails)
    else:
        return None

