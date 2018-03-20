import requests
graph_api_version = 'v2.12'

access_token = 'YOUR TOKEN'

user_id = '390581294464059'

post_id = '860235077498676'
# the graph API endpoint for comments on LHL's post
url = 'https://graph.facebook.com/{}/{}_{}/comments'.format(graph_api_version, user_id, post_id)
comments = []
r = requests.get(url, params={'access_token': access_token})
while True:
    data = r.json()
# catch errors returned by the Graph API
    if 'error' in data:
        raise Exception(data['error']['message'])
# append the text of each comment into the comments list
    for comment in data['data']:
        # remove line breaks in each comment
        text = comment['message'].replace('\n', ' ')
        comments.append(text)
    print('got {} comments'.format(len(data['data'])))
# check if there are more comments
    if 'paging' in data and 'next' in data['paging']:
        r = requests.get(data['paging']['next'])
    else:
        break
# save the comments to a file
with open('comments.txt', 'w', encoding='utf-8') as f:
    for comment in comments:
        f.write(comment + '\n')