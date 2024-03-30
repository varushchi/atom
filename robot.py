import asyncio
async def robot(startpoint):
        i = startpoint
        while True:
            print(i)
            i += 1
            await asyncio.sleep(1)