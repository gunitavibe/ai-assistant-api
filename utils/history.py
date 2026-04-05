import json

HISTORY_FILE = "data/history.json"

def load_history():
    try:
        with open(HISTORY_FILE,"r") as f:
            return json.load(f)
    except:
        return[]

def save_history(history):
     with open(HISTORY_FILE , "w") as f:
        return json.dump(history,f,indent = 2)
     
def clear_history():
    with open(HISTORY_FILE,"w") as f:
        json.dump([],f)     
