CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/ask/',
    'args': (
         'wsgi',
         '--bind=0.0.0.0:8000',
         '--workers=3',
         '--access-logfile acc.log',
         '--error-logfile err.log', 
     ),     
 
}
