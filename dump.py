import json
import os
import shutil

INDEX_FILE = r"./indexes/1.8.json"

OBJECTS_FOLDER = r"./objects"

OUTPUT_FOLDER = r"./1.8"


def checkFolder(folder):
  if not os.path.exists(folder):
    os.makedirs(folder)

def checkFileFolder(file):
  rindex = file.rindex("/")
  folder = file[:rindex]
  # print(f"{file} {folder}")
  checkFolder(folder)


checkFolder(OUTPUT_FOLDER)


with open(INDEX_FILE,"r") as f:
  json_dict = json.load(f)
  for kv in json_dict["objects"].items():
    key,dict2 = kv
    _hash, size = dict2["hash"], dict2["size"]

    src = OBJECTS_FOLDER + "/" + _hash[:2] + "/" + _hash
    dst = OUTPUT_FOLDER + "/" + key.replace("/","_")

    checkFileFolder(dst)

    if key.endswith("ogg"):
      shutil.copy(src, dst)

    # print(f"key {key}, hash {_hash}, size {size}")
    print(f"src {src}, dst {dst}")





