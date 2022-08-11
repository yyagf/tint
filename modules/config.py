import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "9660290"))
API_HASH = getenv("API_HASH", "03048a53b37d81fd68d6a651f5911064")
BOT_TOKEN = getenv("BOT_TOKEN", "5485393339:AAFFrOIWC9y941T0k_FWIPRZX8GYTqG6Z7Q")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BACDy7lY5ukTARYgpXK7qLzKUNWP7vIYl0SyI9U2hemVkSWlSz5VRSGp9ZivAJHWEj0brZvRLy6lj0z9EVhStnmITwA-gc47KbsuWuirLytmYTNFe55c4CtDFDwEKRIh8mKse-xiTqlSR5dvGlo1koXdeIYujXY0DSf6skV6NQq2afO9xpdUMXRMtcfG7FWCV2Ic9CpPut4PYzBB4eUXBcM984HD2XAWH4wkkhyewMM_xjFc2T0XJR43VOb-S7EPEbXJPyzgs1YcVWcUnwzitKzsJLhm9dFRzSFazXQ5pPVZIDOU9qdQnVvTRGcFwGuZTHdeMK5Xq4T7bnp3b0ePjgoCAAAAAUjXOUUA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
