info = {
    "key": "Value",
    "name": "Abdul Moiz",
    "subject": ["Python","C","Java"],
    "topics" : ("dict","set"),
    "age": 19,
    12.4: 1.5
}

print(type(info))

print(info["name"])
print(info["subject"])
print(info["topics"])
print(info["age"])
print(info[12.4])


info["name"] = "Bhatti"

print(info)

info["status"] = True

print(info)


student ={
    "name" : "Abdul Moiz",
    "subject" : {
        "phy":46,
        "chem":46,
        "math" : 87
    }
}


print(student["subject"]["phy"])

print(len(list(student.keys())))

print(list(student.values()))

pairs = list(student.items())

print(pairs[0])


print(student.get("name"))  #Error
print(student["name"])    # no Error -> None

student.update({"city": "Lahore  "})

