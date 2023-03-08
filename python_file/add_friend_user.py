from .get_birthdays import get_birthdays 


def add_friend_user(vk, id):
    friend_list = []

    try:
        friends = vk.friends.get(
                                user_id=id, 
                                fields=['sex', 'bdate', 'city', 'country']
                                )['items']
        
        #sort friends by first_name
        friends = sorted(
                        friends, 
                        key=lambda x: x['first_name'])
    except vk.exceptions.VkAPIError as e:
        print(f'Some troubles: {e.code} - {e.message}')
        return 1

    try:
        for friend_id in friends:
            vk_dict = {}

            vk_dict["first_name"] = friend_id.get('first_name', '-')
            vk_dict["last_name"] = friend_id.get('last_name', '-')
            vk_dict["country"] = dict(friend_id.get('country', '')).get('title', '-')
            vk_dict["city"] = dict(friend_id.get('city', '')).get('title', '-')
            bdate = friend_id.get('bdate', '').split('.')
            vk_dict["bdate"] = get_birthdays(bdate)
            sex = friend_id.get('sex')
            vk_dict["sex"] = 'male' if sex == 2 else 'female'
            
            friend_list.append(vk_dict)
    except Exception as e:
        print(f'Something went wrong adding friends to the dictionary: {e}')    
   
    return friend_list
