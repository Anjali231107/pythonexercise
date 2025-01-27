import pprint

# Define the nested list
t = [
    [
        [['black', 'cyan'], 'white', ['green', 'red']],
        [['magenta', 'yellow'], 'blue']
    ]
]

# Pretty print the list with a specified width
pprint.pprint(t, width=30)
