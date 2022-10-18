# Discord Bot Base
### Description
This is Discord Bot base using [Python](https://github.com/python/cpython) and [Discord.PY library](https://github.com/Rapptz/discord.py).
It contains:
 - Cogs Autoloader
 - Ping (Client Latency) command
 - On Ready event
 - Auto change Discord Presence on ready
 - Help Command
 - Template of categories in help command

### Installation
Install Discord.py:

```
$  pip3 install discord.py
```

Install Asyncio:

```
$  pip3 install asyncio
```

### Using
Discord Bot base looks like this:
```
discord-bot-base/
    main.py              # Main File
    cogs/                # Cogs Directory
        ready.py         # On Ready cog
        help.py          # Help Command cog
        ping.py          # Latency Command cog
```

In **main.py** you need to:
 - Paste your [Discord Bot's token](https://discord.com/developers/applications).
 - Make your own bot's prefix (default is **!**).
Also, you can:
 - Paste your own code, like `connect bot to MongoDB`, `connect bot to Bot's Web-Dashboard` etc.

In **cogs/ready.py** you need to:
 - Remove or set your own Discord Presence (default is **Discord Bot by yer#7700**).

In **cogs/help.py** you need to:
 - Add your own categories or edit already added.
 - Add your commands.
