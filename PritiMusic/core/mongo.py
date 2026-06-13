from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

import config

from ..logging import LOGGER

# Agar URI nahi hai, toh code ko fail hone se bachayein
if not config.MONGO_DB_URI:
    LOGGER(__name__).warning("No MONGO DB URL found. Bot start nahi ho sakta!")
    # Yahan se bot ko exit kar dena chahiye kyunki bina DB ke ye nahi chalega
    exit() 
else:
    try:
        _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
        _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
        mongodb = _mongo_async_.Anon
        pymongodb = _mongo_sync_.Anon
        LOGGER(__name__).info("MongoDB Successfully Connected.")
    except Exception as e:
        LOGGER(__name__).error(f"MongoDB Connection Error: {e}")
        exit()
