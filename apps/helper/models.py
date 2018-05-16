from __future__ import unicode_literals
from django.db import models

class OrderManager(models.Manager):
    def create(self, post):
        isPaid = False
        isPurchased = False
        isArrived = False
        isShipped = False

        if post.get('isPaid'):
            isPaid = True

        if post.get('isPurchased'):
            isPurchased = True

        if post.get('isArrived'):
            isArrived = True

        if post.get('isShipped'):
            isShipped = True

        order = Order(
            name = post['name'],
            item = post['item'],
            isPaid = isPaid,
            isPurchased = isPurchased,
            isArrived = isArrived,
            isShipped = isShipped
        )

        order.save()

        return True

    def update(self, post, id):
        order = Order.objects.get(id = id)

        if post.get('isPaid'):
            order.isPaid = True
        else:
            order.isPaid = False

        if post.get('isPurchased'):
            order.isPurchased = True
        else:
            order.isPurchased = False

        if post.get('isArrived'):
            order.isArrived = True
        else:
            order.isArrived = False

        if post.get('isShipped'):
            order.isShipped = True
        else:
            order.isShipped = False

        order.save()

        return True

class Order(models.Model):
    name = models.CharField(max_length = 20)
    item = models.CharField(max_length = 40)
    isPaid = models.BooleanField()
    isPurchased = models.BooleanField()
    isArrived = models.BooleanField()
    isShipped = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = OrderManager()
