# Generated by Django 2.2 on 2021-04-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210414_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pro_pic',
            field=models.ImageField(blank=True, null=True, upload_to='student_images/'),
        ),
    ]