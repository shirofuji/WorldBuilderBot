import discord
import asyncio
import argparse
import uuid
import random
from discord.ext import commands
import d20
from lib import db_func

default_prefixes = '$'

intents = discord.Intents.default()
intents.members = True
intents.presences = True

print(intents)

async def determine_prefix(bot, message):
	guild = message.guild

	if guild:
		return db_func.get_guild_prefix(message.guild)
	else:
		return default_prefixes

async def send_embed_as_author(ctx, title, description, fields=[], color=""):
	if (len(color.strip()) == 0):
		color = discord.Color.blue()
	embed = discord.Embed(title=title, description=description, color=ctx.author.color)
	embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
	for field in fields:
		embed.add_field(name=field[0], value=field[1], inline=field[2])
	await ctx.send(embed=embed)

def r(dice):
    print("DEBUG ROLL")
    print(dice)
    maximum = int(dice.lower().replace('d',''))
    result = random.randint(1, maximum)

    print(maximum)
    print(result)
    return result

bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send('```\nError: Command not found!\n```')
	else:
		raise error
		await ctx.send('```python\n' + str(error) + '\n```')

@bot.command(aliases=['Prefix','PREFIX'])
@commands.guild_only()
async def prefix(ctx, prefixes=""):
	current_prefix = db_func.get_guild_prefix(ctx.guild)
	prefix = prefixes.split() or default_prefixes
	if current_prefix == None:
		db_func.add_guild_prefix(ctx.guild, ''.join(prefix))
	else:
		db_func.update_guild_prefix(ctx.guild, ''.join(prefix))
	print("Prefix Command: " + str(ctx.guild.id) + " -> " + str(prefix))
	await send_embed_as_author(ctx,"WorldBuilderBot Prefix Updated","You should now use **" + ''.join(prefix) + "** as prefix for commands")

@prefix.error
async def prefix_error(ctx, error):
	print(error)
	message = '```python\n' + error.__traceback__ + '\n```'
	dm = await ctx.author.create_dm()
	await dm.send_message()

@bot.command(aliases=['Roll','ROLL','r','R'])
@commands.guild_only()
async def roll(ctx, *args):
    dice_result = d20.roll(' '.join(args))
    
    await send_embed_as_author(ctx, 'Dice Roll', dice_result.result)

