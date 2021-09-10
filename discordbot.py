import discord
import mysql.connector
from discord.ext import commands

custom_prefixes = {}
default_prefixes = ['$']
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="worldbuilderbot"
)

def get_guild_prefix(guild):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM guild_prefixes WHERE guild_identifier=%s', (guild.id,))
    prefixes = cursor.fetchone()
    cursor.close()

    if prefixes == None:
        prefixes = default_prefixes

    return prefixes

def add_guild_prefix(guild, prefixes):
    cursor = db.cursor(prepared=True)
    cursor.execute('INSERT INTO guild_prefixes (guild_identifier, prefixes, date_added, date_updated) VALUES (%s, %s, now(), now())',(guild.id, prefixes))
    db.commit()
    cursor.close()

def update_guild_prefix(guild, prefixes):
    cursor = db.cursor(prepared=True)
    cursor.execute('UPDATE guild_prefixes SET prefixes=%s, date_updated=now() WHERE guild_identifier=%s', (prefixes, guild.id))
    db.commit()
    cursor.close()

async def determine_prefix(bot, message):
    guild = message.guild

    if guild:
        return get_guild_prefix(message.guild)
    else:
        return default_prefixes

bot = commands.Bot(command_prefix=determine_prefix)

def register_guild (guild):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM guilds WHERE identifier=%s',(guild.id,))
    guild = cursor.fetchone()
    if guild==None:
        cursor.execute('INSERT INTO guilds (identifier,date_added,date_updated) VALUES (%s,NOW(),NOW())',(guild.id,))
        db.commit()
    cursor.close()

def get_army_breakdown(army, realm, guild, user):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM game_units WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s AND army_identifier=%s',(guild,user,realm,army))
    db_units = cursor.fetchall()
    cursor.close()

    return db_units

def get_active_realm(guild, user):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM active_realm WHERE user_identifier=%s AND guild_identifier=%s',(user, guild))
    db_active_realm = cursor.fetchone()
    cursor.close()

    return db_active_realm

def get_active_army(guild, user, realm):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM active_army WHERE user_identifier=%s AND guild_identifier=%s AND realm_identifier=%s',(ctx.author.id, ctx.guild.id,db_active_realm[3]))
    db_active_army = cursor.fetchone()
    cursor.close()

    return db_active_army

def get_realm(guild, author, realm):
    cursor = db.cursor(prepared=True)
    cursor.execute("SELECT * FROM game_realms WHERE guild_identifier=%s AND user_identifier=%s AND identifier=%s",(guild.id,author.id,realm))
    db_realm = cursor.fetchone()
    cursor.close()

    return db_realm

def get_army(guild, author, realm, army):
    pass

def get_unit(guild, author, realm, army, unit):
    pass

def add_realm(guild, author, realm):
    cursor = db.cursor(prepared=True)
    cursor.execute('INSERT INTO game_realms (guild_identifier,user_identifier,identifier,date_added,date_updated) VALUES (%s,%s,%s,NOW(),NOW())',(guild.id,author.id,name))
    db.commit()
    cursor.close()

def add_army(guild, author, realm, army):
    cursor = db.cursor(prepared=True)
    cursor.execute('INSERT INTO game_armies(guild_identifier,user_identifier,realm_identifier,identifier,date_added,date_updated) VALUES (%s,%s,%s,%s,NOW(),NOW())',(guild.id,author.id,realm,army))
    db.commit()
    cursor.close()

def add_unit(guild, author, realm, army, unit):
    cursor = db.cursor(prepared=True)
    cursor.close()

async def send_embed_as_author(title, description, color="", author):
    if (len(color.strip()) == 0):
        color = discord.Color.blue()
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_author(name=author.display_name,icon_url=author.avatar_url)
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
@commands.guild_only()
async def prefix(ctx, prefixes=""):
    current_prefix = get_guild_prefix(ctx.guild)
    prefix = prefixes.split() or default_prefixes

    if current_prefix == None:
        add_guild_prefix(ctx.guild, prefix)
    else:
        update_guild_prefix(ctx.guild, ''.join(prefix))

    await send_embed_as_author("WorldBuilderBot Prefix Updated","You should now use **" + prefixes + "** as prefix for commands","",ctx.author)

