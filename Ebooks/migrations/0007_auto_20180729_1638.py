# Generated by Django 2.0.6 on 2018-07-29 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ebooks', '0006_pdfinfo_pdfprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfinfo',
            name='PdfPrice',
            field=models.CharField(max_length=6),
        ),
    ]