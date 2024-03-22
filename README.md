# Airbnb calendar fix

The standard Airbnb calendar has this annoying "feature" where the iCal event
for each reservation ends the day *before* the guests check out. This little
Flask app reads the [iCal URL from
Airbnb](https://www.airbnb.com/help/article/99) and exports an updated feed with
the feature corrected. 

Set a `.env` file like this:
```
ICAL_URL=https://www.airbnb.com/calendar/ical/<URL.ics>
```

Run it:
```
gunicorn app:app
```