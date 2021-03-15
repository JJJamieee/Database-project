from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import 銷售通路, 加工廠商, 加工產品, 餐廳_加工產品, 加工產品_銷售通路, 產銷履歷商品_銷售通路, 生產者, 產銷履歷商品, 加工產品_原料, 餐廳, 餐廳_產銷履歷


@admin.register(銷售通路)
class 銷售通路Admin(ImportExportModelAdmin):
    list_display = ('銷售通路ID', '銷售通路名稱', '電話', '地址')


@admin.register(加工廠商)
class 加工廠商Admin(ImportExportModelAdmin):
    list_display = ('加工廠商ID', '加工廠商名稱', '地址', '電話')


@admin.register(加工產品)
class 加工產品Admin(ImportExportModelAdmin):
    list_display = ('加工批號', '加工產品名稱', '加工廠商ID', '產量', '製造日期')


@admin.register(餐廳_加工產品)
class 餐廳_加工產品Admin(ImportExportModelAdmin):
    list_display = ('餐廳ID', '加工批號', '重量', '訂貨日期')


@admin.register(加工產品_銷售通路)
class 加工產品_銷售通路Admin(ImportExportModelAdmin):
    list_display = ('銷售通路ID', '加工批號', '重量', '訂貨日期')


@admin.register(產銷履歷商品_銷售通路)
class 產銷履歷商品_銷售通路Admin(ImportExportModelAdmin):
    list_display = ('銷售通路ID', '追溯號碼', '重量', '訂貨日期')


@admin.register(生產者)
class 生產者Admin(ImportExportModelAdmin):
    list_display = ('生產者ID', '生產者名稱', '電話', '地址', '農產品經營業者')


@admin.register(產銷履歷商品)
class 產銷履歷商品Admin(ImportExportModelAdmin):
    list_display = ('追溯號碼', '產品名稱', '生產者ID', '產地', '包裝日期', '驗證機構')


@admin.register(加工產品_原料)
class 加工產品_原料Admin(ImportExportModelAdmin):
    list_display = ('加工批號', '追溯號碼')


@admin.register(餐廳)
class 餐廳Admin(ImportExportModelAdmin):
    list_display = ('餐廳ID', '名稱', '電話', '地址')


@admin.register(餐廳_產銷履歷)
class 餐廳_產銷履歷Admin(ImportExportModelAdmin):
    list_display = ('餐廳ID', '追溯號碼', '重量', '訂貨日期')
