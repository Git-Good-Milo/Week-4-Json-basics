import requests


# GET is a server request that sends
    # headers, paths and argumetns
    # Headers are meta data slighty hidden - things like screen soze, device info and other
    # path is the the url section that determines where to send info - location on the internet
    # arguments are the information you send (as in headers)

headers = ''
path = 'http://api.postcodes.io/postcodes/'
arguments = 'N169LN'


post_code_req = requests.get(path + arguments)

print(post_code_req)
print(post_code_req.status_code)
print(post_code_req.headers)
print(type(post_code_req.content))
print(type(post_code_req.json()))

dict_of_req = post_code_req.json() # --> then you ca use it

