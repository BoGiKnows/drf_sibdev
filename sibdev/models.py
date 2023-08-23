from django.db import models
from django.db.models import Sum


class Gem(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Client(models.Model):
    username = models.CharField(max_length=255)
    gems = models.ManyToManyField(Gem, related_name='client')

    @classmethod
    def get_top_five(cls):
        return Client.objects.annotate(spent_money=Sum('client_deals__total')).order_by('-spent_money')[:5]


class Deals(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='client_deals')
    item = models.ForeignKey(Gem, on_delete=models.PROTECT, related_name='gem_deals')
    total = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField()