from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse


class 產銷履歷商品(models.Model):
    # Fields
    追溯號碼 = models.CharField(max_length=30, primary_key=True)
    產品名稱 = models.CharField(max_length=50)
#
    生產者ID = models.ForeignKey(
        '生產者', on_delete=models.CASCADE, null=True, related_name='產銷生產者')
#
    產地 = models.CharField(max_length=20)  # 縣市
    包裝日期 = models.DateField()
    驗證機構 = models.CharField(max_length=100)
    產銷作業基準 = models.CharField(max_length=20, null=True)

    # Metadata
    class Meta:
        ordering = ['追溯號碼']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.追溯號碼)])

    def __str__(self):
        return self.追溯號碼


class 加工產品(models.Model):
    # Fields
    加工批號 = models.CharField(max_length=13, primary_key=True)
    加工產品名稱 = models.CharField(max_length=20)
    加工廠商ID = models.ForeignKey(
        '加工廠商', on_delete=models.CASCADE, null=True, related_name='加工產品廠商')
    產量 = models.FloatField()
    製造日期 = models.DateField()
#
    產銷 = models.ManyToManyField(產銷履歷商品, through='加工產品_原料')
#
    # Metadata

    class Meta:
        ordering = ['加工批號']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.加工批號)])

    def __str__(self):
        return self.加工批號


class 銷售通路(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    銷售通路ID = models.CharField(max_length=10, primary_key=True)
    銷售通路名稱 = models.CharField(max_length=20)
    電話 = models.CharField(max_length=20)
    地址 = models.CharField(max_length=50)
#
    加工 = models.ManyToManyField(加工產品, through='加工產品_銷售通路')
    產銷 = models.ManyToManyField(產銷履歷商品, through='產銷履歷商品_銷售通路')
#
    # Metadata

    class Meta:
        ordering = ['銷售通路ID']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.銷售通路ID)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.銷售通路ID


class 加工廠商(models.Model):
    # Fields
    加工廠商ID = models.CharField(max_length=10, primary_key=True)
    加工廠商名稱 = models.CharField(max_length=20)
    地址 = models.CharField(max_length=50)
    電話 = models.CharField(max_length=15)

    # Metadata
    class Meta:
        ordering = ['加工廠商ID']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.加工廠商ID)])

    def __str__(self):
        return self.加工廠商ID


class 餐廳_加工產品(models.Model):
    # Fields
    餐廳ID = models.ForeignKey('餐廳', on_delete=models.CASCADE, null=True)
    加工批號 = models.ForeignKey('加工產品', on_delete=models.CASCADE, null=True)
    重量 = models.FloatField()
    訂貨日期 = models.DateField()
    # Metadata

    class Meta:
        ordering = ['餐廳ID', '加工批號']

    # Methods
    # def get_absolute_url(self):
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.餐廳ID, self.加工批號)


class 加工產品_銷售通路(models.Model):
    # Fields
    銷售通路ID = models.ForeignKey('銷售通路', on_delete=models.CASCADE, null=True)
    加工批號 = models.ForeignKey('加工產品', on_delete=models.CASCADE, null=True)
    重量 = models.FloatField()
    訂貨日期 = models.DateField()

    # Metadata
    class Meta:
        ordering = ['銷售通路ID', '加工批號']

    # Methods
    # def get_absolute_url(self):
    #    return reverse('model-detail-view', args = [str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.銷售通路ID, self.加工批號)


class 產銷履歷商品_銷售通路(models.Model):
    # Fields
    銷售通路ID = models.ForeignKey('銷售通路', on_delete=models.CASCADE, null=True)
    追溯號碼 = models.ForeignKey('產銷履歷商品', on_delete=models.CASCADE, null=True)
    重量 = models.FloatField()
    訂貨日期 = models.DateField()
    # Metadata

    class Meta:
        ordering = ['銷售通路ID', '追溯號碼']

    # Methods
    # def get_absolute_url(self):
    #    return reverse('model-detail-view', args = [str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.銷售通路ID, self.追溯號碼)


class 生產者(models.Model):
    # Fields
    生產者ID = models.CharField(max_length=20, primary_key=True)
    生產者名稱 = models.CharField(max_length=20)
    電話 = models.CharField(max_length=20)
    地址 = models.CharField(max_length=50)
    農產品經營業者 = models.CharField(max_length=50)

    # Metadata
    class Meta:
        ordering = ['生產者ID']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.生產者ID)])

    def __str__(self):
        return self.生產者ID


class 加工產品_原料(models.Model):
    加工批號 = models.ForeignKey('加工產品', on_delete=models.CASCADE, null=True)
    追溯號碼 = models.ForeignKey('產銷履歷商品', on_delete=models.CASCADE, null=True)

    # Metadata
    class Meta:
        ordering = ['加工批號', '追溯號碼']

    # Methods
    # def get_absolute_url(self):
    #    return reverse('model-detail-view', args = [str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.加工批號, self.追溯號碼)


class 餐廳(models.Model):
    餐廳ID = models.CharField(max_length=10, primary_key=True)
    名稱 = models.CharField(max_length=30)
    電話 = models.CharField(max_length=15)
    地址 = models.CharField(max_length=50)
#
    加工 = models.ManyToManyField(加工產品, through='餐廳_加工產品')
    產銷 = models.ManyToManyField(產銷履歷商品, through='餐廳_產銷履歷')
#
    # Metadata

    class Meta:
        ordering = ['餐廳ID']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.餐廳ID)])

    def __str__(self):
        return self.餐廳ID


class 餐廳_產銷履歷(models.Model):
    餐廳ID = models.ForeignKey('餐廳', on_delete=models.CASCADE, null=True)
    追溯號碼 = models.ForeignKey('產銷履歷商品', on_delete=models.CASCADE, null=True)
    重量 = models.FloatField()
    訂貨日期 = models.DateField()

    # Metadata
    class Meta:
        ordering = ['餐廳ID', '追溯號碼']

    # Methods
    # def get_absolute_url(self):
    #    return reverse('model-detail-view', args = [str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.餐廳ID, self.追溯號碼)
