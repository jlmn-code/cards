
import random
import pandas as pd
import numpy as np
from great_tables import GT
pd.set_option('display.max_columns', None)

################ create mazo 1

animals_1 = ['lion', 'tiger', 'bear', 
#            'wolf', 'fox', 
#           'eagle', 'shark', 'whale', 'dolphin', 'panther', 
#           'leopard', 'cheetah', 'gorilla', 'monkey', 'elephant', 
#          'rhino', 'hippo', 'zebra', 'giraffe', 'crocodile'
           ]

power_1 = random.choices(range(1, 14), k=3)

shield_1 = random.choices(range(50, 100), k=3)

mazo_1 = pd.DataFrame({'animal':animals_1, 
                        'power':power_1, 
                        'shield':shield_1,
                        'player':'j'})

mazo_1['img'] = 'images/player_1/' + mazo_1['animal'] + '.jpeg'

################# create mazo 2

animals_2 = ['penguin', 'kangaroo', 'koala', 
#            'panda', 'sloth', 
#             'otter', 'beaver', 'raccoon', 'squirrel', 'rabbit', 
#             'turtle', 'snake', 'lizard', 'frog', 'owl', 
#             'hawk', 'camel', 'llama', 'bison', 'moose'
    ]


power_2 = random.choices(range(1, 14), k=3)

shield_2 = random.choices(range(50, 100), k=3)

mazo_2 = pd.DataFrame({'animal':animals_2, 
                        'power':power_2, 
                        'shield':shield_2,
                        'player':'s'}
                        )

mazo_2['img'] = 'images/player_2/' + mazo_2['animal'] + '.jpeg'

############### game 1

cards_player_1 = mazo_1.sample(n=1)

cards_player_2 = mazo_2.sample(n=1)



######## select card

select_player_1 = cards_player_1.iloc[[0]].copy()

select_player_2 = cards_player_2.iloc[[0]].copy()



############### loop game

n = 50
for i in range(n):
    ############ attack 1 mazo 1
    select_player_2['shield'] = (select_player_2['shield'].values - 
                                select_player_1['power'].values)
    select_player_2 = select_player_2.assign(status=lambda x: np.where(x['shield'] > 0, 
                                                    'life', 'died'))
    select_player_2['attack'] = i
    
    if 'died' in select_player_2['status'].values:
        break

    ########### attack 1 mazo 2
    select_player_1['shield'] = (select_player_1['shield'].values - 
                                select_player_2['power'].values)

    select_player_1 = select_player_1.assign(status=lambda x: np.where(x['shield'] > 0, 
                                                    'life', 'died'))

    select_player_1['attack'] = i

    if 'died' in select_player_1['status'].values:
        break
            ########## result game


result = pd.concat([select_player_1, select_player_2], axis=0)

(
    GT(result)
    .tab_header(
        title = "Card Game",
        subtitle = "Attack and Defense")
    .fmt_image(columns = 'img', height = 35)

)

