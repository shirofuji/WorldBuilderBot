import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="worldbuilderbot"
)

default_prefixes = '$'

def get_guild_prefix(guild):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM guild_prefixes WHERE guild_identifier=%s', (guild.id,))
    prefixes = cursor.fetchone()
    prefix = default_prefixes
    cursor.close()

    if prefixes != None:
        prefix = prefixes[2]

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

def register_guild (guild):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM guilds WHERE identifier=%s',(guild.id,))
    guild = cursor.fetchone()
    if guild==None:
        cursor.execute('INSERT INTO guilds (identifier,date_added,date_updated) VALUES (%s,NOW(),NOW())',(guild.id,))
        db.commit()
    cursor.close()

def get_army_breakdown(guild, user, realm, army):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM game_units WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s AND army_identifier=%s',(guild.id,user.id,realm,army))
    db_units = cursor.fetchall()
    cursor.close()

    return db_units

def get_active_realm(guild, user):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM active_realm WHERE user_identifier=%s AND guild_identifier=%s',(user, guild))
    db_active_realm = cursor.fetchone()
    cursor.close()

    return db_active_realm

def add_active_realm(guild, user, realm):
    cursor = db.cursor(prepared=True)
    cursor.execute('INSERT INTO active_realm (guild_identifier, user_identifier, realm_identifier, date_added, date_updated) VALUES (%s,%s,%s,now(),now())',(guild.id, user.id, realm))
    db.commit()
    cursor.close()

def delete_active_realm(guild, user, realm):
    cursor = db.cursor(prepared=True)
    cursor.execute('DELETE FROM active_realm WHERE guild_identifier=%s AND user_identifer=%s AND realm_identifier=%s',(guild.id, user.id, realm))
    db.commit()
    cursor.close()

def delete_realm(guild, user, realm):
    cursor = db.cursor(prepared=True)
    cursor.execute('DELETE FROM game_realms WHERE guild_identifier=%s AND user_identifier=%s AND identifier=%s',(guild.id, user.id, realm))
    db.commit()
    cursor.close()

def update_active_realm(guild, user, realm):
    cursor = db.cursor(prepared=True)
    cursor.execute('UPDATE active_realm SET realm_identifier=%s, date_updated=now() WHERE guild_identifier=%s AND user_identifier=%s',(realm, guild.id, user.id))
    db.commit()
    cursor.close()

def get_active_army(guild, user, realm):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM active_army WHERE user_identifier=%s AND guild_identifier=%s AND realm_identifier=%s',(user.id, guild.id,realm))
    db_active_army = cursor.fetchone()
    cursor.close()

    return db_active_army

def add_active_army(guild, user, realm, army):
    cursor = db.cursor(prepared=True)
    cursor.execute('INSERT INTO active_army (guild_identifier, user_identifier, realm_identifier,army_identifier, date_added, date_updated) VALUES (%s,%s,%s,%s,now(),now())',(guild.id, user.id, realm,army))
    db.commit()
    cursor.close()

def update_active_army(guild, user, realm, army):
    cursor = db.cursor(prepared=True)
    cursor.execute('UPDATE active_army SET army_identifier=%s, date_updated=now() WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s',(army, guild.id, user.id, realm))
    db.commit()
    cursor.close()

def get_realm(guild, author, realm):
    cursor = db.cursor(prepared=True)
    cursor.execute("SELECT * FROM game_realms WHERE guild_identifier=%s AND user_identifier=%s AND identifier=%s",(guild.id,author.id,realm))
    db_realm = cursor.fetchone()
    cursor.close()

    return db_realm

def get_realms(guild, author):
    cursor = db.cursor(prepared=True)
    cursor.execute("SELECT * FROM game_realms WHERE guild_identifier=%s AND user_identifier=%s",(guild.id,author.id))
    realms = cursor.fetchall()
    cursor.close()

    return realms

def add_realm(guild, author, realm):
    cursor = db.cursor(prepared=True)
    cursor.execute('INSERT INTO game_realms (guild_identifier,user_identifier,identifier,date_added,date_updated) VALUES (%s,%s,%s,NOW(),NOW())',(guild.id,author.id,realm))
    db.commit()
    cursor.close()

