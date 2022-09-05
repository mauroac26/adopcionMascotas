from .models import Mascotas
from .serializers import MascotasSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status



class MascotasViewSet(viewsets.ModelViewSet):
    queryset = Mascotas.objects.all()
    serializer_class = MascotasSerializer

    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
         serializer.save()
         return Response({'message': 'Mascota agregada correctamente'}, status = status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

  
    def update(self, request, pk=None):
            
              # send information to serializer referencing the instance
        
        serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Mascota actualizado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)