import vk_api
from conf import token
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()


def get_friendlist():
    user_1, user_2 = int(input('Скопируйте ID первого юзера:  ')), int(input('Скопируйте ID второго юзера:  '))
    method, counter = 'friends.search', 1000
    args_1, args_2 = {'user_id': user_1, 'count': counter}, {'user_id': user_2, "count": counter}
    list_1, list_2 = vk_session.method(method, args_1), vk_session.method(method, args_2)
    id_list_2, common = [], []
    for item in list_2['items']:
        id = (item['id'])
        id_list_2.append(id)
    for item in list_1['items']:
        if item['id'] in id_list_2 and item['first_name'] != "DELETED":
            common.append(item['first_name'] + ' ' + item['last_name'])
    print(common, len(common))








