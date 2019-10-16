import os, requests, subprocess

   
# url = 'https://google.come/favicon.ico'
# r = requests.get(url, allow_redirects=True)
# open ('google.ico', 'wb').write(r.content)


req = requests.get()
text = req.text
img_url_list = []

text_list = text.split('img')

def locate_image(e):
    
    e = e.find('"')
    
    img_url = e.split('"')
    img_url = img_url[1]
    img_url_list.append(img_url)
    
for e in text_list:
    if 'src' in e:
        locate_image(e)

print(img_url_list)

for i in img_url_list:
    req = requests.get(f'GITHUB', stream=True)
    
    with open(i[:4])
    
