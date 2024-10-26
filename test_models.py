from models.user import User
from models.challenge import Challenge

from datetime import datetime

# attrs_user = {
#     'name' : "'oleg'",
#     'login' : "'login_oleg'",
#     'password' : "'oleg'",
#     'position' : "'team lead'",
# 	'department' : "'IT'",
# 	'create_date' : f"'{datetime.now()}'"
# }
# user = User(attrs_user)

# user.save()

# [print(row) for row in user.get_all()]

# print(user.get_one())

# changed_attrs_user = user.get_attrs()

# changed_attrs_user['name'] = "'misha'"

# user.set_attrs(changed_attrs_user)
# user.update()

# print(user.get_one())

# user.remove()

# print(user.get_one())

# print(user.get_all())

# print()
# print('время вызовов')
# print()

# attrs_challenge = {
# 	'title' :  "'challenge oleg'",
# 	'description' : f"'{'discription'*30}'",
# 	'prize' : '10',
# 	'amount_members' : '661'
# }
# challenge = Challenge(attrs_challenge)

# challenge.save()

# [print(row) for row in challenge.get_all()]

# print(challenge.get_one())

# changed_attrs_challenge = challenge.get_attrs()

# changed_attrs_challenge['amount_members'] = '123'

# challenge.set_attrs(changed_attrs_challenge)
# challenge.update()

# print(challenge.get_one())

# challenge.remove()

# print(challenge.get_one())

# print(challenge.get_all())


# авторизация
# user = User()

# rez = user.auth_user(login='login_oleg', password='oleg')

# print('rez = ', rez)

# user1 = User()

# rez1 = user1.auth_user(login='login_oleg', password='as')

# print('rez1 = ', rez1)

# user2 = User()

# rez2 = user2.auth_user(login='login_ole', password='as')

# print('rez2 = ', rez2)

# регистрация

user = User()

rez = user.register_user(login='login_oleg', password='oleg')

print('rez = ', rez)

user1 = User()

rez1 = user1.register_user(login='login_oleg', password='as')

print('rez1 = ', rez1)

user2 = User()

rez2 = user2.register_user(login='login_ole', password='as')

print('rez2 = ', rez2)