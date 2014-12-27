
import statistics

teams = {}
all_games = []

def game_update(date, team1, score1, team2, score2, spread):

    d = 100
    
    if team1 not in teams:
        teams[team1] = {'games_played': 0, 'game_values': [], 'team_value': 1.000, 'volatile': 0, 'schedule': []}
        
    if team2 not in teams:
        teams[team2] = {'games_played': 0, 'game_values': [], 'team_value': 1.000, 'volatile': 0, 'schedule': []}
    
    teams[team1]['game_values'].append((d + spread + (score1-score2))/(100/teams[team2]['team_value']))
    teams[team1]['games_played'] += 1
    
    if score1 > score2:
        if (score1-score2)>(spread*-1):
           teams[team1]['schedule'].append([date,team1, score1, team2, score2, 'W', 'Cover'])
        else:
            teams[team1]['schedule'].append([date, team1, score1, team2, score2, 'W', 'No Cover'])
            
    else:
        teams[team1]['schedule'].append([date, team1, score1, team2, score2, 'L', 'No Cover'])
            

    teams[team2]['game_values'].append((d + (spread*(-1)) + (score2-score1))/(100/teams[team1]['team_value']))
    teams[team2]['games_played'] += 1
    
    if score2 > score1:
        teams[team2]['schedule'].append([date,team2, score2, team1, score1, 'W', 'Cover'])
    else:
        if (score2 - score1)>(spread):
            teams[team2]['schedule'].append([date, team2, score2, team1, score1, 'L', 'Cover'])
        else:
            teams[team2]['schedule'].append([date,team2, score2, team1, score1, 'L', 'No Cover'])
            
    all_games.append([date,team1,score1,team2,score2])
            
    
    for i in teams:
        if teams[i]['games_played'] > 0:
            teams[i]['team_value'] = (sum(teams[i]['game_values'])/teams[i]['games_played'])
        if len(teams[i]['game_values']) >= 2:
            teams[i]['volatile'] = statistics.stdev(teams[i]['game_values'])

def stats(z):
    print (z+': ')
    print ('Team Value: ')
    print (teams[z]['team_value'])
    print ('Volatility: ')
    print (teams[z]['volatile'])

def sched(z):
    q = 0
    v = 0
    g = 0
    h = 0
    for i in teams[z]['schedule']:
        if i[4] =='W':
            q+=1
        if i[4] == 'L':
            v+=1
    for i in teams[z]['schedule']:
        if i[5] =='Cover':
            g+=1
        if i[5] == 'No Cover':
            h+=1
    print ('Record: '+str(q)+' - '+str(v)+','+'Vs. Spread: '+str(g)+' - '+str(h))
    for i in teams[z]['schedule']:
        print (i)

def spread_streaks():
    for i in teams:
        x = teams[i]['schedule'][-1][5]
        
        q = -2
        k = 1
        while (q*-1) < len(teams[i]['schedule']):
            if x == teams[i]['schedule'][q][5]:
                           k+=1
                           q-=1
            else:
                           break
                     
        if k >= 2:
                           print (i, x, k, 'in a row')

def result_streaks():
    for i in teams:
        x = teams[i]['schedule'][-1][4]
        
        q = -2
        k = 1
        while (q*-1) < len(teams[i]['schedule']):
            if x == teams[i]['schedule'][q][4]:
                           k+=1
                           q-=1
            else:
                           break
                     
        if k >= 2:
                           print (i, x, k, 'in a row')
                           
def vol_rank():
    z = {}
    for i in teams:
        z[i] = teams[i]['volatile']
    f = [(k,v,) for v,k in sorted([(v,k) for k,v in z.items()])]
    for i in f:
        print (i)

def team_rank():
    z = {}
    for i in teams:
        z[i] = teams[i]['team_value']
    f = [(k,v,) for v,k in sorted([(v,k) for k,v in z.items()], reverse = True)]
    for i in f:
        print (i)

def entire():
    for i in all_games:
        print (i)
        




  

    
    


                                        
                    