def get_army(guild, author, realm, army):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM game_armies WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s AND identifier=%s',(guild.id, author.id, realm, army))
    db_army = cursor.fetchone()
    cursor.close()

    return db_army

def get_armies(guild, author, realm):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM game_armies WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s',(guild.id, author.id, realm))
    armies = cursor.fetchall()
    cursor.close()

    return armies

def add_army(guild, author, realm, army):
    cursor = db.cursor(prepared=True)
    cursor.execute('INSERT INTO game_armies(guild_identifier,user_identifier,realm_identifier,identifier,date_added,date_updated) VALUES (%s,%s,%s,%s,NOW(),NOW())',(guild.id,author.id,realm,army))
    db.commit()
    cursor.close()

def delete_army(guild, author, realm, army):
    cursor = db.cursor(prepared=True)
    cursor.execute('DELETE FROM game_armies WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s AND identifier=%s',(guild.id, author.id, realm, army))
    db.commit()
    cursor.close()

def delete_active_army(guild, author, realm, army):
    cursor = db.cursor(prepared=True)
    cursor.execute('DELETE FROM active_army WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s AND army_identifier=%s',(guild.id, author.id, realm, army))
    db.commit()
    cursor.close()

def get_unit(guild, author, realm, army, unit):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM game_units WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s AND army_identifier=%s AND identifier=%s',(guild.id, author.id, realm, army, unit))
    db_unit = cursor.fetchone()
    cursor.close()

    return db_unit

def add_unit(guild, author, realm, army, unit, size=100):
    cursor=db.cursor(prepared=True)
    cursor.execute('INSERT INTO game_units(guild_identifier,user_identifier,realm_identifier,army_identifier,identifier,size,date_added,date_updated) values (%s,%s,%s,%s,%s,%s,now(),now())',(guild.id,author.id,realm,army,unit,size))
    db.commit()
    cursor.close()

def update_unit(guild, author, realm, army, unit, size=100):
    cursor = db.cursor(prepared=True)
    db_unit = get_unit(guild, author, realm, army, unit)
    cursor.execute('UPDATE game_units SET size=%s, date_updated=now() WHERE id=%s', (int(db_unit[6])+int(size), db_unit[0]))
    db.commit()
    cursor.close()

def remove_unit(guild, author, realm, army, unit, size=100):
    cursor = db.cursor(prepared=True)
    db_unit = get_unit(guild, author, realm, army, unit)
    if (int(db_unit[6])-int(size) > 0):
        update_unit(guild, author, realm, army, unit, -1*int(size))
    else:
        cursor.execute('DELETE FROM game_units WHERE id=%s', (db_unit[0],))
        db.commit()
    cursor.close()

def get_unit_attribute(guild, author, realm, army, unit, attribute):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM game_unit_attributes WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s AND army_identifier=%s AND unit_identifier=%s AND parameter=%s',(guild.id, author.id, realm, army, unit, attribute))
    db_attribute = cursor.fetchone()
    cursor.close()

    return db_attribute

def get_unit_attributes(guild, author, realm, army, unit):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM game_unit_attributes WHERE guild_identifier=%s AND user_identifier=%s AND realm_identifier=%s AND army_identifier=%s AND unit_identifier=%s',(guild.id, author.id, realm, army, unit))
    db_attributes = cursor.fetchall()
    cursor.close()

    return db_attributes

def add_unit_attribute(guild, author, realm, army, unit, attribute, value):
    cursor = db.cursor(prepared=True)
    cursor.execute('INSERT INTO game_unit_attributes (guild_identifier, user_identifier, realm_identifier, army_identifier, unit_identifier, parameter, value, date_added, date_updated) VALUES (%s,%s,%s,%s,%s,%s,%s,now(),now())',(guild.id, author.id, realm, army, unit, attribute, value))
    db.commit()
    cursor.close()

