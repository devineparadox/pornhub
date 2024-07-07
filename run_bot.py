import asyncio
import logging
from PornHub.bot import PornHub

logging.basicConfig(level=logging.DEBUG)

async def main():
    try:
        logging.debug("Initializing PornHub bot...")
        app = PornHub()
        logging.debug("Starting PornHub bot...")
        await app.start()
        logging.debug("PornHub bot started successfully.")
        await asyncio.Event().wait()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
