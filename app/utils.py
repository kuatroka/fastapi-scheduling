import datetime


# convert uuid1 to datetime
def uuid1_time_to_datetime(time: int):
    """
    Convert a uuid1 time to a datetime object.
    """
    return datetime.datetime(1582, 10,
                             15) + datetime.timedelta(microseconds=time // 10)
