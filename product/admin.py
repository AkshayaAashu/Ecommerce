from django.contrib import admin
from myaccount.models import User
from product.models import Product
from product.models import Category

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
