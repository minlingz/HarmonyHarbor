from pyspark.sql.utils import AnalysisException
import matplotlib.pyplot as plt

# error handling and data validation
try:
  file_path = "dbfs:/user/hive/warehouse/prepared_song_data"
  prepared_song_data = spark.read.format("delta").load(file_path)

except AnalysisException as e:
    print(f"Error reading data: {e.description}")

try:
  if prepared_song_data.filter\
  (prepared_song_data["artist_name"].isNull()).count() > 0:
        raise ValueError("Null values found in artist_name column")

except ValueError as ve:
  print(ve)

result_df = spark.sql("""
SELECT
  artist_name,
  COUNT(artist_name) AS num_songs,
  year
FROM
  prepared_song_data
WHERE
  year > 0
GROUP BY
  artist_name, year
ORDER BY
  num_songs DESC, year DESC
""")

# Show some results
result_df.show()



# Convert Spark DataFrame to Pandas DataFrame
df = result_df.toPandas()

# Assuming the result set is large, you might want to visualize the top N
# results
top_n = df.head(20)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_n['artist_name'], top_n['num_songs'])
plt.xlabel('Artist Name')
plt.ylabel('Number of Songs')
plt.title('Number of Songs by Artist and Year')
plt.xticks(rotation=45)
plt.show()
