from flask import Flask, request
import pickle
import os.path
import sys

app = Flask(__name__)

import sys
if len (sys.argv) != 2 :
    print("Usage: python counter.py <urlMap.pkl> ")
    sys.exit (1)

file_name=sys.argv[1]
urlMap = {}


def save_obj(obj, name ):
    with open( name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open( name, 'rb') as f:
        return pickle.load(f)

@app.route("/")
def help():
    return "Running"

@app.route("/api/<prefix>")
def main(prefix):
    global urlMap
    key = prefix
    if prefix in urlMap:
        urlMap[prefix] = urlMap[prefix] + 1
        save_obj(urlMap, file_name)
        return '{0:02d}'.format(urlMap[prefix])
    else:
        urlMap[prefix] = 1
        save_obj(urlMap, file_name)
        return '{0:02d}'.format(urlMap[prefix])
    return "Prefix: %s" % prefix

if os.path.isfile(file_name):
    urlMap = load_obj(file_name)

app.run('0.0.0.0', 5000)
