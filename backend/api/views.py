from rest_framework import mixins, filters, status, serializers, generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from core.paginators import DefaultPaginator
from api.serializers import CoffeeShopSerializer
from scrapers.models import CoffeeShop
# Create your views here.
class CoffeeShopAPIViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):

    serializer_class = CoffeeShopSerializer
    pagination_class = DefaultPaginator

    def get_queryset(self):
        return CoffeeShop.objects.filter()

    def get_object(self):
        return self.get_queryset().get(pk=self.kwargs["pk"])

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except CoffeeShop.DoesNotExist:
            return Response(
                data=dict(message="Shop does not exist"),
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)