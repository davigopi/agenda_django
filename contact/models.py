from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), picture (imagem)
# owner (foreign key)

class Category(models.Model):
    # https://docs.djangoproject.com/en/5.0/ref/models/options/
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)   # blank=True define como opcional
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # apagar categoria contatos null
        blank=True, null=True
    ) # on_delete=models.CASCADE,  -> apagar categoria apaga contatos com categoria
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, 
        blank=True, null=True
    ) 

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
 
