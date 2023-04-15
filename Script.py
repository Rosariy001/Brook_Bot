class script(object):
    START_TXT = """𝘏𝘦𝘭𝘭𝘰 {},
𝘔𝘺 𝘕𝘢𝘮𝘦 𝘐𝘴 <a href=https://t.me/{}>{}</a>, 𝘗𝘳𝘰𝘷𝘪𝘥𝘦 𝘔𝘰𝘷𝘪𝘦𝘴, 𝘑𝘶𝘴𝘵 𝘈𝘥𝘥 𝘔𝘦 𝘛𝘰 𝘠𝘰𝘶𝘳 𝘎𝘳𝘰𝘶𝘱 𝘈𝘯𝘥 𝘌𝘯𝘫𝘰𝘺 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """🤖 ᴍʏ ɴᴀᴍᴇ : {}
👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/MalluBlasters>Mr KD</a>
📝 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏʀᴏɢʀᴀᴍ
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3
📡 ʜᴏsᴛᴇᴅ ᴏɴ : 𝘏𝘦𝘳𝘰𝘬𝘶
𝘋𝘢𝘵𝘢𝘣𝘢𝘴𝘦 : 𝘔𝘰𝘯𝘨𝘰𝘋𝘉
🌟 ᴠᴇʀsɪᴏɴ : ᴠ 13.0 [ ʙᴇᴛᴀ ]
𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘎𝘳𝘰𝘶𝘱 :<a href=https://t.me/CinemaShopGroup>𝘊𝘭𝘪𝘤𝘬 𝘏𝘦𝘳𝘦</a>"""
    SOURCE_TXT = """<b>ѕeттιngѕ
~ sᴇᴛᴛɪɴɢs ɪs ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ғᴇᴀᴛᴜʀᴇs ɪɴ ᴛʜɪs ʙᴏᴛ.
~ ʏᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

noтe
1. ᴏɴʟʏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴄʜᴀɴɢᴇs sᴇᴛᴛɪɴɢs.
2. ɪᴛ ᴡᴏʀᴋs ᴏɴʟʏ ᴡʜᴇɴ ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

coммand and υѕeѕ
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. AwesomeFilter should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- AwesomeFilter Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. AwesomeFilter supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/TechMagazineYT)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

   OWNER_TXT = """<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟</b>
    
<b>• ꜰᴜʟʟ ɴᴀᴍᴇ : 𒆜ᴍʀ ᴋᴅ [ᴏғғɪᴄɪᴀɪʟ] 🇮🇳</b>
<b>• ᴜꜱᴇʀɴᴀᴍᴇ : @MalluBlasters</b>
<b>• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href=https://t.me/MalluBlasters>ᴄʟɪᴄᴋ ʜᴇʀᴇ</b></a>"""
