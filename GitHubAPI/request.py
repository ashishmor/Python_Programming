import requests

url =  "https://github.com/{}"

path = "user"

token = 

headers = { 
    "authorization : Bearer {}".format (token)
}

response = requests.get(url.format(path), headers =headers)

print(response.text)