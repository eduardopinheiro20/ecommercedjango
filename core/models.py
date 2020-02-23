from django.db import models


class Item(model.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    pass

    def __str__(self):
        return self.title


class Order(models.Model):
    pass 



