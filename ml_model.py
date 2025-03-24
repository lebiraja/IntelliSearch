from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_results(results):
    texts = [summary for _, _, summary in results]
    
    if not texts:
        return results

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix).flatten()

    ranked_results = sorted(zip(results, scores), key=lambda x: x[1], reverse=True)
    return [(title, link, summary) for (title, link, summary), _ in ranked_results]
