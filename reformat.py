import json
import os

count = 0
for root_dir, cur_dir, files in os.walk(r'<Your_directory_path_that_contain_all_the_json_to_update>'):
    count += len(files)
print('file count:', count)


for i in range(count):
    with open(f'out/{i}.json') as f:
        data = json.load(f)
        data['token_uri']=f'https://.../{i}.json'
        data['token_id']=f'{i}'
        data['animation_url']='null'
        data['royalty_percentage']='null'
        data['royalty_payment_address']='null'
        # data['extension']={}
        
        

        

    
    for item in data['attributes']:
        item['trait_type'] = item['trait_type'].replace('Mask', 'Face')
        item['trait_type'] = item['trait_type'].replace('Body', 'Clothes')
        item['trait_type'] = item['trait_type'].replace('Head', 'Headwear')
        item['trait_type'] = item['trait_type'].replace('Flying Objects', 'Special Items')
        item['trait_type'] = item['trait_type'].replace('Neclaces', 'Necklace')

    with open(f'new_json/{i}.json', 'w') as f:
        json.dump(data, f)


f.close()
