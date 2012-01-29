import os, sys
import django.core.handlers.wsgi
PROJECT_DIRNAME='projects'
#PROJECT_NAME=os.listdir('/'.join([os.curdir,PROJECT_DIRNAME]))[0]
PROJECT_NAME=os.listdir('/'.join([os.path.abspath(os.path.dirname(__file__)),PROJECT_DIRNAME]))[0]
#print os.listdir(os.curdir) ##es $HOME!!!!!!
PROJECT_DIR='/'.join([os.path.abspath(os.path.dirname(__file__)),PROJECT_DIRNAME,PROJECT_NAME])
#print PROJECT_DIR
#print PROJECT_NAME ##    HOSTIAAAAAs!!!
#print PROJECT_DIRNAME
#sys.path.append('/media/sda6/DOC/UTN/PAGINA/Pagina/projects/proyecto/')
if PROJECT_DIR not in sys.path:
	sys.path.append(PROJECT_DIR)
#print sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()
