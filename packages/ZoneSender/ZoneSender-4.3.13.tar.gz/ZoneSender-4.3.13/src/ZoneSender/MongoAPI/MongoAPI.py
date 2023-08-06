import pymongo
from bson.objectid import ObjectId


class MongoAPI:
    """
    函数功能：初始化加载参数
    """

    def __init__(self, host, port, db, collect):
        self._mongo_client = pymongo.MongoClient("mongodb://{0}:{1}/".format(host, port))
        self._mongo_db = db
        self.mongo_collect = self._mongo_client[db][collect]

    """检查数据库是否存在"""

    def CheckDataBase(self):
        pass
        # dblist = self._mongo_client.list_database_names()
        # if self._mongo_db not in dblist:
        #     raise Exception("数据库:{0}不存在{1}中".format(self._mongo_db, dblist))

    """函数功能：插入一条数据"""

    def InsertOne(self, tupstr):
        try:
            # self.CheckDataBase()
            result = self.mongo_collect.insert_one(tupstr)
            result.inserted_id
        except Exception as e:
            raise Exception("执行函数：insert_one失败，错误信息{0}".format(e))

    """函数功能：插入多条数据"""

    def InsertMany(self, listStr):
        try:
            self.CheckDataBase()
            result = self.mongo_collect.insert_many(listStr)
            result.inserted_ids
        except Exception as e:
            raise Exception("执行函数：insert_many失败，错误信息{0}".format(e))

    """函数功能：查找表中第一条元素"""

    def FindOne(self):
        try:
            self.CheckDataBase()
            dit = self.mongo_collect.find_one()
            return dit
        except Exception as e:
            raise Exception("执行函数：find_one失败，错误信息:{0}".format(e))

    """函数功能：查找全部数据"""

    def FindAll(self):
        try:
            self.CheckDataBase()
            dits = self.mongo_collect.find()
            return dits
        except Exception as e:
            raise Exception("执行函数：find_all失败，错误信息:{0}".format(e))

    """函数功能：查询指定字段显示"""

    def FindPartShow(self, rules):
        try:
            self.CheckDataBase()
            dits = self.mongo_collect.find({}, rules)
            return dits
        except Exception as e:
            raise Exception("执行函数：find_partShow失败，错误信息:{0}".format(e))

    """函数功能: 查询指定的字段"""

    def FindRules(self, rules):
        try:
            self.CheckDataBase()
            dits = self.mongo_collect.find(rules)
            return dits
        except Exception as e:
            raise Exception("执行函数：find_rules失败，错误信息:{0}".format(e))

    """函数功能：按照查询的条数返回数据"""

    def FindLimit(self, num: int):
        try:
            self.CheckDataBase()
            dits = self.mongo_collect.find().sort([('_id', 1)]).limit(num)
            # dits = self.mongo_collect.find({"data.btrCfgArb":1268777296, "data.timeOffsetBrsNs":70672,"data.flags":3174400})

            return dits
        except Exception as e:
            raise Exception("执行函数：find_limit失败，错误信息:{0}".format(e))

    """函数功能：仅仅修改匹配条件的第一条数据"""

    def UpdateOne(self, rules, newValue):
        try:
            self.CheckDataBase()
            self.mongo_collect.update_one(rules, newValue)
        except Exception as e:
            raise Exception("执行函数：updata_one失败，错误信息:{0}".format(e))

    """函数功能：按照条件返回所有满足条件的数据"""

    def UpdateMany(self, rules, newValue):
        try:
            self.CheckDataBase()
            dits = self.mongo_collect.update_one(rules, newValue)
            return dits
        except Exception as e:
            raise Exception("执行函数：update_many失败，错误信息:{0}".format(e))

    """数据库操作：排序"""

    def Sort(self, key, order=1):
        try:
            self.CheckDataBase()
            mydoc = self.mongo_collect.find().sort(key, order)
            return mydoc
        except Exception as e:
            raise Exception("执行函数：sort 失败:错误信息:{0}".format(e))

    """函数功能：删除单条数据"""

    def DeleteOne(self, rule):
        try:
            self.CheckDataBase()
            self.mongo_collect.delete_one(rule)
        except Exception as e:
            raise Exception("执行函数delete_one失败，错误信息:{0}".format(e))

    """删除多条数据"""

    def DeleteMany(self, rules):
        try:
            self.CheckDataBase()
            self.mongo_collect.delete_many(rules)
        except Exception as e:
            raise Exception("执行函数delete_many失败，错误信息:{0}".format(e))

    """删除所有数据"""

    def DeleteAll(self):
        try:
            self.CheckDataBase()
            self.mongo_collect.delete_many({})
        except Exception as e:
            raise Exception("执行函数delete_all失败，错误信息:{0}".format(e))

    """删除表"""

    def Drop(self):
        try:
            self.CheckDataBase()
            self.mongo_collect.drop()
        except Exception as e:
            raise Exception("执行函数drop失败，错误信息:{0}".format(e))

    """统计数量"""

    def GetCount(self):
        c = self.mongo_collect.estimated_document_count()
        try:
            return c
        except Exception as e:
            raise Exception("执行函数GetCount失败，错误信息:{0}".format(e))

    """函数功能：分页查询数据"""
    def FindByPaging(self, rid: ObjectId, span:int):
        try:
            self.CheckDataBase()
            dits = self.mongo_collect \
                .find({'_id': {"$gt": rid}}) \
                .sort([('_id', 1)]).limit(span)
            return dits
        except Exception as e:
            raise Exception("执行函数：FindLimitByID失败，错误信息:{0}".format(e))


