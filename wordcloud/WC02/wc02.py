%matplotlib inline
import sqlite3
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

dbfile = "applenews.db"
conn = sqlite3.connect(dbfile)

sql_str = "select * from news;"
rows = conn.execute(sql_str)
all_news = ""
for row in rows:
    all_news += row[3]

mask = np.array(Image.open('cloud.jpg'))
wordcloud = WordCloud(background_color="white",
                      width=1000, height=860, 
                      margin=2, font_path="simhei.ttf", 
                      mask=mask).generate(all_news)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()