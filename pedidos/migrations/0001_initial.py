# Generated by Django 3.2.15 on 2022-10-13 01:56

from django.db import migrations, models
import django.db.models.deletion
import pedidos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=50, verbose_name='Nombre de Categoría')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('modify_at', models.DateField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name_plural': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion_producto', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('imagen_producto', models.ImageField(blank=True, null=True, upload_to="productos/", verbose_name='Imagen de Producto')),
                ('costo_producto', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Costo de Producto')),
                ('valor_venta', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor de Venta de Producto')),
                ('cantidad_stock', models.IntegerField(max_length=4, verbose_name='Cantidad Disponible')),
                ('disponibilidad', models.BooleanField(default=True)),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('modify_at', models.DateField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.categoria')),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
