from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=255)
    user_password = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    mem = models.ForeignKey('Memasik', on_delete=models.DO_NOTHING)

"""    def __str__(self):
        return f"{self.user_name}: {self.email}
"""

class Massege(models.Model):
    massege = models.TextField()
    date_time_massege = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)


"""    def __str__(self):
        return f"{user}: {self.massege}: {self.date_time_massege}"
"""


class Memasik(models.Model):
    article_image = models.ImageField(null=True, blank=True, upload_to="images/")
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='memasik_category')


class Category(models.Model):
    name_category = models.CharField(max_length=255)
    memasik = models.ManyToManyField('Memasik')


"""   def __str__(self):
        return self.name_category"""
