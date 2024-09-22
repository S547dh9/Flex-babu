   from telegram import Update
   from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

   # Replace 'YOUR_TOKEN' with your actual bot token
   TOKEN = 'YOUR_TOKEN'
   # Replace 'YOUR_CHANNEL_ID' with your actual channel ID
   CHANNEL_ID = 'YOUR_CHANNEL_ID'

   def start(update: Update, context: CallbackContext) -> None:
       update.message.reply_text('Bot is online!')

   def log_added(update: Update, context: CallbackContext) -> None:
       if update.message.chat.type in [update.message.chat.GROUP, update.message.chat.SUPERGROUP]:
           chat = update.message.chat
           added_by = update.message.from_user
           members_count = chat.get_members_count()  # Note: Not always available
           log_message = (
               "🏠 Added To New Group\n\n"
               f"🆔 Group ID: {chat.id}\n"
               f"📛 Group Name: {chat.title}\n"
               f"✳ Group Username: {chat.username or 'N/A'}\n"
               f"👤 Added By: {added_by.full_name}\n"
               f"🔗 Username: @{added_by.username or 'N/A'}\n"
               f"📊 Members Count: {members_count}\n"
           )
           context.bot.send_message(chat_id=CHANNEL_ID, text=log_message)
           print(log_message)

   def log_left(update: Update, context: CallbackContext) -> None:
       if update.message.chat.type in [update.message.chat.GROUP, update.message.chat.SUPERGROUP]:
           chat = update.message.chat
           left_by = update.message.from_user
           log_message = (
               "👋 Left Group\n\n"
               f"🆔 Group ID: {chat.id}\n"
               f"📛 Group Name: {chat.title}\n"
               f"✳ Group Username: {chat.username or 'N/A'}\n"
               f"👤 Left By: {left_by.full_name}\n"
               f"🔗 Username: @{left_by.username or 'N/A'}\n"
           )
           context.bot.send_message(chat_id=CHANNEL_ID, text=log_message)
           print(log_message)

   def main() -> None:
       updater = Updater(TOKEN)

       dp = updater.dispatcher

       dp.add_handler(CommandHandler("start", start))
       dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, log_added))
       dp.add_handler(MessageHandler(Filters.status_update.left_chat_member, log_left))

       updater.start_polling()
       updater.idle()

   if __name__ == '__main__':
       main()
   
