'''
python -m uvicorn main:app --reload
'''

import pandas as pd
import numpy as np
from fastapi import FastAPI




data = pd.read_csv('movies_dataset_clean1_1.csv')
rs_data = pd.read_csv('movie_simil_genres.csv')

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}



'''
def peliculas_idioma( Idioma: str ): Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). 
Debe devolver la cantidad de películas producidas en ese idioma. 
Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma
'''

@app.get('/peliculas_idioma/{idioma}')
async def peliculas_idioma(idioma: str):
    a = len(data[data['original_language'] == idioma])
    return {'idioma': idioma, 'cantidad': a}


'''
def peliculas_duracion( Pelicula: str ): Se ingresa una pelicula. Debe devolver la duracion y el año.
Ejemplo de retorno: X . Duración: x. Año: xx
'''
@app.get('/peliculas_duracion/{pelicula}')
async def peliculas_duracion(pelicula):
    d = data[['runtime', 'release_year']][data['title'] == pelicula]
    duracion = int(d['runtime'][1])
    anio = int(d['release_year'][1])
    return {'pelicula':pelicula, 'duracion':f'{duracion}min', 'anio':anio}


'''
def franquicia( Franquicia: str ): Se ingresa la franquicia, retornando la cantidad de peliculas, 
ganancia total y promedio Ejemplo de retorno: La franquicia X posee X peliculas, una ganancia 
total de x y una ganancia promedio de xx
'''
@app.get('/franquicia/{franquicia}')
async def franquicia(franquicia: str):
    collection = data[data['belongs_to_collection'] == franquicia]
    numero = len(collection) 
    ganacia = collection['revenue'].sum()
    promedio = collection['revenue'].mean()
    return {'franquicia':franquicia, 'cantidad':numero, 'ganancia_total':ganacia, 'ganancia_promedio':promedio}

'''
def peliculas_pais( Pais: str ): Se ingresa un país (como están escritos en el dataset, 
no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.
Ejemplo de retorno: Se produjeron X películas en el país X
'''

@app.get('/peliculas_pais/{pais}')
async def peliculas_pais(pais: str):
    collection = data[data['country'] == pais]
    num = len(collection)
    return {'pais':pais, 'cantidad':num}

'''
def productoras_exitosas( Productora: str ): Se ingresa la productora, 
entregandote el revunue total y la cantidad de peliculas que realizo.
Ejemplo de retorno: La productora X ha tenido un revenue de x 
'''

@app.get('/productoras_exitosas/{Productora}')
async def productoras_exitosas(Productora: str):
    collection = data[data['pro_comp1'] == Productora]
    num = len(collection)
    revenue = collection['revenue'].sum()
    return {'productora':Productora, 'revenue_total': revenue,'cantidad':num}

'''
def get_director( nombre_director ): Se ingresa el nombre de un director 
que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido 
a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de 
lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista. 
'''

@app.get('/get_director/{nombre_director}')
async def get_director(nombre_director: str):
    collection = data[data['director'] == nombre_director]
    exito = collection['return'].sum()
    v = {}
    v['director'] = nombre_director
    v['retorno_director'] = exito
    movies = []
    for i in range(int(len(collection))):
        w = {}
        w['titulo'] = collection['title'].iloc[i]
        w['return'] = str(collection['return'].iloc[i])
        w['revenue'] = collection['revenue'].iloc[i]
        w['anio'] = str(collection['release_year'].iloc[i])  
        movies.append(w)
    
    v['peliculas'] = movies    
    return v



'''
# ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    Ingresas un nombre de pelicula y te recomienda las similares en una lista
    return {'lista recomendada': respuesta}
'''
#rs_data = np.array(rs_data.tol).tolist()
#@app.get('/recomendacion/{titulo}')
#async def recomendacion(titulo:str, cosine_sim=rs_data):
#    idx = data.index[data['title'] == titulo].tolist()[0]
#    sim_scores = enumerate(cosine_sim[idx])
#    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#    sim_scores = sim_scores[1:6]
#    movie_indices = [i[0] for i in sim_scores] 
#    return {'lista recomendada' : list(data['title'].iloc[movie_indices])}