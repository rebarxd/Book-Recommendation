# Litera Search

This code implements a collaborative filtering-based recommender system for books. It first filters users who have rated more than 200 books and selects books that have received at least 50 ratings. The resulting DataFrame is then transformed into a pivot table for further processing.

Cosine similarity scores are calculated between books based on user ratings. The **`recommend`** function takes a book title as input, finds its index in the pivot table, and identifies the most similar books using cosine similarity scores. The function returns a list of recommended books along with their authors, sorted by similarity.

In the provided example, when 'Animal Farm' is given as input, the system recommends four books: '1984' by George Orwell, 'Angus, Thongs and Full-Frontal Snogging: Confessions of Georgia Nicolson' by Louise Rennison, 'Midnight' by Dean R. Koontz, and 'Second Nature' by Alice Hoffman, based on their similarity to 'Animal Farm' in terms of user ratings.
