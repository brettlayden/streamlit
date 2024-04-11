import exchange_calendars as ec
import streamlit as st
import streamlit_calendar as sc

markets = ec.get_calendar_names()

market = st.selectbox("Market", markets)

calendar = ec.get_calendar(market)
calendar_events = [
    {
        "title": "Ad-hoc holiday",
        "start": f"{x.strftime('%Y-%m-%d')}",
        "end": f"{x.strftime('%Y-%m-%d')}",
    }
    for x in calendar.adhoc_holidays
]

calendar_options = {
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridMonth,multiMonthYear,listYear",
    }
}

calendar_events.extend(
    [
        {
            "title": f"{x[1]}",
            "start": f"{x[0].strftime('%Y-%m-%d')}",
            "end": f"{x[0].strftime('%Y-%m-%d')}",
        }
        for x in calendar.regular_holidays.holidays(return_name=True).items()
    ]
)

sc.calendar(events=calendar_events, options=calendar_options)
