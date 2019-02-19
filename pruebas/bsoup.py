from bs4 import BeautifulSoup
import requests

"""
espol = requests.get('http://www.espol.edu.ec')
print(espol.status_code)
print(espol.content[:200])#slicing: desde que inicia hasta el caracter 200
if "<table>" in espol.content:
    print("tiene tablas")
print(espol.headers)
print(espol.cookies.items())


Extract ALL of the locations from Icee's website via this page
http://www.icee.com/locationsICEE.asp
"""

states = ['AK']
for state in states:
    stateSelection = "http://www.icee.com/locationsICEE.asp?state=%s" % state
    r = requests.get(stateSelection)
    soup = BeautifulSoup(r.text, "html.parser")
    rows = soup.find_all("option")
    cities = [row.attrs['value'] for row in rows]#list comprehensions -> Cities=[] for row in rows: cities.append(row.attrs[value])
    print(end='\n')
    print("Cities with locations on the state of %s : " % state)
    print(cities)
    i=1
    print("html del resultado de la busqueda en todas las ciudades")
    for city in cities:
        data = {'city': city, 'state': state, 'submit': 'submit'}
        url = "http://www.icee.com/locationsresults.asp"
        req = requests.get(url, data=data)
        print(i)
        soup2 = BeautifulSoup(req.text, "html.parser")
        print(soup2)
        i += 1
        print(end='\n')
        print("tds")
        for page in soup2:
            celdas = soup2.find_all("td",{"class":"order_table2"})
            print("-----------------")
            print(celdas)
            print(end='\n')
            print("Direccion")
            interes = [celda.getText()for celda in celdas]
            print(interes[6])
