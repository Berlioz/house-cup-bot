import ast
import os
import pickle
import mod
import marriages
import pact
from constants import *


IS_TEST_ENV = os.environ.get("IS_TEST_ENV")

DATA_FILE = "data.json"
if IS_TEST_ENV:
    DATA_FILE = "test_data.json"


def load_old_participants():
    global participants
    global servers

    with open(DATA_FILE, 'rb') as f:
        data = pickle.load(f)
        servers = data["servers"]
        participants = data["participants"]
        mod.imprisoned = data["imprisoned"]
        mod.voting = data["voting"]
        marriages.proposals = data["proposals"]
        marriages.marriage_info = data["marriage_info"]
        pact.pacts = data["pacts"]
        pact.failed_pacts = data["failed_pacts"]
        pact.finished_pacts = data["finished_pacts"]


def save_participants():
    with open(DATA_FILE, 'wb') as f:
        data = {
            "members": {},
            "participants": participants,
            "servers": servers,
            "imprisoned": mod.imprisoned,
            "voting": mod.voting,
            "proposals": marriages.proposals,
            "marriage_info": marriages.marriage_info,
            "pacts": pact.pacts,
            "failed_pacts": pact.failed_pacts,
            "finished_pacts": pact.finished_pacts
        }
        pickle.dump(data, f)


load_old_participants()

save_participants()
