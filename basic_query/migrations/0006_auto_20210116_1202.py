# Generated by Django 3.1.4 on 2021-01-16 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_query', '0005_auto_20210116_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='餐廳',
            old_name='加工產品',
            new_name='加工',
        ),
        migrations.RenameField(
            model_name='餐廳',
            old_name='產銷履歷商品',
            new_name='產銷',
        ),
    ]