from django.shortcuts import render, redirect
from mainApp.services.productService import GetAllProducts, FindProductById
from mainApp.services.toppingService import GetAlltopping
from mainApp.services.cartService import GetCart as GC, AddProductInCart, GetCheck, GetProductsInCart, GetSum
from mainApp.EmailSander import EmailSender

# Create your views here.
def Main(request):
    products = GetAllProducts()
    return render(request, 'index.html', {'products':products})
def Product(request, product_id):
    product = FindProductById(product_id)
    toppings = GetAlltopping()
    return render(request, 'product.html', {"product":product,"toppings":toppings})
def AddInCart(request,product_id):
    AddProductInCart(product_id)
    return redirect('main')
def GetCart(request):
    context ={
        "products":GetProductsInCart(),
        "summ":GetSum()
    }
    return render(request, 'cart.html', context)

def SendEmail(request):
    if request.method == "POST":
        email = request.POST.get("email")
        cart = GC()
        cart.save()
        message = "GetCheck"
        emailSender = EmailSender(email)
        emailSender.SendEmail("Заказ ", message)
    return redirect('main')


