# Generated by Django 4.1 on 2022-09-12 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_blog_l'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bigblog',
            new_name='Blog_body',
        ),
        migrations.RenameModel(
            old_name='blog_L',
            new_name='Blog_right',
        ),
    ]