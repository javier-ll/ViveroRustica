# Generated by Django 5.0 on 2024-01-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vivero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='Descripción del producto', max_length=200),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]