class Armies(commands.Cog, name="Army Management"):

	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	@commands.command(aliases=['createArmy','CreateArmy','CREATEARMY'],brief="Creates an army on the active realm for user on the discord server.",description="Creates an army on the active realm for user on the discord server.")
	@commands.guild_only()
	async def createarmy(self, ctx, name):
		db_func.register_guild(ctx.guild)
		db_active_realm = db_func.get_active_realm(ctx.guild.id,ctx.author.id)
		if db_active_realm == None:
			await send_embed_as_author(ctx,'Army Creation Failed!','No active realm selected.')
			return
		army = db_func.get_army(ctx.guild, ctx.author, db_active_realm[3], name)
		if army==None:
			db_func.add_army(ctx.guild, ctx.author, db_active_realm[3], name)
			db_active_army = db_func.get_active_army(ctx.guild, ctx.author, db_active_realm[3])
			if db_active_army == None:
				db_func.add_active_army(ctx.guild, ctx.author, db_active_realm[3], name)
			else:
				db_func.update_active_army(ctx.guild, ctx.author, db_active_realm[3], name)
			print('Create Army Command: ['+ctx.author.display_name+']' + str(ctx.guild.id) + ' created army ' + name)
			await send_embed_as_author(ctx,'Army Created!',"Army **" + name + "** has been created on **"+db_active_realm[3]+"**.")
			return
		else:
			await send_embed_as_author(ctx,'Army Creation Failed!','The army **' + name + '** already exists on **'+db_active_realm[3]+'**.')
			return

	@commands.command(aliases=['useArmy','UseArmy','USEARMY','army','Army','ARMY'],brief="Shows active army or activates specified army.",description="Shows active army or activates specified army.")
	@commands.guild_only()
	async def usearmy(self, ctx, name=""):
		db_func.register_guild(ctx.guild)
		db_active_realm = db_func.get_active_realm(ctx.guild.id, ctx.author.id)

		if db_active_realm == None:
			await send_embed_as_author(ctx, 'Army Selection Failed!','No active realm selected.')
			return
		if name==None or len(name.strip())== 0:
			db_active_army1 = db_func.get_active_army(ctx.guild, ctx.author, db_active_realm[3])
			if db_active_army1 == None:
				await send_embed_as_author(ctx,'Army Select','No army selected!')
				return
			else:
				db_army_units = db_func.get_army_breakdown(ctx.guild, ctx.author, db_active_realm[3], db_active_army1[4])
				db_map_data = db_func.get_army_map_data(ctx.guild, ctx.author, db_active_realm[3], db_active_army1[4])
				fields = []
				breakdown = ''
				total_size = 0
				for unit in db_army_units:
					total_size+=int(unit[6])
					breakdown+=(unit[5] + ' : ' + str(unit[6]) + '\n')
				if len(breakdown) == 0:
					breakdown = 'No units in this army.'
				fields.append(('Units', breakdown, False))
				fields.append(('Total Size', total_size, False))
				if db_map_data != None:
					fields.append(('Army Location', db_map_data[3] + '('+str(db_map_data[5])+','+str(db_map_data[6])+')',False))
				else:
					fields.append(('Army Location', 'Not in any maps.',False))
				await send_embed_as_author(ctx,'Army Select','**' + db_active_army1[4] + "** is currently selected.",fields)
				return
		army = db_func.get_army(ctx.guild, ctx.author, db_active_realm[3], name)
		if army==None:
			await send_embed_as_author(ctx,'Army Selection Failed!','**'+name+'** does not exist on realm **'+db_active_realm[3]+'**.')
			return
		else:
			db_active_army = db_func.get_active_army(ctx.guild, ctx.author, db_active_realm[3])
			db_army_units = db_func.get_army_breakdown(ctx.guild, ctx.author, db_active_realm[3], name)
			db_map_data = db_func.get_army_map_data(ctx.guild, ctx.author, db_active_realm[3], name)
			fields = []
			breakdown = ''
			total_size = 0
			for unit in db_army_units:
				total_size += int(unit[6])
				breakdown += (unit[5] + ' : ' + str(unit[6]) + '\n')
			if len(breakdown) == 0:
					breakdown = 'No units in this army.'
			fields.append(('Units', breakdown, False))
			fields.append(('Total Size', total_size, False))
			if db_map_data != None:
				fields.append(('Army Location', db_map_data[3] + '('+str(db_map_data[5])+','+str(db_map_data[6])+')',False))
			else:
				fields.append(('Army Location', 'Not in any maps.',False))
			if db_active_army == None:
				db_func.add_active_army(ctx.guild, ctx.author, db_active_realm[3], name)
				await send_embed_as_author(ctx,'Army Selected',"**"+name+"** army is now active.", fields)
				return
			else:
				db_func.update_active_army(ctx.guild, ctx.author, db_active_realm[3], name)
				await send_embed_as_author(ctx,'Army Selected',"**"+name+"** army is now active.",fields)

	@commands.command(aliases=['Armies','ARMIES'],brief="Shows list of army for user's active realm on current discord server.",description="Shows list of army for user's active realm on current discord server.")
	@commands.guild_only()
	async def armies(self, ctx):
		db_func.register_guild(ctx.guild)
		db_active_realm = db_func.get_active_realm(ctx.guild.id,ctx.author.id)
		db_active_army = None
		if db_active_realm == None:
			await send_embed_as_author(ctx,'Armies Detail Failed!','No active realm selected.')
			return
		else:
			db_active_army = db_func.get_active_army(ctx.guild,ctx.author,db_active_realm[3])

		armies = db_func.get_armies(ctx.guild, ctx.author, db_active_realm[3])
		message = ''
		for army in armies:
			active = ''
			if db_active_army!=None:
				if army[4] == db_active_army[4]:
					active = ' **[active]**'
			message+=(army[4] + active + '\n')
		await send_embed_as_author(ctx,'Armies in realm ' + db_active_realm[3], message)

	@commands.command(brief="Delete specified army on active realm.",description="Delete specified army on active realm.")
	async def delarmy(self, ctx, army):
		db_active_realm = db_func.get_active_realm(ctx.guild.id, ctx.author.id)
		def check(m):
			return m.content=='YES' and m.channel== ctx.channel and m.author == ctx.author
		if db_active_realm == None:
			await send_embed_as_author(ctx,'Army Deletion Failed', 'No active realm selected.')
			return

		db_army = db_func.get_army(ctx.guild, ctx.author, db_active_realm[3], army)
		if db_army == None:
			await send_embed_as_author(ctx,'Army Deletion Failed', 'Army not found on current realm.')
			return

		await send_embed_as_author(ctx,'Army Delete', 'Are you sure you want to delete **'+army+'**\n\nPlease send `YES` to confirm.')

		try:
			msg = await bot.wait_for('message',check=check, timeout=60)
			if msg != None:
				await send_embed_as_author(ctx,'Army Delete Success', '**'+army+'** has been deleted.')
				db_func.delete_army(ctx.guild, ctx.author, db_active_realm[3], army)
				db_func.delete_active_army(ctx.guild, ctx.author, db_active_realm[3], army)
				return
		except asyncio.TimeoutError:
			await send_embed_as_author(ctx,'Army Delete Failed!','Maximum allowed time to confirm has elapsed.')
			return

