from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=150,unique=True)
    slug = models.SlugField(max_length=150,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('slug',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name =models.CharField(max_length=150,unique=True)
    slug = models.CharField(max_length=150,unique=True)
    desc = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField()
    avail = models.BooleanField()
    category = models.ForeignKey(Shop,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product')

    def get_urls(self):
        return reverse('ProdDetail', args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
    