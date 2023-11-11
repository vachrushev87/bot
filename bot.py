from telethon import TelegramClient, events

api_id = 'тут личный_id'
api_hash = 'тут личный api_hash'
inputo = '-1001262043055'
outputo = '-1001938240953'
perisilaka = TelegramClient('spektrrnd', api_id, api_hash)
perisilaka.start()

@perisilaka.on(events.NewMessage(inputo))
async def main(event):
    await perisilaka.forward_messages(outputo, event.message)

perisilaka.run_until_disconnected()
