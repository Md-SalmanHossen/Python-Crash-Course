# mutable: ordered,duplicate allowed,heterogeneous
# append = last add
# insert(i,x) = particular value add
# pop(i) = delete with index
# remove(x) = specific value delete

arr = ["apple",'orange',100,5,5.7,[3,1],(5,6)]
print(len(arr));

print(type(arr),"\n")
print(f"print the value: {arr[4]} , {arr[5][0]} , {arr[5][1]}\n")


arr.append("grape")
print(f"after append: {arr}\n");

arr.insert(0,"potato")
print(arr,"\n")

print(arr.pop(2),"\n")

print(arr)

arr.remove(5.7);
print(arr)


print(len(arr))


if 'grape' in arr:
   print(f"did not found grape\n")
if 'orange' not in arr:
   print(f"orange found \n")

# arr[start:end:step]- start inclusive,end exclusive , [::-1] = reverse

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
print(arr[::-1]); #reverse number

print(arr[1:5],"\n") # print 4,6,8,10

a=[]
for i in range(0,5):
   x=int(input())
   a.append(x)
print(a,"\n")


foo=[1,2,4]
bar=foo
bar.append(4);
print(f"foo : {foo} , bar: {bar}\n")



foo=[1,2,3]
bar=foo.copy()
bar.append(5)
print(f"foo: {foo} , bar: {bar}\n")


