from flask import Flask, render_template, request
import requests
import urllib.parse

#ACA no tengo folium
import folium

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')
    
@app.route('/', methods=['POST'])
def my_form_post():
    mapa = ""
    adress_lat = 0
    adress = request.form['adress']
    processed_adress = adress.lower()
    #imprime en la consola
    print(processed_adress)
    url = 'http://nominatim.openstreetmap.org/search/' + urllib.parse.quote(processed_adress) +'?format=json'
    
    #ACA no se que pasa con el request - en Mac con datascience va bien!!
    response = requests.get(url, verify=False).json()
    adress_lat = (response[0]["lat"])
    adress_lon = (response[0]["lon"])
    
    
    mapa = folium.Map(location=[float(response[0]["lat"]),float(response[0]["lon"])], zoom_start=13)
    folium.Marker(
                location=[float(response[0]["lat"]),float(response[0]["lon"])], 
                popup="Ubicación seleccionada",
                icon=folium.Icon(color="red")
                 ).add_to(mapa)
    mapa.save('ms_map/templates/mapa.html')
    print(type(mapa))
    return render_template('mapa.html')
if __name__ == '__main__':
    app.run(debug=True)
