django-pooldb
=============
基于DBUtils.PooledDB封装的Django数据库连接池引擎
Django database connection pool engine based on DBUtils.PooledDB
------------------------
~~~~~
pip install django-pooldb
~~~~~

Using django-pooldb
-------------------

Add the following to your ``settings.py``:
```python
DATABASES = {
    'default': {
        'ENGINE': 'pooldb.backends.mysql',
        'NAME': 'test',
        'HOST': '127.0.0.1',
        'PORT': 13306,
        'USER': 'root',
        'PASSWORD': '123456',

        'OPTIONS': {  #  dbutils extra params
            'maxconnections': 100,
        },
    }
}
```



