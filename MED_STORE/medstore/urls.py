from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("view", views.view, name='view'),
    path("cart", views.cart, name='cart'),
    path("order", views.OrderView, name='order'),
    path("check-out", views.CheckOut, name='CheckOut'),
    path("diabetic", views.diabetic, name='diabetic'),
    path("malaria", views.malaria, name='malaria'),
    path("thyroid", views.thyroid, name='thyroid'),
    path("typhoid", views.typhoid, name='typhoid'),
    path("cancer", views.cancer, name='cancer'),
    
    

    
]