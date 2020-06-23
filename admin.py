from django.contrib import admin
from .models import Product, CContact, Orders, OrderUpdate
# Register your models here.
admin.site.register(Product)
admin.site.register(CContact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)