# Movies_recommendation 🎦
![](https://s3-us-west-2.amazonaws.com/prd-rteditorial/wp-content/uploads/2018/03/13153742/RT_300EssentialMovies_700X250.jpg)
## Sistema de recomendacion basado en contenido
Proyecto Individual MLops: 🧮 Daniel Vielma DTPT02
https://www.linkedin.com/in/daniel-vielma-10bb42269/

El desarrollo de este proyecto tiene como finalidad la construccion de un modelo de recomendacion basado en 
contenido, disponiendo de los datasets `movies_dataset.csv` y `credits.csv`, Ademas de esto, se incorpora la 
elaboracion de una *API*, la cual tiene definida distintas funciones, en total siete, con las cuales podemos 
consultar informacion relevante sobre las peliculas.

A parte de esto mencionado anteriormente, para la realizacion de este proyecto tambien fue necesario realizar un proceso
*ETL*, a los datos iniciales para poder tenerlos mas limpios y poder trabajar de forma mas optima.

### Acerca del proceso `ETL`

En el archivo `ETL_1.1.ipynb` esta toda la elaboracion del proceso `ETL`, donde se comienza en un principio con `movies_dataset.csv`,
y aqui es necesario para nuestro proyecto poder contar con datos limpios, en este caso entre los pasos mas importantes a tomar
es el desanidado de ciertas columnas y posteriormente se hace un tratado con los campos nulos de ciertas columnas y se eliminan 
algunas variables que no son necesarias para el desarrollo del proyecto

### *API* 

La elaboracion de la *API* se hizo en base al framework de fastapi, donde se crearon 7 funciones con las cuales podemos
consultar informacion util de las peliculas. Dichas funciones son las siguientes:

* def peliculas_idioma( Idioma: str ): Se ingresa un idioma (como están escritos en el dataset). Devuelve la cantidad de películas producidas en ese idioma.
* def peliculas_duracion( Pelicula: str ): Se ingresa una pelicula. Devuelve la duracion y el año.
* def franquicia( Franquicia: str ): Se ingresa la franquicia, retornando la cantidad de peliculas, 
ganancia total y promedio Ejemplo de retorno
* def peliculas_pais( Pais: str ): Se ingresa un país (como están escritos en el dataset), retornando la cantidad de peliculas producidas en el mismo.
* def productoras_exitosas( Productora: str ): Se ingresa la productora, 
entregandote el revunue total y la cantidad de peliculas que realizo.
*def get_director( nombre_director ): Se ingresa el nombre de un director 
que se encuentre dentro de un dataset devuelve el éxito del mismo medido 
a través del retorno. Además, retorna el nombre de cada película con la fecha de 
lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista

Todas estas definiciones estan en el archivo main.py de este repositorio.

### Sistema de recomendacion de peliculas.

En la carpeta `ETL_EDA_RS` en el archivo `model.ipynb` donde se hace toda la construccion de el sistema de recomendacion basado
en el contenido del dataset resultante del proceso de *ETL*. El sistema se basa en hacer un analisis de las columnas `overview`
y `genre`, en estas variables podemos encontrar informacion relevante acerca del contenido de la pelicula

El trabajo a realizar fue hacer calculo del TD-IDF de ambas columnas, para poder obtener los `tdidf_vectors`
con la informacion de las palabras mas relevantes, i.e, las que ofrecen una mejor descripcion de la pelicula.
Posteriormente ya calculados estos arrays de vectores se procede a calcular la matriz de similitud que relaciona
todas las peliculas, a partir de esta matriz se puede obtener la recomendacion de una pelicula buscando su indice
correspondiente y ordenando dicha fila de la matriz de similitud. ademas se incorporo en la *API* la funcion de recomendacion
donde se le da de entrada una pelicula y esta retorna las 5 peliculas recomendadas para dicha pelicula de entrada. Recomendacion
la hace gracias a la matriz de similitud `movie_simil_genres.csv`, que se encuentra en este repositorio. Esta matriz se puede
calcular (si los recursos lo permiten) para mas registros de peliculas y asi obtener una mejor recomendacion

### Herramientas utilizadas para la elaboracion del proyecto

* Python
* Pandas
* Numpy
* Fastapi
* render para el deploy
* scikit_learn, especificamente los modulos TdidfVectorizer y cosine_similarity

  ### Enlaces
  link deploy de la *API*: https://movies-rs.onrender.com/docs
  
