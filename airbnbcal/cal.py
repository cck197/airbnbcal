import os
from datetime import timedelta
from urllib.parse import urlparse

import requests
from icalendar import Calendar

ICAL_URL = os.environ["ICAL_URL"]


def download_ical(url):
    """Download iCal data from a URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "DNT": "1",  # Do Not Track Request Header
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Ensure the request was successful
    return response.content  # Return the content of the response


def get_ical_fname():
    return urlparse(ICAL_URL).path.split("/")[-1]


def extend_events_by_one_day(ical_content):
    """Extend the end date of each event in the iCal data by one day."""
    cal = Calendar.from_ical(ical_content)
    for component in cal.walk("vevent"):
        # Check if the event has an end date
        if component.get("dtend"):
            # Extend the end date by one day
            component["dtend"].dt += timedelta(days=1)
    return cal.to_ical()


def generate_updated_ical_content():
    ical_content = download_ical(ICAL_URL)
    return extend_events_by_one_day(ical_content)
