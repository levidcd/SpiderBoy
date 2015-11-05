import sae  
from spiderboy import wsgi  
application = sae.create_wsgi_app(wsgi.application)  