@bot.command(aliases=['CreateRealm','createrealm','CREATEREALM'])
@commands.guild_only()
async def createRealm(ctx, name):
    cursor = db.cursor(prepared=True)
    register_guild(ctx.guild)
    realm = get_realm(ctx.guild, ctx.author, name)
    if realm==None:
        add_realm(ctx.guild, ctx.author, realm)
        await send_embed_as_author('Realm Created','Realm **' + name + '** has been created.','',ctx.author)
        return
    else:
        cursor.close()
        await send_embed_as_author('Realm Creation Failed!','Realm **' + name + '** already exists.','',ctx.author)
        return

@bot.command(aliases=['UseRealm','userealm','USEREALM','realm','Realm','REALM'])
@commands.guild_only()
async def useRealm(ctx, realm=""):
    cursor = db.cursor(prepared=True)
    register_guild(ctx.guild)
    if realm==None or len(realm.strip())== 0:
        db_active_realm1 = get_active_realm(ctx.author.id, ctx.guild.id)
        if db_active_realm1 == None:
            cursor.close()
            await send_embed_as_author('Realm Select','No realm selected!','',ctx.author)
            return
        else:
            cursor.close()
            await send_embed_as_author('Realm Select','**' + db_active_realm1[3] + "** is currently selected.",'',ctx.author)
            return
    db_realm = get_realm(ctx.guild, ctx.author, realm)
    if db_realm==None:
        cursor.close()
        await send_embed_as_author('Realm Selection Failed!','The realm you are trying to select does not exists on this server.','',ctx.author)
        return
    else:
        db_active_realm = get_active_realm(ctx.author.id, ctx.guild.id)
        if db_active_realm == None:
            cursor.execute('INSERT INTO active_realm (guild_identifier,user_identifier,realm_identifier,date_added,date_updated) VALUES (%s,%s,%s,now(),now())',(ctx.guild.id,ctx.author.id,realm))
            db.commit()
            cursor.close()
        else:
            cursor.execute('UPDATE active_realm SET realm_identifier=%s WHERE id=%s',(realm, db_active_realm[0]))
            db.commit()
            cursor.close()
        await send_embed_as_author('Realm Selected',"**"+realm+"** is currently active.",'',ctx.author)
        return

@bot.command()
@commands.guild_only()
async def createArmy(ctx, name):
    cursor = db.cursor(prepared=True)
    register_guild(ctx.guild)
    db_active_realm = get_active_realm(ctx.author.id, ctx.guild.id)
    if db_active_realm == None:
        cursor.close()
        await send_embed_as_author('Army Creation Failed!','No active realm selected.','',ctx.author)
        return
    army = get_army(ctx.guild, ctx.author, db_active_realm[3], name)
    if army==None:
        add_army(ctx.guild, ctx.author, db_active_realm[3], name)
        await send_embed_as_author('Army Created!',"Army **" + name + "** has been created on **"+db_active_realm[3]+"**.",'',ctx.author)
        return
    else:
        cursor.close()
        await send_embed_as_author('Army Creation Failed!','The army **' + name + '** already exists on **'+db_active_realm[3]+'**.','',ctx.author)
        return

@bot.command()
@commands.guild_only()
async def createarmy(ctx, name):
    await createArmy(ctx, name)

