#coding:utf-8
import keygen
import MySQLdb
import MySQLConn
import time
print keygen.keygen(20)

def keyToMySQL():
    mysql = MySQLConn.MySQLConn()
    mysql.newConnection(
        host="localhost",
        user="yuwhuawang",
        passwd="wyhwyh22",
        defaultdb="test"
    )

    #建表

    sqlText = """CREATE TABLE IF NOT EXISTS `test`.`key` ( `id` INT(8) NOT NULL , `key` TEXT NULL , `time` TIMESTAMP NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;"""
    mysql.execute(sqlText)



    #生成待插入数据
    args = []
    for i in range(1,201):
        new_list = (i,keygen.keygen(20))
        print time.time()
        args.append(new_list)

    #执行插入
    sqlText3 = """ INSERT INTO `key`(`id`, `key`) VALUES (%s,%s)"""
    try:
        mysql.execute(sqlText3, args, mode=MySQLConn.DICTCURSOR_MODE, many=True)
        mysql.conn.commit()
    except Exception,e:
        print e
if __name__ == "__main__":

    keyToMySQL();