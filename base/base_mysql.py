import pymysql
from base.base_log import Log
from base.base_readConfig import Config


# mysql数据库
class MySqlDatabase:
    def __init__(self):
        try:
            # 读取配置文件里面的内容，连接mysql数据库
            self.connect = pymysql.Connect(
                host=Config().read_config('mysql_db.ini', 'mysql_db', 'host'),
                user=Config().read_config('mysql_db.ini', 'mysql_db', 'user'),
                passwd=Config().read_config('mysql_db.ini', 'mysql_db', 'passwd'),
                db=Config().read_config('mysql_db.ini', 'mysql_db', 'db'),
                charset=Config().read_config('mysql_db.ini', 'mysql_db', 'charset'),
            )
            # 获取游标对象
            self.cursor = self.connect.cursor()
        # 数据库连接可能会出错，这里抛个异常
        except Exception as e:
            Log().error('数据库连接失败！{}'.format(e))

    def get_select_result(self, sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 获取查询结果的第一个数据
            result = self.cursor.fetchone()
            return result
        # sql语句查询可能会出错，这里抛个异常
        except Exception as e:
            Log().error("数据库语言查询失败,原因为:{}".format(e))

    def db_connect_quit(self):
        # 关闭游标对象
        self.cursor.close()
        # 关闭数据库连接
        self.connect.close()


if __name__ == '__main__':
    A = MySqlDatabase()