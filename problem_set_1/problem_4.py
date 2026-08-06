#problem 4
def coordinateIntegrityCheck(records):
    #invalid records
    print("INVALID: ", end=" ")
    validRecords = []
    for codeName, lat, lon in records:
        if lat < -90 or lat > 90 or lon < -180 or lon > 180:
            print(codeName, "(", lat, lon, ")")
        else:
            validRecords.append((codeName, lat, lon))

    print("Briefing (N -> )")
    sortedValid = sorted(validRecords, key=lambda x : x[1], reverse=True)
    for codeName, lat, lon in sortedValid:
        print(codeName.upper(), " → Lat: ", lat, "Lon: ", lon)

record1 = [("Falcon", 34.05, -118.24), ("Ghost",
99.9, 12.0), ("Condor", 40.71, -74.00)]

coordinateIntegrityCheck(record1)

#A tuple is right for a locked record, since it's immutable.