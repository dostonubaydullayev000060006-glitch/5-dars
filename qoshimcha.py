import os 
os.system("cls")

# 1.m
# mahsulotlar = ["olma", "banan", "anor", "olma", "uzum", "olma"]
# mahsulotlar.pop(0)
# print(mahsulotlar[::-1])


# 2.m
# baholar = [56, 89, 72, 91, 64, 77, 88]
# lst2 = []
# a = max(baholar)
# print("Eng kattasi: ",a)
# b = min(baholar)
# print("Eng kichigi: ",b)

# for i in baholar:
#     if i%2==0:
#         lst2.append(i)
# print("Juft baholar: ",lst2)


# 3.m
# fanlar = ("Matematika", "Biologiya", "Tarix")
# vaqt = ("10:00", "11:00")

# birlash = fanlar + vaqt
# print(birlash)


# 4.m
# A = {"futbol", "basketbol", "tennis"}
# B = {"tennis", "shaxmat", "futbol"}

# a = A.intersection(B)
# print("Umumiy: ",a)
# b = A.difference(B)
# print("Faqat A da: ",b)


# 5.m
# fanlar = ("Matematika", "Fizika", "Kimyo")
# baholar = (5, 4, 5)

# birlashma = fanlar + baholar
# print("Birlashgan :",birlashma)

# a = fanlar.index("Fizika")

# print("Fizika  bahosi: ",baholar[a])
# print("Oxirgi 3 ta: ",birlashma[-3::])


# 6.m
# shaharlar = ("Toshkent", "Samarqand", "Buxoro")
# aholi = (3000000, 600000, 300000)

# birlash = shaharlar + aholi
# print("Birlashgan: ",birlash)

# i = shaharlar.index("Buxoro")
# print("Buxaro aholisi: ",aholi[i])
# print("Shaharlar qismi: ",birlash[::3])


# 7.m
# narxlar = {
#     "olma": 8000,
#     "banan": 12000,
#     "uzum": 15000,
#     "anor": 9000
# }
# list2 = []

# for i,j in narxlar.items():
#     if j>=10000:
#         list2.append(i)
# print(list2)


# 8.m
# narxlar = {
#     "olma": 5000,
#     "shaftoli": 7000,
#     "gilos": 12000
# }

# a = max(narxlar , key = narxlar.get)
# print(a)


# 9.m
# ballar = {
#     "Ali": 70,
#     "Vali": 85,
#     "Sami": 60
# }
# dict2 = {}
# for i,j in ballar.items():
#     dict2 .update({i:j+5})
# print(dict2)


# 10.m
# baholar = {
#     "Ali": 80,
#     "Vali": 90,
#     "Sami": 70
# }
# a=0
# s=0
# for i,j in baholar.items():
#     a+=j
#     s+=1
# print("Ortacha: ",a/s)