events = '9/13 2:30 PM\n9/14 11:15 AM\n9/14 1:00 PM\n9/15 9:00 AM'

print(events)

# The number of events on 9/14
print(events.count('9/14'))

# The index of the substring describing the 1st event on 9/14
start = events.find('9/14')
print(start)

# The index just past the substring describing the last event on 9/14
end = events.find('9/15')
print(end)

# The list of substrings describing the events on 9/14
substr = events[start:end]
print(substr)
print(substr.strip().split('\n'))
