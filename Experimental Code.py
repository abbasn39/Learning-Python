# Set_F = {1, 2, 3}
# l=[[2,3],[4,5],[6,7]]
#
# # print(l[0])
# # for x in l[0]:
# #     for a in x:
# #         print (a)
#
# # print(l[0][0])
# # for x in l[0:1]:
# #     for a in x:
# #         print(a)
# #         break

Dict1={"A":1,"B":2,"C":3}
Dict2={"A":2,"B":3,"C":4}
for item,x in Dict1.items():            #Dict1.items() returns key-value pairs as tuples
    a = x
    break
print("a",a)

for item,x in Dict2.items():            #Dict1.items() returns key-value pairs as tuples
    b = x
    break
print("b",b)

if a > b:
    print(a)
else:
    print(b)