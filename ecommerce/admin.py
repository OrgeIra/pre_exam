from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Product, Category, ProductImage, Attribute, AttributeValue, ProductAttribute
from django.utils.html import format_html
from django.contrib.auth.models import User, Group

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image_tag')
    search_fields = ('name', 'price')
    list_filter = ('category', 'quantity', 'rating' )
    autocomplete_fields = ['category']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

class ProductInline(admin.TabularInline):
    model = Product


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'product_count')
    search_fields = ('title',)

    inlines = [
        ProductInline,
    ]

    def product_count(self, category):
        return category.product_set.count()

admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)
admin.site.unregister(User)
admin.site.unregister(Group)