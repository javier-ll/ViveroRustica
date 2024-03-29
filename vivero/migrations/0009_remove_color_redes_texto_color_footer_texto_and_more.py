# Generated by Django 5.0 on 2024-03-15 14:21

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vivero', '0008_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='redes_texto',
        ),
        migrations.AddField(
            model_name='color',
            name='footer_texto',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de texto del footer'),
        ),
        migrations.AlterField(
            model_name='color',
            name='carrusel_fondo_texto',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de fondo del texto dentro del Carrusel'),
        ),
        migrations.AlterField(
            model_name='color',
            name='carrusel_texto',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de texto dentro del Carrusel'),
        ),
        migrations.AlterField(
            model_name='color',
            name='color_fondos',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de los fondos'),
        ),
        migrations.AlterField(
            model_name='color',
            name='fondo_secciones',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de los fondos de cada título de sección'),
        ),
        migrations.AlterField(
            model_name='color',
            name='form_boton',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de fondo del botón de formulario'),
        ),
        migrations.AlterField(
            model_name='color',
            name='form_texto_boton',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de texto del botón del formulario'),
        ),
        migrations.AlterField(
            model_name='color',
            name='frase_principal',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de texto de la frase principal'),
        ),
        migrations.AlterField(
            model_name='color',
            name='header_texto_botones',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de texto de botones en header'),
        ),
        migrations.AlterField(
            model_name='color',
            name='hover_carrusel',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de activación de botones en Carrusel'),
        ),
        migrations.AlterField(
            model_name='color',
            name='hover_header',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de activación de botones en Header'),
        ),
        migrations.AlterField(
            model_name='color',
            name='hover_productos',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de activación de cuadro de cada producto'),
        ),
        migrations.AlterField(
            model_name='color',
            name='hover_redes',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de activación de redes del footer'),
        ),
        migrations.AlterField(
            model_name='color',
            name='productos_fondo',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de fondo de los cuadros de productos'),
        ),
        migrations.AlterField(
            model_name='color',
            name='productos_quienes_form_texto_detalles',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de texto de los productos, detalles y formulario'),
        ),
        migrations.AlterField(
            model_name='color',
            name='titulos_secciones',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Color de cada título de sección'),
        ),
    ]
