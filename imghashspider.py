#!/usr/bin/env python3

from __future__ import print_function

import urllib3
import re
import datetime
from dateutil.rrule import rrule, DAILY

from settings import URL_FILE, DILBERT_URL_PATTERN, DILBERT_FIRST_COMMIC_DATE

img_pattern = re.compile('<meta property="og:image" content="http://assets.amuniversal.com/([0-9a-fA-F]*)"/>')

http = urllib3.PoolManager()

def urlcrawler():

    with open(URL_FILE, 'w') as url_file:
        date_start = datetime.datetime.strptime(DILBERT_FIRST_COMMIC_DATE, "%Y-%m-%d")
        date_end = datetime.date.today()

        for dt in rrule(DAILY, dtstart=date_start, until=date_end):
            try:
                url_to_dilbert_page = DILBERT_URL_PATTERN % dt.strftime("%Y-%m-%d")
                page_contents = http.request('GET', url_to_dilbert_page).data.decode("utf-8") 
                image_hash = img_pattern.search(page_contents).group(1)
                print(image_hash, file=url_file)
                print('wrote hash for {0} : {1}'.format(dt.strftime("%Y-%m-%d"), image_hash))
            except Exception as e:
                print('error', e)

if __name__ == "__main__":
    urlcrawler()
