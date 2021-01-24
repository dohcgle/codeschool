cars = {"BMW": 525000, "Audi": 632000, "Honda": 612000, "Mazda": 632000, "Ford": 710000}

def fun(a, b):
    if a > b:
        return True
    elif a < b:
        return False
    else:
        return a + b
summ = fun(1,1)
print(summ)


# def func(a, d, b=2):
#     a + b - d
#     return a + b - d
# summa = func(3,1)

# print(summa)

# def set_order(order):
#     menu = ["Choy", "Kofe", "Shakar", "Limon", "Sut", "Kompot"]
#     for i in menu:
#         ask = input(f"Вы хотите {i}: y/n ")
#         if ask == "y":
#             order.append(i)

# def main():
#     order = []
#     while True:
#         set_order(order)
#         ask = input(f"Заказ верен {order}: y/n ")
#         if ask == "y":
#             print("Заказ принят")
#             break
#         elif ask == "n":
#             ask = input("Презакажите? ")
#             if ask == "y":
#                 continue
#             else:
#                 exit()
    
# main()

# i=10
# while True:
#     print(i)
#     i -= 1
#     if i == 4:
#         print('Hi')
#         continue
#     if i == 1:
#         break
    



# for i in menu:
#     print(i)


# for k, v in cars.items():
#     print(k, v)