# 测试用例
def TestInsert():
    db = MongoAPI("localhost", 27017, "test", "test")
    # 测试单条数据
    mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
    db.InsertOne(mydict)

    # 测试多条数据
    mylist = [
        {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
        {"_id": 2, "name": "Google", "address": "Google 搜索"},
        {"_id": 3, "name": "Facebook", "address": "脸书"},
        {"_id": 4, "name": "Taobao", "address": "淘宝"},
        {"_id": 5, "name": "Zhihu", "address": "知乎"}
    ]
    db.InsertMany(mylist)


def testFind():
    db = MongoAPI("localhost", 27017, "test", "test")
    # 查找单条数据
    x = db.FindOne()
    print(x)

    # 查找全部数据
    x1 = db.FindAll()
    for data in x1:
        print(data)

    # 按照规则查询
    myqurey1 = {'_id': 0, 'name': 1, 'address': 1}
    x2 = db.FindPartShow(myqurey1)
    for data in x2:
        print(data)
    # 仅显示一条数据
    myqurey2 = {'name': 1}
    x3 = db.FindPartShow(myqurey2)
    for data in x3:
        print(data)

    # 高级查询
    myqurey3 = {"name": {"$gt": "H"}}  # 查询首字符大于H的数据
    x4 = db.FindRules(myqurey3)
    for data in x4:
        print(data)

    # 按照指定数据显示
    myqurey4 = {"name": "Taobao"}
    x5 = db.FindRules(myqurey4)
    for data in x5:
        print(data)

    # 正则表达式查询
    myqurey5 = {"name": {"$regex": "R"}}  # 查询首字母为R的数据
    x6 = db.FindRules(myqurey5)
    for data in x6:
        print(data)

    # 查询指定的数据量
    x7 = db.FindLimit(10)
    for data in x7:
        print(data)


def testUpdate():
    db = MongoAPI("localhost", 27017, "test", "test")

    # 仅修改匹配到的第一条数据
    myquery = {"name": "RUNOOB"}
    newValue = {"$set": {"name": "kangxin"}}  # 修改对应的字段名
    db.UpdateOne(myquery, newValue)
    for data in db.FindAll():
        print(data)

    # 条件查找
    myquery1 = {"name": {"$regex": "^G"}}
    newValue1 = {"$set": {"address": "王丽霞"}}
    db.UpdateMany(myquery1, newValue1)
    for x in db.FindAll():
        print(x)


def sort():
    db = MongoAPI("localhost", 27017, "test", "test")

    mydoc = db.Sort("_id", -1)  # 默认正序，-1为逆序
    for data in mydoc:
        print(data)


def delete():
    db = MongoAPI("localhost", 27017, "test", "test")

    # 删除单条数据
    myquery = {"name": "kangxin"}
    # db.delete_one(myquery)
    for x in db.FindAll():
        print(x)

    # 删除多条数据
    myquery1 = {"name": {"$regex": "Z"}}  # 数据中存在Z的name项
    db.DeleteAll(myquery1)
    for x in db.FindAll():
        print(x)

    # 删除所有数据
    db.DeleteAll()
    for x in db.FindAll():
        print(x)

    # 删除表
    db.Drop()

    db.CheckDataBase()
