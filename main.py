from requests_html import HTMLSession

s= HTMLSession()


'''f string lets us put what ever is in query into variable'''


query = 'London'
url = f'https://www.google.com/search?q=weather+liverpool{query}'




r = s.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'})


print (r.html.find('title'))