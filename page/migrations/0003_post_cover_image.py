# Generated by Django 4.1.7 on 2023-03-17 06:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_post_delete_iletisim'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='post'),
            preserve_default=False,
        ),
    ]
