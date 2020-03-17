class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def isFull(self):
        return len(self.items) == 4

    def size(self):
        return len(self.items)


def arrive(soi, carNo):
    if not soi.isFull():
        # เอารถเข้ามาจอดได้
        soi.push(carNo)
        print("car", carNo, "arrive", '\t\t', "space left", 4-soi.size())
    else:
        # ซอยเต็มแล้ว
        print("car", carNo, "cannot arrive : SOI FULL")

def depart(soi, soi_temp, carNo):
    if not soi.isEmpty():
        # มีรถอยู่ (ซอยไม่ว่าง), เอารถออกได้
        if carNo in soi.items:
            # เอารถคันที่ต้องการออกได้
            while not soi.peek() == carNo:
                # ที่ peek อยู่ ไม่ใช่รถคันที่ต้องการ
                car_pop = soi.pop()
                soi_temp.push(car_pop)
                print("pop", car_pop)
            print("pop", soi.pop())
            # เอารถจากซอย ข กลับมาซอย ก
            while not soi_temp.isEmpty():
                car_pop = soi_temp.pop()
                soi.push(car_pop)
                print("push", car_pop)
            print("space left", 4-soi.size())
        else:
            print("car", carNo, "cannot depart: No car", carNo)
    else:
        # ซอยว่าง ไม่มีรถ
        print("car", carNo, "cannot depart: soi empty")

soi_a = Stack() # ซอยของนาย ก
soi_b = Stack() # ซอยของนาย ข

depart(soi_a, soi_b, 6)
arrive(soi_a, 1)
arrive(soi_a, 2)
arrive(soi_a, 3)
arrive(soi_a, 4)
arrive(soi_a, 5)
print("print soi =", soi_a.items)
depart(soi_a, soi_b, 7)
depart(soi_a, soi_b, 2)
print("print soi =", soi_a.items)