import pymysql
import configparser
import os

def connect(db):
    '''
    连接数据库
    :return:
    '''
    cf = configparser.ConfigParser()
    cf.read('db_conf.ini')
    # if os.path.isfile('../../config/conf.ini'):
    #     cf.read('../../config/conf.ini')
    # elif os.path.isfile('../config/conf.ini'):
    #     cf.read('../config/conf.ini')
    # elif os.path.isfile('../conf.ini'):
    #     cf.read('../conf.ini')
    # elif os.path.isfile('conf.ini'):
    #     cf.read('conf.ini')
    # elif os.path.isfile('/home/zhangxh/git/Interface_auto/config/conf.ini'):
    #     cf.read('/home/zhangxh/git/Interface_auto/config/conf.ini')
    # else:
    #     print('配置文件的相对路径有问题')
    db_host = cf.get(db, 'host')
    db_port = cf.get(db, 'port')
    db_user = cf.get(db, 'user')
    db_password = cf.get(db, 'password')
    db_name = cf.get(db, 'db_name')
    con = pymysql.connect(host=db_host,
                          port=int(db_port),
                          user=db_user,
                          passwd=db_password,
                          db=db_name,
                          charset='utf8')
    return con