def update_unit_attribute(guild, author, realm, army, unit, attribute, value):
    cursor = db.cursor(prepared=True)
    db_attribute = get_unit_attribute(guild, author, realm, army, unit, attribute)
    cursor.execute('UPDATE game_unit_attributes SET value=%s WHERE id=%s',(value, db_attribute[0]))
    db.commit()
    cursor.close()

def delete_unit_attribute(guild, author, realm, army, unit, attribute):
    cursor = db.cursor(prepared=True)
    db_attribute = get_unit_attribute(guild, author, realm, army, unit, attribute)
    if db_attribute == None:
        return
    cursor.execute('DELETE FROM game_unit_attributes WHERE id=%s',(db_attribute[0],))
    db.commit()
    cursor.close()

def get_map(guild, author, map_identifier):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM game_maps WHERE guild_identifier=%s AND user_identifier=%s AND map_identifier=%s',(guild.id, author.id, map_identifier))
    db_map = cursor.fetchone()
    cursor.close()

    return db_map

def add_map(guild, author, map_identifier, x=100,y=100):
    cursor = db.cursor(prepared=True)
    cursor.execute('INSERT INTO game_maps(guild_identifier,user_identifier,map_identifier,x,y,date_added,date_updated) VALUES (%s,%s,%s,%s,%s,now(),now())',(guild.id, author.id,map_identifier,x,y))
    db.commit()
    cursor.close()

def get_active_map(guild, author):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM active_map WHERE guild_identifier=%s AND user_identifier=%s',(guild, author))
    db_map = cursor.fetchone()
    cursor.close()

    return db_map

def add_active_map(guild, author, map_identifier):
    cursor = db.cursor(prepared=True)
    cursor.execute('INSERT INTO active_map(guild_identifier,user_identifier,map_identifier,date_added,date_updated) VALUES (%s,%s,%s,now(),now())',(guild.id, author.id,map_identifier))
    db.commit()
    cursor.close()

def update_active_map(guild, author, map_identifier):
    cursor = db.cursor(prepared=True)
    db_map = get_active_map(guild.id, author.id)
    cursor.execute('UPDATE active_map SET map_identifier=%s,date_updated=now() WHERE id=%s',(map_identifier,db_map[0]))
    db.commit()
    cursor.close()

def get_map_object(guild, author, mapid, objectid):
    cursor = db.cursor(prepared=True)
    cursor.execute('SELECT * FROM game_map_objects WHERE guild_identifier=%s AND user_identifier=%s AND map_identifier=%s AND object_identifier=%s',(guild.id, author.id, mapid, objectid))
    db_map_object = cursor.fetchone()
    cursor.close()
    return db_map_object

def add_map_object(guild, author, mapid, objectid, x, y):
    cursor = db.cursor(prepared=True)
    cursor.execute('INSERT INTO game_map_objects (guild_identifier,user_identifier,map_identifier,object_identifier,x,y,date_added,date_updated) VALUES (%s,%s,%s,%s,%s,%s,now(),now())',(guild.id, author.id, mapid, objectid, x, y))
    db.commit()
    cursor.close()

def update_map_object(guild, author, mapid, objectid, x, y):
    cursor=db.cursor(prepared=True)
    db_map_object = get_map_object(guild, author, mapid, objectid)
    cursor.execute('UPDATE game_map_objects SET x=%s, y=%s, date_updated=now() WHERE id=%s',(x,y,db_map_object[0]))
    db.commit()
    cursor.close()

def delete_map_object(guild, author, mapid, objectid):
    cursor=db.cursor(prepared=True)
    cursor.execute('DELETE FROM game_map_objects WHERE guild_identifier=%s AND user_identifier=%s AND map_identifier=%s AND object_identifier=%s',(guild.id,author.id, mapid, objectid))
    db.commit()
    cursor.close()

def get_army_map_data(guild, author, realm, army):
    cursor = db.cursor(prepared=True)
    db_army = get_army(guild, author, realm, army)
    cursor.execute('SELECT * FROM game_map_objects WHERE object_identifier=%s', (db_army[0],))
    db_map_data = cursor.fetchone()
    cursor.close()

    return db_map_data