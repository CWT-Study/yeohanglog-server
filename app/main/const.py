import datetime
import pytz
import os


# PROFILE_PATH = os.join(os.getcwd(), "image", "profile")
# TRIP_PICTURE_PATH = os.join(os.getcwd(), "image", "trip")


def get_utctime_string():
    return str(datetime.datetime.now(tz=pytz.utc).isoformat())