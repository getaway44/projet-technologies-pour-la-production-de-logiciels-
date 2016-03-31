from libs.bottle import route, template, run
from ActivityService import allActivities

@route('/InstallationsSportivesPDL')
def index():
    #return('Voici les installations sportives des Pays de la Loire :')
    liste_activite = ActivityService.allActivities()
    form = """ <div id='header'> Veuillez choisir une activité et une commune </div> """
    form += """<p>Activite</p> <br>"""
    form += """<select id='activite' name=activite>"""
    for com in liste_activite:
        if com[1] != "":
            form += """<option value='""" + str(com[0]) + """'>""" + com[1] + """ </option> """
    form += """</select>"""      
    return {"body" : form}

run(host='localhost', port=8080)