class Units(commands.Cog, name="Unit Management"):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	@commands.command(aliases=['addUnit','AddUnit','ADDUNIT'])
	@commands.guild_only()
	async def addunit(self,ctx, name, size=100):
		db_func.register_guild(ctx.guild)
		db_active_realm =  db_func.get_active_realm(ctx.guild.id, ctx.author.id)
		db_active_army = None
		if (db_active_realm == None):
			await send_embed_as_author(ctx,'Unit Creation Failed!','No active realm selected!')
			return
		else:
			db_active_army = db_func.get_active_army(ctx.guild, ctx.author, db_active_realm[3])

		if db_active_army==None:
			await send_embed_as_author(ctx,'Unit Creation Failed!','No active army selected!')
			return

		db_units = db_func.get_unit(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], name)
		if db_units == None:
			db_func.add_unit(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], name, size)
			await send_embed_as_author(ctx,'Units created!',"Unit **" + name + " ("+str(size)+")** added to army **" + db_active_army[4] +"** successfully.")
			return
		else:
			db_func.update_unit(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], name, size)
			await send_embed_as_author(ctx,'Units created!',"Unit **" + name + " ("+str(size)+")** added to army **" + db_active_army[4] +"** successfully.")
			return

	@commands.command(aliases=['Units','UNITS'])
	@commands.guild_only()
	async def units(self,ctx):
		db_func.register_guild(ctx.guild)
		db_active_realm =  db_func.get_active_realm(ctx.guild.id, ctx.author.id)
		db_active_army = None
		if (db_active_realm == None):
			await send_embed_as_author(ctx,'Unit Creation Failed!','No active realm selected!')
			return
		else:
			db_active_army = db_func.get_active_army(ctx.guild, ctx.author, db_active_realm[3])

		if db_active_army==None:
			await send_embed_as_author(ctx,'Unit Creation Failed!','No active army selected!')
			return

		db_units = db_func.get_army_breakdown(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4])
		message = ''
		total_size = 0
		for unit in db_units:
			total_size+=int(unit[6])
			message += (unit[5] + ' : ' + str(unit[6]) + '\n')
			attributes = db_func.get_unit_attributes(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], unit[5])
			if len(attributes)>0:
				message+='```\n'
			for attribute in attributes:
				message += ('\t' + attribute[6] + ' : ' + attribute[7] + '\n')
			if len(attributes)>0:
				message+='```'
		await send_embed_as_author(ctx, 'Units in ' + db_active_army[4], message,[('Total Army Size', str(total_size), False)])

	@commands.command(aliases=['setAttribute','SetAttribute','SETATTRIBUTE','setattributes','SetAttributes','SETATTRIBUTES','setAttributes'])
	@commands.guild_only()
	async def setattribute(self,ctx, unit, attribute, value=""):
		db_func.register_guild(ctx.guild)
		db_active_realm =  db_func.get_active_realm(ctx.guild.id, ctx.author.id)
		db_active_army = None
		if (db_active_realm == None):
			await send_embed_as_author(ctx,'Attribute Setting Failed!','No active realm selected!')
			return
		else:
			db_active_army = db_func.get_active_army(ctx.guild, ctx.author, db_active_realm[3])

		if db_active_army==None:
			await send_embed_as_author(ctx,'Attribute Setting Failed!','No active army selected!')
			return

		db_unit = db_func.get_unit(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], unit)
		if db_unit == None:
			await send_embed_as_author(ctx, 'Attribute Setting Failed!', 'Unit does not exist within this army.')
			return

		db_attribute = db_func.get_unit_attribute(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], unit, attribute)
		if db_attribute == None:
			db_func.add_unit_attribute(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], unit, attribute, value)
		else:
			db_func.update_unit_attribute(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], unit, attribute, value)
		await send_embed_as_author(ctx,'Attribute Set','**' + unit + '**\'s **' + attribute + '** is set to **' + value + '**')

	@commands.command()
	@commands.guild_only()
	async def removeunit(self, ctx, unit, size=100):
		db_active_realm = db_func.get_active_realm(ctx.guild.id, ctx.author.id)
		db_active_army = None
		if db_active_realm == None:
			await send_embed_as_author(ctx,'Unit Remove Failed','No active realm selected.')
			return
		else:
			db_active_army = db_func.get_active_army(ctx.guild, ctx.author, db_active_realm[3])

		if db_active_army == None:
			await send_embed_as_author(ctx, 'Unit Remove Failed','No active army selected.')
			return

		db_unit = db_func.get_unit(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], unit)
		if db_unit == None:
			await send_embed_as_author(ctx, 'Unit Remove Failed','Unit not found in your active army.')
			return

		db_func.remove_unit(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], unit, size)
		await send_embed_as_author(ctx,'Unit Removed', str(size) + ' **'+unit+'**s has been removed from **'+db_active_army[4]+'**')

	@commands.command()
	@commands.guild_only()
	async def removeattribute(self, ctx, unit, attribute):
		db_active_realm = db_func.get_active_realm(ctx.guild.id, ctx.author.id)
		db_active_army = None
		if db_active_realm == None:
			await send_embed_as_author(ctx,'Attribute Remove Failed','No active realm selected.')
			return
		else:
			db_active_army = db_func.get_active_army(ctx.guild, ctx.author, db_active_realm[3])

		if db_active_army == None:
			await send_embed_as_author(ctx, 'Attribute Remove Failed','No active army selected.')
			return

		db_unit = db_func.get_unit(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], unit)
		if db_unit == None:
			await send_embed_as_author(ctx, 'Attribute Remove Failed','Unit not found in your active army.')
			return

		db_attribute = db_func.get_unit_attribute(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], unit, attribute)
		if db_attribute == None:
			await send_embed_as_author(ctx, 'Attribute Remove Failed', 'attribute not in unit **'+unit+'**.')
			return

		db_func.delete_unit_attribute(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4], unit, attribute)
		await send_embed_as_author(ctx,'Attribute Removed','**'+attribute+'** has been removed from **'+unit+'**')

