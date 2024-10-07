from sentence_transformers import SentenceTransformer
from sklearn.manifold import TSNE
import seaborn as sns
import json

with open('strings.json') as fp:
    text = json.load(fp)

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
sentence_embeddings = embedding_model.encode(text)

viz_embeddings = TSNE(n_components=2, perplexity=100, n_iter=10000).fit_transform(sentence_embeddings)

sns.scatterplot(x=viz_embeddings[:, 0], y=viz_embeddings[:, 1], palette=None, s=100)
