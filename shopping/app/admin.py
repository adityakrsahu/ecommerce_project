from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(State)
admin.site.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display= '__all__'


admin.site.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display= '__all__'


admin.site.register(Cart)
admin.site.register(OrderPlaced)