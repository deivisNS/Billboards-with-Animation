from flask import Flask, render_template


#creamos la instancia de flask
app = Flask(__name__)


#creamos un decorador con la ruta que se visitara en la url y se la indexsmos a la funcion
@app.route("/")
def index():
		
	#diccionario con las rutas de la imagenes a cargar
	context = {
		"pictures" : ["img/1.webp", "img/2.webp", "img/3.webp"]
	}

	#indicamos cual html debe ser renderizado y le pasamos tambien el diccionario desempaquetado usando ** 
	return render_template("cartelera.html", **context)


#para correr la app en el servidor local
app.run(
	host = "0.0.0.0",	#para que acepte cualquier direccion ip
	port = 5004,		#puerto que se usa en el local
	debug = True 		#para que muestre los errores de del codigo, si es que los hay
	)