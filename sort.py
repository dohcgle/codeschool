cars = {"BMW": 525000, "Audi": 632000, "Honda": 612000, "Mazda": 632000, "Ford": 710000}

for i in sorted(cars.items(), key=lambda kv: kv[1]):
    print(i)

for v, k in sorted(zip( cars.values(), cars.keys() )):
    print(k, v)
