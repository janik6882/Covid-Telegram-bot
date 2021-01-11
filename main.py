# -*- coding: utf-8 -*-
import json
from Bot import *
creds = json.load(open("creds.json", "r"))
bot = Wrapper(creds["token"])
