# Generated by Django 2.2 on 2021-04-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210414_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pro_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
