url = https://github.com/{}

path = "user"

token = 

headers = { 
    authorization : "Bearer {}".format (token)
}

response = request.get(url.format(path), headers =headers)