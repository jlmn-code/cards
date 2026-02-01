
import random
import pandas as pd
import numpy as np

################ create mazo 1

words_1 = ['apple', 'butterfly', 'castle', 'dolphin', 'elephant', 
                'firefly', 'giraffe', 'harmony', 'island', 'jungle',
                'kangaroo', 'lighthouse', 'mountain', 'nebula', 'octopus',
                'penguin', 'rainbow', 'starfish', 'tornado', 'umbrella']

power_1 = random.choices(range(1, 14), k=20)

shield_1 = random.choices(range(50, 100), k=20)

mazo_1 = pd.DataFrame({'words':words_1, 
                        'power':power_1, 
                        'shield':shield_1,
                        'player':'j'})

mazo_1 = mazo_1.assign(status=lambda x: np.where(x['shield'] > 0, 'life', 'died'))



################# create mazo 2

words_2 = ['adventure', 'breeze', 'canyon', 'diamond', 'eclipse', 
                'falcon', 'galaxy', 'horizon', 'iceberg', 'journey',
                'kingdom', 'lagoon', 'meadow', 'nomad', 'oasis',
                'palace', 'quartz', 'safari', 'thunder', 'volcano']

power_2 = random.choices(range(1, 14), k=20)

shield_2 = random.choices(range(50, 100), k=20)

mazo_2 = pd.DataFrame({'words':words_2, 
                        'power':power_2, 
                        'shield':shield_2,
                        'player':'s'})

mazo_1
mazo_2

############### game 1

selection_1_mazo_1 = mazo_1.sample(n=1)

selection_1_mazo_2 = mazo_2.sample(n=1)

############ attack 1 mazo 1


## selection_1_mazo_2['shield'] = (selection_1_mazo_2['shield'].values - 
##                            selection_1_mazo_1['power'].values)


## selection_1_mazo_2

########### attack 1 mazo 2

## selection_1_mazo_1['shield'] = (selection_1_mazo_1['shield'].values - 
##                            selection_1_mazo_1['power'].values)


## selection_1_mazo_1

############### attack 2 mazo 1

## selection_1_mazo_2['shield'] = (selection_1_mazo_2['shield'].values - 
##                            selection_1_mazo_1['power'].values)


## selection_1_mazo_2

############### attack 2 mazo 2

## selection_1_mazo_1['shield'] = (selection_1_mazo_1['shield'].values - 
##                            selection_1_mazo_1['power'].values)


## selection_1_mazo_1


############### loop game

n = 20
for i in range(n):
    ############ attack 1 mazo 1
    selection_1_mazo_2['shield'] = (selection_1_mazo_2['shield'].values - 
                                selection_1_mazo_1['power'].values)
    selection_1_mazo_2 = selection_1_mazo_2.assign(status=lambda x: np.where(x['shield'] > 0, 
                                                    'life', 'died'))
    selection_1_mazo_2['attack'] = i
    
    if 'died' in selection_1_mazo_2['status'].values:
        break

    ########### attack 1 mazo 2
    selection_1_mazo_1['shield'] = (selection_1_mazo_1['shield'].values - 
                                selection_1_mazo_2['power'].values)

    selection_1_mazo_1 = selection_1_mazo_1.assign(status=lambda x: np.where(x['shield'] > 0, 
                                                    'life', 'died'))

    selection_1_mazo_1['attack'] = i

    if 'died' in selection_1_mazo_1['status'].values:
        break


## result game



result = pd.concat([selection_1_mazo_1, selection_1_mazo_2], axis=0)

print(result)
