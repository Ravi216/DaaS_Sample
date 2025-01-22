from pyspark.sql import SparkSession

def run_etl():
    # Initialize Spark Session
    spark = SparkSession.builder \
        .appName("DaaS_ETL") \
        .getOrCreate()

    # Step 1: Extract data (for example, a CSV file from S3)
    input_data = "s3://your-bucket/raw_data.csv"
    df = spark.read.csv(input_data, header=True, inferSchema=True)

    # Step 2: Transform data (example transformation)
    df_transformed = df.filter(df['age'] > 30).select('name', 'age', 'location')

    # Step 3: Load data (Save to Parquet for better performance)
    output_data = "s3://your-bucket/transformed_data/"
    df_transformed.write.parquet(output_data)

    # Stop Spark session
    spark.stop()

if __name__ == "__main__":
    run_etl()
