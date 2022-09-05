from .models import Mascotas
from rest_framework import serializers

class MascotasSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mascotas
    # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
    fields = '__all__'