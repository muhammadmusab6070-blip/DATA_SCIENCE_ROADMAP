-- 1. Numerical Operators

SELECT * FROM movies
WHERE imdb_rating > 8;

SELECT * FROM movies
WHERE imdb_rating < 5;

SELECT * FROM movies
WHERE imdb_rating >= 8;

SELECT * FROM movies
WHERE imdb_rating <= 5;


-- 2. AND

SELECT * FROM movies
WHERE imdb_rating > 8
AND industry = 'Bollywood';


-- 3. OR

SELECT * FROM movies
WHERE industry = 'Bollywood'
OR industry = 'Hollywood';


-- 4. BETWEEN

SELECT * FROM movies
WHERE imdb_rating BETWEEN 7 AND 9;


-- 5. IN

SELECT * FROM movies
WHERE industry IN ('Bollywood', 'Hollywood');


-- 6. ORDER BY - Ascending

SELECT * FROM movies
ORDER BY imdb_rating ASC;


-- 7. ORDER BY - Descending

SELECT * FROM movies
ORDER BY imdb_rating DESC;


-- 8. LIMIT - Top 5

SELECT * FROM movies
ORDER BY imdb_rating DESC
LIMIT 5;


-- 9. LIMIT - Top 10

SELECT * FROM movies
ORDER BY imdb_rating DESC
LIMIT 10;


-- 10. LIMIT - Bottom 5

SELECT * FROM movies
ORDER BY imdb_rating ASC
LIMIT 5;


-- 11. OFFSET - Skip first 5 and get next 5

SELECT * FROM movies
ORDER BY imdb_rating DESC
LIMIT 5 OFFSET 5;


-- 12. Highest-rated Bollywood movies

SELECT * FROM movies
WHERE industry = 'Bollywood'
ORDER BY imdb_rating DESC;


-- 13. Top 5 highest-rated Bollywood movies

SELECT * FROM movies
WHERE industry = 'Bollywood'
ORDER BY imdb_rating DESC
LIMIT 5;


-- 14. Bollywood movies rated between 7 and 9

SELECT * FROM movies
WHERE industry = 'Bollywood'
AND imdb_rating BETWEEN 7 AND 9;


-- 15. Top 10 Hollywood movies

SELECT * FROM movies
WHERE industry = 'Hollywood'
ORDER BY imdb_rating DESC
LIMIT 10;


-- 16. 6th to 10th highest-rated movies

SELECT * FROM movies
ORDER BY imdb_rating DESC
LIMIT 5 OFFSET 5;


-- 17. 11th to 15th highest-rated movies

SELECT * FROM movies
ORDER BY imdb_rating DESC
LIMIT 5 OFFSET 10;


-- 18. Combined Query

SELECT * FROM movies
WHERE imdb_rating >= 8
ORDER BY imdb_rating DESC
LIMIT 5 OFFSET 2;