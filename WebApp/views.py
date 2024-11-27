from django.shortcuts import render,redirect
from FApp.models import ProductDb,CategoryDb,BlogDb
from WebApp.models import ContactDb,SignupDb,CartDb,OrderDb
from django.contrib import messages
import razorpay

# Create your views here.
def home_page(request):
    categories = CategoryDb.objects.all()
    x = CartDb.objects.filter(Username=request.session['Name']).count()
    return  render(request,"Home.html",{'categories':categories,"x":x})

def Product_page(request):
    Products = ProductDb.objects.all()
    return render(request,"Products.html",{'Products':Products})

def about_page(request):
    return render(request,"about.html")

def contact_page(request):
    return render(request,"contact.html")

def save_page(request):
    if request.method == "POST":
        a = request.POST.get('firstname')
        b = request.POST.get('lastname')
        c = request.POST.get('email')
        d = request.POST.get('message')
        obj = ContactDb(Firstname=a,Lastname=b,Email=c,Message=d)
        obj.save()
    return redirect(contact_page)

def category_filter(request,cat_name):
    data = ProductDb.objects.filter(Selectproduct=cat_name)
    return render(request, "category_filtered.html",{'data':data})

def singleproduct(request,pro_id):
    data = ProductDb.objects.get(id=pro_id)
    return render(request,"single_product.html",{'data':data})

def displayblog(request):
    data = BlogDb.objects.all()
    return render(request,"display_blog.html",{'data':data})

def sign_up(request):
    return render(request,"sign_up.html")

def sign_in(request):
    return render(request,"sign_in.html")

def save_signup(req):
    if req.method == "POST":
        a = req.POST.get('name')
        b = req.POST.get('email')
        c = req.POST.get('mobile')
        d = req.POST.get('pass')
        e = req.POST.get('re_pass')
        obj = SignupDb(Name=a,Email=b,Mobile=c,Password=d,Re_password=e)
        if SignupDb.objects.filter(Name=a).exists():
            messages.warning(req,"User already exists...!")
            return redirect(sign_up)

        obj.save()
        messages.success(req, "Saved..!")
    return redirect(sign_in)

def user_login(request):
    if request.method == "POST":
        un = request.POST.get('name')
        pwd = request.POST.get('pass')
        if SignupDb.objects.filter(Name=un,Password=pwd).exists():
            request.session['Name']=un
            request.session['Password']=pwd
            messages.success(request, "Welcome..!")
            return redirect(home_page)
        else:
            messages.error(request, "Invalid Password..!")
            return redirect(sign_in)
    else:
        messages.error(request, "Invalid Username..!")
        return redirect(sign_in)

def user_logout(request):
    del request.session['Name']
    del request.session['Password']
    messages.success(request, "Logout Successfully..!")
    return redirect(sign_in)

def save_cart(request):
    if request.method == "POST":
        a = request.POST.get('username')
        b = request.POST.get('productname')
        c = request.POST.get('quantity')
        d = request.POST.get('price')
        e = request.POST.get('total')
        obj = CartDb(Username=a,Productname=b,Quantity=c,Price=d,Total_price=e)
        obj.save()
    return redirect(home_page)

def cart_page(request):
    data = CartDb.objects.filter(Username=request.session['Name'])
    subtotal = 0
    shipping = 0
    total_amount = 0
    for i in data:
        subtotal = subtotal + i.Total_price
        if subtotal>50000:
            shipping = 0
        else:
            shipping = 100
        total_amount = shipping + subtotal
    return render(request,"Cart.html",{'data':data,'subtotal':subtotal,
                                       'shipping':shipping,
                                       'total_amount':total_amount})

def delete_cart(req,del_id):
    x = CartDb.objects.filter(id=del_id)
    x.delete()
    return redirect(cart_page)

def checkout_page(request):
    data = CartDb.objects.filter(Username=request.session['Name'])
    subtotal = 0
    shipping = 0
    total_amount = 0
    for i in data:
        subtotal = subtotal + i.Total_price
        if subtotal > 50000:
            shipping = 0
        else:
            shipping = 100
        total_amount = shipping + subtotal

    return render(request,"Checkout.html",{'data':data,'subtotal':subtotal,
                                       'shipping':shipping,
                                       'total_amount':total_amount})

def save_order(request):
    if request.method == "POST":
        a = request.POST.get("name")
        b = request.POST.get("place")
        c = request.POST.get("address")
        d = request.POST.get("email")
        e = request.POST.get("mobile")
        f = request.POST.get("totalprice")
        g = request.POST.get("message")
        obj = OrderDb(Name=a,Place=b,Address=c,Email=d,Mobile=e,Totalprice=f,Message=g)
        obj.save()
    return redirect(payment)

def payment(request):
    customer = OrderDb.objects.order_by('-id').first()

    payy = customer.Totalprice

    amount = int(payy*100)

    payy_str = str(amount)

    for i in payy_str:
        print(i)
    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_MuWQaWpoGDgtsD','BVFlbt7yzBdwZ6u19nzXpKPB'))
        payment = client.order.create({'amount':amount,'currency':order_currency})

    return render(request,"Payment.html",{'customer':customer,'payy_str':payy_str})
