import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def obtenercontacto(url):
    '''A partir de la página de una PyME, se obtienen correo, facebook,
    instagram, tiktok, twitter y youtube'''
    links = {'correo':None, 'facebook':None, 'instagram':None,
             'tiktok':None, 'twitter':None, 'youtube':None}
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        ref = [tag.get('href', None) for tag in tags]
        for i in ref:
            if '@' in i:
                links['correo'] = i
            if 'facebook' in i:
                links['facebook'] = i
            if 'instagram' in i:
                links['instagram'] = i
            if 'tiktok' in i:
                links['tiktok'] = i
            if 'twitter' in i:
                links['twitter'] = i
            if 'youtube' in i:
                links['youtube'] = i
        return [direc for direc in links.values()]
    except:
        return links