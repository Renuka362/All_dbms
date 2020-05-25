#r = requests.get('https://xkcd.com//353')

#print(type(r))

#print(dir(r))

#print(help(r))


#r = requests.get('https://imgs.xkcd.com/comics/python.png')

#print(r.content)
 
#with open('comic.png','wb') as f:
 #   f.write(r.content)
 
#print(r.ok)

import requests

payload = {'username':'Renuka','password':'Renu'}

r = requests.post('https://httpbin.org/post',data=payload)

#print(r.text)

r_dict = r.json()

print(r_dict['form'])