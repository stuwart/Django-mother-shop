from django.contrib import admin
from .models import *

# admin.site.register(Types)
# admin.site.register(CommodityInfos)

# 修改title和header
admin.site.site_title = '母婴后台系统'
admin.site.site_header = '母婴电商后台管理系统'
admin.site.index_title = '母婴平台管理'


@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display = [x for x in list(Types._meta._forward_fields_map.keys())]
    search_fields = ['firsts', 'seconds']
    list_filter = ['firsts']


# @admin.register(CommodityInfos)
# class CommodityInfosAdmin(admin.ModelAdmin):
#     list_display = [x for x in list(CommodityInfos._meta._forward_fields_map.keys())]
#     search_fields = ['name']
#     date_hierarchy = 'created'
#
#     def formfield_for_dbfield(self, db_field, **kwargs):
#         if db_field.name == 'types':
#             db_field.choices = [(x['seconds'], x['seconds'])for x in Types.objects.values('seconds')]
#         return super().formfield_for_dbfield(db_field, **kwargs)

@admin.register(CommodityInfos)
class CommodityInfosAdmin(admin.ModelAdmin):
    # 在数据新增页或数据修改页设置可编辑的字段
    # fields = ['name','sizes','types','price','discount']

    # 在数据新增或修改的页面设置不可编辑的字段
    # exclude = []

    # 改变数据新增页或数据修改页的网页布局
    fieldsets = (
        ('商品信息', {
            'fields': ('name', 'sizes', 'types', 'price', 'discount')
        }),
        ('收藏数量', {
            # 设置隐藏与显示
            'classes': ('collapse',),
            'fields': ('likes',),
        }),
    )

    # 将下拉框改为单选按钮
    # admin.HORIZONTAL是水平排列
    # admin.VERTICAL是垂直排列
    # radio_fields = {'types': admin.HORIZONTAL}

    # 在数据新增页或数据修改页设置可读的字段，不可编辑
    # readonly_fields = ['sold',]

    # 设置排序方式，['id']为升序，降序为['-id']
    ordering = ['id']

    # 设置数据列表页的每列数据是否可排序显示
    sortable_by = ['price', 'discount']

    # 在数据列表页设置显示的模型字段
    list_display = ['id', 'name', 'sizes', 'types', 'price', 'discount']
    list_display.append('colored_name')

    # 为数据列表页的字段id和name设置路由地址，该路由地址可进入数据修改页
    # list_display_links = ['id', 'name']

    # 设置过滤器，若有外键，则应使用双下画线连接两个模型的字段
    list_filter = ['types']

    # 在数据列表页设置每一页显示的数据量
    list_per_page = 100

    # 在数据列表页设置每一页显示最大上限的数据量
    list_max_show_all = 200

    # 为数据列表页的字段name设置编辑状态
    list_editable = ['name']

    # 设置可搜索的字段
    search_fields = ['name', 'types']

    # 在数据列表页设置日期选择器
    date_hierarchy = 'created'

    # 在数据修改页添加“另存为”功能
    save_as = True

    # 设置“动作”栏的位置
    # actions_on_top = False
    # actions_on_bottom = True

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'types':
            db_field.choices = [(x['seconds'], x['seconds']) for x in Types.objects.values('seconds')]
        return super().formfield_for_dbfield(db_field, **kwargs)

    # 数据批量操作
    def get_datas(self, request, queryset):
        temp = []
        for d in queryset:
            t = [d.name, d.types, str(d.discount)]
            temp.append(t)
        f = open('d://data.txt', 'a')
        for t in temp:
            f.write(','.join(t) + '\r\n')
        f.close()
        # 设置提示信息
        self.message_user(request, '数据导出成功！')

    # 设置函数的显示名称
    get_datas.short_description = '导出所选数据'
    # 添加到“动作”栏
    actions = ['get_datas']

    # 设置超级管理员和普通用户的权限
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        else:
            self.readonly_fields = ['types']
        return self.readonly_fields

    # 查询信息,不同级别用户权限不同
    def get_queryset(self, request):
        qs = super().get_queryset(request)  # 通过super方法获取父类ModelAdmin函数get_queryset所生成的模型查询对象,可查询CommodityInfos的全部数据
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(id__lt=2)

    # 改变非外键字段的下拉框数据,可重写
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field == 'types':  # 若该字段为types,则修改下拉框属性
            kwargs['choices'] = (('童装', '童装'),
                                 ('进口奶粉', '进口奶粉'),)
        return super().formfield_for_choice_field(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if change:
            user = request.user.username  # 获取当前用户名
            name = self.model.objects.get(pk=obj.pk).name  # 使用模型获取数据, pk为外键字段
            types = form.cleaned_data['types']  # 使用表单获取数据
            f = open('/log.txt', 'a')
            f.write(name + '商品类型:' + types + ',被' + user + '修改' + '\r\n')
            f.close()
        else:
            pass
        super().save_model(request, obj, form, change)

    # 若要删除数据,则使用delete_model实现
    # def delete_model(self, request, obj):


    # 数据批量处理


    def get_datas(self, request, queryset):
        temp = []
        for d in queryset:
            t = [d.name, d.types, str(d.discount)]
            temp.append(t)

        f = open('/data.txt', 'a')
        for t in temp:
            f.write(','.join(t)+'\r\n')
        f.close()
        self.message_user(request,'数据导出成功!')  # 提示信息

    get_datas.short_description = '导出所选数据'
    actions = ['get_datas']