@bot.command()
@commands.guild_only()
async def useArmy(ctx, name=""):
    cursor = db.cursor(prepared=True)
    register_guild(ctx.guild)
    db_active_realm = get_active_realm(ctx.author.id, ctx.guild.id)
    if db_active_realm == None:
        embed=discord.Embed(title='Army Selection Failed!',description='No active realm selected.',color=discord.Color.blue())
        embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
        cursor.close()
        await ctx.send(embed=embed)
        return
    if name==None or len(name.strip())== 0:
        db_active_army1 = get_active_army(ctx.guild, ctx.author, db_active_realm[3])
        if db_active_army1 == None:
            cursor.close()
            await send_embed_as_author('Army Select','No army selected!','',ctx.author)
            return
        else:
            cursor.close()
            await send_embed_as_author('Army Select','**' + db_active_army1[4] + "** is currently selected.",'',ctx.author)
            return
    cursor.execute('SELECT * FROM game_armies WHERE identifier=%s AND user_identifier=%s AND guild_identifier=%s AND realm_identifier=%s',[name, ctx.author.id, ctx.guild.id, db_active_realm[3]])
    army = cursor.fetchone()
    if army==None:
        cursor.close()
        await send_embed_as_author('Army Selection Failed!','**'+name+'** does not exist on realm **'+db_active_realm[3]+'**.','',ctx.author)
        return
    else:
        cursor.execute('SELECT * FROM active_army WHERE user_identifier=%s AND guild_identifier=%s AND realm_identifier=%s', (ctx.author.id,ctx.guild.id,db_active_realm[3]))
        db_active_army = cursor.fetchone()
        if db_active_army == None:
            cursor.execute('INSERT INTO active_army(guild_identifier,user_identifier,realm_identifier,army_identifier,date_added,date_updated) VALUES (%s,%s,%s,%s,now(),now())',(ctx.guild.id,ctx.author.id, db_active_realm[3], name))
            db.commit()
            cursor.close()
            await send_embed_as_author('Army Selected',"**"+name+"** army is now active.",'',ctx.author)
            return
        else:
            cursor.execute('UPDATE active_army SET army_identifier=%s, date_updated=now() WHERE id=%s', (name, db_active_army[0]))
            db.commit()
            cursor.close()
            await send_embed_as_author('Army Selected',"**"+name+"** army is now active.",'',ctx.author)


@bot.command()
@commands.guild_only()
async def usearmy(ctx, name=""):
    await useArmy(ctx, name)

@bot.command()
@commands.guild_only()
async def addUnit(ctx, name, size=100):
    cursor = db.cursor(prepared=True)
    register_guild(ctx.guild)
    db_active_realm =  get_active_realm(ctx.author.id, ctx.guild.id)
    db_active_army = get_active_army(ctx.guild, ctx.author, db_active_realm[3])

    realm = db_active_realm[3]
    army = db_active_army[4]

    cursor.execute('SELECT * FROM game_units WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s AND army_identifier=%s AND identifier=%s',(ctx.guild.id,ctx.author.id,realm,army,name))
    db_units = cursor.fetchone()
    if db_units == None:
        cursor.execute('INSERT INTO game_units(guild_identifier,user_identifier,realm_identifier,army_identifier,identifier,size,date_added,date_updated) values (%s,%s,%s,%s,%s,%s,now(),now())',(ctx.guild.id,ctx.author.id,realm,army,name,size))
        db.commit()
        cursor.execute("SELECT army_identifier, sum(size) FROM game_units WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s AND army_identifier=%s",(ctx.guild.id,ctx.author.id,realm,army))
        army_data = cursor.fetchone()
        cursor.close()
        await send_embed_as_author('Units created!',"Unit **" + name + " ("+str(size)+")** added to army **" + army +"** successfully.",'',ctx.author)
        return
    else:
        cursor.execute('UPDATE game_units SET size=size+%s WHERE id=%s',(size, db_units[0]))
        db.commit()
        cursor.execute("SELECT army_identifier, sum(size) FROM game_units WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s AND army_identifier=%s",(ctx.guild.id,ctx.author.id,realm,army))
        army_data = cursor.fetchone()
        cursor.close()
        await send_embed_as_author('Units created!',"Unit **" + name + " ("+str(size)+")** added to army **" + army +"** successfully.",'',ctx.author)
        return

@bot.command()
@commands.guild_only()
async def addunit(ctx, name, size=100):
    await addUnit(ctx, name, size)

bot.run('ODg1MDU1NTUyMTM5NDQ4MzMy.YTheNw.T5seW9S5qX2W85l1-_AZQyVp9CE')