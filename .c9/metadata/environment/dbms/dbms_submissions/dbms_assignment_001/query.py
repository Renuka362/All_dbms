{"filter":false,"title":"query.py","tooltip":"/dbms/dbms_submissions/dbms_assignment_001/query.py","undoManager":{"mark":12,"position":12,"stack":[[{"start":{"row":0,"column":181},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":2,"column":116},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":4,"column":123},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":6,"column":115},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":5}],[{"start":{"row":8,"column":73},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":10,"column":27},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":12,"column":45},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":14,"column":80},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":16,"column":74},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":10}],[{"start":{"row":18,"column":43},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":12}],[{"start":{"row":22,"column":0},"end":{"row":73,"column":0},"action":"insert","lines":["","Q1 = '''","        SELECT a.id,a.fname,a.lname,a.gender FROM Actor a","        INNER JOIN Cast c ON a.id = c.pid INNER JOIN ","        Movie m ON m.id = c.mid WHERE name LIKE 'Annie%'; ","     '''    ","","Q2 = '''","        SELECT m.id,m.name,m.rank,m.year FROM Movie m INNER JOIN","        MovieDirector md ON m.id = md.mid INNER JOIN ","        Director d ON d.id =  md.did WHERE d.fname = 'Biff'","        AND lname = 'Malibu' AND year IN(1999,1994,2003) ORDER BY rank","        DESC , year ASC;","     '''","     ","Q3 = '''","        SELECT year,COUNT(name) FROM Movie m GROUP BY (year)","        HAVING ( (SELECT AVG(rank) FROM Movie WHERE m.year = `Movie`.year) > ","        (SELECT AVG(rank) FROM Movie) ) ORDER BY year ASC;","     '''    ","     ","Q4 = '''","        SELECT id,name,year,rank FROM Movie  WHERE year = 2001 AND","        rank < (SELECT AVG(rank) FROM Movie) ORDER BY rank DESC LIMIT 10;","     '''    ","","Q6 = '''","        SELECT DISTINCT(a.id) FROM Actor a INNER JOIN Cast c ON a.id = c.pid","        INNER JOIN Movie m ON m.id = c.mid GROUP BY m.id,a.id HAVING","        COUNT(DISTINCT role) > 1 ORDER BY a.id ASC LIMIT 100;","     '''","     ","Q7 = '''","        SELECT fname, COUNT(fname) FROM Director GROUP BY(fname)","        HAVING COUNT(fname) > 1;","        ","     '''             ","     ","Q8 = '''","        SELECT id,fname,lname FROM Director d","        WHERE EXISTS (SELECT ","        pid FROM MovieDirector md INNER JOIN Cast c","        ON c.mid = md.mid WHERE d.id = did GROUP BY md.mid HAVING COUNT(DISTINCT pid) >= 100)","        AND NOT EXISTS (SELECT c.pid FROM MovieDirector md INNER JOIN Cast c","        ON c.mid = md.mid WHERE d.id = did GROUP BY md.mid HAVING COUNT(DISTINCT pid) < 100);","        ","     '''","","Q8 =    SELECT DISTINCT id,fname,lname FROM Director d INNER JOIN MovieDirector md ON","        d.id = md.did INNER JOIN Cast c ON c.mid = md.mid GROUP BY md.mid,d.id","        HAVING COUNT(DISTINCT(c.pid)) > 100;         ",""],"id":13}],[{"start":{"row":23,"column":0},"end":{"row":73,"column":0},"action":"remove","lines":["Q1 = '''","        SELECT a.id,a.fname,a.lname,a.gender FROM Actor a","        INNER JOIN Cast c ON a.id = c.pid INNER JOIN ","        Movie m ON m.id = c.mid WHERE name LIKE 'Annie%'; ","     '''    ","","Q2 = '''","        SELECT m.id,m.name,m.rank,m.year FROM Movie m INNER JOIN","        MovieDirector md ON m.id = md.mid INNER JOIN ","        Director d ON d.id =  md.did WHERE d.fname = 'Biff'","        AND lname = 'Malibu' AND year IN(1999,1994,2003) ORDER BY rank","        DESC , year ASC;","     '''","     ","Q3 = '''","        SELECT year,COUNT(name) FROM Movie m GROUP BY (year)","        HAVING ( (SELECT AVG(rank) FROM Movie WHERE m.year = `Movie`.year) > ","        (SELECT AVG(rank) FROM Movie) ) ORDER BY year ASC;","     '''    ","     ","Q4 = '''","        SELECT id,name,year,rank FROM Movie  WHERE year = 2001 AND","        rank < (SELECT AVG(rank) FROM Movie) ORDER BY rank DESC LIMIT 10;","     '''    ","","Q6 = '''","        SELECT DISTINCT(a.id) FROM Actor a INNER JOIN Cast c ON a.id = c.pid","        INNER JOIN Movie m ON m.id = c.mid GROUP BY m.id,a.id HAVING","        COUNT(DISTINCT role) > 1 ORDER BY a.id ASC LIMIT 100;","     '''","     ","Q7 = '''","        SELECT fname, COUNT(fname) FROM Director GROUP BY(fname)","        HAVING COUNT(fname) > 1;","        ","     '''             ","     ","Q8 = '''","        SELECT id,fname,lname FROM Director d","        WHERE EXISTS (SELECT ","        pid FROM MovieDirector md INNER JOIN Cast c","        ON c.mid = md.mid WHERE d.id = did GROUP BY md.mid HAVING COUNT(DISTINCT pid) >= 100)","        AND NOT EXISTS (SELECT c.pid FROM MovieDirector md INNER JOIN Cast c","        ON c.mid = md.mid WHERE d.id = did GROUP BY md.mid HAVING COUNT(DISTINCT pid) < 100);","        ","     '''","","Q8 =    SELECT DISTINCT id,fname,lname FROM Director d INNER JOIN MovieDirector md ON","        d.id = md.did INNER JOIN Cast c ON c.mid = md.mid GROUP BY md.mid,d.id","        HAVING COUNT(DISTINCT(c.pid)) > 100;         ",""],"id":14}]]},"ace":{"folds":[],"customSyntax":"sql","scrolltop":91.5,"scrollleft":0,"selection":{"start":{"row":23,"column":0},"end":{"row":23,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":4,"state":"start","mode":"ace/mode/sql"}},"timestamp":1589779035495,"hash":"a2df0a84cdc2909aaaadef67f1ecd4c142a346fc"}