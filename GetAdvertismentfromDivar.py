import signal
import sys
import asyncio
import aiohttp
import json

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)



async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()


async def get_adver_top(subreddit, client):
    while True:
        data1 = await get_json(client, 'https://api.divar.ir/v8/web-search/tehran/car?q='+ subreddit)
        print("get response")
        j = json.loads(data1.decode('utf-8'))
        for k, i in enumerate(j['widget_list']):
            if k <= 3:
                print(i['data']['title'])
        print('DONE:', subreddit + '\n')



def signal_handler(signal, frame):
    loop.stop()
    client.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

asyncio.ensure_future(get_adver_top('پراید', client))
asyncio.ensure_future(get_adver_top('206', client))
loop.run_forever()


