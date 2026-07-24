distance_mi = 20
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = True

if distance_mi:
    print(bool(distance_mi))

if distance_mi <= 1:
    print('True')
elif not is_raining:
    print('True')
else:
    print('False')

if distance_mi > 1 and distance_mi <= 6 and (has_bike == True and is_raining == False):
    print('True')
else:
    print('False')

if distance_mi > 6 and (has_car or has_ride_share_app):
    print('True')
else:
    print('False')