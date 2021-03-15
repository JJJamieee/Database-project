# Generated by Django 3.1.4 on 2020-12-31 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_query', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='生產者',
            old_name='名稱',
            new_name='生產者名稱',
        ),
        migrations.AddField(
            model_name='加工產品',
            name='產銷',
            field=models.ManyToManyField(through='basic_query.加工產品_原料', to='basic_query.產銷履歷商品'),
        ),
        migrations.AddField(
            model_name='銷售通路',
            name='加工',
            field=models.ManyToManyField(through='basic_query.加工產品_銷售通路', to='basic_query.加工產品'),
        ),
        migrations.AddField(
            model_name='銷售通路',
            name='產銷',
            field=models.ManyToManyField(through='basic_query.產銷履歷商品_銷售通路', to='basic_query.產銷履歷商品'),
        ),
        migrations.AddField(
            model_name='餐廳',
            name='加工',
            field=models.ManyToManyField(through='basic_query.餐廳_加工產品', to='basic_query.加工產品'),
        ),
        migrations.AddField(
            model_name='餐廳',
            name='產銷',
            field=models.ManyToManyField(through='basic_query.餐廳_產銷履歷', to='basic_query.產銷履歷商品'),
        ),
        migrations.AlterField(
            model_name='產銷履歷商品',
            name='生產者ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='產銷生產者', to='basic_query.生產者'),
        ),
    ]