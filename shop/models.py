from django.db import models
from datetime import datetime
from django.urls import reverse


class Category(models.Model):
  name = models.CharField(max_length=128, db_index=True)
  slug = models.SlugField(max_length=128, unique=True)
  
  class Meta:
    ordering = ('name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse(
      'shop:product_list_by_category', 
      args=[self.slug]
    )

class Supplier(models.Model):
  name = models.CharField(max_length=128, db_index=True)
  slug = models.SlugField(max_length=128, unique=True)
  
  class Meta:
    ordering = ('name',)
    verbose_name = 'supplier'
    verbose_name_plural = 'suppliers'

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse(
      'shop:product_list_by_supplier', 
      args=[self.slug]
    )

class Brand(models.Model):
  name = models.CharField(max_length=128, db_index=True)
  slug = models.SlugField(max_length=128, unique=True)
  
  class Meta:
    ordering = ('name',)
    verbose_name = 'brand'
    verbose_name_plural = 'brands'

  def __str__(self):
    return self.name

class Product(models.Model):

  # barcode = models.AutoField(
  #   verbose_name='ID', 
  #   serialize=False, 
  #   auto_created=True, 
  #   primary_key=True
  # )

  category = models.ForeignKey(
    Category,
    related_name='products',
    on_delete=models.CASCADE
  )
  supplier = models.ForeignKey(
    Supplier,
    related_name='products',
    on_delete=models.CASCADE
  )
  brand = models.ForeignKey(
    Brand,
    related_name='products',
    on_delete=models.CASCADE
  )

  barcode = models.TextField(
    max_length=48,
    default=str(id)
  )

  made = models.TextField(
    max_length=10, 
    default=datetime.now().year
  )
  name = models.CharField(max_length=128, db_index=True)
  slug = models.SlugField(max_length=128, db_index=True)

  image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=20, decimal_places=0)

  available = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('name',) 
    index_together = (('id', 'slug'),)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse(
      'shop:product_detail',
      args=[self.id, self.slug]
    )
