import json
import time
import traceback
import math
from statistics import mean

FILE=r"REA3049_Karakter_6_PY1\REA3049_Karakter_6_PY\IT_Eksamen\googleplaystore.json"

def categoryPresentation(category, data):
    '''return a string containing a presentation of a given category from data'''

    # get apps in category
    apps = [i for i in data if i["Category"] == category]

    # get rating and installs of apps in category
    # assuming that an app with e.g. "1,000+" installs has 3,000 installs on average
    ratings=[i["Rating"] for i in apps if not math.isnan(i["Rating"])]
    installs = [i["Installs"]*3 for i in apps]

    # get most popular apps in category
    appInstallations={}
    [appInstallations.update({i["App"] : i["Installs"]}) for i in apps]
    appnames=[i["App"] for i in apps]
    appnames.sort(key=appInstallations.get)

    return f'''------------------------------
            {category}
------------------------------
Average Rating:   {mean(ratings):.2f}
Average Installs: {mean(installs):,.0f}

Top 3 apps:
    {appnames[-1]}
    {appnames[-2]}
    {appnames[-3]}

'''



# Parse JSON from file
data=[]
with open(FILE, encoding="utf-8") as f:
    data=json.load(f)

# Convert to fitting datatypes
for i in data:
    try:
        _i=i
        _i["Rating"]=float(i["Rating"])
        _i["Reviews"]=int(i["Reviews"])
        sizePostfix=i["Size"][-1]
        POSTFIX_TRANS={"k":1000,"M":1000000}
        _i["Size"] = None if i["Size"] == "Varies with device" else float(i["Size"][:-1])*POSTFIX_TRANS[sizePostfix]
        _i["Installs"] = 0 if i["Installs"] == "0" else int(i["Installs"][:-1].replace(",",""))
        _i["Free"] = i["Type"] == "Free"
        del _i["Type"]
        _i["Price"] = 0 if i["Price"] == "0" else float(i["Price"][1:])
        _i["Last Updated"]=time.strptime(i["Last Updated"], "%B %d, %Y")
        i=_i
    except:
        # Error in dataset
        print(f"\033[33m[?]\033[m Error in dataset, application name: {i['App']}")
        traceback.print_exc()

# Remove duplicates
_data = []
[_data.append(i) for i in data if i not in _data]
data = _data

# Count apps in category
categoryCount={}
for i in data:
    category = i["Category"]
    if category in categoryCount:
        categoryCount[category] += 1
    else:
        categoryCount[category] = 1

# Sort list of categories
categories=list(categoryCount.keys())
categories.sort(key=categoryCount.get)


for i in range(1,4):
    print(categoryPresentation(categories[-i], data))