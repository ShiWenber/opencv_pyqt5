import csv

# List of event logs to save as a CSV file
event_logs = [
    {'event': '<a, b, c, d, e, f>2', 'count': 2},
    {'event': '<a, b, c, d, e, g>3', 'count': 3},
    {'event': '<a, b, c, d, i, c, d, e, f>3', 'count': 3},
    {'event': '<a, b, c, d, i, c, d, e, g>', 'count': 1},
    {'event': '<a, c, d, e, f>', 'count': 1},
    {'event': '<a, c, d, e, g>2', 'count': 2},
    {'event': '<a, b, c, d, e, h, f>', 'count': 1},
    {'event': '<a, b, c, d, h, e, f>', 'count': 1},
    {'event': '<a, b, c, d, e, h, g>', 'count': 1},
    {'event': '<a, b, c, d, h, e, g>', 'count': 1},
    {'event': '<a, b, j>', 'count': 1},
]

# Open a file for writing and create a CSV writer object
with open('event_logs.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['event', 'count'])

    # Write the headers to the CSV file
    writer.writeheader()

    # Iterate over the event logs and write each one to the CSV file
    for event in event_logs:
        writer.writerow(event)


with open('event_logs.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)
