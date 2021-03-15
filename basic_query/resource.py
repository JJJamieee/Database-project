from import_export import resources, fields
from .model import 銷售通路, 加工廠商, 加工產品, 餐廳_加工產品, 加工產品_銷售通路, 產銷履歷商品_銷售通路, 生產者, 產銷履歷商品, 加工產品_原料, 餐廳, 餐廳_產銷履歷


class 銷售通路Resource(resources.ModelResource):
    class Meta:
        model = 銷售通路
        import_id_fields = ['銷售通路ID', ]
        #exclude = ('id')
        #skip_unchanged = True
        #fields = ('銷售通路ID', '銷售通路名稱', '電話', '地址')


class 加工廠商Resource(resources.ModelResource):
    class Meta:
        model = 加工廠商
        import_id_fields = ['加工廠商ID', ]
        #exclude = ('id')
        #skip_unchanged = True
        #fields = ('加工廠商ID', '加工廠商名稱', '地址', '電話')


class 加工產品Resource(resources.ModelResource):
    class Meta:
        model = 加工產品
        import_id_fields = ['加工批號', ]
        #exclude = ('id')
        #skip_unchanged = True
        #fields = ('加工批號', '加工產品名稱', '加工廠商ID', '產量', '製造日期', )


class 餐廳_加工產品Resource(resources.ModelResource):
    class Meta:
        model = 餐廳_加工產品
        import_id_fields = ['餐廳ID', '加工批號', ]


class 加工產品_銷售通路Resource(resources.ModelResource):
    class Meta:
        model = 加工產品_銷售通路
        import_id_fields = ['銷售通路ID', '加工批號', ]


class 產銷履歷商品_銷售通路Resource(resources.ModelResource):
    class Meta:
        model = 產銷履歷商品_銷售通路
        import_id_fields = ['銷售通路ID', '追溯號碼', ]


class 生產者Resource(resources.ModelResource):
    class Meta:
        model = 生產者
        import_id_fields = ['生產者ID', ]
        #exclude = ('id')
        #skip_unchanged = True
        #fields = ('生產者ID', '名稱', '電話', '地址', '農產品經營業者')


class 產銷履歷商品Resource(resources.ModelResource):
    class Meta:
        model = 產銷履歷商品
        import_id_fields = ['追溯號碼', ]
        #exclude = ('id')
        #skip_unchanged = True
        #fields = ('追溯號碼', '產品名稱', '生產者ID', '產地','包裝日期','驗證機構')


class 加工產品_原料Resource(resources.ModelResource):
    class Meta:
        model = 加工產品_原料
        import_id_fields = ['加工批號', '追溯號碼', ]


class 餐廳Resource(resources.ModelResource):
    class Meta:
        model = 餐廳
        import_id_fields = ['餐廳ID', ]
        #exclude = ('id')
        #skip_unchanged = True
        #fields = ('餐廳ID', '名稱', '電話', '地址')


class 餐廳_產銷履歷Resource(resources.ModelResource):
    class Meta:
        model = 餐廳_產銷履歷
        import_id_fields = ['餐廳ID', '追溯號碼', ]
