def connect():
    import network, ntptime
    import wlanscan
    from time import sleep_ms

    netscan = wlanscan.WLANscan()
    ssidlist = netscan.ssid()


    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print('Searching for Network...')
        sta_if.active(True)

        for net in ssidlist:
            #print(net)
            if net == 'WLAN1':
                sta_if.connect('WLAN1', 'WLAN1PW')
                while not sta_if.isconnected():
                    print('connecting ...')
                    sleep_ms(500)
                break

            if str(net) == 'WLAN2':
                sta_if.connect('WLAN2', 'WLAN2PW')
                while not sta_if.isconnected():
                    print('connecting ...')
                    sleep_ms(500)
                break

            if str(net) == 'WLAN3':
                sta_if.connect('WLAN3', 'WLAN3PW')
                while not sta_if.isconnected():
                    print('connecting ...')
                    sleep_ms(500)
                break

    if not sta_if.isconnected():
        print('Kein bekanntes Netzwerk gefunden')
    else:
        print('Network connected:', sta_if.ifconfig())
	sleep_ms(500)
        ntptime.settime()
        sleep_ms(500)

def no_debug():
    import esp
    esp.osdebug(None)

def disconnect():
	import network
	sta_if = network.WLAN(network.STA_IF)
	sta_if.disconnect()

no_debug()
connect()
