class Config:
    NAME = 'AIHub'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@2019@192.168.23.166:3306/aihub'

    # 每次请求结束后都提交数据库变动
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True
