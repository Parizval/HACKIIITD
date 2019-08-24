from firebase import firebase

firebase = firebase.FirebaseApplication(
    'https://fit-game-92ad4.firebaseio.com/', None)
# result = firebase.get('/users', None)
# result = firebase.post('/users', 'Hello')
result = firebase.post(
    '/ethbalance', {'email': 'ds1979@bennett.edu.in', 'balance': 1000})
print(result)
