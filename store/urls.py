from django.urls import path

from . import views 
# from .views import RegisterPage
from django.contrib.auth.views import LogoutView

from django.contrib.auth import views as auth_views

urlpatterns = [
	path('login/', views.CustomLoginView.as_view(), name='login'),
 	path('logout/', LogoutView.as_view(next_page='store'), name='logout'),
 	path('register/', views.register, name='register'),
  
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('account/', views.accountSettings, name="account"),
	path('profile/', views.profile, name="profile"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('product_details/<str:id>/', views.product_details,name='product_details'),
	path('contact', views.contact, name="contact"),
	path('search', views.search, name="search"),
	path('pop', views.pop, name="pop"),
 	path('submit_pop', views.submit_pop, name="submit_pop"),	
 
 	path('order_confirm', views.order_confirm, name='order_confirm'),
   	path('create_order/<str:pk>/', views.createOrder, name="create_order"),
	path('user/', views.userpage, name="user"),
 	path('customer/<str:pk_test>/', views.customer, name="customer"),
	path('dashboard', views.dashboard, name="dashboard"),
	path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
	path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('orderitems/', views.orderitems, name="orderitems"),
    path('slide/', views.slide, name="slide"),
    
	path('play', views.play, name='play'),
 
 
	path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="store/password_reset.html"),
     name="reset_password"),
 
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="store/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="store/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="store/password_reset_done.html"), 
        name="password_reset_complete"),


]