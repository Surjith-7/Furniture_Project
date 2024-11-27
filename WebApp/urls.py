from django.urls import path
from WebApp import views


urlpatterns = [
    path('Home/',views.home_page,name="Home"),
    path('Product_page/',views.Product_page,name="Product_page"),
    path('about_page/',views.about_page,name="about_page"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('save_page/',views.save_page,name="save_page"),
    path('category_filter/<cat_name>/',views.category_filter,name="category_filter"),
    path('singleproduct/<int:pro_id>/',views.singleproduct,name="singleproduct"),
    path('displayblog/',views.displayblog,name="displayblog"),


    path('sign_up/',views.sign_up,name="sign_up"),
    path('',views.sign_in,name="sign_in"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('delete_cart/<int:del_id>/',views.delete_cart,name="delete_cart"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),
    path('save_order/',views.save_order,name="save_order"),
    path('payment/',views.payment,name="payment"),


]