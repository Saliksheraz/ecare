from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from administrator.models import pharmacy, products
from .serializers import pharmacySerializer, productsSerializer


class pharmacyViewSet(viewsets.ModelViewSet):
    queryset = pharmacy.objects.all()
    serializer_class = pharmacySerializer
    # permission_classes = [permissions.IsAuthenticated]


class productsViewSet(viewsets.ModelViewSet):
    queryset = products.objects.all()
    serializer_class = productsSerializer


@api_view(['GET', 'POST'])
def productsViewSet2(request):
    if request.method == 'GET':
        snippets = products.objects.all()
        serializer = productsSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = productsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
