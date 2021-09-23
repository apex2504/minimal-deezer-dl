# example of saving a downloaded track to a file.

import asyncio
from deezer import Deezer


client = Deezer()


async def main(track_name):
    track_list = await client.search('track', track_name)

    to_get = track_list[0]
    bio = await client.download(to_get)

    filename = f'{to_get["ART_NAME"]} - {to_get["SNG_TITLE"]}'

    with open(f'{filename}.mp3', 'wb') as f:
        f.write(bio.getbuffer())

    await client.http.close()


asyncio.get_event_loop().run_until_complete(main('you are a pirate'))