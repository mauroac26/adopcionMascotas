
from django.db import models

from base.models import BaseModel

sexo = [
  ['Macho', 'Macho'],
  ["Hembra", 'Hembra']
]

edad = [
  ['Cachorro', 'Cachorro'],
  ["Adulto", 'Adulto']
]

tamaño = [
  ['Grande', 'Grande'],
  ['Mediano', 'Mediano'],
  ['Pequeño', 'Pequeño']
]

caracter = [
  ['Timido', 'Timido'],
  ['Cariñoso', 'Cariñoso'],
  ['Malhumorado', 'Malhumorado']
]

opciones = [
  ['SI', 'SI'],
  ['NO', 'NO']
]

class Mascotas(BaseModel):
  nombre = models.CharField(max_length=150)
  sexo = models.CharField(choices=sexo, null=False, max_length=150)
  edad = models.CharField(choices=edad, max_length=150)
  tamaño = models.CharField(choices=tamaño, max_length=150)
  caracter = models.CharField(choices=caracter, max_length=150)
  castrado = models.CharField(choices=opciones, max_length=150)
  desparacitado = models.CharField(choices=opciones, max_length=150)
  vacunado = models.CharField(choices=opciones, max_length=150)
  descripcion = models.CharField(max_length=150)


  class Meta:
    ordering = ['nombre']

  def __str__(self):
      return self.nombre
