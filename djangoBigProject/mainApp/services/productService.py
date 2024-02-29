from ..models import Product
imgs = ["https://www.gotovim.ru/pics/sbs/pelmeny/rec.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpokqCNZPzrHdGKXwsefXJIy6IuFYNIZHlFg&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd1ho7vu2SONOjCzKO_u_k6cvX96B53Vd8zw&usqp=CAU"]
products = [Product(1,150.0, "Медвежье ухо", "Пельмени вкусные",imgs[0]),
                Product(2,250.0, "Вятское ухо","Пельмени вкусные", imgs[1]),
                Product(3,100.0, "Татарские","Пельмени вкусные", imgs[2])]
def GetAllProducts() -> list:
    return Product.objects.all()
def FindProductById(id:int) -> Product:
    return Product.objects.get(id=id)

