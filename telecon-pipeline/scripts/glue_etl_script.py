import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1741287884527 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://mypracticadeclientes/clientes.csv"], "recurse": True}, transformation_ctx="AmazonS3_node1741287884527")

# Script generated for node SQL Query
SqlQuery3507 = '''
select * from myDataSource

'''
SQLQuery_node1741287888008 = sparkSqlQuery(glueContext, query = SqlQuery3507, mapping = {"myDataSource":AmazonS3_node1741287884527}, transformation_ctx = "SQLQuery_node1741287888008")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1741287890103 = glueContext.write_dynamic_frame.from_catalog(frame=SQLQuery_node1741287888008, database="datapipelines", table_name="clientes_csv", transformation_ctx="AWSGlueDataCatalog_node1741287890103")

job.commit()