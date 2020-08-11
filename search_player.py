from bs4 import BeautifulSoup as sopa
import urllib.request
'''
url - plataforma
pc - PC
xbox - xone
psn - ps4

[-15] = KDRatio
[2] = rank_name
[8] = general_kd

'''


def s_player(nick, plataforma='pc'):
    url = 'https://r6.tracker.network/profile/'+plataforma+'/'+nick
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent': user_agent,}

    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    data = sopa(data,'html.parser')

    player_banner = data.findAll('div', {'style': 'flex-grow: 1; display: flex; justify-content: space-between; align-items: center;'})

    player_mmr = player_banner[0].find('div', attrs={'class':'trn-text--dimmed'}).text

    general_stats = data.findAll('div', {'class': 'trn-defstat__value'})
    ranked_kd_ratio = general_stats[-15].text
    ranked_kd_ratio = ranked_kd_ratio[1:-1:]
    

    player_rank = general_stats[2].text
    player_rank = player_rank[1:-1:]
    
    general_kd_ratio = general_stats[8].text
    general_kd_ratio = general_kd_ratio[1:-1:]

    infos = 'MMR: '+ player_mmr+ '\nRank: '+ player_rank+ '\nRanked-KD: '+ ranked_kd_ratio

    return infos










    


    
