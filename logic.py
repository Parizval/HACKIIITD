from firebase import firebase
import validate
firebase = firebase.FirebaseApplication(
    'https://fit-game-92ad4.firebaseio.com/', None)


def get_rank(dct):
    lst = []
    for i in dct:
        lst.append([dct[i]['steps'], i])
    lst.sort(reverse=True)
    return lst


data = firebase.get('/fitdata', None)
# print(data)
dct = {}
for i in data:
    dct[data[i]['email']] = {'from': data[i]['from'],
                             'to': data[i]['to'], 'steps': data[i]['steps']}
# print(dct)
rank = get_rank(dct)
unit = 1
tot = len(rank) * unit
new_list = []
counter = 2
for i in rank:
    new_list.append([tot * (1/counter), i])
    counter += 2
print(new_list)
counter = 1
for i in new_list:
    dd = {'email': i[1][1], 'pos': counter, 'price': i[0]}
    counter += 1
    firebase.post('/message', dd)
res = firebase.get('/ethdata', None)
bal = firebase.get('/ethbalance', None)
dct = {}
bal_dct = {}
for i in res:
    dct[res[i]['email']] = res[i]['public_key']
for i in bal:
    bal_dct[bal[i]['email']] = bal[i]['balance']
print(bal_dct, dct)
for j in new_list:
    if j[1][1] in dct:
        validate.send_money(j[0], dct[j[1][1]])
        bal_dct[j[1][1]] += j[0]
for i in bal_dct:
    tmp = {'email': i, 'balance': bal_dct[i]}
    print(tmp)
    _ = firebase.post('/ethbalance', tmp)
