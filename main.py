import json,requests,os
biru = "\033[96m"
putih = "\033[97m"
merah = "\033[91m"
hijau = "\033[92m"
os.system("clear")
print("""\033[97m
    _ _..._ __
    \)`    (` /
     /      `\

    |  0  0   | TrackingTools @Drian-o
    =\  Y    =/--..-="````"-.
      '.=__.-'               `\

         o/                 /\ \

          |                 | \ \   / )
           \    .--""`\    <   \ '-' /
          //   |      ||    \   '---'
         ((,,_/      ((,,___/

      %s••{%sCoded By %s@muh4k3mos%s}••
      %s••{%sThanks To : %s407 Authentic Exploit%s}••
      %s••{%sTelegram : %shttps://t.me/muhakemos%s}••


"""%(putih,hijau,biru,putih,putih,hijau,biru,putih,putih,hijau,biru,putih))
ucok = input("[?] Enter Your IP Address : ")
url = "http://www.geoplugin.net/json.gp?ip="+ucok
sabyan = json.loads(requests.get(url).text)
print("-"*40)
print("[!] Ip Publik : "+str(sabyan["geoplugin_request"]))
print("[!] Status : "+str(sabyan["geoplugin_status"]))
print("[!] Delay : "+str(sabyan["geoplugin_delay"]))
print("[!] Kota : "+str(sabyan["geoplugin_city"]))
print("[!] Nama Wilayah "+str(sabyan["geoplugin_region"]))
print("[!] Kode Wilayah : "+str(sabyan["geoplugin_regionCode"]))
print("[!] Kode Area : "+str(sabyan["geoplugin_areaCode"]))
print("[!] Kode Dma : "+str(sabyan["geoplugin_dmaCode"]))
print("[!] Kode Kota : "+str(sabyan["geoplugin_countryCode"]))
print("[!] Nama Kota : "+str(sabyan["geoplugin_countryName"]))
print("[!] Benua : "+str(sabyan["geoplugin_continentName"]))
print("[!] Kode Benua : "+str(sabyan["geoplugin_continentCode"]))
print("[!] Garis Lintang : "+str(sabyan["geoplugin_latitude"]))
print("[!] Garis Bujur :"+ str(sabyan["geoplugin_longitude"]))
print("[!] Radius Akurasi Lokasi : "+str(sabyan["geoplugin_locationAccuracyRadius"]))
print("[!] Zona Waktu :"+str(sabyan["geoplugin_timezone"]))
print("[!] Mata Uang : "+str(sabyan["geoplugin_currencyCode"]))
print("[!] Tipe Mata Uang : "+ str(sabyan["geoplugin_currencySymbol"]))
print("[!] Konverter Mata Uang : "+str(sabyan["geoplugin_currencyConverter"]))

