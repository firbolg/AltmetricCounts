import os
import json
from collections import Counter
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

path = r"C:\Users\Levi\source\repos\AltmetricCounts\altmetric_data"

os.chdir(path)

geo_list = []
tweets_total = 0
tweeters_total = 0

for file in os.listdir():
    file_path = f"{path}\{file}"
    with open(file_path, "r") as f:
 
        data = json.loads(f.read())
        
 
        if "posts_count" in data["counts"]["twitter"]:
            #print("tweets: ",data["counts"]["twitter"]["posts_count"])
            tweets = data["counts"]["twitter"]["posts_count"]
            tweets_total = tweets_total + tweets
        if "unique_users_count" in data["counts"]["twitter"]:
            #print("tweeters: ",data["counts"]["twitter"]["unique_users_count"])
            tweeters = data["counts"]["twitter"]["unique_users_count"]
            tweeters_total = tweeters_total + tweeters
        if "geo" in data["demographics"]:
            if "twitter" in data["demographics"]["geo"]:
        #returns dict
            #print("location: ",data["demographics"]["geo"]["twitter"])
                geo = data["demographics"]["geo"]["twitter"]
                geo_list.append(geo)  
            else:
                continue
        else:
            continue
  


print(tweets_total, tweeters_total)

geo_result = Counter()
for d in geo_list:
    geo_result.update(d)
print(len(geo_result))


df = pd.read_csv(r"C:\Users\Levi\source\repos\AltmetricCounts\altmetric_country_coords_colorTEST.csv")

print(df.head())

# Set the dimension of the figure
plt.rcParams["figure.figsize"]=30,20;

# Make the background map
m=Basemap(llcrnrlon=-180, llcrnrlat=-65, urcrnrlon=180, urcrnrlat=80, projection='merc');
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0);
m.fillcontinents(color='grey', alpha=0.3);
m.drawcoastlines(linewidth=0.1, color="white");

# Make the background map
m=Basemap(llcrnrlon=-180, llcrnrlat=-65, urcrnrlon=180, urcrnrlat=80)
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.3)
m.drawcoastlines(linewidth=0.1, color="white")

# prepare a color for each point depending on the continent.
df['labels_enc'] = pd.factorize(df['color_range'])[0]
 
# Add a point per position
m.scatter(
    x=df['long'], 
    y=df['lat'], 
    s=df['tweets']/2, 
    alpha=0.4, 
    c=df['labels_enc'], 
    cmap="Set1"
)

plt.text( -175, -62,'Where People are Tweeting About Articles in the NIH Preprint Pilot\n\nData Collected from PMC, bioRxiv, medRxiv, and Altmetric\nPlotted with Python Basemap library', 
         ha='left', va='bottom', size=9, color='#555555' )

plt.show()
plt.savefig('maptest.png')

