# Generated by Django 5.0 on 2024-03-17 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vivero', '0010_color_fondo_header_alter_color_carrusel_fondo_texto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_header', models.ImageField(blank=True, null=True, upload_to='')),
                ('logo_form', models.ImageField(blank=True, null=True, upload_to='')),
                ('logo_footer', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]