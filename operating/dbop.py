import pymysql


class DB:
    # 连接数据库，并返回连接到的数据库对象
    def con_db(self):  # 默认参数
        try:
            db = pymysql.connect(host='localhost', user='root', password='mysql', database='carpooling')

        except:
            print("数据库链接异常!")
        finally:
            return db

    # 查询数据库
    def search_db(self, sql, *args):
        db = self.con_db()  # 连接数据库
        cu = db.cursor()  # 得到一个游标
        cu.execute(sql, *args)  # 通过游标执行sql语句
        result = cu.fetchall()  # 获取sql执行结果
        db.commit()  # 提交数据库
        db.close()  # 关闭数据库连接对象
        print("查询成功")
        return result

    # 增删改数据库
    def fix_db(self, sql, *args):
        db = self.con_db()
        cu = db.cursor()  # 得到一个游标
        cu.execute(sql, *args)  # 通过游标执行sql语句
        db.commit()  # 提交数据库
        db.close()  # 关闭数据库连接对象
        print("增删改成功")


# 测试pdbc工具类是否可用
if __name__ == '__main__':
    d = DB()
    sql = "select * from driver "
    result = d.search_db(sql);
    print(result);
    sql = "insert into route(start,end,length) values(%s,%s,%s)"
    a = 'sss'
    b = 's'
    c = int(1)

    d.fix_db(sql, (a, b, c))

    # d.fix_db("delete from userinfo where username='q2'")
    # result = d.search_db("select * from userinfo where username='q1'")
    # print(result)

# try:
#     cursor=con.cursor();
#     # 执行sql语句的方法:\
#     # print(db);
#     sql="select * from driver;";
#     # cursor.execute(s);
#
#     cursor.execute(sql);
#     print(cursor.fetchone());
#     print(cursor.fetchone());
#     print(cursor.fetchone());
# except:
#     print("执行失败");
# finally:
#     con.close();
