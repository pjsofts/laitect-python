import asyncio


async def say_hello():
    print("Hello")
    await asyncio.sleep(1) 
    
    data = await db.async_query()

    print("World!")


async def main():
    await say_hello()


# Run the coroutine
asyncio.run(main())
