from django.contrib import admin
from .models import User, Cart, Category, Product, Client, Seller


admin.site.register(User)

admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Seller)