class Realms(commands.Cog, name='Realm Management'):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	@commands.command(aliases=['CreateRealm','createRealm','CREATEREALM'],brief="Creates a realm for the user on the discord server.",description="Creates a realm for the user on the discord server.")
	@commands.guild_only()
	async def createrealm(self, ctx, name):
		db_func.register_guild(ctx.guild)
		realm = db_func.get_realm(ctx.guild, ctx.author, name)
		if realm==None:
			db_func.add_realm(ctx.guild, ctx.author, name)
			print("Create Realm Command: ["+ctx.author.display_name+"]" + str(ctx.guild.id) + " created realm " + name)
			db_active_realm = db_func.get_active_realm(ctx.guild.id,ctx.author.id)
			if db_active_realm == None:
				db_func.add_active_realm(ctx.guild, ctx.author, name)
			else:
				db_func.update_active_realm(ctx.guild, ctx.author, name)
			await send_embed_as_author(ctx,'Realm Created','Realm **' + name + '** has been created.')
			return
		else:
			await send_embed_as_author(ctx,'Realm Creation Failed!','Realm **' + name + '** already exists.')
			return

	@commands.command(aliases=['UseRealm','useRealm','USEREALM','realm','Realm','REALM'],brief="Shows active realm or activates specified realm.",description="Shows active realm or activates specified realm.")
	@commands.guild_only()
	async def userealm(self, ctx, realm=""):
		db_func.register_guild(ctx.guild)
		db_active_realm = db_func.get_active_realm(ctx.guild.id,ctx.author.id)

		if realm==None or len(realm.strip())== 0:
			if db_active_realm == None:
				await send_embed_as_author(ctx,'Realm Select','No realm selected!')
				return
			else:
				await send_embed_as_author(ctx,'Realm Select','**' + db_active_realm[3] + "** is currently selected.")
				return
		db_realm = db_func.get_realm(ctx.guild, ctx.author, realm)
		if db_realm==None:
			await send_embed_as_author(ctx,'Realm Selection Failed!','The realm you are trying to select does not exist on this server.')
			return
		else:
			if db_active_realm == None:
				print("Use Realm Command: ["+ctx.author.display_name+"]" + str(ctx.guild.id) + " registered active realm " + realm)
				db_func.add_active_realm(ctx.guild, ctx.author, realm)
			else:
				print("Use Realm Command: ["+ctx.author.display_name+"]" + str(ctx.guild.id) + " modified active realm " + realm)
				db_func.update_active_realm(ctx.guild, ctx.author, realm)
			await send_embed_as_author(ctx,'Realm Selected',"**"+realm+"** is currently active.")
			return

	@commands.command(aliases=['Realms','REALMS'],brief="Show all realms of user within the discord server.",description="Show all realms of user within the discord server.")
	@commands.guild_only()
	async def realms(self, ctx):
		db_func.register_guild(ctx.guild)
		db_active_realm = db_func.get_active_realm(ctx.guild.id,ctx.author.id)
		realms = db_func.get_realms(ctx.guild, ctx.author)
		message = ''
		for realm in realms:
			active = ''
			if db_active_realm != None:
				if realm[3] == db_active_realm[3]:
					active = ' **[active]**'
			message = message + realm[3] + active
			message = message + '\n'
		await send_embed_as_author(ctx,'Your realms on this server', message)

	@commands.command(aliases=['delRealm','DELREALM','DelRealm'],brief="Deletes specified user realm on discord server.",description="Deletes specified user realm on discord server.")
	@commands.guild_only()
	async def delrealm(self, ctx, realm):
		await send_embed_as_author(ctx,'Realm Delete','Are you sure you want to delete **'+realm+'**\n\nPlease send `YES` to confirm.')
		def check(m):
			return m.content=='YES' and m.channel== ctx.channel and m.author == ctx.author
		try:
			msg = await bot.wait_for('message',check=check, timeout=60)
			if msg != None:
				await send_embed_as_author(ctx,'Realm Delete Success', '**'+realm+'** has been deleted.')
				db_func.delete_realm(ctx.guild, ctx.author, realm)
				db_func.delete_active_realm(ctx.guild, ctx.author, realm)
				return
		except asyncio.TimeoutError:
			await send_embed_as_author(ctx,'Realm Delete Failed!','Maximum allowed time to confirm has elapsed.')
			return

