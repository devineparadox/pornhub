# run_bot.py
import asyncio
from PornHub.bot import PornHub

async def main():
    app = PornHub()
    await app.start()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
