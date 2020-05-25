  
SELECT name,jersey_no,age,COUNT(`GoalDetails`.goal_id) FROM Player INNER JOIN 
GoalDetails ON GoalDetails.player_id = Player.player_id 
WHERE <= 27 GROUP BY GoalDetails.player_id ORDER BY player.name ; 
        
Q3 = '''
        SELECT DISTINCT(team_id),(SELECT COUNT(m.team_id) FROM Team 
        WHERE Team.team_id = m.team_id AND m.win_lose = 'W' ORDER BY m.team_id desc)
        From MatchTeamDetails m ORDER BY m.team_id ASC,; 
     '''

Q5 = '''SELECT `Match`.match_no,`captain`.teamid FROM Match INNER JOIN MatchCaptain ON 
        `Match`.match_no = `MatchCaptain`.match_no ;'''
        


Q6 = '''
        SELECT `Match`.match_no,Player.name(SELECT `Match`.player_of_match),`Player`.jersey_no FROM
        GoalDetails INNER JOIN Match ON `GoalDetails`.match_no = `Match`.match_no
        INNER JOIN Player ON `GoalDetails`.team_id = `Player`.team_id
        ORDER BY `Match`.match_no ASC;
     '''    

Q7 = '''
        SELECT Team.name,AVG(Player.age) FROM Team INNER JOIN Player ON 
        `Team`.team_id = `Player`.team_id
        WHERE AVG(Player.age) > 26; 
        
     '''
Q9 = '''
       SELECT team_id,( (SELECT count(mt.goal_score) FROM MatchTeamDetails) * 100) / (SELECT count(goal_score) FROM MatchTeamDetails)
       FROM MatchTeamDetails mt;
     '''

Q10 = '''SELECT AVG(goal_score) FROM MatchTeamDetails INNER JOIN Team 
        ON `MatchTeamDetails`.team_id = `Team`.team_id;
      '''
      
Q11 = '''
        SELECT player_id,name,date_of_birth FROM Player WHERE 
        NOT EXISTS (SELECT t.team_id FROM MatchTeamDetails mt INNER JOIN Team ON  
      '''

Q6 =
        SELECT `Match`.match_no,`Match`.player_of_match,`Player`.jersey_no FROM
        MatchCaptain INNER JOIN Match ON `MatchCaptain`.match_no = `Match`.match_no
        INNER JOIN Player ON `MatchCaptain`.team_id = `Player`.team_id
        ORDER BY `Match`.match_no ASC;

