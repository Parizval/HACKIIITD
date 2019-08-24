from oauth2client.client import OAuth2WebServerFlow
from apiclient.discovery import build
from datetime import timedelta
from datetime import datetime
import time
import json
import httplib2
from firebase import firebase
firebase = firebase.FirebaseApplication(
    'https://fit-game-92ad4.firebaseio.com/', None)

CLIENT_ID = '1031502619062-d85pl5hkiu8b36fbmmmgaoc9gtd21kco.apps.googleusercontent.com'
CLIENT_SECRET = 'iC4ss_Eh7DrOicyNw3Sr6vy3'

OAUTH_SCOPE = 'https://www.googleapis.com/auth/fitness.activity.read'


DATA_SOURCE = "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps"

#email = input('Enter email')
TODAY = datetime.today().date()
NOW = datetime.today()
START = int(time.mktime(TODAY.timetuple())*1000000000)
END = int(time.mktime(NOW.timetuple())*1000000000)
DATA_SET = "%s-%s" % (START, END)


REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'


flow = OAuth2WebServerFlow(
    CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)


def retrieve_data():
    """
    https://developers.google.com/fit/rest/v1/reference/users/dataSources/datasets
    """
    flow = OAuth2WebServerFlow(
        CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
    authorize_url = flow.step1_get_authorize_url()
    #print('Go to the following link in your browser:')
    return authorize_url


CODE = ''


def get_code(CODE):
    code = CODE.strip()
    credentials = flow.step2_exchange(code)

    http = httplib2.Http()
    http = credentials.authorize(http)

    fitness_service = build('fitness', 'v1', http=http)

    return fitness_service.users().dataSources(). \
        datasets(). \
        get(userId='me', dataSourceId=DATA_SOURCE, datasetId=DATA_SET). \
        execute()


def nanoseconds(nanotime):
    dt = datetime.fromtimestamp(nanotime // 1000000000)
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def start():
    dataset = get_code(CODE)
    with open('dataset.txt', 'w') as outfile:
        json.dump(dataset, outfile)

    starts = []
    ends = []
    values = []
    for point in dataset["point"]:
        if int(point["startTimeNanos"]) > START:
            starts.append(int(point["startTimeNanos"]))
            ends.append(int(point["endTimeNanos"]))
            values.append(point['value'][0]['intVal'])
    try:
        frm = nanoseconds(min(starts))
        to = nanoseconds(max(ends))
        steps = sum(values)
    except:
        frm = 'None'
        to = 'None'
        steps = 0
    finally:
        print("From: ", frm)
        print("To: ", to)
        print("Steps: %d" % steps)
        result = firebase.post(
            '/fitdata', {'email': email, 'from': frm, 'to': to, 'steps': steps})
        print(result)
