from django.contrib import admin
from django.contrib.admin.decorators import register
from  .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ('code','date','producer')


@admin.register(Detail)
class DetilAdmin(admin.ModelAdmin):
    list_display = ('code','title','category','price','quantity','slug')
    prepopulated_fields = {'slug':('title',),}
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk','name')
    
admin.site.register(Invoice)
admin.site.register(InvoiceItem)


