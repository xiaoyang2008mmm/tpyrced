import peewee
import json
from db import *

from playhouse.shortcuts import model_to_dict, dict_to_model

user = TpyrcedClerk.select().get()

json_data = json.dumps(model_to_dict(user))
