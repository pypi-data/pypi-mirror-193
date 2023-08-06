# coding: utf-8
# author: shiqiangliang

import pymysql
from dbutils.pooled_db import PooledDB
from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper

_pools = {}


class DatabaseWrapper(MySQLDatabaseWrapper):
    def _set_autocommit(self, autocommit):
        """重写父类方法为空方法，因为PooledDB的conn没有autocommit属性
        """
        pass

    def get_new_connection(self, conn_params):
        global _pools
        if not _pools.get(self.alias):
            conn_params['creator'] = pymysql
            _pools[self.alias] = PooledDB(autocommit=True, **conn_params)

        return _pools.get(self.alias).connection()

    def init_connection_state(self):
        """无需初始化数据库信息
        """
        pass
