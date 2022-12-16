from matplotlib import pyplot as plt
import numpy as np
import csv
import pandas as pd
from collections import Counter

plt.style.use("fivethirtyeight")

df=pd.read_csv('data.csv')
ids=df['Responder_id']
responses=df['LanguagesWorkedWith']
language_counter=Counter()

for response in responses:
    language_counter.update(response.split(';'))
total_language_response=sum(language_counter.values())
languages=[]
popularity=[]
for i in language_counter.most_common(9):
    languages.append(i[0])
    popularity.append(i[1])
total_most_freq_lang=sum(popularity)
other_lang = total_language_response - total_most_freq_lang

languages.insert(0, 'Other')
popularity.insert(0, other_lang)


#plt.bar(languages,popularity)          # to see the bars upright
languages.reverse() # reverse is used to see highest values item on the top
popularity.reverse()
plt.barh(languages,popularity)



plt.title("My Title")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.tight_layout()
plt.savefig("bar_2.png")
plt.show()
