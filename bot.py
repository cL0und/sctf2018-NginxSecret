import requests
from time import sleep
from bs4 import BeautifulSoup


headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0","Connection":"close","Accept-Language":"ja","Accept-Encoding":"gzip, deflate"}
cookies = {"session":".eJwljzsOAjEMBe-SmiJO4tjhMivHH4GQQNqFCnF3gihfMaN577TF7sclnZ_7y09pu1o6J9PqPp0wGNRx1mqNByMJ5U6hIIDDOgxVUudC7HPCZA6oLqTgMsrogUVqLzKtNuwqsgwuPMkKRunmNRoqIdZRgIiMeiMn4nRKeuyxPR83v68ezzm3TMuWPUCtNDLWtTkwN89g49cki3sdvv9PQPp8AQzXPzM.Dd_t9A.m1VV1-C08aoYeiaeKDgcSdmtAck"}

print(cookies)
while 1:
	rp = requests.get("http://116.62.137.155:4455/88e6955d09f5ab8e75a96706507b04a5", headers=headers, cookies=cookies)
	soup = BeautifulSoup(rp.content, 'html.parser')
	lists = soup.find_all(class_='post-url')
	try:
		for url in lists:
			url = url.text
			print(url)
			if url.startswith('http://116.62.137.155:4455/'):
				rp = requests.get(url=url, headers=headers, cookies=cookies, timeout=5)
				print(len(rp.text))
			else:
				requests.get(url=url, timeout=3)
	except Exception as e:
		print(e)
	sleep(1)
