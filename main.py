import json
from time import asctime
from datetime import datetime

date_db = json.load(open('./date.json'))
'''date database container'''

# Convert the db into real date
back_date = datetime(
    year=date_db['year'],
    month=date_db['month'],
    day=date_db['day'],
    hour=date_db['hour'],
    minute=date_db['min'])

duration = back_date - datetime.now()

print(duration)

