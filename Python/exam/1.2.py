class Shoes:
    def __init__(self, brand, price, color, size, quantity):
        self.brand = brand
        self.price = price
        self.color = color
        self.size = size
        self.quantity = quantity

    def __repr__(self):
        return f"Brand: {self.brand} Price: {self.price} Color: {self.color} Size: {self.size} Quantity: {self.quantity} \n"

    def Sale(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
        else:
            print("There is no enough quantity!")

    def Purchase(self, quantity):
        self.quantity += quantity


def sort_price(shoes):
    shoes.sort(key=lambda x: x.price, reverse=True)
    for shoe in shoes:
        shoe.__repr__()


def shoes_searching(shoes, brand, size):
    sum = 0
    c = 0
    for s in shoes:
        sum += s.price
        c += 1
    averagePrice = sum / c
    newlist = []
    for i in range(len(shoes)):
        if shoes[i].size == size and shoes[i].brand == brand and shoes[i].price < averagePrice and shoes[
            i].quantity > 0:
            newlist.append(shoes[i])
    return newlist


def cheapest_shoes(shoes, color):
    newlist = []
    for i in range(len(shoes)):
        if shoes[i].color == color and shoes[i].quantity > 0:
            newlist.append(shoes[i])
        else:
            continue
    if len(newlist) != 0:
        newlist.sort(key=lambda x: x.price)
        print(newlist[0])
    else:
        print("Color is not available")
        colors = []
        for shoe in shoes:
            if shoe.quantity > 0 and shoe.color not in colors:
                colors.append(shoe.color)
        print(colors)


def delete_shoes(shoes, brand):
    for shoe in shoes:
        if shoe.brand == brand:
            shoes.remove(shoe)
        else:
            continue


shoes_list = []
shoes_list.append(Shoes("puma", 120, "black", 37, 5))
shoes_list.append(Shoes("nike", 150, "white", 36, 8))
shoes_list.append(Shoes("puma", 10, "black", 40, 10))
shoes_list.append(Shoes("china", 20, "green", 39, 2))
shoes_list.append(Shoes("germany", 50, "white", 37, 9))
shoes_list.append(Shoes("nike", 90, "blue", 45, 5))
shoes_list.append(Shoes("adidas", 70, "white", 36, 3))

print(shoes_list)

sort_price(shoes_list)
print(shoes_list)

print(shoes_searching(shoes_list, "puma", 40))

cheapest_shoes(shoes_list, "brown")

delete_shoes(shoes_list, "china")
print(shoes_list)
