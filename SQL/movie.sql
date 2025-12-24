CREATE DATABASE Movies;
USE Movies;
 CREATE TABLE telugu_Movies(
 Movie_id INT PRIMARY KEY,
 title VARCHAR(50),
 hero VARCHAR(50),
 heroine VARCHAR(50),
 director VARCHAR(50),
 release_year INT,
 budget INT,
 box_office int
 );
 
 INSERT INTO telugu_Movies VALUES
 (1,'Bahubali','Prabhas','Anushka','Rajamouli',2015,180,1000),
 (2,'Bahubali2','Prabhas','Anushka','Rajamouli',2017,250,1800),
 (3,'Pushpa','Alluarjun','Rasmika','Sukumar',2021,170,360),
 (4,'RRR','Ram charan','Alia Bhatt','SS Rajamouli',2022,550,1250),
 (5,'Ninnu Kori','Nani','Nivetha thomas','trivikram',2000,132,500),
 (6,'Aata','Siddharth','thrisha','Anil',1999,100,1999);
 
 SELECT * FROM telugu_Movies;
 
 SELECT title,hero,release_year FROM telugu_Movies;
 
 SELECT * FROM telugu_Movies
 WHERE hero ='Alluarjun';
 
 SELECT * FROM telugu_Movies
 WHERE hero='Prabhas';
 
 SELECT * FROM telugu_Movies
 WHERE release_year>2018;
 
 SELECT * FROM telugu_Movies
 WHERE release_year<2018;
 
 SELECT * FROM telugu_Movies
 ORDER BY box_office DESC;
 
 SELECT * FROM telugu_Movies
 ORDER BY box_office ASC;
 
 SELECT * FROM telugu_Movies
 ORDER BY release_year ASC;
 
 SELECT title,box_office
 FROM telugu_Movies
 ORDER BY box_office DESC
 LIMIT 1;
 
 SELECT director, COUNT(*) AS total_Movies
 FROM telugu_Movies
 GROUP BY director;
 
 SELECT title, budget
 FROM telugu_movies
 ORDER BY budget ASC
 LIMIT 1;
 
 SELECT AVG(box_office) AS avg_collection
 FROM telugu_Movies;
 
 SELECT *  FROM telugu_Movies
 WHERE title LIKE 'B%';
 
 SELECT * FROM telugu_Movies
 WHERE release_year BETWEEN 2015 AND 2020;
 
 UPDATE telugu_Movies
 SET budget=200
 WHERE title='Ninnu Kori'
 LIMIT 1;
 
 ALTER TABLE telugu_Movies
 ADD COLUMN genre_type VARCHAR(30);
 
 
 
 
 
 
 