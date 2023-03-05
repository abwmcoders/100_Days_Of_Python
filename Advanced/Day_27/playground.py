def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


def calulate(**kwargs):
    for key, values in kwargs.items():
        print(f"{key}:{values}")


class Cars:
    def __init__(self, **kwargs):
        #self.model = kwargs["model"]
        #self.make = kwargs["make"]

        #  ------ Better solution to avoid error
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.sits = kwargs.get("sits")

#a = (2,4,5,6,7,8,9,9,00,0,1,2,5,6,7,78,990,76)
result = add(2,3,4,5,6,7,8)
print(calulate(add=4, mul=5, div=8, min=6))
#result1 = add(a)
print(result)
#print(result1)

my_car = Cars(make= "GT-R")
print(my_car.model)
