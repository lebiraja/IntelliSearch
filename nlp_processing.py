import spacy

nlp = spacy.load("en_core_web_sm")

def summarize_results(results):
    summarized_results = []
    for title, link, snippet in results:
        doc = nlp(snippet)
        summary = " ".join([sent.text for sent in doc.sents][:2])  # Take first two sentences
        summarized_results.append((title, link, summary))
    return summarized_results
