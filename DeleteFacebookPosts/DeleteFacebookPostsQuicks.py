"""
Delete Many Facebook Posts At The Same Time
"""
import requests
import pprint
import sys

payload = {
            'until': 1443200285, # Unix Timestamps
            'since': 1443200285, # Unix Timestamps
            'limit': 100, # Number Of Posts
            'access_token': '', # Your Access Token
        }

base_api = 'https://graph.facebook.com'
posts_endpoint = base_api + '/me/posts/'

posts_response = requests.get(posts_endpoint, params=payload)

if posts_response.status_code != requests.codes.ok:
    print('Error: ' + posts_response.json()['error']['message'])
    sys.exit(0)

posts_dict = posts_response.json()['data']

print("Total Posts To Delete: %d" % len(posts_dict))
for post in posts_dict:
    print("Deleting [%s] %s" % (post['id'], post['name']))
    requests.delete(base_api + '/' + post['id'], params=payload)
    print("Deleted [%s] %s\n" % (post['id'], post['name']))