from firebase import firebase

firebase = firebase.FirebaseApplication(
    'https://fit-game-92ad4.firebaseio.com/', None)


def register(email, name, password):
    firebase.post('/login', {'email': email, 'name': name, 'pass': password})


def login(email, password):
    res = firebase.get('/login', None)
    for i in res:
        if res[i]['email'] == email:
            if res[i]['pass'] == password:
                return True
    return False


print(login('ds1979@bennett.edu.in', '12we3'))
