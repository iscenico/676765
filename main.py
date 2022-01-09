import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
  print('{0.user} è on'.format(client))

@client.command()
async def clear(ctx, amount=2):
  await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send('{user.mention} è stato kickato correttamente')

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send('{user.mention} è stato bannato correttamente')

@client.command()
async def unban(ctx, *, member): 
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if {user.name, user.discriminator} == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'{user.mention} è stato sbannato correttamente')
      return

client.run('OTI4OTU1MDY2MzMxODQ4NzQ0.YdgS0g.K7v89Ku0evib3qcDtKisyVUr6kI')