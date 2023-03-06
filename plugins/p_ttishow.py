from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT, MELCOW_NEW_USERS
from database.users_chats_db import db
from database.ia_filterdb import Media
from utils import get_size, temp, get_settings
from Script import script
from pyrogram.errors import ChatAdminRequired

"""-----------------------------------------https://t.me/GetTGLink/4179 --------------------------------------"""

@Client.on_message(filters.new_chat_members & filters.group)
async def save_group(bot, message):
    r_j_check = [u.id for u in message.new_chat_members]
    if temp.ME in r_j_check:
        if not await db.get_chat(message.chat.id):
            total=await bot.get_chat_members_count(message.chat.id)
            r_j = message.from_user.mention if message.from_user else "Anonymous" 
            await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, r_j))       
            await db.add_chat(message.chat.id, message.chat.title)
        if message.chat.id in temp.BANNED_CHATS:
            # Inspired from a boat of a banana tree
            buttons = [[
                InlineKeyboardButton('✨ Uᴘᴅᴀᴛᴇ 👩‍💻', url=f'https://t.me/{SUPPORT_CHAT}')
            ]]
            reply_markup=InlineKeyboardMarkup(buttons)
            k = await message.reply(
                text='<b>CHAT NOT ALLOWED 🐞\n\nGᴀʏᴀ,Tᴀᴛᴀ,Gᴏᴏᴅ Bʏᴇ :- Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪ</b>',
                reply_markup=reply_markup,
            )

            try:
                await k.pin()
            except:
                pass
            await bot.leave_chat(message.chat.id)
            return
        buttons = [[
            InlineKeyboardButton('🧩𝘚𝘜𝘗𝘗𝘖𝘙𝘛🧩', url='https://t.me/CinemaShopGroup'),
            InlineKeyboardButton('🛡𝘜𝘗𝘋𝘈𝘛𝘌𝘚🛡', url='https://t.me/CinemaShopLinkz')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=f"<b>💌 Aᴅᴅ PᴀɴɴᴀTʜᴜᴋᴜ Nᴀɴᴅʀɪ ♥️ {message.chat.title} ❣️\n\nIf you have any questions & doubts about using me contact support.</b>",
            reply_markup=reply_markup)
    else:
        settings = await get_settings(message.chat.id)
        if settings["welcome"]:
            for u in message.new_chat_members:
                if (temp.MELCOW).get('welcome') is not None:
                    try:
                        await (temp.MELCOW['welcome']).delete()
                    except:
                        pass
                temp.MELCOW['welcome'] = await message.reply(f"<b>Hey , {u.mention}, Welcome to {message.chat.title}</b>")


@Client.on_message(filters.command('leave') & filters.user(ADMINS))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('✨ Uᴘᴅᴀᴛᴇ 👩‍💻', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text='<b>Hᴇʟʟᴏ Fʀɪᴇɴᴅs, \nMʏ ᴀᴅᴍɪɴ ʜᴀs ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ɢʀᴏᴜᴘ sᴏ ɪ ɢᴏ! Iғ ʏᴏᴜ ᴡᴀɴɴᴀ ᴀᴅᴅ ᴍᴇ ᴀɢᴀɪɴ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.</b>',
            reply_markup=reply_markup,
        )

        await bot.leave_chat(chat)
        await message.reply(f"left the chat `{chat}`")
    except Exception as e:
        await message.reply(f'Error - {e}')

@Client.on_message(filters.command('disable') & filters.user(ADMINS))
async def disable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Cʜᴀᴛ Iᴅ Tʜᴀɴɢᴀ')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Cᴏʀʀᴇᴄᴛ Aɴᴀ Cʜᴀᴛ Iᴅ Kᴜᴅᴜɴɢᴀ')
    cha_t = await db.get_chat(int(chat_))
    if not cha_t:
        return await message.reply("Uɴɢᴀ Cʜᴀᴛ Nᴏᴛ Fᴏᴜɴᴅ Iɴ Mʏ Lᴏᴅɢᴇ")
    if cha_t['is_disabled']:
        return await message.reply(f"Iɴᴛʜᴀ Cʜᴀᴛ Aʟʀᴇᴀᴅʏ Dɪsᴀʙʟᴇᴅ:\nReason-<code> {cha_t['reason']} </code>")
    await db.disable_chat(int(chat_), reason)
    temp.BANNED_CHATS.append(int(chat_))
    await message.reply('🔱 SᴜᴄᴄᴇsFᴜʟʟʏ DɪsCᴏɴɴᴇᴄᴛᴇᴅ 🙄')
    try:
        buttons = [[
            InlineKeyboardButton('✨ Uᴘᴅᴀᴛᴇ 👩‍💻', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat_, 
            text=f'<b>Hᴇʟʟᴏ Fʀɪᴇɴs, \nMʏ ᴀᴅᴍɪɴ ʜᴀs ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ɢʀᴏᴜᴘ sᴏ ɪ ɢᴏ! Iғ ʏᴏᴜ ᴡᴀɴɴᴀ ᴀᴅᴅ ᴍᴇ ᴀɢᴀɪɴ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.</b> \nReason : <code>{reason}</code>',
            reply_markup=reply_markup)
        await bot.leave_chat(chat_)
    except Exception as e:
        await message.reply(f"Error - {e}")


@Client.on_message(filters.command('enable') & filters.user(ADMINS))
async def re_enable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Cʜᴀᴛ Iᴅ Sᴇɴᴅ Pᴀɴɴᴜɴɢᴀ')
    chat = message.command[1]
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Cᴏʀʀᴇᴄᴛ Aʜ Cʜᴀᴛ Iᴅ Kᴜᴅᴜɴɢᴀ')
    sts = await db.get_chat(int(chat))
    if not sts:
        return await message.reply("Cʜᴀᴛ Nᴏᴛ Fᴏᴜɴᴅ Iɴ Nʏ Lᴏᴅɢᴇ !")
    if not sts.get('is_disabled'):
        return await message.reply('Tɢɪs Cʜᴀᴛ Nᴏ Yᴇᴛ Dɪsᴀʙʟᴇ')
    await db.re_enable_chat(int(chat_))
    temp.BANNED_CHATS.remove(int(chat_))
    await message.reply("Cʜᴀᴛ Aʜ Rᴇ-Eɴᴀʙʟᴇ Pᴀɴɴɪʏᴀᴄʜɪ")


@Client.on_message(filters.command('stats') & filters.incoming)
async def get_ststs(bot, message):
    rju = await message.reply('Fetching stats..')
    total_users = await db.total_users_count()
    totl_chats = await db.total_chat_count()
    files = await Media.count_documents()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)
    await rju.edit(script.STATUS_TXT.format(files, total_users, totl_chats, size, free))


# a function for trespassing into others groups, Inspired by a Vazha
# Not to be used , But Just to showcase his vazhatharam.
# @Client.on_message(filters.command('invite') & filters.user(ADMINS))
async def gen_invite(bot, message):
    if len(message.command) == 1:
        return await message.reply('Cʜᴀᴛ Iᴅ Sᴇɴᴅ Pᴀɴɴᴜɴɢᴀ')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('Cᴏʀʀᴇᴄᴛ Aʜ Cʜᴀᴛ Iᴅ Kᴜᴅᴜɴɢᴀ')
    try:
        link = await bot.create_chat_invite_link(chat)
    except ChatAdminRequired:
        return await message.reply("Iɴᴠɪᴛᴇ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴇ Pᴀɴɴᴀ Aᴅᴍɪɴ Rɪɢʜᴛ Kᴜᴅᴜᴋᴀʟᴀ")
    except Exception as e:
        return await message.reply(f'Error {e}')
    await message.reply(f'Uɴɢᴀ Iɴᴠɪᴛᴇ Lɪɴᴋ Hᴇʀᴇ {link.invite_link}')

@Client.on_message(filters.command('ban') & filters.user(ADMINS))
async def ban_a_user(bot, message):
    # https://t.me/GetTGLink/4185
    if len(message.command) == 1:
        return await message.reply('Uɴɢᴀ Usᴇʀ ɪᴅ / Usᴇʀ Nᴀᴍᴇ Kᴜᴅᴜɴɢᴀ')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("Tʜɪs ɪs ᴀɴ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ, ᴍᴀᴋᴇ sᴜʀᴇ ɪᴀ ʜᴀᴠᴇ ᴍᴇᴛ ʜɪᴍ ʙᴇғᴏʀᴇ.")
    except IndexError:
        return await message.reply("Tʜɪs ᴍɪɢʜᴛ ʙᴇ ᴀ ᴄʜᴀɴɴᴇʟ, ᴍᴀᴋᴇ sᴜʀᴇ ɪᴛs ᴀ ᴜsᴇʀ.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if jar['is_banned']:
            return await message.reply(f"{k.mention} is already banned\nReason: {jar['ban_reason']}")
        await db.ban_user(k.id, reason)
        temp.BANNED_USERS.append(k.id)
        await message.reply(f"SᴜᴄᴄᴇsFᴜʟʟʏ Bᴀɴɴᴇᴅ 🙄 {k.mention}")


    
@Client.on_message(filters.command('unban') & filters.user(ADMINS))
async def unban_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('Uɴɢᴀ Usᴇʀ ɪᴅ / Usᴇʀ Nᴀᴍᴇ Kᴜᴅᴜɴɢᴀ')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("Tʜɪs ɪs ᴀɴ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ, ᴍᴀᴋᴇ sᴜʀᴇ ɪᴀ ʜᴀᴠᴇ ᴍᴇᴛ ʜɪᴍ ʙᴇғᴏʀᴇ.")
    except IndexError:
        return await message.reply("Tʜɪs ᴍɪɢʜᴛ ʙᴇ ᴀ ᴄʜᴀɴɴᴇʟ, ᴍᴀᴋᴇ sᴜʀᴇ ɪᴛs ᴀ ᴜsᴇʀ.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if not jar['is_banned']:
            return await message.reply(f"{k.mention} is not yet banned.")
        await db.remove_ban(k.id)
        temp.BANNED_USERS.remove(k.id)
        await message.reply(f"Successfully unbanned {k.mention}")


    
@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    # https://t.me/GetTGLink/4184
    raju = await message.reply('Getting List Of Users')
    users = await db.get_all_users()
    out = "Users Saved In DB Are:\n\n"
    async for user in users:
        out += f"<a href=tg://user?id={user['id']}>{user['name']}</a>"
        if user['ban_status']['is_banned']:
            out += '( Bᴀɴɴᴇᴅ Usᴇʀ )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="List Of Users")

@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def list_chats(bot, message):
    raju = await message.reply('Gᴇᴛᴛɪɴɢ Lɪsᴛ Oғ Cʜᴀᴛs')
    chats = await db.get_all_chats()
    out = "Chats Saved In DB Are:\n\n"
    async for chat in chats:
        out += f"**Title:** `{chat['title']}`\n**- ID:** `{chat['id']}`"
        if chat['chat_status']['is_disabled']:
            out += '( Dɪsᴀʙʟᴇ Cʜᴀᴛ )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="List Of Chats")
