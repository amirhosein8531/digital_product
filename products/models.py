from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self',verbose_name=('parent') ,on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    avatar= models.ImageField(upload_to='categories',blank=True)
    situation=models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='products/', blank=True)
    situation = models.BooleanField(null=True)
    category=models.ManyToManyField('Category',verbose_name='category',blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return self.title



class File(models.Model):
    title = models.CharField(max_length=50,default='')
    product = models.ForeignKey('Product',on_delete=models.CASCADE,verbose_name=('product'))
    file = models.FileField(upload_to='files/%Y/%m/%d/',blank=True)
    situation = models.BooleanField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name='file'
        verbose_name_plural='files'