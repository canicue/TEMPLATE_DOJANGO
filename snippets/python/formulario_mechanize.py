from mechanize import Browser

def consultar(query, motor='google', sitio='wikipedia.com', nro_resultados=10, nro_iteraciones=1):
	b = Browser()

	for i in range(0, nro_iteraciones):
		#b.open('http://127.0.0.1:8000/limpieza/')
		#b.open('http://localhost/actual/limpieza/')
		b.open('http://localhost:8000/limpieza/')
		b.select_form(nr=0)
		b['motor'] = (motor,)
		b['nro_resultados'] = str(nro_resultados)
		b['query'] = query
		b['sitio'] = (sitio,)
		rta = b.submit()
		#print rta.read()

if __name__ == '__main__':
	consultar('caballos', nro_iteraciones=5, sitio='twitter.com')


