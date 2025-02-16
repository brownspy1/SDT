
db = {
    "DB01":{"name":"Mahadi","roll":"743678"}
}

db["DB02"] = {"name":"Mahir","roll":"789654"}
for i,j in db.items():
    print(f"{i} {j["name"]} {j["roll"]} ")
uniq_id = "DB01"
print(db.get("DB03",{}).get("name","Not found!"))
print(db.get("DB02",{}).keys())
print(db.get(uniq_id,{}).values())
for i,j in db.get(uniq_id,{}).items():
    print(i," ",j)
# db.update({uniq_id:{"name":"munnah","roll":"74526"}})
db[uniq_id].update({"name":"mahmud"}) 
print(db.get(uniq_id,{}).values())
