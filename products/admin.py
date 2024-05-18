from django.contrib import admin

# Register your models here.
from.models import Product,Brand,Review, ProductImages
from modeltranslation.admin import TranslationAdmin

class ProductImagesInline(admin.TabularInline):
    model= ProductImages

class ProductAdmin(TranslationAdmin):
    inlines=[ProductImagesInline]
    list_display=['id','name','review_count','avg_count']
    list_filter=['flag','brand']
    search_field=['name','subtitle','discription']
 
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)
