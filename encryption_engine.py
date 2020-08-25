import re
import csv
from hashlib import sha256

__author__ = "hemanthmb3110"
__version__ = 1.0


DBF = ["Name","Email","Phone","Password","Hash"]
UIF = ["AppName", "Passcode"]


def recognize(name,email,phone,password,dob=None) -> str:
    vault = open("database.db", "r+")
    reader = csv.DictReader(vault, fieldnames=["Name","Email","Phone","Password","Hash"])
    for row in reader:
        if row.get("Email") == grind(email):
            return "Account with the given email id already exists!"
        if row.get("Phone") == grind(phone):
            return "Account with the given phone number already exists!" 
    vault.close()
    if re.search(r"[a-zA-Z\.]{1,}[a-zA-Z \.]*", name) == None:
        return "Invalid Name"
    if re.search(r"[a-z0-9_]*@[a-z0-9\.\-]*", email) == None:
        return "Invalid Email"
    if re.search(r"\d{10}", phone) == None:
        return "Invalid Phone Number"
    name = grind(name)
    email = grind(email)
    phone = grind(phone)
    password = grind(password)
    hpass = sha256(bytes(password, "utf-8")).hexdigest()
    info = {"Name":name, "Email":email, "Phone":phone,"Password":password,"Hash":hpass}
    print(f"N:{name},E:{email},PN:{phone},P:{password},hp:{hpass}") 
    with open("database.db", 'a') as vault:
        writer = csv.DictWriter(vault,fieldnames=DBF)
        writer.writerow(info)
    return "Account Created!"
    
def grind(val) -> str:
    newval = ""
    for i in val:
        if i.isdigit():
            newval += str(int(i)+31)
        elif i.islower() and not i.isdigit():
            newval += chr(122 - (ord(i) - 97))
        elif not i.isdigit():
            newval += chr(90 - (ord(i) - 65))
        else:
            newval += i
    return newval

def validate(email, password) -> bool:
    with open("database.db", 'r') as vault:
        reader = csv.DictReader(vault, fieldnames=DBF)
        for row in reader:
            if row["Email"] == grind(email):
                if row["Password"] == grind(password):
                    return True
    return False

def get_user_cred(email):
    fname = who_is(email)
    rlist = []
    fh = open(fname, 'r')
    reader = csv.DictReader(fh, fieldnames=UIF)
    i=1
    for row in reader:
        temp = []
        temp.append(row["AppName"])
        temp.append(row["Passcode"])
        i+=1
        rlist.append(temp)
    fh.close()
    return rlist

def add_to_vault(email, appname, password) -> bool:
    fname = who_is(email)
    credential = {"AppName": appname, "Passcode": password}
    try:
        with open(fname, 'a') as vault:
            writer = csv.DictWriter(vault, fieldnames=UIF)
            writer.writerow(credential)
        return True
    except :
        return False
      
def who_is(credential_name,id="Email"):
    with open("database.db", 'r') as f:
        reader = csv.DictReader(f, fieldnames=DBF)
        for row in reader:
            if row[id] == grind(credential_name):
                return row["Hash"]+".db"

def main():
    pass

if __name__ == "__main__":
    main()