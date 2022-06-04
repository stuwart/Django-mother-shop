from django.db import models


# Create your models here.

class Types(models.Model):
    id = models.AutoField(primary_key=True)  # 自增长类型.    primary_key：设置主键
    firsts = models.CharField('一级类型', max_length=100)  # Verbose_name:默认为None，在Admin站点管理设置字段的显示名称。
    seconds = models.CharField('二级类型', max_length=100)

    def __str__(self):  # 重写函数，设置模型的返回值，只允许返回字符类型的字段
        return str(self.id)

    class Meta:  # 重写Meta选项：设置模型的常用属性，有19个
        verbose_name = '商品类型'  # 属性值为字符串，设置模型直观可读的名称并以复数形式表示。
        verbose_name_plural = '商品类型'  # 与verbose_name相同，以单数形式表示。


class CommodityInfos(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('商品名称', max_length=100)
    sizes = models.CharField('颜色规格', max_length=100)
    types = models.CharField('商品类型', max_length=100)
    price = models.FloatField('商品价格')
    discount = models.FloatField('折后价格')
    stock = models.IntegerField('存货数量')
    sold = models.IntegerField('已售数量')
    likes = models.IntegerField('收藏数量')
    created = models.DateField('上架日期', auto_now_add=True)
    img = models.FileField('商品主图', upload_to=r'imgs')
    details = models.FileField('商品介绍', upload_to=r'details')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'
