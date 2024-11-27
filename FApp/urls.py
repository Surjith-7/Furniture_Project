from django.urls import path
from FApp import views
urlpatterns = [
    path('add_page/',views.add_page,name="add_page"),
    path('add_category/',views.add_category,name="add_category"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:edit_id>/',views.edit_category,name="edit_category"),
    path('update_category/<int:up_id>/',views.update_category,name="update_category"),
    path('delete_category/<int:del_id>/', views.delete_category, name="delete_category"),


    path('add_product/',views.add_product,name="add_product"),
    path('save_products/',views.save_products,name="save_products"),
    path('display_product/',views.display_product,name="display_product"),
    path('edit_product/<int:edit_id>/',views.edit_product,name="edit_product"),
    path('update_product/<int:up_id>/',views.update_product,name="update_product"),
    path('delete_product/<int:del_id>/',views.delete_product,name="delete_product"),


    path('admin_page/',views.admin_page,name="admin_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),


    path('contact_detail/',views.contact_details,name="contact_details"),
    path('delete_contact/<int:del_id>/',views.delete_contact,name="delete_contact"),
    path('blog_page/',views.blog_page,name="blog_page"),
    path('save_blog/',views.save_blog,name="save_blog"),
]