import vk_api, os, sys
token = '586f8410dc573591bbdcd638703bba6bfe23b8aa37719bbe96b6e4b8fb2e8bcf04bf522b868d46247089b'
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()


def get_friendlist():
    user = (input('Скопируйте ID первого юзера:  '))
    method, counter = 'friends.search', 1000
    args= {'user_id': user, 'count': counter}
    list= vk_session.method(method, args)
    voc = []
    for item in list['items']:
        voc.append(item['id'])
    print(voc)

get_friendlist()











    # args_2 = {'user_id': user_2}
    # list_2 = vk_session.method(method, args_2)
    # names_1, names_2 = [],[]
    # for item in list_1['items']:
    #     fullname = item["first_name"]+" "+item['last_name']
    #     names_1.append(fullname)
    # for item in list_2:
    #     fullname = item["first_name"]+" "+item['last_name']
    #     names_2.append(fullname)
    # print(names_1)
    # print(names_2)





# get_friendlist(68580675, 55866604)
# get_friendlist(397100882, 120532794)

# def get_user_status(user_id):
#     status = vk_session.method("status.get", {'user_id': user_id})
#     print(status['text'])
#
#
# get_user_status(120532794)






#print(vk.wall.post(message='what'))