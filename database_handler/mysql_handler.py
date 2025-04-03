import pymysql


class DBHandler:
    def __init__(self,
                 host=None,
                 port=3306,
                 user='root',
                 password='',
                 charset='utf8',
                 database=None,
                 **kw
                 ):

        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset=charset,  # 不能是 utf-8
            database=database,
            **kw
        )
        self.cursor = self.conn.cursor()

    def query_one(self, sql, args=None):
        """查询数据库一条记录"""
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.fetchone()

    def query_all(self, sql, args=None):
        """查询数据库一条记录"""
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.fetchall()

    def query(self, sql, args=None, one=True):
        """主体查询函数"""
        if one:
            return self.query_one(sql, args)
        return self.query_all(sql, args)

    def close(self):
        """关闭"""
        self.cursor.close()
        self.conn.close()