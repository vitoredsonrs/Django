from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from cadastros.models import Cidade
from cadastros.serializers import CidadeSerializer


# class CidadeAPI(APIView):
#     def get(self, request, format=None):
#         cidades = Cidade.objects.all()
#         serializer = CidadeSerializer(cidades, many=True)
#
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#

class CidadeAPIList(ListCreateAPIView):

    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
