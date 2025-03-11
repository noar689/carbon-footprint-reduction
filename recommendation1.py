import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer , ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity

"""* `read the data`"""

path = os.path.join(os.getcwd(), 'dataset' , 'dataset.csv' )
df = pd.read_csv(path)


df['nam_category'] = df['name'] + ' ' + df['category']


custom_stopwords = list(ENGLISH_STOP_WORDS.union({
    'raw', 'dried', 'red', 'unknown',
    'concentrated', 'average', 'ready',
    'meals', 'frozen', 'products'
}))



tfidf = TfidfVectorizer(stop_words=custom_stopwords)
tfidf_matrix=tfidf.fit_transform(df['nam_category'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
pd.DataFrame(cosine_sim)


# tfidf_matrix.toarray() , len(tfidf.get_feature_names_out())

def product_index_(product_name):
    try:
        return df[df['name'] == product_name].index[0]
    except IndexError:
        print(" not found ")
        return None
product_index_('Pepper, sweet, red, raw')

def recommend_low_carbon(product_name, top_n):
    product_index = product_index_(product_name)
    if product_index is None:
        return None

    similarities = list(enumerate(cosine_sim[product_index]))

    similarities = [item for item in similarities if item[0] != product_index]

    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_n]

    similar_products = df.iloc[[int(i[0]) for i in similarities]].copy()

    similar_products = similar_products[similar_products['total_kg_co2-eq/kg'] < df.loc[product_index, 'total_kg_co2-eq/kg']]

    return similar_products[['id_ra','name', 'total_kg_co2-eq/kg', 'Price']]

product_name = "Tomato, dried"
recommendations = recommend_low_carbon(product_name, top_n=5)
print(recommendations)



