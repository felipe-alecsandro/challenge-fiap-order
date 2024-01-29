from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.contrib.sessions.backends.db import SessionStore
from order.models.orders import Order
from order.serializers.orders import OrderSerializer
from order.use_cases.orders import ListOrdersUseCase


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    
    def create(self, request, *args, **kwargs):

        # Retrieve data from the request body
        order_data = {
            'order_id': request.data.get('order_id'),
            'transaction': request.data.get('transaction'),
            'products': request.data.get('products'),
            'status': request.data.get('status'),
        }

        serializer = OrderSerializer(data=order_data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['post'], url_path='cancel', permission_classes=[AllowAny])
    def cancel(self, request, pk=None):
        order = self.get_object()

        if order.status == 'em aberto':
            order.status = 'cancelado'
            order.save()
            return Response({'message': 'Order status updated to "cancelado".'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Esse pedido não pode ser finalizado.'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response([])

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_queryset(self):
        use_case = ListOrdersUseCase()
        return use_case.execute(self.request)