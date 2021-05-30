from django.db import models


# Create your mo
class Destination(models.Model):
    f_name = models.CharField(max_length=100)
    e_id = models.EmailField(max_length=254)
    passw = models.CharField(max_length=564)
    c_passw = models.CharField(max_length=556)