
import random
import pandas as pd
import numpy as np
from great_tables import GT
from plotnine import *
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

mazo_1['img'] = 'images/player_1/' + mazo_1['animal'] + '.png'

################# create mazo 2

animals_2 = ['penguin', 'kangaroo', 'koala'#, 
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

mazo_2['img'] = 'images/player_2/' + mazo_2['animal'] + '.png'

############### game 1

select_player_1 = mazo_1.sample(n=1)

select_player_2 =  mazo_2.sample(n=1)


############# player 1
(
    GT(select_player_1, rowname_col='img')
    .tab_header(
        title = "Card Game",
        subtitle = "Attack and Defense of player 1")
    .fmt_image(columns = 'img', height = 35)

)

########### player 2

(
    GT(select_player_2, rowname_col='img')
    .tab_header(
        title = "Card Game",
        subtitle = "Attack and Defense of player 1")
    .fmt_image(columns = 'img', height = 35)

)



######## select card

# select_player_1 = cards_player_1.iloc[[0]].copy()

# select_player_2 = cards_player_2.iloc[[0]].copy()



############### loop game

# Storage for game history
game_history = []

n = 50
for i in range(n):
    ############ attack 1 mazo 1
    select_player_2['shield'] = (select_player_2['shield'].values - 
                                select_player_1['power'].values)
    select_player_2 = select_player_2.assign(status=lambda x: np.where(x['shield'] > 0, 
                                                    'life', 'died'))
    select_player_2['attack'] = i
    
    # Store current state of both players
    current_state = pd.concat([select_player_1.copy(), select_player_2.copy()], axis=0)
    game_history.append(current_state)
    
    if 'died' in select_player_2['status'].values:
        break

########### attack 1 mazo 2
    select_player_1['shield'] = (select_player_1['shield'].values - 
                                select_player_2['power'].values)

    select_player_1 = select_player_1.assign(status=lambda x: np.where(x['shield'] > 0, 
                                                    'life', 'died'))

    select_player_1['attack'] = i

    # Store updated state after player 1 takes damage
    current_state = pd.concat([select_player_1.copy(), select_player_2.copy()], axis=0)
    game_history.append(current_state)

    if 'died' in select_player_1['status'].values:
        break

################# game history
game_history = pd.concat(game_history, ignore_index=True)

(
    ggplot(game_history.dropna(), 
                aes(x='attack', y='shield', color='player')) +
    geom_line() +
    geom_point() 
)


########## result game

result = pd.concat([select_player_1, select_player_2], axis=0)

(
    GT(result, rowname_col='img')
    .tab_header(
        title = "Card Game",
        subtitle = "Attack and Defense")
    .fmt_image(columns = 'img', height = 35)

)

