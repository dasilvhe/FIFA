mport urllib.request
import json

player_list = {}

with urllib.request.urlopen("https://www.easports.com/fifa/ultimate-team/api/fut/item?page=100000") as url_to_find_max_page:
    data_to_find_max_page = json.loads(url_to_find_max_page.read().decode())
    max_page = data_to_find_max_page['totalPages']

    for number in range(1, 2):
        print ('Page Number Being Processing:' + str(number))
        with urllib.request.urlopen("https://www.easports.com/fifa/ultimate-team/api/fut/item?page=" + str(number)) as url:
            data = json.loads(url.read().decode())

        for item in data['items']:
            player_list_elements = {}
            for key, value in item.items():
                if key in ('league', 'headshot', 'specialImages','nation', 'club'):
                    for dictionary_key, dictionary_value in value.items():
                        if dictionary_key in ('imageUrls'):
                            for dictionary_key2, dictionary_value2 in dictionary_value.items():
                                if dictionary_key2 in ('dark','normal'):
                                    for dictionary_key3, dictionary_value3 in dictionary_value2.items():
                                        player_list_elements[key + ' ' + str(dictionary_key) + ' ' + str(dictionary_key2) + ' ' + str(dictionary_key3)] = str(dictionary_value3)
                                else:
                                    player_list_elements[key + ' ' + str(dictionary_key) + ' ' + str(dictionary_key2)] = str(dictionary_value2)
                        else:
                            player_list_elements[key + ' ' + str(dictionary_key)] = str(dictionary_value)
                elif key in ('traits'):
                    for list_item in value:
                        player_list_elements[list_item + ' ' + key] = True
                elif key in ('attributes'):
                    for list_item in value:
                        for dictionary_key, dictionary_value in list_item.items():
                            if dictionary_key in ('name'):
                                key = dictionary_value
                            elif dictionary_key in ('value'):
                                value = dictionary_value
                        player_list_elements[key] = value
                else:
                    player_list_elements[key] = str(value)
            player_list[item['id']]=player_list_elements
    print (player_list)
