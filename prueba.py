import requests
import datetime
api_url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
response=requests.get(api_url)
data=response.json()
#variable de las respuestas contestadas
is_answered=0
#variable de las respuestas no contestadas
not_answered=0
#variable de la respuesta con menor numero de vistas
view_low=100000000000
#variable de la reputacion
reputation=0

#Ciclo para obtener fechas de referencia convirtiendolas de timestamp a time
for i in data['items']:
    fecha=i['creation_date']
    date1=datetime.datetime.fromtimestamp(fecha/ 1e3)
    date2=datetime.datetime.fromtimestamp(fecha/ 1e3)
    question_old=i['question_id']
    question_new=i['question_id']



for i in data['items']:
    #pp(i)
    #obtencion de fecha y conversion a datatime 
    fecha=i['creation_date']
    date=datetime.datetime.fromtimestamp(fecha/ 1e3)
    #Condicional para sacar la fecha mas nueva
    if date2<date:
        date2=date
        question_new=i['question_id']
    #Condicional para sacar la fecha mas antigua
    if date1>date:
        date1=date
        question_old=i['question_id']
    #Condicional que valida las preguntas contestadas y no contestadas
    if i['is_answered']==False:
        not_answered+=1
    else:
        is_answered+=1
    #Condicional para identificar la pregunta con menor numero de vistas
    if view_low>int(i['view_count']):
        answer_view_low=i['question_id']
        view_low=int(i['view_count'])
    #Condicional para sacar la mayor reputacion
    if int(i['owner']['reputation'])>reputation:
        reputation=int(i['owner']['reputation'])
        owner=i['owner']['display_name']
#Impresion de datos en consola
print(f"Preguntas contestadas: {is_answered}")
print(f"preguntas sin contestar {not_answered}")
print(f"La pregunta con menos vistas es la pregunta con el id {answer_view_low} con {view_low} vistas")
print(f"La pregunta mas antigua es la de el id {question_old} creada en {date1}")
print(f"La pregunta mas nueva es la de el id {question_new} creada en {date2}")
print(f"El usuario con mayor reputacion es {owner} con una reputacion de {reputation}")
