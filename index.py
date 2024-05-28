import asyncio
import pytmi

import os
print(os.environ)
print(os.environ.get('USERNAME'))

async def main() -> None:
    nick = os.environ.get('USERNAME')
    token = os.environ.get('TOKEN')
    channels = ["thabuttress"]

    async with pytmi.Client() as client:
        for channel in channels:
            await client.login_oauth(token, nick, channel)
            await client.join(channel)
            await client.send_message(f"HELLO {channel.upper()}!!")

if __name__ == "__main__":
    try:
        loop = asyncio.new_event_loop()
        loop.run_until_complete(main())
    except:
        print("Something went wrong.")