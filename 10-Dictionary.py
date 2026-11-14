
# key: value pair, mutable , key must be mutable

a= {
   "name":"salman",
   "joined":"2024",
   2:"?",
   (1,2,3):[2,3]
}
print(a["name"])
print(a.get('joined'));

for key in a.keys():
   print(key)

for value in a.values():
   print(value)

for item in a.items():
   print(item)
