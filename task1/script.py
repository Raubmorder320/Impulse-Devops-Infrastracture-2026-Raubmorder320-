import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def make_request(status_code):
    url = f'https://httpbin.org/status/{status_code}'
    logging.info(f'Making request to {url}')
    try:
        response = requests.get(url, allow_redirects=False)
        code = response.status_code
        body = response.text        
        if code < 400:
            logging.info(f'Request Successful - Status Code: {code}')
            logging.info(f'Response Body: {body}')
        else:
            logging.error(f'Request Failed - Status Code: {code}')
            raise requests.exceptions.HTTPError(f'Exception: Status Code {code}')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
if __name__ == "__main__":
    status_codes = [200, 201, 301,404, 500]
    for code in status_codes:
        make_request(code)
        print('-'*30)