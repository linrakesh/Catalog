from django.shortcuts import render
from .models import orderItem
from .forms import OrderfCreateForm
from cart.cart import Cart

# Create your views here.

class order_create(request):
    cart = Cart(request)
    if request.method=='POST':
        form = OrderfCreateForm(request.FORM)
        if form.is_valid():
            order = form.save()
            for item in cart:
                orderItem.objects.create(order=order,product =item['product'],price=item['price'],quantity=item['quantity'] )
            cart.clear()
            return render(request,'orders/order/created.html',{'order':order})
    else:
        form = OrderfCreateForm()
        return render(request,'orders/order/creat.html',{'cart':cart,'form':form})
