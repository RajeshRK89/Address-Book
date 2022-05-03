from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *
from .log import log_entry
from rest_framework_extensions.mixins import NestedViewSetMixin


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("-datetime_created")
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    search_fields = ("email",)
    filter_fields = ("first_name",)
    # ordering_fields = ""

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update":
            return UserCreateUpdateSerializer
        else:
            return UserSerializer

    def get_queryset(self):
        # log_entry(self.queryset.query)
        return self.queryset

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["created_by"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        customer_connectivity_user = serializer.save()

        serializer = self.get_serializer(customer_connectivity_user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all().order_by("-datetime_created")
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    search_fields = ("user__email",)
    filter_fields = ("user__email",)
    # ordering_fields = ""

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update":
            return AddressCreateUpdateSerializer
        else:
            return AddressSerializer

    def get_queryset(self):
        # log_entry(self.queryset.query)
        return self.queryset
