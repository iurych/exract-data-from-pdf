import pdfplumber
import re

pdf_path = ".venv/lista.pdf"

def extract_data_from_page(page_text):
    """Extrai os dados de uma página usando expressões regulares."""
    pattern = r'(\d{10})\s+.*?\s+(\d+,\d+|faltou)'
    matches = re.findall(pattern, page_text)
    return [item for match in matches for item in match]

def extract_text_with_plumber(pdf_path):
    result_list = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                result_list.extend(extract_data_from_page(page_text))
    return result_list

pdf_text = extract_text_with_plumber(pdf_path)
print(len(pdf_text))