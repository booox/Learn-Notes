# Flask Questions and Answers

* `UnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 33: ordinal not in range(128)`
    * 请参考 [Unicode in Flask](http://flask.pocoo.org/docs/0.10/unicode/)
    * 请参考 [中文译文：Flask 中的 Unicode](http://www.phperz.com/article/15/0825/150980.html)
    * 要点如下：
        * 为了提供基本的无痛的 *Unicode* 支持， *Flask* 假定你的程序：
            * 站点编码： *UTF-8* 
            * 对非 *ASCII* 字符（即除字母、数字和一些符号外）一律采用 *Unicode* 编码，即在字符串前面加上小写的 *u* 。
            * 
    * 所以在保证文件编码为 *utf-8* 的前提下，只要做到下面两点即可正确显示中文：
        * 在 *.py* 文件中如果包含中文，则中文前面加 *u* ；文件顶端声明文件编码格式： `#coding=utf-8`
        * 在 *jinja* 模板中 ( *.html* ) 中直接写中文。
    * *flash* 消息时，则不需要用 *utf-8* 解码
        * `{{ message }}`
            * 即不需要： `{{ message.decode('utf-8') }}`
        

* 如何在 *jinja* 模板中使用 config 中的变量


* Flask error： `werkzeug.routing.BuildError`
    * *url_for* looks for a function.
    *  if you are using blueprints, *url_for* should be invoked as `url_for(blueprint_name.func_name)` . 
    * 最后检查来检查去，原来是没有将对应的 *blueprint* 与应用的工厂函数联系起来。
        ```
            def create_app(config_name):
                # ...
                from .auth import auth as auth_blueprint
                app.register_blueprint(auth_blueprint, url_prefix='/auth')
                
                return app
        
        ```