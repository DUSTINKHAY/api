from django.db import models

# Create your models here.


class Image_u(models.Model):
    image=models.ImageField(upload_to='images/', null=True)
    title=models.CharField(max_length=50, null=True)
    product_description=models.CharField(max_length=200, null=True)
    price=models.CharField(max_length=20, null=True)
    # date=models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
        return self.image


