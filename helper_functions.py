# Coronavirus Developer API: GOV.UK
# https://coronavirus.data.gov.uk/details/developers-guide
# input: URL (can be with filtering), output: JSON format

from requests import get

def get_data(url):
    response = get(url, timeout=10)
    # any response >= 400: indicates error 
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()
