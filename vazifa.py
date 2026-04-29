import os
os.system("cls")

# 1.m
# cars = {
#     "Malibu": 35000,
#     "Spark": 12000,
#     "Cobalt": 18000,
#     "Tracker": 28000
# }

# a = list(cars.values())
# print(a)
# print(sum(a)/len(a))

# s  = max(a)
# b = min(a)
# print("Eng qimmat avtomobil: ",s)
# print("Eng arzon avtomobil: ",b)


# 2.m
# movies = {
#     "Titanic": 1997,
#     "Avatar": 2009,
#     "Inception": 2010,
#     "Interstellar": 2014
# }
# list2 = []
# a = list(movies.values())

# for i,j in movies.items():
#     if j>=2000:
#         list2.append(i)
# print(list2)


# 3.m
# speed = {
#     "Tesla": 250,
#     "BMW": 240,
#     "Mercedes": 260,
#     "Audi": 230
# }
# a = list(speed.values())
# a.sort()
# a = a[::-1]
# for i in a:
#     for d,k in speed.items():
#         if k==i:
#             print(f"{d}:{i}")
 
# 4.m
# professions = {
#     "Bill Gates": "Dasturchi",
#     "Cristiano Ronaldo": "Futbolchi",
#     "Elon Musk": "Tadbirkor",
#     "Messi": "Futbolchi"
# }
# a = input("Ism kriting: ")

# b = professions.get(a)

# if b:
#     print(f"{a}ning kasbi {b}")
# else:
#     print("Bunday ism yoq?")


# 5.m
# car_count = {
#     "Chevrolet": 120,
#     "Toyota": 95,
#     "BMW": 60,
#     "Kia": 75
# }

# a = list(car_count.values())

# d = max(a)
# s = min(a)


# for i,j in car_count.items():
#     if j == d:
#         print("Eng kop sotilgani: ",i)
#     if j == s:
#         print("Eng kam sotilgani: ",i)


# 6.
# books = {
#     "O'tkan kunlar": {
#         "muallifi": "Abdulla Qodiriy",
#         "janri": "Roman",
#         "chop etilgan yili": 1926,
#         "tarjimalar soni": 5
#     },
#     "Mehrobdan chayon": {
#         "muallifi": "Abdulla Qodiriy",
#         "janri": "Roman",
#         "chop etilgan yili": 1929,
#         "tarjimalar soni": 3
#     },
#     "Kecha va kunduz": {
#         "muallifi": "Cho'lpon",
#         "janri": "Roman",
#         "chop etilgan yili": 1934,
#         "tarjimalar soni": 4
#     },
#     "Sarob": {
#         "muallifi": "Abdulla Qahhor",
#         "janri": "Roman",
#         "chop etilgan yili": 1935,
#         "tarjimalar soni": 2
#     },
#     "Ulug'bek xazinasi": {
#         "muallifi": "Odil Yoqubov",
#         "janri": "Tarixiy roman",
#         "chop etilgan yili": 1974,
#         "tarjimalar soni": 6
#     },
#     "Don Kixot": {
#         "muallifi": "Migel de Servantes",
#         "janri": "Roman",
#         "chop etilgan yili": 1605,
#         "tarjimalar soni": 50
#     },
#     "Urush va tinchlik": {
#         "muallifi": "Lev Tolstoy",
#         "janri": "Tarixiy roman",
#         "chop etilgan yili": 1869,
#         "tarjimalar soni": 45
#     },
#     "Alkimyogar": {
#         "muallifi": "Paulo Koelyo",
#         "janri": "Falsafiy roman",
#         "chop etilgan yili": 1988,
#         "tarjimalar soni": 80
#     },
#     "1984": {
#         "muallifi": "Jorj Oruell",
#         "janri": "Antiutopik roman",
#         "chop etilgan yili": 1949,
#         "tarjimalar soni": 65
#     },
#     "Kichkina shahzoda": {
#         "muallifi": "Antuan de Sent-Ekzyuperi",
#         "janri": "Falsafiy ertak",
#         "chop etilgan yili": 1943,
#         "tarjimalar soni": 300
#     }
# }
