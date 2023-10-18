#set data type
#implict
a = {"a","b","c"}
print(a)

#explict
a = set(("a","b","c"))
print(type(a))

#data type/variable annotation
a : set = {"a","b","c"}
print(type(a))

#crud operations
#create
#add

a : set = {"a","b","c"}
a.add(4)
print(a)

#update
a : set = {"a","b","c"}
b : set = {"d","a","c"}
a.update(b)
print(a)

#delete
#remove
a : set = {"a","b","c"}
a.remove("a")
print(a)

#discard
a : set = {"a","b","c"}
a.discard("c")
print(a)

a : set = {"1","2","3"}
a.discard("4")
print(a)

#pop
a : set = {"1","2","3"}
a.pop()
print(a)

#some set methods
#union
a:set={"1","2","3"}
b:set={"2","4","5"}
print(a.union(b))

#intersection
a:set={"1","2","3"}
b:set={"2","4","5"}
print(a.intersection(b))

