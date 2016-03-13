CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/ask/',
    'args': (
         'ask.wsgi',
         '--bind=0.0.0.0:8000',
         '--workers=3', 
     ),     
 
}
