# Generated by Django 3.1.4 on 2021-01-03 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_query', '0002_auto_20201231_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='加工產品',
            name='加工廠商ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='產銷生產者', to='basic_query.加工廠商'),
        ),
    ]
