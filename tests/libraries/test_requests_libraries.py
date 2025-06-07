import requests
import json
from urllib.parse import urljoin

baseURI = "https://demoqa.com"
get_url = "https://demoqa.com/BookStore/v1/Books"
get_headers = {
    'accept':'application/json'
}
post_url = "/Account/v1/Authorized"
full_post_url = urljoin(baseURI, post_url)

post_body = {
  "userName": "string",
  "password": "string"
}

# response = requests.get(get_url, headers=get_headers)

response = requests.post(full_post_url, data=post_body)

print (response.status_code)
print (json.dumps(response.json(), indent=4))


# print (json.dumps(response.json(), indent=4))
# books_data = response.json()
# print (json.dumps(books_data['books'][0], indent=4))
# # for book in books_data['books']:
# #     if book['title'] == "You Don't Know JS":
# #         print (json.dumps(book, indent=4))
