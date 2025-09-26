import os
import logging
from pymongo import MongoClient, errors

try:
	from dotenv import load_dotenv
	load_dotenv()  # load from .env if python-dotenv is available
except Exception:
	# python-dotenv not installed; proceed using environment variables only
	pass

"""MongoDB helper that reads MONGO_URI and MONGO_DB from env/.env.

Defaults to mongodb://localhost:27017/ and database name 'hope_bridge'
so it matches the Django `DATABASES` setting in `hope_bridge/settings.py`.
This module attempts a quick ping on import and logs the outcome.
"""

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
# prefer explicit MONGO_DB, fall back to Django-like default 'hope_bridge'
MONGO_DB = os.getenv("MONGO_DB") or "hope_bridge"

logger = logging.getLogger(__name__)
if not logger.handlers:
	logging.basicConfig(level=logging.INFO)

client = None
db = None

try:
	# short server selection timeout so failures surface quickly in dev
	client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
	# force a quick round-trip to make sure connection is valid
	client.admin.command("ping")
	db = client[MONGO_DB]
	logger.info("Connected to MongoDB at %s, using DB '%s'", MONGO_URI, MONGO_DB)
except Exception as e:
	# keep client/db as None so callers can handle missing connection
	logger.exception("Failed to connect to MongoDB at %s: %s", MONGO_URI, e)


def get_db(raise_on_missing: bool = True):
	"""Return the connected database object or raise a helpful error.

	raise_on_missing: if True, raises a RuntimeError when no DB is connected.
	"""
	if db is None and raise_on_missing:
		raise RuntimeError(
			"MongoDB not connected. Check MONGO_URI/MONGO_DB and that the server is running."
		)
	return db