from gps import gps, WATCH_ENABLE 

gps = gps(mode=WATCH_ENABLE)
'''
lock = False 
while not lock: 
    report = gps.next() 
    # 3D Fix 
    if report['class'] == 'TPV' and report['mode'] == 3: 
     print(report.lon) 
     print(report.lat) 
     print(report.alt) 
     print(report.speed) 
     print(report.track) 
     print(report.climb) 
    else: 
     time.sleep(5)
'''
