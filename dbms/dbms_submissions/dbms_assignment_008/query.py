Q1 = ''' 
         SELECT id,fname FROM Director d 
         WHERE EXISTS (SELECT m.id  FROM MovieDirector INNER JOIN Movie AS m ON m.id = `MovieDirector`.mid
         WHERE d.id = MovieDirector.did AND m.year > 2000)
         AND NOT EXISTS ( SELECT m.id FROM MovieDirector INNER JOIN Movie AS m ON m.id=`MovieDirector`.mid 
         WHERE d.id = MovieDirector.did AND m.year < 2000) ORDER BY d.id ASC;
     ''' 
     
Q2 = '''
         SELECT fname,
         (SELECT name FROM Movie  INNER JOIN MovieDirector ON `Movie`.id = `MovieDirector`.mid 
          WHERE `Director`.id=`MovieDirector`.did ORDER BY rank DESC,name ASC LIMIT 1)
         FROM Director LIMIT 100;
         
     '''         
         
Q3 = '''
         SELECT * FROM Actor a WHERE
         NOT EXISTS (SELECT m.id FROM Cast INNER JOIN Movie m ON `Cast`.mid = m.id
         WHERE a.id = `Cast`.pid AND year BETWEEN 1990 AND 2000 ) 
         ORDER BY a.id DESC LIMIT  100;
     '''
     
     
     
 