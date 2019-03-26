import crawl_sptfy as spotify
import pandas as pd
import numpy as np

print('\n\nSongs Project.\n_______________________________\n\nGetting Spotify data...\n\n')

# Define countries list
countries_list = ['de', 'es', 'fr', 'il', 'pl', 'us']

# Define dates
start = '2017-12-31'
end = '2019-01-01'

charts_dict = {}

for country in countries_list:

    sleep = np.clip(abs(np.random.normal()),1.2,5)

    print(f'\nGetting chart for {country.upper()}...\n')
    data = spotify.get_charts(start=start, end=end, region=country, freq='weekly', chart='top200', sleep=sleep)
    filename = fr'data/{country}_{start[:4]}.csv'
    data.to_csv(filename, index=False)
    print(f'Chart for {country.upper()} ({start[:4]}) saved as {filename}\n')
    print('__________________________________________')



