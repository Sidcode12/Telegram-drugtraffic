from telethon import TelegramClient

# Replace these with your own values from https://my.telegram.org
api_id = 25333298
api_hash = 'aca9a860499b58236bebe585ecf18caf'
phone = '+919545511731'   # your phone number with country code

# Start the client
client = TelegramClient('session', api_id, api_hash)

async def main():
    # Connect to Telegram
    await client.start(phone=phone)

    # Replace this with your group invite link or username
    group = await client.get_entity("https://t.me/+20kr1VpDj3BmMDU1")

    # Send the message
    await client.send_message(group, "Click me https://4c846ecd3429.ngrok-free.app")

    print("✅ Message sent successfully!")

with client:
    client.loop.run_until_complete(main())
