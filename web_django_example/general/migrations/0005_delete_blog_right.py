# Generated by Django 4.0.6 on 2022-10-26 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_rename_bigblog_blog_body_rename_blog_l_blog_right'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog_right',
        ),
    ]
