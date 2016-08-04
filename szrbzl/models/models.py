# -*- coding: UTF8 -*-

#为了测试而导入相关路径
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from datetime import datetime

from mongoengine import *

from vmall import settings

connect(settings.db_name, host=settings.db_host)

class AvailableDocument(object):
    '''权限处理'''
    @classmethod
    def available_objects(cls, user, **filters):
        # 根据user查询集过滤，由各子类进行实现
        return cls.objects(**filters)

    @classmethod
    def search_objects(cls, user, searchkey=u'', **filters):
        # 根据user查询集过滤，由各子类进行实现
        return cls.objects(**filters)

    @classmethod
    def is_createable(cls, user):
        # 缺省允许创建对象
        return True

    def is_readable(self, user):
        # 缺省允许读
        return True

    def is_editable(self, user):
        # 缺省不允许编辑
        if user.role not in ['superuser', 'operator']:
            return False
        else:
            return True


class Advert(Document, AvailableDocument):
    #广告推广
    create_time = DateTimeField(required=True, default=datetime.now, verbose_name=u'创建时间')
    text = StringField(required=True, default=u'', min_length=1, max_length=256, verbose_name=u'内容')   

class  GoodsAttribute(Document, AvailableDocument):
    #商品扩展属性
    pass

class Sort(Document, AvailableDocument):
    #分类
    name = StringField(required = True, max_length = 16, verbose_name=u'名字')
    sn = StringField(required = True, max_length = 8, verbose_name=u'序号')

class GoodsPic(EmbeddedDocument):
    #商品图片
    name = StringField(required = True, default=u'', min_length = 1, max_length = 32, verbose_name=u'名字')
    path = StringField(required = True, max_length = 128, verbose_name=u'路径')

class Goods(Document, AvailableDocument):
    #商品信息
    attribute = ReferenceField(GoodsAttribute, required=False, verbose_name=u'属性')
    brand = StringField(required=False, default=None, min_length=1, max_length=32, verbose_name=u'品牌')
    brief = StringField(min_length = 1, max_length = 256, required = False, verbose_name = u'简介')
    category = ReferenceField(Sort, required = False, verbose_name = u'类别')
    color = StringField(required=False, default=None, min_length=1, max_length=16, verbose_name=u'颜色')
    made_in = StringField(required=False, default=None, min_length=1, max_length=16, verbose_name=u'产地')
    name = StringField(required = True, default = u'',min_length = 1, max_length = 64, verbose_name=u'名字')
    num = IntField(required = True, default = 0, verbose_name=u'数量')
    origin = StringField(required=False, default=None, min_length=1, max_length=16, verbose_name=u'来源')
    pic = ListField(EmbeddedDocumentField(GoodsPic), required=False, default=[], verbose_name=u'图片')
    price = FloatField(required = True, verbose_name=u'单价')
    size = StringField(required=False, default=None, min_length=1, max_length=8, verbose_name=u'尺寸')
    upload_time = DateTimeField(required = True, default=datetime.now, verbose_name=u'上传时间')
    unit = StringField(required = True, default=u'', min_length = 1, max_length = 16, verbose_name=u'计数单位')
    weight = FloatField(required=False, default=0, verbose_name=u'重量')


class Navigation(Document, AvailableDocument):
    #导航条
    display = BooleanField(required = True, default = True, verbose_name=u'显示')
    name = StringField(required = True, min_length = 1, max_length = 16, default = u'', verbose_name=u'名字')
    pic = StringField(required = False, max_length = 128, verbose_name=u'图片')
    type = StringField(required = False, default = None, verbose_name=u'类型')
    url = StringField(required = False, max_length = 128, verbose_name=u'链接')

PaymentTypeChoice = (('0', u'在线支付'),
                ('1', u'货到付款'))

