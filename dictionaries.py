thisdict =	{
  "brand": "moto",
  "model": "2nd gen",
  "year": 2016
}
print(thisdict)


#Accessing Items

thisdict =	{
  "brand": "moto",
  "model": "2nd gen",
  "year": 2016
}
x = thisdict["model"]
print(x)

#Accessing Item in another method

thisdict =	{
  "brand": "moto",
  "model": "2nd gen",
  "year": 2016
}
x = thisdict.get("model")
print(x)

#Change Values

thisdict =	{
  "brand": "moto",
  "model": "2nd gen",
  "year": 2016
}
thisdict["year"] = 2020
print(thisdict)

#Copy a Dictionary

thisdict = {
  "brand": "moto",
  "model": "2nd gen",
  "year": 2016
}
mydict = thisdict.copy()
print(mydict)

