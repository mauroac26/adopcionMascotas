# Generated by Django 3.2.13 on 2022-07-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('sexo', models.CharField(choices=[['Macho', 'Macho'], ['Hembra', 'Hembra']], max_length=150)),
                ('edad', models.CharField(choices=[['Cachorro', 'Cachorro'], ['Adulto', 'Adulto']], max_length=150)),
                ('tamaño', models.CharField(choices=[['Grande', 'Grande'], ['Mediano', 'Mediano'], ['Pequeño', 'Pequeño']], max_length=150)),
                ('caracter', models.CharField(choices=[['Timido', 'Timido'], ['Cariñoso', 'Cariñoso'], ['Malhumorado', 'Malhumorado']], max_length=150)),
                ('castrado', models.CharField(choices=[['SI', 'SI'], ['NO', 'NO']], max_length=150)),
                ('desparacitado', models.CharField(choices=[['SI', 'SI'], ['NO', 'NO']], max_length=150)),
                ('vacunado', models.CharField(choices=[['SI', 'SI'], ['NO', 'NO']], max_length=150)),
                ('descripcion', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
