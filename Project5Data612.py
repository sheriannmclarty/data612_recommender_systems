# Step 1: Fix the casting issues and index your columns

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.recommendation import ALS
from pyspark.ml.feature import StringIndexer
from pyspark.ml.evaluation import RegressionEvaluator

# Start Spark
spark = SparkSession.builder.appName("CleanBeautyALS").getOrCreate()

# Load data
df = spark.read.csv("filtered_skintone_reviews_r.csv", header=True, inferSchema=True)

# Cast ratings to float
df = df.withColumn("rating_x", col("rating_x").cast("float"))

# Index string columns for ALS
user_indexer = StringIndexer(inputCol="author_id", outputCol="userIndex")
item_indexer = StringIndexer(inputCol="product_name_x", outputCol="itemIndex")

df = user_indexer.fit(df).transform(df)
df = item_indexer.fit(df).transform(df)

# Drop rows with missing data
als_df = df.select("userIndex", "itemIndex", "rating_x").na.drop()
# Step 2: Build the ALS model

als = ALS(
    maxIter=10,
    regParam=0.1,
    userCol="userIndex",
    itemCol="itemIndex",
    ratingCol="rating_x",
    coldStartStrategy="drop",
    nonnegative=True
)

model = als.fit(als_df)
# Step 3: Evaluate

# Split data
(train, test) = als_df.randomSplit([0.8, 0.2], seed=2025)

# Fit and predict
model = als.fit(train)
predictions = model.transform(test)

# Evaluate RMSE
evaluator = RegressionEvaluator(
    metricName="rmse",
    labelCol="rating_x",
    predictionCol="prediction"
)
rmse = evaluator.evaluate(predictions)
print(f"RMSE: {rmse:.4f}")