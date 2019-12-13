import discord
import asyncio
import os
import csv
import sys
import random
import requests
import fileinput
from discord.ext.commands import Bot
from discord.ext import commands
import urllib3
import time
import datetime
from lxml import html
from discord.utils import get

Client=discord.Client()
bot_prefix="kana"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Kanabama Bot Running")
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(name="Prefix: *"))

client.run("NTA1NDY3NTE1OTA5MTc3Mzk2.D0NyMQ.R6LkCyP0S-mMLC7lzI5inA57jZc")
