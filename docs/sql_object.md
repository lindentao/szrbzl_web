
对象定义
========

__目录__

-  [Advert](#advert)  广告推广
-  [Goods](#goods)  商品信息
-  [GoodsAttribute](#goodsattribute)  商品扩展属性
-  [GoodsPic](#goodspic)  商品图片
-  [Navigation](#navigation)  导航条
-  [OrderInfo](#orderinfo)  订单信息
-  [Payment](#payment)  支付
-  [ReceiptInformation](#receiptinformation)  收货信息
-  [ShorpCart](#shorpcart)  购物车信息
-  [Sort](#sort)  分类
-  [User](#user)  用户

#advert

广告推广

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id	 |		| ObjectId |	 |		   | False	  | None   |	 |
| create_time | 创建时间 | DateTime | |    | True	  |	now	   |	 |
| text	 | 内容 | String	 | 1	 | 256	   | True	  |		   |	 |

#goods

商品信息

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id     |      | ObjectId |	 |		   | False    | None   |	 |
| attribute | 属性 | Reference: [GoodsAttribute](#goodsattribute) | | | False | | |
| brand  | 品牌 | String | 1		 | 32	   | False	  |	None   |	 |
| brief  | 简介 | String | 1		 | 256	   | False	  |		   |	 |
| category | 类别 | Reference: [Sort](#sort) | | | False |     |	 	 |
| color | 颜色 | String | 1     | 16 	   | False	  |	None   |	 |
| made_in | 产地 | String | 1	 | 16 	   | False	  |	None   |	 |
| name	 | 名字 | String | 1		 | 64	   | True	  |		   |	 |
| num	 | 数量 | Int |          |         | True	  |	0	   |	 |
| origin | 来源 | String | 1  	 | 16  	   | False	  |	None   |	 |
| price	 | 单价 | Float |		 |		   | True	  |		   |	 |
| size | 尺寸 | String | 1	     | 8 	   | False	  |	None   |	 |
| upload_time | 上传时间 | DateTime | |	   | True	  |	now	   |	 |
| unit	 | 计数单位 | String | 1	 | 16      | True	  |		   |	 |
| weight | 重量 | Float |		 |   	   | False	  |	0	   |	 |
| pic	 | 图片 | List: Embedded [GoodsPic](#goodspic) | | | False | | |

#goodsattribute

商品扩展属性

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id     |      | ObjectId |	 |		   | False    | None   |	 |

#goodspic

商品图片

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id     |      | ObjectId |	 |		   | False    | None   |	 |
| name   | 名字 | String | 1		 | 32	   | True	  |		   |	 |
| path   | 路径 | String |  		 | 128	   | True	  |		   |	 |

#navigation

导航条

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id     |      | ObjectId |	 |		   | False    | None   |	 |
| display | 显示 | Bool |		 |		   | True	  | True   | True:显示 |
| name	 | 名字 | String | 1		 | 16	   | True	  |		   |	 |
| pic	 | 图片 | String |		 | 128	   | False	  |		   |	 |
| type   | 类型 | String |		 |		   | False    | None   |	 |
| url	 | 链接 | String |		 | 128	   | False	  |		   |	 |

#orderinfo

订单信息

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id     |      | ObjectId |	 |		   | False    | None   |	 |
| status | 订单状态 | String |	 | 32 	   | True	  | None   |	 |
| order_time | 下单时间 | DateTime | |	   | True	  |        |	 |
| pay	 | 支付 | Reference: [Payment](#payment) | | | True | None | |
| receive_time | 收货时间 | DateTime | |	   | False	  | None   |	 |
| user   | 用户 | Reference: [User](#user) | | | True | None   |		 |

#payment

支付

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id	 |		| ObjectId |	 |		   | False	  | None   |	 |
| money	 | 金额 | Float |		 |		   | True	  | 0	   |	 |
| name	 | 名称 | String	 |		 |	16	   | True	  | wechat | 微信,支付宝 |
| status | 状态 | Bool |			 |		   | True	  |	0	   |0:未支付;1:支付成功|
| type	 | 类型 | String |    	 |	16	   | True	  | 	   | 0:在线支付,1:货到付款 |

#receiptinformation

收货信息

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id	 |		| ObjectId |	 |		   | False	  | None   |	 |
| address | 地址 | String |		 | 128	   | True	  |        |	 |
| name	 | 名字 | String	 |		 | 16 	   | True	  |		   |	 |
| telephone | 手机号 | String |	 | 16 	   | True	  |		   |	 |

#shorpcart

购物车信息

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id	 |		| ObjectId |	 |		   | False	  | None   |	 |
| goods   | 商品 | Reference: [Goods](#goods) | | | True | None |	 |


#sort

分类

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id	 |		| ObjectId |	 |		   | False	  | None   |	 |
| name	 | 名字 | String	 |		 | 16 	   | True	  |		   |	 |
| sn	 | 序号 | String	 |		 | 8	   | True	  |		   |	 |

#user

用户

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id	 |		| ObjectId |	 |		   | False	  | None   |	 |
| email	 | 邮箱 | String  |		 |64	   | False	  |		   |	 |
| gender | 性别 | String  |		 | 10	   | False	  |	woman  |	 |
| level	 | 等级 | Int  |			 |		   | True	  |	0	   | 会员级别 |
| password | 用户口令 | String | | 64	   | True	  |        |	 |
| receipt | 收货信息 | List: Embedded: [ReceiptInformation](#receiptinformation) | | | False | | |
| role	 | 角色 | String |		 | 10	   | True	  | user   | user:用户;operator:操作员;superuser:超级管理员 |
| status | 状态 | Bool |			 |		   | False	  |		   | 0:禁用;1:启用 |
| telephone | 手机号 | String |	 | 16 	   | True	  |	None   |	 |
| real_name | 真实姓名 | String | | 16	   | False	  |	None   |     |
