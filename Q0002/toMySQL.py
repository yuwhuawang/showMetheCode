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
    sqlText = """CREATE TABLE key (id INT(8) NOT NULL , key TEXT NOT NULL , time TIMESTAMP NOT NULL , PRIMARY KEY (id));"""
    sqlText2 = """CREATE TABLE IF NOT EXISTS `test`.`key` ( `id` INT(8) NOT NULL , `key` TEXT NULL , `time` TIMESTAMP NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;"""

    #mysql.execute(sqlText2)

    sqlText3 = """ INSERT INTO `key`(`id`, `key`, `time`) VALUES (%s,%s,%s)"""
    args = (1,keygen.keygen(20),time.time())
    mysql.execute(sqlText3,args,mode=MySQLConn.DICTCURSOR_MODE,many=False)
    mysql.conn.commit()

keyToMySQL()