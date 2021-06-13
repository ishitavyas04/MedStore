from django.contrib import admin
from .models import Product
from .models import Productview
from .models import Catergory
from .models import Customer
from .models import Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Productview)
admin.site.register(Catergory)
admin.site.register(Customer)
admin.site.register(Order)