# based on pyspark standard example
from random import random
from operator import add

def within_circle_quarter (_):
	# x, y in [0,1)
	x, y = random(), random()
	return 1 if x**2 + y**2 <= 1.0 else 0

spark = SparkSession.builder.appName( 'breakit' ).getOrCreate()
spark.sparkContext.setLogLevel( "INFO" )

n = 10000
partitions = 10
quarter_count = spark.sparkContext.parallelize( range(n), partitions).map(within_circle_quarter).reduce(add)

pi = 4.0 * quarter_count / n

print("pi={}" .format(pi))