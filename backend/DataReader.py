import csv
import numpy as np

venues = {
    0: {'name': 'PLOEGENDIENST', 'long': '51.6248573', 'lat': '4.7389255'},
    1: {'name': 'VESTROCK', 'long': '51.283112', 'lat': '4.0283127'},
    2: {'name': 'THE FLYING DUTCH - ROTTERDAM', 'long': '51.8808041', 'lat': '4.4808997'},
    3: {'name': 'THE FLYING DUTCH - EINDHOVEN', 'long': '51.347275', 'lat': '5.3167355'},
    4: {'name': 'THE FLYING DUTCH - AMSTERDAM', 'long': '52.132633', 'lat': '5.291265999999999'},
    5: {'name': 'AMSTERDAM OPEN AIR', 'long': '52.3065615', 'lat': '4.9933607'},
    6: {'name': 'FULL MOON FESTIVAL', 'long': '52.132633', 'lat': '5.291265999999999'},
    7: {'name': 'OMG! FESTIVAL', 'long': '51.40993', 'lat': '5.9814482'},
    8: {'name': 'PUSSY LOUNGE AT THE PARK', 'long': '51.6248573', 'lat': '4.7389255'},
    9: {'name': 'KOMM SCHON ALTER FESTIVAL', 'long': '52.3765795', 'lat': '4.783460199999999'},
    10: {'name': 'DRIFT FESTIVAL', 'long': '51.8532423', 'lat': '5.8346224'},
    11: {'name': 'BOOTHSTOCK', 'long': '51.9262323', 'lat': '4.5193922'},
    12: {'name': 'OHM FESTIVAL', 'long': '52.0043623', 'lat': '4.3779313'},
    13: {'name': 'BEATCOIN FESTIVAL', 'long': '52.132633', 'lat': '5.291265999999999'},
    14: {'name': 'CREATIONS - FESTIVAL', 'long': '52.132633', 'lat': '5.291265999999999'},
    15: {'name': 'ATMOZ OUTDOOR', 'long': '51.4570505', 'lat': '5.503711699999999'},
    16: {'name': 'THE LIVING VILLAGE', 'long': '52.52525', 'lat': '6.288808299999999'},
    17: {'name': 'DEFQON1', 'long': '52.4605804', 'lat': '5.6627062'},
    18: {'name': 'CAMP MOONRISE', 'long': '52.2177917', 'lat': '6.146942'},
    19: {'name': 'STRANGE SOUNDS FROM BEYOND', 'long': '52.4095854', 'lat': '4.8868895'},
    20: {'name': 'INDIAN SUMMER FESTIVAL', 'long': '52.132633', 'lat': '5.291265999999999'},
    21: {'name': 'PITCH FESTIVAL', 'long': '52.39230449999999', 'lat': '4.8558842'},
    22: {'name': 'LAKESIDE FESTIVAL', 'long': '52.1333569', 'lat': '4.672636199999999'},
    23: {'name': 'BKJN VS PARTYRAISER FESTIVAL', 'long': '52.05471660000001', 'lat': '4.5090727'},
    24: {'name': 'NOMADS FESTIVAL', 'long': '52.3517216', 'lat': '4.8371533'},
    25: {'name': 'STEREO SUNDAY', 'long': '51.3723862', 'lat': '6.1721338'},
    26: {'name': 'EXTREMA OUTDOOR - NETHERLANDS', 'long': '51.6550094', 'lat': '5.8293974'},
    27: {'name': 'IN RETRAITE', 'long': '51.7154414', 'lat': '5.994456899999999'},
    28: {'name': 'WE ARE ELECTRIC', 'long': '51.347275', 'lat': '5.3167355'},
    29: {'name': 'OUTLANDS', 'long': '51.5990689', 'lat': '5.995824499999999'},
    30: {'name': 'ESSENTIAL FESTIVAL', 'long': '50.8675626', 'lat': '5.9726234'},
    31: {'name': 'BY THE CREEK', 'long': '51.9815011', 'lat': '5.0697869'},
    32: {'name': 'GEORGIES WUNDERGARTEN', 'long': '52.34319319999999', 'lat': '4.817434'},
    33: {'name': 'HELLBOUND FESTIVAL', 'long': '52.132633', 'lat': '5.291265999999999'},
    34: {'name': 'WASTELAND SUMMERFEST', 'long': '52.39230449999999', 'lat': '4.8558842'},
    35: {'name': 'FESTIFOORT FESTIVAL', 'long': '52.1624', 'lat': '5.365198299999999'},
    36: {'name': 'ELECTRONIC PICNIC', 'long': '52.4989741', 'lat': '4.9881531'},
    37: {'name': 'EXPEDITION FESTIVAL', 'long': '51.9262323', 'lat': '4.5193922'},
    38: {'name': 'VOGELVRIJ FESTIVAL', 'long': '52.132633', 'lat': '5.291265999999999'},
    39: {'name': 'DAYLIGHT FESTIVAL', 'long': '51.5613331', 'lat': '4.545243'},
    40: {'name': 'FULL MOON FESTIVAL TILBURG', 'long': '51.5565973', 'lat': '5.078740799999999'},
    41: {'name': 'WE ARE THE FUTURE', 'long': '52.3087775', 'lat': '4.940659699999999'},
    42: {'name': 'WILDEBURG', 'long': '52.652138', 'lat': '5.906661499999999'},
    43: {'name': '18HRS FESTIVAL', 'long': '52.4419029', 'lat': '4.818048399999999'},
    44: {'name': 'INTIEM OUTDOOR FESTIVAL', 'long': '50.9361951', 'lat': '5.803277'},
    45: {'name': 'SUBMERGED - AMSTERDAM', 'long': '52.39230449999999', 'lat': '4.8558842'},
    46: {'name': 'SUNBEATS BEACH FESTIVAL', 'long': '53.0853945', 'lat': '4.7586682'},
    47: {'name': 'DANCE BOULEVARD', 'long': '51.47135480000001', 'lat': '4.3483687'},
    48: {'name': 'SUMMER OF LOVE', 'long': '52.39230449999999', 'lat': '4.8558842'},
    49: {'name': 'EXPLOSION FESTIVAL', 'long': '52.4938566', 'lat': '6.4734585'},
    50: {'name': 'MILKSHAKE FESTIVAL', 'long': '52.132633', 'lat': '5.291265999999999'},
    51: {'name': 'EDELWISE FESTIVAL', 'long': '52.3670713', 'lat': '4.853111699999999'},
    52: {'name': 'ELECTRONIC FAMILY', 'long': '51.7048327', 'lat': '5.3953314'},
    53: {'name': 'FATALITY THE RAW', 'long': '51.7468601', 'lat': '5.5152837'},
    54: {'name': 'VERKNIPT FESTIVAL', 'long': '52.3517216', 'lat': '4.8371533'},
    55: {'name': 'LA REVE FESTIVAL', 'long': '52.39230449999999', 'lat': '4.8558842'},
    56: {'name': 'KARMA OUTDOOR', 'long': '51.4570505', 'lat': '5.503711699999999'},
    57: {'name': 'GAASPERPLEASURE', 'long': '52.3065615', 'lat': '4.9933607'},
    58: {'name': 'DANCETOUR - GOES', 'long': '51.5057781', 'lat': '3.892463599999999'},
    59: {'name': 'GUILTY PLEASURE FESTIVAL', 'long': '52.3065615', 'lat': '4.9933607'}
    }

# Returns tuples of all festivals with their corresponding long and latitude
def open_file(input_file):
    suppliers = []
    if ((type(input_file) == str) and input_file.endswith(".csv")):
        print("hee")
        with open(input_file, 'rt') as file:
            file = csv.reader(file, delimiter='\n', quotechar='|')
            for row in file:
                row = row[0].split(",")[-3:]
                suppliers.append((row[0], row[1], row[2]))
            print("imhere")
            return suppliers
    else:
        print("here")
        print(type(input_file))
        for row in range(len(input_file)):
            print(row)
            row = input_file[row]
            suppliers.append((row['name'], row['long'], row['lat']))
        return suppliers

# example calls
# venues_csv = open_file("MusicEventsInfo.csv")
# venues_dict = open_file(venues)
