from ..models import Topping
toppings = [Topping(1,"кетчуп", 30.0),
            Topping(2,"Сметана", 30.0)]
def GetAlltopping() -> list:
    print("Подключение к БД")
    return toppings
