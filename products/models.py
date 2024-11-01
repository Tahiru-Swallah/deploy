from django.db import models
from account.models import CustomUser
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('clothes', 'Clothes'),
        ('phones', 'Phones'),
        ('laptops', 'Laptops'),
        ('food', 'Food'),
        ('art', 'Art Works'),
    ]

    name = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True)
    slug = models.SlugField(max_length=20, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

        indexes = [
            models.Index(fields=['name'])
        ]
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:product_list_slug', args=[self.slug])
    
    def __str__(self):
        return self.name 
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image/%Y/%m/%d', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id, self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name