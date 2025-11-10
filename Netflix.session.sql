SELECT t.title, t.type
FROM Netflix_IMDB t
WHERE t.director IS NULL
ORDER BY t.type;

SELECT t.title, t.averageRating, t.country
FROM Netflix_IMDB t
WHERE t.director IS NULL
ORDER BY t.country;
