Q1 = "SELECT COUNT(name) FROM Movie WHERE (year =2002 AND name LIKE 'Ha%' AND rank > 2);"
Q2 = "SELECT MAX(rank) FROM Movie WHERE (name LIKE 'Autom%') AND (year=1983 OR year=1994);"
Q3 = "SELECT COUNT(id) FROM Actor WHERE gender = 'M' AND (fname LIKE '%ei' OR lname LIKE 'ei%');"    
Q5 = "SELECT SUM(rank) FROM Movie WHERE name LIKE '%Hary%' AND year BETWEEN 1981 AND 1984 AND rank < 9;"
Q6 = "SELECT TOP(r) FROM Movie WHERE rank = 5"