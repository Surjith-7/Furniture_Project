from django.shortcuts import render,redirect
from FApp.models import CategoryDb,ProductDb,BlogDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from WebApp.models import ContactDb
from django.contrib import messages

# Create your views here.
def add_page(req):
    return render(req, "index.html")

def add_category(req):
    return render(req,"Add_category.html")

def save_category(req):
    if req.method == "POST":
        a = req.POST.get('categoryname')
        img = req.FILES['image']
        b = req.POST.get('description')
        obj = CategoryDb(Categoryname=a,Description=b,Categoryimage=img)
        obj.save()
        messages.success(req,"Category saved...!")
    return redirect(add_category)

def edit_category(req,edit_id):
    data = CategoryDb.objects.get(id=edit_id)
    return render(req,"Edit_category.html",{'data':data})

def display_category(req):
    data = CategoryDb.objects.all()
    return render(req,"display_category.html",{'data':data})

def update_category(req,up_id):
    if req.method == "POST":
        a = req.POST.get('categoryname')
        b = req.POST.get('description')
    try:
        img = req.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    except MultiValueDictKeyError:
        file = CategoryDb.objects.get(id=up_id).Categoryimage
    CategoryDb.objects.filter(id=up_id).update(Categoryname=a,Description=b,Categoryimage=file)
    messages.success(req, "Update Success...!")
    return redirect(display_category)

def delete_category(req,del_id):
    x = CategoryDb.objects.filter(id=del_id)
    x.delete()
    messages.error(req, "Category Deleted...!")
    return redirect(display_category)


def add_product(req):
    data = CategoryDb.objects.all()
    return render(req,"Add_products.html",{'data':data})

def save_products(req):
    if req.method == "POST":
       a = req.POST.get('select')
       b = req.POST.get('productname')
       c = req.POST.get('quantity')
       d = req.POST.get('mrp')
       e = req.POST.get('description')
       f = req.POST.get('country')
       g =  req.POST.get('manufactured')
       img1 = req.FILES['image1']
       img2 = req.FILES['image2']
       img3 = req.FILES['image3']
       obj = ProductDb(Selectproduct=a,Productname=b,Quantity=c,Mrp=d,Description=e,Country=f,Manufactured=g,Productimage1=img1,Productimage2=img2,Productimage3=img3)
       obj.save()
       messages.success(req, "Product saved...!")
    return redirect(add_product)

def display_product(req):
    data = ProductDb.objects.all()
    return render(req,"display_products.html",{'data':data})

def edit_product(req,edit_id):
    pro = ProductDb.objects.get(id=edit_id)
    data = CategoryDb.objects.all()
    return render(req,"edit_product.html",{'pro':pro,'data':data})

def update_product(req,up_id):
    if req.method == "POST":
       a = req.POST.get('select')
       b = req.POST.get('productname')
       c = req.POST.get('quantity')
       d = req.POST.get('mrp')
       e = req.POST.get('description')
       f = req.POST.get('country')
       g =  req.POST.get('manufactured')
    try:
        img1 = req.FILES['image1']
        fs = FileSystemStorage()
        file1 = fs.save(img1.name, img1)
    except MultiValueDictKeyError:
        file1 = ProductDb.objects.get(id=up_id).Productimage1
    try:
        img2 = req.FILES['image2']
        fs = FileSystemStorage()
        file2 = fs.save(img2.name, img2)
    except MultiValueDictKeyError:
        file2 = ProductDb.objects.get(id=up_id).Productimage2
    try:
        img3 = req.FILES['image3']
        fs = FileSystemStorage()
        file3 = fs.save(img3.name, img3)
    except MultiValueDictKeyError:
        file3 = ProductDb.objects.get(id=up_id).Productimage3
    ProductDb.objects.filter(id=up_id).update(Selectproduct=a,Productname=b,Quantity=c,Mrp=d,Description=e,Country=f,Manufactured=g,Productimage1=file1,Productimage2=file2,Productimage3=file3)
    messages.success(req, "Update Success...!")
    return redirect(display_product)

def delete_product(req,del_id):
    x = ProductDb.objects.filter(id=del_id)
    x.delete()
    messages.error(req,"Product Deleted..!")
    return redirect(display_product)

def admin_page(req):
    return render(req,"admin_login.html")

def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('name')
        ps = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=ps)
            if user is not None:
                login(request,user)
                request.session['username'] = un
                request.session['password'] = ps
                messages.success(request, "Welcome...!")
                return redirect(add_page)
            else:
                messages.error(request, "Incorrect Password...!")
                return redirect(admin_page)
        else:
            messages.warning(request, "Invalid Username...!")
            return redirect(admin_page)
    else:
        return redirect(admin_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully...!")
    return redirect(admin_page)

def contact_details(request):
    contact = ContactDb.objects.all()
    return render(request,"contact_data.html",{'contact':contact})

def delete_contact(request,del_id):
    x = ContactDb.objects.filter(id=del_id)
    x.delete()
    return redirect(contact_details)

def blog_page(request):
    return render(request,"add_blog.html")

def save_blog(request):
    if request.method == "POST":
        img = request.FILES['image']
        a = request.POST.get('description')
        obj = BlogDb(Blogimage=img,Description=a)
        obj.save()
    return redirect(blog_page)








