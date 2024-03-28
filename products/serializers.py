from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Product,Brand,ProductImages,Review


class ProductImagesSerializer(serializers.ModelSerializer):
    model=ProductImages
    fields=['image']

class ProductReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Review
        fields=['user','review','rate','created_at']

class ProductListSerializer(TaggitSerializer,serializers.ModelSerializer):
    brand = serializers.StringRelatedField
    tags = TagListSerializerField()
    #review_count=serializers.SerializerMethodField()
    #avg_rate = serializers.SerializerMethodField()
    class Meta:
        model =Product
        fields=['name','price','flag','subtitle','description','sku','brand','review_count','avg_rate','tags']
        
        '''
    def get_review_count(self,object):
        reviews = object.review_product.all().count()
        return reviews
    
    def get_avg_rate(self,object):
        total=0 #sum rate : object
        reviews = object.review_product.all()
        if len(reviews)>0:
            for item in reviews:
                total+=item.rate 
            avg= total/len(reviews)
        else: 
            avg =0
        return avg
           '''  
        
class ProductDetailSerializer(TaggitSerializer,serializers.ModelSerializer):
    brand = serializers.StringRelatedField
    #review_count=serializers.SerializerMethodField()
    #avg_rate = serializers.SerializerMethodField()
    image = ProductImagesSerializer(source='product_image',many=True)
    reviews=ProductReviewsSerializer(source='review_product',many=True)
    tags = TagListSerializerField()
    class Meta:
        model =Product
        fields=['name','price','flag','subtitle','description','sku','brand','review_count','avg_rate','image','reviews','tags']
    ''' 
    def get_review_count(self,object):
        #reviews = object.review_product.all().count()
        reviews =  object.review_count()
        return reviews
    
    def get_avg_rate(self,object):
        avg= object.avg_rate()
        return avg
    ''' 
    '''
        total=0 #sum rate : object
        reviews = object.review_product.all()
        if len(reviews)>0:
            for item in reviews:
                total+=item.rate 
            avg= total/len(reviews)
        else: 
            avg =0
        return avg
    ''' 
        
        
class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model =Brand
        fields='__all__'
        
class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =Brand
        fields='__all__'