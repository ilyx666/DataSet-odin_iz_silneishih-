import pandas as pd
import requests
import lxml
import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import undetected_chromedriver
import time




pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)



request_site = Request(url='https://www.dotabuff.com/matches?lobby_type=ranked_matchmaking', headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"})
webpage = urlopen(request_site)
soup__ = BeautifulSoup(webpage, 'lxml')
region_option = soup__.find_all('option')

f = 0
d = 0
region_dict = {}
dungeon = ['Europe West', 'Chile', 'Australia', 'Dubai', 'Peru', 'India']
for i in region_option:
    if 172 > d >= 156:
        if 'Europe West' != i.text:
            if 'Chile' != i.text:
                if 'Dubai' != i.text:
                    if 'South Africa' != i.text:
                        if 'India' != i.text:
                            if 'China' != i.text:
                                region_text = i.text.lower().replace(' ', '_')
                                region_href_ = 'https://www.dotabuff.com/matches?lobby_type=ranked_matchmaking&region=' + region_text
                                region_dict[region_text] = region_href_
    d += 1


with open("region_dict.json", "w") as file:
    json.dump(region_dict, file, indent=4, ensure_ascii=False)

with open("region_dict.json") as file:
    region_ = json.load(file)


team1_1p = []
team1_2p = []
team1_3p = []
team1_4p = []
team1_5p = []
team2_1p = []
team2_2p = []
team2_3p = []
team2_4p = []
team2_5p = []
matches_id = []
duration = []
game_mode = []
all_heroes = []
region = []
who_win = []




try:
    for i in range(11):
        for redion_name, region_href in region_.items():



            print()






            request_site = Request(url=region_href, headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"})
            webpage = urlopen(request_site)
            soup_ = BeautifulSoup(webpage, 'lxml')
            qwe = soup_.find_all('a')
            for_who_winner = soup_.find_all('a')
            for_duration = soup_.find_all('td')
            for_game_mode = soup_.find_all('td')
            hero_names_in_match = soup_.find_all('a')
            for_region = soup_.find_all('div', class_='subtext')
                # if i.text == '00:00':
                #
                # # time.sleep(900)
                # # print('wait-__')
                #     d += 1

            for times in for_duration:
                if ':' in times.text:
                    duration.append(times.text)






            d = 0

            for igg in qwe:
                if d % 2 == 0:
                    if 'matches' and '6' in igg.get('href'):
                        matches_id.append(igg.get('href').removeprefix('/matches/'))

                d += 1

            d = 0

            for ggi in for_who_winner:
                if 'Victory' in ggi.text:
                    who_win.append(ggi.text)
                d += 1






            for iqwe in for_game_mode:
                if "All" in iqwe.text:
                    game_mode.append(iqwe.text.removesuffix('Ranked Matchmaking'))



            # d = 0
            # for names in hero_names_in_match:
            #     if 'heroes' in names.get('href'):
            #         if d >= 11:
            #
            #             all_heroes.append(names.get('href').removeprefix('/heroes/').title().replace('-', '_'))
            #
            #         d += 1


            d = 1

            for ie in for_region:
                if d % 3 == 0:
                    region.append(ie.text)

                d += 1






            d = 0
            xxx = 0
            for names in hero_names_in_match:
                if 'heroes' in names.get('href'):
                    if d >= 11:


                        if xxx % 10 == 0:

                            team1_1p.append(names.get('href').removeprefix('/heroes/').title().replace('-', '_'))

                        elif xxx % 10 == 1:
                            team1_2p.append(names.get('href').removeprefix('/heroes/').title().replace('-', '_'))

                        elif xxx % 10 == 2:
                            team1_3p.append(names.get('href').removeprefix('/heroes/').title().replace('-', '_'))

                        elif xxx % 10 == 3:
                            team1_4p.append(names.get('href').removeprefix('/heroes/').title().replace('-', '_'))

                        elif xxx % 10 == 4:
                            team1_5p.append(names.get('href').removeprefix('/heroes/').title().replace('-', '_'))

                        elif xxx % 10 == 5:
                            team2_1p.append(names.get('href').removeprefix('/heroes/').title().replace('-', '_'))

                        elif xxx % 10 == 6:
                            team2_2p.append(names.get('href').removeprefix('/heroes/').title().replace('-', '_'))

                        elif xxx % 10 == 7:
                            team2_3p.append(names.get('href').removeprefix('/heroes/').title().replace('-', '_'))

                        elif xxx % 10 == 8:
                            team2_4p.append(names.get('href').removeprefix('/heroes/').title().replace('-', '_'))
                        elif xxx % 10 == 9:
                            team2_5p.append(names.get('href').removeprefix('/heroes/').title().replace('-', '_'))

                    d += 1
                    xxx += 1

            alina_ne_daet = []
            for nuls in duration:
                if '00:00' == nuls:
                    g = duration.index(nuls)
                    alina_ne_daet.append(g)
                    for nnn in alina_ne_daet:

                        duration.pop(nnn)
                        matches_id.pop(nnn)
                        who_win.pop(nnn)
                        region.pop(nnn)
                        if len(team1_1p) > len(duration):
                            team1_1p.pop(nnn)
                        if len(team1_2p) > len(duration):
                            team1_2p.pop(nnn)
                        if len(team1_3p) > len(duration):
                            team1_3p.pop(nnn)
                        if len(team1_4p) > len(duration):
                            team1_4p.pop(nnn)
                        if len(team1_5p) > len(duration):
                            team1_5p.pop(nnn)
                        if len(team2_1p) > len(duration):
                            team2_1p.pop(nnn)
                        if len(team2_2p) > len(duration):
                            team2_2p.pop(nnn)
                        if len(team2_3p) > len(duration):
                            team2_3p.pop(nnn)
                        if len(team2_4p) > len(duration):
                            team2_4p.pop(nnn)
                        if len(team2_5p) > len(duration):
                            team2_5p.pop(nnn)


            while (len(team1_1p)*4) != (len(duration)+len(who_win)+len(region)+len(matches_id)):
                duration.pop(-1)
                who_win.pop(-1)
                region.pop(-1)
                matches_id.pop(-1)

            print(len(matches_id))
            print(len(who_win))
            print(len(duration))
            print(len(region))
            print(len(team1_1p))
            print(len(team1_2p))
            print(len(team1_3p))
            print(len(team1_4p))
            print(len(team1_5p))
            print(len(team1_1p))
            print(len(team2_2p))
            print(len(team2_3p))
            print(len(team2_4p))
            print(len(team2_5p))
            print(matches_id)
            print(who_win)
            print(duration)
            print(region)
            print(team1_1p)
            print(team1_2p)
            print(team1_3p)
            print(team1_4p)
            print(team1_5p)
            print(team1_1p)
            print(team2_2p)
            print(team2_3p)
            print(team2_4p)
            print(team2_5p)
            # team1_1p.pop(0)
            # team1_2p.pop(0)
            # team1_3p.pop(0)
            # team1_4p.pop(0)
            # team1_5p.pop(0)
            # team2_1p.pop(0)
            # team2_2p.pop(0)
            # team2_3p.pop(0)
            # team2_4p.pop(0)
            # team2_5p.pop(0)



        df = pd.DataFrame({'id_matches': matches_id,
                           'winner': who_win,
                           'duration': duration,
                           'region': region,
                           'team radiant 1p': team1_1p,
                           'team radiant 2p': team1_2p,
                           'team radiant 3p': team1_3p,
                           'team radiant 4p': team1_4p,
                           'team radiant 5p': team1_5p,
                           'team dire 1p': team2_1p,
                           'team dire 2p': team2_2p,
                           'team dire 3p': team2_3p,
                           'team dire 4p': team2_4p,
                           'team dire 5p': team2_5p})

        print(df)
        time.sleep(1200)

except ValueError:
    df.to_excel('tabl_3000.xlsx')
    pass
    # time.sleep(900)
df.to_excel('tabl_3000_1.xlsx')




















# if soup.find(class_='match-result team radiant') in qwe_:
#     print(qwe_.text.removeprefix('Powered by TrueSight Beta')[:4])
#     who_win.append(qwe_.text.removeprefix('Powered by TrueSight Beta')[:7].removesuffix(' Vi'))
# else:
#     print(qwe_.text.removeprefix('Powered by TrueSight Beta')[:7].removesuffix(' Vi'))
#     who_win.append(qwe_.text.removeprefix('Powered by TrueSight Beta')[:7].removesuffix(' Vi'))
#
# for match_name, match_href in matches.items():
#     try:
#         driver = undetected_chromedriver.Chrome()
#         driver.get(match_href)
#         time.sleep(15)
#     except Exception as ex:
#         print(ex)
