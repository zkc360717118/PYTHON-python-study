# encoding:utf-8
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, LongType, StringType

spark = SparkSession.builder.appName("test").getOrCreate()

# json - sql
def read_json_sql():
    # 构造用于测试的Json数据
    stringJSONRDD = spark.sparkContext.parallelize((
    """{"id": "123","name": "Katie","age": 19,"eyeColor": "brown"}""",
    """{"id": "234","name": "Michael","age": 22,"eyeColor": "green"}""",
    """{"id": "345","name": "Simone","age": 23,"eyeColor": "blue"}""")
    )
    # 创建DataFrame
    swimmersJSON = spark.read.json(stringJSONRDD)
    # DataFrame 注册为临时表 swimmersJSON
    swimmersJSON.createOrReplaceTempView("swimmersJSON")
    # DataFrame API 查看数据
    swimmersJSON.show()

    # 使用SQL查询
    data=spark.sql("select * from swimmersJSON").collect()  # sql函数返回的 DataFrame对象
    for i in data:             # 对于data中的每行是 Row类型,数据内容像键值对。
        print(i['eyeColor'])
    swimmersJSON.printSchema() # 查看模型树

# 前提条件是hive  的metastore 服务是开启的
def test_spark_sql_connect_hive_metastore():

    # os.environ["HADOOP_HOME"] = "D:\\hadoop-2.7.1"
    spark = SparkSession.builder.appName('test_local_conn_hive') \
    .config("hive.metastore.uris", "thrift://192.168.0.21:9083") \
    .master("local[*]") \
    .enableHiveSupport().getOrCreate()


    spark.sql('show tables').show()
    # spark.sql('select distinct id from test_table').show()
    # # spark.sql('create table copy_table as select * from test_table')
    # spark.sql('show tables').show()
    # spark.sql("insert into table test_table values('3', 38)")
    # spark.sql("insert into table test_table values('4', 48)")
    # spark.sql('select * from test_table').show()

    spark.stop()

def test_spark_sql_connect_hive_jdbc():
    spark = SparkSession.builder.appName('test_local_conn_hive') \
        .master("local[*]") \
        .enableHiveSupport().getOrCreate()

    jdbcDF = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:hive2://192.168.0.21:10000/default") \
        .option("dbtable", "default") \
        .option("user", "kevin") \
        .option("password", "11111") \
        .load()

    jdbcDF

if __name__ == "__main__":
    # read_json_sql()
    # specify_schema()
    # multi_table_query()
    # test_spark_sql_connect_hive_metastore()
    test_spark_sql_connect_hive_jdbc()