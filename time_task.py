"""
Time Tool
Description:
    Need to display an appropriate "time since" message
    You are given a creation date for a record in your archive
    You should analyse how much time has passed since then and another time (i.e. Now)
    The "then" time is given as a string in the form
		"jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec, date, year"
        e.g. "jan 2 1954" or "aug 4 2003" - assume this refers to midnight, the start of the day
    The "now" time is a unix timestamp, as given by a time.time() float, e.g. 1516113774.3526516
    You should print a message saying how many years, weeks or days have passed
    Round down to the biggest time unit:
		3 years, 24 weeks, 6 days is "3 years".
		11 weeks, 6 days is "11 weeks".
		52 weeks is "1 year".
		7 days is "1 week".
        4 days, 23 hours is "4 days".
    If there is only 1 unit, format as singular, e.g. "1 year", "1 week", "1 day"
    Assume you will always be given something in the correct format with "then" in the past
    Assume you are always in the same time zone - UTC+0000
    You may ignore leap seconds:
        a year is 365.25 days
        a week is 7 days.
        Ignore any leftovers
When is the problem solved?
    You write a method that returns a string that tells you how long
	it has been since something happened in terms of days, weeks or years.
"""
def time_since(then, now):
    return "2 days"

print(time_since("feb 26 2001", time.time()))