class Maps(commands.Cog, name='Map Management'):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(brief="Creates a data storage for map and map tiles",description="Creates a data storage for map and map tiles.")
    @commands.guild_only()
    async def createmap(self, ctx, name, x=100,y=100):
        map_identifier = name
        db_func.add_map(ctx.guild, ctx.author, str(map_identifier),x,y)
        await send_embed_as_author(ctx, 'Map Created!', 'Map ['+str(map_identifier)+'] has been created.\n\nUse `$map '+str(map_identifier)+'` to activate this map.')

    @commands.command(brief="Shows current active map, or activates the specified map.",description="Shows current active map, or activates the specified map.")
    @commands.guild_only()
    async def map(self, ctx, map_identifier=""):
        db_active_map = db_func.get_active_map(ctx.guild.id, ctx.author.id)

        if len(map_identifier.strip()) == 0:
            if db_active_map == None:
                await send_embed_as_author(ctx,'Map Select','No active map selected.')
                return
            else:
                await send_embed_as_author(ctx,'Map Select','Map ['+db_active_map[3]+'] active.')
                return
        else:
            db_map = db_func.get_map(ctx.guild, ctx.author, map_identifier)
            if db_map == None:
                await send_embed_as_author(ctx,'Map Select','Map ['+map_identifier+'] does not exist.')
                return
            else:
                if db_active_map == None:
                    db_func.add_active_map(ctx.guild, ctx.author, map_identifier)
                else:
                    db_func.update_active_map(ctx.guild, ctx.author, map_identifier)
                await send_embed_as_author(ctx,'Map Selected!','Map ['+map_identifier+'] has been selected.')

    @commands.command(brief="Places user's active army at a map tile specified by the x and y coordinates",description="Places user's active army at a map tile specified by the x and y coordinates")
    @commands.guild_only()
    async def placeuserarmy(self, ctx, user, x, y):
        user_obj = None
        for member in ctx.guild.members:
            if user == member.display_name:
                user_obj = member
        if user_obj == None:
            await send_embed_as_author(ctx,'Army Placement Failed!','Unable to find user.')
            return
        db_active_realm = db_func.get_active_realm(ctx.guild.id, user_obj.id)
        db_active_army = None
        if db_active_realm == None:
            await send_embed_as_author(ctx,'Army Placement Failed!','**'+user+'** has no active realm selected.')
            return
        else:
            db_active_army = db_func.get_active_army(ctx.guild, user_obj, db_active_realm[3])
        if db_active_army == None:
            await send_embed_as_author(ctx,'Army Placement Failed!','**'+user+'** has no active army selected.')
            return
        db_active_map = db_func.get_active_map(ctx.guild.id, ctx.author.id)
        if db_active_map == None:
            await send_embed_as_author(ctx,'Army Placement Failed!','No active map selected.')
            return
        db_army = db_func.get_army(ctx.guild, ctx.author, db_active_realm[3], db_active_army[4])
        db_map_object = db_func.get_map_object(ctx.guild, ctx.author, db_active_map[3], db_army[0])
        if (db_map_object == None):
            db_func.add_map_object(ctx.guild, ctx.author, db_active_map[3], db_army[0], x, y)
        else:
            db_func.update_map_object(ctx.guild, ctx.author, db_active_map[3], db_army[0], x, y)
        await send_embed_as_author(ctx,'Army Placed in Map','**'+user+'**\'s **'+db_active_army[4]+'** has been placed at **'+db_active_map[3]+'**('+str(x)+','+str(y)+')')

class Combat(commands.Cog, name="Combat Management"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    @commands.guild_only()
    async def attack(self, ctx, *args):
        parser = argparse.ArgumentParser(description='$attack -u <target_user> [-r target_realm -a target_army] -t <target ...>',usage=argparse.SUPPRESS,add_help=False)
        required_args = parser.add_argument_group('required arguments')
        required_args.add_argument('--user','-u',help='target user',required=True)
        parser.add_argument('--realm','-r',help='realm of target user which contains the target unit/s. uses target user\'s active realm if empty.')
        parser.add_argument('--army','-a',help='army of target user which contains the target unit/s. uses target user\'s active army if empty.')
        required_args.add_argument('--target','-t',help='target unit',nargs='+',required=True)
        arguments = parser.parse_args(args)


        print(arguments)

        await send_embed_as_author(ctx, 'DEBUG','This is a test',[('Usage',parser.format_help(),False)])

bot.add_cog(Maps(bot))
bot.add_cog(Realms(bot))
bot.add_cog(Armies(bot))
bot.add_cog(Units(bot))
bot.add_cog(Combat(bot))
bot.run('ODg1MDU1NTUyMTM5NDQ4MzMy.YTheNw.T5seW9S5qX2W85l1-_AZQyVp9CE')