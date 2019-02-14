


trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

# Save the direction of train 111 into a variable.

train_111_direction = trains[7]['direction']
print("The direction of train 111 is: {}".format(train_111_direction))

#frequency of 80B
train_80b_freq = trains[5]['frequency_in_minutes']
print("This is the frequncy of train 80B: {}".format(train_80b_freq))

# Save the direction of train 610 into a variable.

train_610_direction = trains[2]['direction']
print("The direction of train 610 is: {}".format(train_610_direction))

def trains_in_direction(trains, direction):
    trains_direction = []
    for train in trains:
        if train['direction'] == direction:
            trains_direction.append(train)
    return trains_direction

# all trains going north

trains_north = trains_in_direction(trains, 'north')
print("These are all the trains travelling north: {}".format(trains_north))

# trains going east

trains_east = trains_in_direction(trains, 'east')
print("These are all the trains travelling east: {}".format(trains_east))

# adding a key/value to one of the trains_east

trains[1]['first_departure_time'] = 8
print(trains)


def trains_to_freq(trains):
    trains_by_frequency = {}
    for train in trains:
        name = train['train']
        freq = train['frequency_in_minutes']
        if freq in trains_by_frequency:
            trains_by_frequency[freq].append(name)
        else:
            trains_by_frequency[freq] = [name]
    return trains_by_frequency


trains_freq = trains_to_freq(trains)
print("These are the trains according to their frequency: {}".format(trains_freq))   
