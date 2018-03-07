import discord
from discord.ext import commands
from discord.ext.commands import Bot
from cogs.utils import checks 

bot = commands.Bot(command_prefix='Prefix Here')
client = discord.Client()
client = discord.AutoShardedClient()

bot.remove_command("help")

@bot.event
async def on_ready():
	print("Hello, I am EveryBot!")
	print("Guilds: {}".format(len(bot.guilds)))
	print("Users: {}".format(sum([x.member_count for x in bot.guilds])))
	users = sum([x.member_count for x in bot.guilds])
	message = ('Hello | {} members'.format(sum([x.member_count for x in bot.guilds])))
	game = discord.Game(name=message, type=3)
	await bot.change_presence(game=game, status="dnd")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
	try:
		embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
		embed.add_field(name="Name", value=user.name, inline=True)
		embed.add_field(name="ID", value=user.id, inline=True)
		embed.add_field(name="Status", value=user.status, inline=True)
		embed.add_field(name="Highest role", value=user.top_role)
		embed.add_field(name="Joined", value=user.joined_at)
		embed.set_thumbnail(url=user.avatar_url)
		await ctx.send(embed=embed)
	except:
		error = discord.Embed(title=":exclamation: Error", description=" :warning: You need to mention the user you want this info for!", color=0xe51e1e)
		await ctx.send(embed=error)
"""
Moderation Commands
"""

@bot.command(pass_context=True)
@checks.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
	try:
		await ctx.send("*Slam!*.. Take that! {} has been banished from this realm! *Hahahaha..* :wave:".format(user.name))
		await ctx.guild.ban(user)
	except:
		embed = discord.Embed(title=":exclamation: Error", description=" :warning: I could not ban this user, I do not have the proper permissions! \n*(Move me visually above who you want to ban)*", color=0xe51e1e)
		await ctx.send(embed=embed)

@bot.command(pass_context=True)
@checks.has_permissions(kick_users=True)
async def kick(ctx, user: discord.Member):
	try:
		await ctx.send("*Wham!*... {} just got their ass kicked out! :wave:".format(user.name))
		await ctx.guild.kick(user)
	except:
		embed = discord.Embed(title=":exclamation: Error", description=" :warning: I could not kick this user, I do not have the proper permissions! \n*(Move me visually above who you want to kick)*", color=0xe51e1e)
		await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def unban(ctx, user: discord.Member):
	try:
		await ctx.send("*Poof!..* {} has been given another chance! Welcome back young one.. :squish1:".format(user.name))
		await ctx.guild.unban(user)
	except:
		embed = discord.Embed(title=":exclamation: Error", description=" :warning: I could not unban this user, I do not have the proper permissions! \n*(Move me visually above who you want to unban)*", color=0xe51e1e)
		await ctx.send(embed=embed)

bot.run("~~Token Here~~")