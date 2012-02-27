import jinja2
import re
from datetime import datetime, timedelta

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')
env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


def nl2br(value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br />\n')
                          for p in _paragraph_re.split(value))

    return result


def truncate_words(value, w):
    return " ".join(value.split(' ')[:w])


def elapsed_time(seconds, suffixes=['a', 's', 'd', 'h', 'm'], add_s=False,
        separator=' '):
    """Takes an amount of seconds and turns it into a human-readable amount of
    time.

    """
    # the formatted time string to be returned
    time = []

    # the pieces of time to iterate over (days, hours, minutes, etc)
    # - the first piece in each tuple is the suffix (d, h, w)
    # - the second piece is the length in seconds (a day is 60s * 60m * 24h)
    parts = [(suffixes[0], 60 * 60 * 24 * 7 * 52),
          (suffixes[1], 60 * 60 * 24 * 7),
          (suffixes[2], 60 * 60 * 24),
          (suffixes[3], 60 * 60),
          (suffixes[4], 60)]

    # for each time piece, grab the value and remaining seconds, and add it to
    # the time string
    for suffix, length in parts:
        value = seconds / length
        if value > 0:
            seconds = seconds % length
            time.append('%s%s' % (str(value),
                           (suffix, (suffix, suffix + 's')[value > 1])[add_s]))
        if seconds < 1:
            break

    return separator.join(time)


# one day in seconds = 86400
def date_diff(value, internal=False):
    if type(value) == 'str':
        fmt = '%Y-%m-%d %H:%M:%S'
        value = datetime.strptime(value, fmt)

    limit = timedelta(days=3)

    now = datetime.now()
    limit = value + limit

    diff_in_seconds = "%2.0f" % (limit - now).total_seconds()
    if not internal:
        return elapsed_time(int(diff_in_seconds))
    else:
        return int(diff_in_seconds)


env.filters['nl2br'] = nl2br
env.filters['truncate_words'] = truncate_words
env.filters['date_diff'] = date_diff