class Payment(Document, AvailableDocument):
    #支付
    money = FloatField(required = True, default = 0, verbose_name = u'金额')
    name = StringField(required = True, max_length = 16, default = 'wechat', verbose_name = u'名称')
    status = BooleanField(required = True, default = False, verbose_name = u'状态')
    type = StringField(required = True, default = '0', max_length = 16, verbose_name = u'类型')

class ReceiptInformation(EmbeddedDocument):
    #收货信息
    address = StringField(required = True, max_length = 128, verbose_name = u'地址')
    name = StringField(required = True, max_length = 16, verbose_name = u'名字')
    telephone = StringField(required = True, max_length = 16, verbose_name = u'手机号')

GenderChoice = (('man', u'男 '),
                ('woman', u'女'))

RoleChoice = (('user', u'用户'),
        ('operator',u'操作员'),
        ('superuser', u'超级管理员'))

class User(Document, AvailableDocument):
    #用户
    email = StringField(required = False, default=None, max_length = 64, verbose_name=u'邮箱')
    gender = StringField(required=False, max_length=10, default='woman', choices=GenderChoice, verbose_name=u'性别')
    level = IntField(required = True, default = 0, verbose_name = u'会员级别')
    password = StringField(required = True, max_length = 64, verbose_name = u'用户口令')
    receipt = ListField(EmbeddedDocumentField(ReceiptInformation),required = False, default=[], verbose_name = u'收货信息')
    role = StringField(required = True, default = 'user', max_length=10, choices = RoleChoice, verbose_name=u'角色')
    status = BooleanField(required = False, default = True, verbose_name=u'状态')
    telephone = StringField(required = True, max_length=16, default=None, verbose_name=u'手机号')
    real_name = StringField(required = False, default = None, max_length=16, verbose_name=u'真实姓名')

OrderStatusChoices = (('wait_payment', u'等待付款'),
        ('wait_delivery',u'等待发货'),
        ('finish_payment',u'已付款'),
        ('finish_deliverey',u'已发货'),
        ('finish',u'完成'),
        ('customer_refuse',u'客户拒收'),
        ('canceled', u'已取消'))

class OrderInfo(Document, AvailableDocument):
    #订单信息
    status = StringField(required = True, max_length = 32, choices = OrderStatusChoices, default = None, verbose_name=u'订单状态')
    order_time = DateTimeField(required = True, default = datetime.now, verbose_name=u'下单时间')
    pay = ReferenceField(Payment, required = True, verbose_name = u'支付')
    receive_time = DateTimeField(required = False, default = None, verbose_name=u'收货时间')
    user = ReferenceField(User, required = True, verbose_name = u'用户')

class ShorpCart(Document, AvailableDocument):
    #购物车信息
    goods = ReferenceField(Goods, required = True, verbose_name = u'商品')

if __name__ == '__main__':
    pass
    # linden = User(telephone = '15007984229', password = '123456').save()
    # lorempic = GoodsPic(name = 'lorem',path = '/static/images/p6.jpg')
    # lorem = Goods(name = 'equal blame', num = 110, price = 295.59, unit = '件')
    # lorem.pic = [lorempic]
    # lorem.save()

    # lorempic = GoodsPic(name='l2.jpg', path='/static/images/l2.jpg')
    # lorem = Goods.objects(id='57523baf36dc6a16940abdb6')
    # lorem.update_one(push__pic=lorempic)
    # lorem = Goods.objects[0]
    # print lorem.pk,lorem.id
    #t_resp = {}
    #l_resp = []
    #for good in Goods.objects:
    #    t_resp['name'] = good.name
    #    t_resp['price'] = good.price
    #    t_resp['pic'] = good.pic[0].path
    #    l_resp.append(t_resp.copy())
    #    print t_resp
    #    print t_resp.copy()
    #print l_resp

    good = Goods.objects.get(id='575d38e336dc6a55d048f35f')
    print good.made_in
    # print good.pic[0]
    # for p in good.pic:
    #     print p.path

