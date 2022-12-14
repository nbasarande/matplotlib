from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

df=pd.read_csv('data.csv')
ids=df['Responder_id']
responses=df['LanguagesWorkedWith']
language_counter=Counter()

for response in responses:
    language_counter.update(response.split(';'))
total_language_response=sum(language_counter.values())
languages=[]
popularity=[]
for i in language_counter.most_common(6):
    languages.append(i[0])
    popularity.append(i[1])
total_most_freq_lang=sum(popularity)
other_lang = total_language_response - total_most_freq_lang

languages.insert(0, 'Other')
popularity.insert(0, other_lang)
color=['tab:blue','tab:orange','tab:green','tab:purple','tab:red','tab:cyan','tab:gray','tab:pink','tab:olive']
explode = [0, 0, 0, 0, 0.07, 0, 0]
plt.pie(popularity, labels=languages, explode=explode, shadow=True, colors=color,
        startangle=140, autopct='%1.1f%%',
        wedgeprops={'edgecolor':"k"})

plt.title("My Title")
plt.tight_layout()
plt.savefig("pie_1.png")
plt.show()