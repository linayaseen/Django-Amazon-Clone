from django.contrib import admin

# Register your models here.
from.models import Product,Brand,Review, ProductImages

class ProductImagesInline(admin.TabularInline):
    model= ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImagesInline]
    list_display=['name','review_count','avg_count']
 
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)
