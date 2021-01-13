from django.db import models

# Create your models here.
class POST(models.Model): #สร้างตาราง
    name = models.CharField(max_length = 200)
    desc = models.TextField()

