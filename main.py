import json
import time

with open('int.json') as f:
   data = json.load(f)

def write():
    json_object = json.dumps(data, indent=4)
    with open("int.json", "w") as outfile:
        outfile.write(json_object)

def GetValidItems(item):
    element = item in data["items"]
    return element

def GetUserItems(user):
    keys = list(data["userdata"][user]["inventorys"].keys())
    values = list(data["userdata"][user]["inventorys"].values())
    return [keys] + [values]

def GetUserItem(user,item,boolorint):
    if(GetValidItems(item) == True):
        ex = item in data["userdata"][user]["inventorys"]
        if(ex == True):
            if(boolorint == "bool"):
                return True
            elif(boolorint == "int"):
                return data["userdata"][user]["inventorys"][item]

def RemoveItem(user,item, intorstr):
    if(GetValidItems(item) == True):
        if(type(intorstr) == str):
            del data["userdata"][user]["inventorys"][item]
        elif(type(intorstr) == int):
            if(int(GetUserItem(user,item,"int")) >= intorstr):
                if(int(GetUserItem(user,item,"int")) == intorstr):
                    del data["userdata"][user]["inventorys"][item]
                else:
                    q = data["userdata"][user]["inventorys"][item] - intorstr
                    data["userdata"][user]["inventorys"][item] = q
        write()

def GetUserMaxWeight(user):
    bag = data["userdata"][user]["bag"]
    bagSize = data["bags"][bag]["max-weight"]
    return bagSize

def GetItemWeight(item):
    return data["items"][item]["weight"]

def GetUserWeight(user):
    weight = 0
    invItems = list(data["userdata"][user]["inventorys"])
    for i in invItems:
        count = data["userdata"][user]["inventorys"][i]
        z = (count * GetItemWeight(i)) + weight
        weight = z
    return weight

def GiveUserItem(user,item,count):
    newuserweight = GetUserWeight(user) + (GetItemWeight(item) * count)
    oldcount = GetUserItem(user, item, "int")
    if(newuserweight < GetUserMaxWeight(user)):
        if(GetUserItem(user,item,"bool") == True):
            data["userdata"][user]["inventorys"][item] = oldcount + count
        else:
            data["userdata"][user]["inventorys"][item] = count
        write()