#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os

import tornado.web

from handlers.index import fe_url

settings = dict(
    ##设置cookie密钥,默认为字符串"secure cookies"
    cookie_secret= "lN2ImsFwS0yZlOM+d68dJZ5Ko7mrqEPEpInixMSWG84=",
    ##设置登陆路径，未登陆用户在操作时跳转会用到这个参数,默认为@tornado.web.authenticated
    #login_url= "/login",
    ##设置防跨站请求攻击,默认为False，即不可防御。
    #xsrf_cookies= True,

    #设置templates路径
    template_path = os.path.join(os.path.dirname(__file__), "templates"),

    ##设置静态文件解析路径
    static_path = os.path.join(os.path.dirname(__file__), "static"),

    #设置调试模式,默认为False，即不是调试模式。
    debug = True,

    ##设置是否自动编码：在2.0以上需要设置此项来兼容您之前的APP,不设置默认为自动编码。
    #autoescape = None,

    ##设置template_loader，可以从独立的路径中导入template：其中utils为自己定义的模块，ZipLoader是tornado.template.BaseLoader的子类。
    #template_loader=utils.ZipLoader,

    ##设置gzip压缩：
    #gzip=True

    #设置静态路径头部,默认是"/static/"
    #static_url_prefix = "/templates/"


    ##设置静态文件处理类.默认是tornado.web.StaticFileHandler
    #static_handler_class = MyStaticFileHandler,

    ##设置静态文件的参数,默认为空字典。
    #static_handler_args = {{ "key1":"value1", "key2":"value2"  }

    ##设置日志处理函数,日志处理函数your_fun，按照自己的意图记录日志。
    #log_function = your_fun,
    )

routes = fe_url

application = tornado.web.Application(
    handlers = routes,
    **settings
    )