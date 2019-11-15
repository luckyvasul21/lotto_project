# importing the requests library
import requests

# api-endpoint
URL = "http://52.17.102.78:43619/api/npi"

# location given here
request_npi_number = "1083671887"

# defining a params dict for the parameters to be sent to the API
PARAMS = {"number":request_npi_number}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
print(r.encoding, r.status_code)
print(r.headers)

# extracting data in json format
data = r.json()

response_npi_number = data["results"][0]["number"]

assert r.status_code == 200
assert r.encoding == 'UTF-8'
assert response_npi_number == response_npi_number