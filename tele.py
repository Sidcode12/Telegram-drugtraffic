# from telethon import TelegramClient
# from telethon.tl.functions.messages import ImportChatInviteRequest
# import asyncio

# # Replace with your own values from https://my.telegram.org
# api_id = 25333298
# api_hash = 'aca9a860499b58236bebe585ecf18caf'
# phone = '+919545511731'  # <-- your full phone number with country code

# # Create the client (session file will be saved as 'session_name.session')
# client = TelegramClient('session_name', api_id, api_hash)

# async def main():
#     # Invite link: https://t.me/+20kr1VpDj3BmMDU1
#     invite_hash = "20kr1VpDj3BmMDU1"   # <-- no "+" here
    
#     # Join the group
#     await client(ImportChatInviteRequest(invite_hash))
#     print("✅ Successfully joined the private group!")

# async def runner():
#     # Ensures login (asks for code on first run)
#     await client.start(phone)
#     await main()

# # Run
# asyncio.run(runner())
# from telethon import TelegramClient
# import asyncio

# # Your credentials
# api_id = 25333298
# api_hash = 'aca9a860499b58236bebe585ecf18caf'
# phone = '+919545511731'  # your Telegram phone number

# # Create client (session will be reused if already logged in)
# client = TelegramClient('session_name', api_id, api_hash)

# async def main():
#     # Use the group link (since you’re already a member)
#     group = "https://t.me/+20kr1VpDj3BmMDU1"

#     print("📥 Extracting messages...")

#     # Save all text messages to a file
#     count = 0
#     with open("group_messages.txt", "w", encoding="utf-8") as f:
#         async for message in client.iter_messages(group, limit=None):
#             if message.text:  # only plaintext messages
#                 f.write(message.text.replace("\n", " ") + "\n")
#                 count += 1

#     print(f"✅ Extracted {count} text messages")
#     print("💾 Saved to group_messages.txt")

# async def runner():
#     await client.start(phone)  # login if first time
#     await main()

# # Run
# asyncio.run(runner())
from telethon import TelegramClient
import asyncio
import os

# Your credentials
api_id = 25333298
api_hash = 'aca9a860499b58236bebe585ecf18caf'
phone = '+919545511731'

# Create client
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    group = "https://t.me/+20kr1VpDj3BmMDU1"

    # Create folders for saving media
    os.makedirs("downloads/images", exist_ok=True)
    os.makedirs("downloads/videos", exist_ok=True)
    os.makedirs("downloads/audios", exist_ok=True)
    os.makedirs("downloads/documents", exist_ok=True)

    print("📥 Extracting messages and media...")

    text_count, media_count = 0, 0
    with open("group_messages.txt", "w", encoding="utf-8") as f:
        async for message in client.iter_messages(group, limit=None):
            # --- Save text messages ---
            if message.text:
                f.write(message.text.replace("\n", " ") + "\n")
                text_count += 1

            # --- Save media (images, videos, audio, docs) ---
            if message.media:
                file = await message.download_media(file="downloads/")
                if file:
                    media_count += 1
                    print(f"📂 Downloaded: {file}")

    print(f"\n✅ Saved {text_count} text messages")
    print(f"✅ Downloaded {media_count} media files into 'downloads/'")

async def runner():
    await client.start(phone)
    await main()

asyncio.run(runner())
