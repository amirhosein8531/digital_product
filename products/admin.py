from django.contrib import admin
from .models import Category,Product,File

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent','title','created_time','situation')
    list_filter = ('situation','parent')
    search_fields = ['title']

class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title','file','situation']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','created_time','situation')
    list_filter = ('situation',)
    filter_horizontal =["category"]
    search_fields = ['title']
    inlines = [FileInlineAdmin]