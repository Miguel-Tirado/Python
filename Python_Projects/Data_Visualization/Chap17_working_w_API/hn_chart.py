import requests

from plotly.graph_objs import bar
from plotly import offline
from operator import itemgetter

# Make an API call and store the responce.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
post_comments, post_links, labels = [], [], []
for submission_id in submission_ids[:40]:
    # Make a seperate API call for each submission 
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    responce_dict = r.json()

    post_name = responce_dict['title']
    post_url = responce_dict['url']
    post_link = f"<a href='{post_url}'>{post_name}</a>"
    post_links.append(post_link)

    try:
        post_comment = responce_dict['descendants']
    except KeyError:
        continue
    else:
        post_comments.append(post_comment)
        madeby = responce_dict['by']
        label = f"{madeby}"
        labels.append(label)

# Make Visualization.
data = [{
    'type' : 'bar',
    'x' : post_links,
    'y' : post_comments,
    'hovertext' : labels,
    'marker' : {
        'color' : 'rgb(60, 100, 150)',
        'line' : {'width' : 1.5, 'color' : 'rgb(25,25,25)'}
    },
    'opacity' : 0.6,
}]

my_layout = {
    'title' : 'Most-Discussed Post on Hackernews',
    'xaxis' : {
        'title' : 'Posts',
        'titlefont' : {'size' : 24},
        'tickfont' : {'size' : 14},
    },
    'yaxis' : {
        'title' : 'Comments',
        'titlefont' : {'size' : 24},
        'tickfont' : {'size' : 14},
    },
}

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='hn_posts.html')


        
        


