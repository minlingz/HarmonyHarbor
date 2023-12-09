from pyspark.sql.utils import AnalysisException
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import pi


# error handling and data validation
try:
  file_path = "dbfs:/user/hive/warehouse/prepared_song_data"
  prepared_song_data = spark.read.format("delta").load(file_path)

except AnalysisException as e:
    print(f"Error reading data: {e.description}")

# convert into a DataFrame
song_data_df = prepared_song_data.toPandas()
song_data_df.head()

# Grouping by year and calculating the average for duration, tempo,
# and time signature
yearly_averages = song_data_df.groupby('year').mean()

# Determine the min and max year from your dataset
# min_year = song_data_df['year'].min()
max_year = song_data_df['year'].max()

# Plotting the trends over years using an area chart
plt.figure(figsize=(10, 6))
plt.fill_between(yearly_averages.index, yearly_averages['duration'],
        color="skyblue", alpha=0.4)
plt.plot(yearly_averages.index, yearly_averages['duration'],
        color="Slateblue", alpha=0.6, label='Average Duration (seconds)')

plt.fill_between(yearly_averages.index, yearly_averages['tempo'],
        color="olive", alpha=0.3)
plt.plot(yearly_averages.index, yearly_averages['tempo'],
        color="olivedrab", alpha=0.6, label='Average Tempo (BPM)')
plt.title('Trend Analysis of Song Characteristics Over Years')
plt.xlabel('Year')
plt.ylabel('Average Values')
plt.xlim(1925, max_year)
plt.legend()
plt.grid(True)
plt.show()


# Selecting top N artists based on the number of songs they have in the dataset
top_n = 5
top_artists = song_data_df['artist_name'].value_counts().head(top_n).index

# Filtering data for only top artists and calculating their average song
# duration, tempo, and time signature
filtered_df = song_data_df[song_data_df['artist_name'].isin(top_artists)]
artist_analysis = filtered_df.groupby('artist_name').mean()

# Selecting relevant columns for radar chart
columns = ['duration', 'tempo', 'time_signature']
artist_analysis = artist_analysis[columns]

# Normalizing the data for better comparison in the radar chart
for col in columns:
    artist_analysis[col] = (
        (artist_analysis[col] - artist_analysis[col].min()) /
        (artist_analysis[col].max() - artist_analysis[col].min())
    )
# Preparing to plot the radar chart
num_vars = len(columns)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Setting up the subplot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Drawing one artist per variable
for artist, row in artist_analysis.iterrows():
    values = row.tolist()
    values += values[:1]
    ax.plot(angles, values, label=artist)

# Adding labels
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(columns)

# Adding a legend and title
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
plt.title('Comparative Analysis of Top Artists')

plt.show()
