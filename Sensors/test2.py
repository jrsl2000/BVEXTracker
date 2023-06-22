from gps import ubx, gps_io
#gpsio = gps_io(input_speed=38400, input_file_name="gps.raw")
ubxt = ubx.ubx()

with open("gps.raw", "rb") as file:
    contents = file.read()

res = -1
while res < len(contents)+1:
    res = ubxt.decode_msg(contents)
    print(res, len(contents))
    #print(contents[:res])
    contents = contents[res:]
