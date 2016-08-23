import datetime as dt
import dateutil.parser
from pytz import timezone

def compute_age_years(when, on=None):
    if on is None:
        on = dt.date.today()
    was_earlier = (on.month, on.day) < (when.month, when.day)
    return on.year - when.year - (was_earlier)

def date_iso8601(dob, time_zone=None):
    try:
        d = dt.datetime.strptime(str(dob), '%Y-%m-%d %H:%M:%S')
        if time_zone == None:
            loc_dt = timezone('US/Eastern'.localize(d)
        else:
            loc_dt = timezone(timez_zone).localize(d)
        est_dt = loc_dt.astimezone(eastern)
        offset = est_dt.strftime('%z').strip('-')[:2]
        date_string = est_dt.strftime('%Y-%m-%d')
        date_string += 'T%s:00:00.000Z'%(offset)
        return date_string
    except:
        return None
