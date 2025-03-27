# config_vars.py
from pymongo import MongoClient

discord_token = "MTMzMDU1MDAwOTA1NzI0NzMwMg.GujFie.aU0Alub44Amwdx0MWcZzbbGhLT7QDPrB_GgZFA"
mongodb_connection = "mongodb+srv://electrotech156:Aadikaashikunji3@ctfbot.uz3uz3g.mongodb.net/?retryWrites=true&w=majority&appName=CTFBOT"

client = MongoClient(mongodb_connection)

ctfdb = client['ctftime'] # Create ctftime database
ctfs = ctfdb['ctfs'] # Create ctfs collection

teamdb = client['ctfteams'] # Create ctf teams database

serverdb = client['serverinfo'] # configuration db
