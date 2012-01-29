rom buscador import Buscador
class BuscadorTwitter(Buscador):

    def __init__(self):
        return Buscador.__init__(self)


    def obtener_quantum(self):
        return Buscador.obtener_quantum(self)


    def crear_searcher(self):
        from twitter import Api
        api = Api()

         esto anda:
         lista_usuarios = [api.GetStatus(s.id)._user for s in api.GetSearch('palabra')]
         lista_con_followers_y_demas = [s for s in lista_usuarios]
         lista_status = [api.GetStatus(s.id) for s in api.GetSearch('palabra')]

        return api.FilterPublicTimeline('aca va la palabradios')#esto es lo publico!!! no usar WebSearch
    def buscar(self, *args, **kwars):
        return Buscador.buscar(self, *args, **kwars)

    pass
