# coding: utf-8
# author: shiqiangliang

import psycopg2
from dbutils.pooled_db import PooledDB
from django.db.backends.postgresql.base import DatabaseWrapper as PGDatabaseWrapper

_pools = {}


class DatabaseWrapper(PGDatabaseWrapper):
    def _set_autocommit(self, autocommit):
        """重写父类方法为空方法，因为PooledDB的conn没有autocommit属性
        """
        pass

    def init_connection_state(self):
        """重写父类方法为空方法，因为PooledDB的conn不在这里设置编码
        """
        pass

    def get_new_connection(self, conn_params):
        global _pools
        if not _pools.get(self.alias):
            conn_params['creator'] = psycopg2
            _pools[self.alias] = PooledDB(autocommit=True, **conn_params)

        return _pools.get(self.alias).connection()
