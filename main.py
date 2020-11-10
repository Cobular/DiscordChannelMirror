from discord.ext.commands.bot import Bot
from discord import Message, TextChannel, Webhook, AsyncWebhookAdapter
from os import getenv
import aiohttp

bot = Bot("m!")

quote_wall_id = 692999924349927514
webhook_url = getenv("WEBHOOK_URL")
bot_token = getenv("BOT_TOKEN")


@bot.event
async def on_ready():
    print("I'm awake now")


@bot.event
async def on_message(message: Message):
    async with aiohttp.ClientSession() as session:
        target_webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
        if message.channel.id == quote_wall_id:
            await target_webhook.send(message.content, username=message.author.display_name,
                                      avatar_url=message.author.avatar_url,
                                      files=[await file.to_file(spoiler=file.is_spoiler()) for file in
                                             message.attachments])


bot.run(bot_token)
