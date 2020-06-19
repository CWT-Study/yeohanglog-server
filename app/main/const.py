import datetime
import pytz

def get_utctime_string():
    return str(datetime.datetime.now(tz=pytz.utc).isoformat())