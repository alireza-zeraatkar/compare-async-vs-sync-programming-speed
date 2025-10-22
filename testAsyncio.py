import asyncio, aiohttp, requests, time

url1 = 'https://google.com'
url2 = 'https://github.com'

async def req(url):
	print(f'Sending Request To {url}')
	async with aiohttp.ClientSession() as session:
		await session.get(url)
	print(f'Request Sent to {url}')
	
async def main():
	now = time.time()
	tasks = [req(url1), req(url2)]
	await asyncio.gather(*tasks)
	print(f'All Reqests Done in {str(time.time() - now)} Seconds For Asynciooo!')
	
asyncio.run(main())
print('\nTrync Sync Requests..')
now1 = time.time()
requests.get(url1)
requests.get(url2)
now2 = time.time()
print(f'Sync Requests Sent in {str(now2-now1)} Seconds')
