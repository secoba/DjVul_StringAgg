# Create your views here.


from django.contrib.postgres.aggregates.general import StringAgg
from django.http import HttpResponse

from app.models import Address, Customer


def init(request):
    Address.objects.all().delete()
    Customer.objects.all().delete()
    c1 = Customer.objects.create(name="haha1")
    c2 = Customer.objects.create(name="haha2")
    Address.objects.create(customer=c1, phone="0123456")
    Address.objects.create(customer=c1, phone="1234567")
    Address.objects.create(customer=c2, phone="7654321")
    return HttpResponse("init succ")


def query(request):
    queryset = Address.objects.values("customer__name").annotate(
        phones=StringAgg('phone', delimiter="'"),
    )
    return HttpResponse(queryset)
