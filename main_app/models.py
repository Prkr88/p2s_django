from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SiteUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username


class Fleet(models.Model):
    company = models.CharField(max_length=256,primary_key=True)
    manager = models.CharField(max_length=256)

    def __str__(self):
        return self.company

class Ship_Type(models.Model):
    type_name = models.CharField(max_length=256,primary_key=True)
    type_pic = models.ImageField(upload_to='static/main_app/items_pics',blank=True)

    def __str__(self):
        return self.type_name


class Ship(models.Model):
    ship_id = models.CharField(max_length=256,primary_key=True)
    status = models.CharField(max_length=256)
    n_m = models.CharField(max_length=256)
    type = models.ForeignKey(Ship_Type, related_name='type', on_delete=models.CASCADE)
    fleet = models.ForeignKey(Fleet, related_name='ships', on_delete=models.CASCADE)

    def __str__(self):
        return self.ship_id


class Section(models.Model):
    section_name = models.CharField(max_length=256,primary_key=True)
    parent = models.ForeignKey(Ship, related_name='parent', on_delete=models.CASCADE)

    class Meta:
        unique_together = (("section_name", "parent"),)

    def __str__(self):
        return self.section_name


class Item(models.Model):
    item_id = models.CharField(max_length=256, primary_key=True)
    item_name = models.CharField(max_length=256)
    item_quantity = models.IntegerField()
    item_picture = models.ImageField(upload_to='static/main_app/items_pics',blank=True)
    section = models.ForeignKey(Section, related_name='items', on_delete=models.CASCADE)
    ship = models.ForeignKey(Ship, related_name='on_board', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_id

class Order(models.Model):
    order_id = models.IntegerField()
    creator = models.ForeignKey(SiteUser,related_name='creator', on_delete=models.CASCADE)
    items = models.ForeignKey(Item, related_name='items', on_delete=models.CASCADE)
    order_date = models.DateField()
    status = models.CharField(max_length=256)

    def __str__(self):
        return self.order_id
