from discord import *
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

        # command_name: (description, syntax)
        self.commands = {
            'ping': ("Send client latency", '!ping')
        }

        # category: ' `command1 command2 command...` '
        self.categories = {
            'Fun   🪗':        ' `...` ',
            'Moderation   🪖': ' `...` ',
            'Utilities   🛠️':  ' `!ping ...` ',
            'Setup   🚀':      ' `...` '
        }

        self.fun_name       = 'fun'
        self.mod_name       = 'moderation'
        self.utilities_name = 'utilities'
        self.setup_name     = 'setup'

        self.default_help = f"""   This is Discord Base Bot!
Categories:
  -  Fun 🪗         (!help {self.fun_name})
  -  Moderation 🪖  (!help {self.mod_name})
  -  Utilities 🛠️   (!help {self.utilities_name})
  -  Setup 🚀       (!help {self.setup_name})

Thank you for using Discord Base by yer#7700!
"""

    @commands.command(name="help", alias=["commands", "info"])
    async def help(self, ctx, text=None):
        if not text == None:
            # If text is command
            if text in self.commands.keys():
                cmd_info = self.commands[text]

                embed = Embed(title = f'{text.capitalize()} command', colour = 0xf2525a)
                embed.add_field(name=text, value=cmd_info[0] + '\n Syntax: ' + cmd_info[1])
            else:
                # If text is category
                match text:
                    case self.fun_name:
                        ctg = list(self.categories.keys())[0]

                        embed = Embed(title = ctg, colour = 0xf2525a,
                            description = self.categories[ctg]
                        )
                    case self.mod_name:
                        ctg = list(self.categories.keys())[1]

                        embed = Embed(title = ctg, colour = 0xf2525a,
                            description = self.categories[ctg]
                        )
                    case self.utilities_name:
                        ctg = list(self.categories.keys())[2]

                        embed = Embed(title = ctg, colour = 0xf2525a,
                            description = self.categories[ctg]
                        )
                    case self.setup_name:
                        ctg = list(self.categories.keys())[3]

                        embed = Embed(title = ctg, colour = 0xf2525a,
                            description = self.categories[ctg]
                        )
                    case _:
                        embed = Embed(title = f'Discord Base Bot Help', colour = 0xf2525a,
                            description = f"Cannot recognize: {text}"
                        )
        else:
            embed = Embed(title = f'Discord Base Bot Help', colour = 0xf2525a,
                description = self.default_help
            )

        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar.url)
        await ctx.send(embed=embed)

# Setup cog...
async def setup(bot):
	await bot.add_cog( Help(bot) )