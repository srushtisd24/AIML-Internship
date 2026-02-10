contact={
    "druvi":"6738288687",
    "druti":"7832968989",
    "deepti":"3487927968"
}

contact["drisha"]="6782984372"
print(contact)
contact["druti"]="5643675434"
print(contact)

if contact.get("druvi") is not None:
    print("contact found")
    print("druvi:",contact["druvi"])
else:
    print("contact not found")
    
if contact.get("drushti") is not None:
    print("key Exist")
else:
    print("contact not found")
    
for key,value in contact.items():
    print(key,":",value)
    