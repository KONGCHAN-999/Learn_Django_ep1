# Generated by Django 4.0.6 on 2022-11-01 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_delete_blog_right'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog_body',
        ),
    ]