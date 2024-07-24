import time
import logging
import pyrogram
import requests
from pyrogram import Client, filters
from pyrogram.errors import BadRequest
from pyrogram.raw.all import layer

from . import __version__, __version_code__
from .config import API_HASH, API_ID, TOKEN, log_chat

logger = logging.getLogger(__name__)

class PornHub(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()

        super().__init__(
            name=name,
            app_version=f"PornHub v{__version__}",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TOKEN,
            plugins=dict(root="pornhub.plugins"),
            in_memory=True,
        )

    async def start(self):
        await super().start()

        self.start_time = time.time()

        logger.info(
            "PornHub running with Pyrogram v%s (Layer %s) started on %s. Hello!",
            pyrogram.__version__,
            layer,
            self.me.username,
        )

        start_message = (
            "<b>PornHub started!</b>\n\n"
            f"<b>Version:</b> <code>v{__version__} ({__version_code__})</code>\n"
            f"<b>Pyrogram:</b> <code>v{pyrogram.__version__}</code>"
        )

        try:
            await self.send_message(chat_id=log_chat, text=start_message)
        except BadRequest:
            logger.warning("Unable to send message to log_chat!")

    async def stop(self):
        await super().stop()
        logger.warning("PornHub stopped, Bye!")

    async def download_video(self, video_url, output_path):
        try:
            response = requests.get(video_url, stream=True)
            if response.status_code == 200:
                with open(output_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                logger.info(f"Video downloaded successfully: {output_path}")
            else:
                logger.error(f"Failed to download video. Status code: {response.status_code}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")

    async def handle_message(self, message):
        # Extract the command and video URL from the message
        if message.text.startswith("/download"):
            video_url = message.text.split(" ", 1)[1]
            output_path = "path/to/save/video.mp4"  # Update this path as needed
            
            # Call the download function
            await self.download_video(video_url, output_path)
            
            # Notify the user
            await message.reply("Downloading video, please wait...")
