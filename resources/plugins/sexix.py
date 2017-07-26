'''
    urlresolver XBMC Addon
    Copyright (C) 2016 Gujal

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
import re
from urlresolver import common
from urlresolver.plugins.lib import helpers
from urlresolver.resolver import UrlResolver, ResolverError

class SexixResolver(UrlResolver):
    name = 'sexix'
    domains = ['sexix.net']
    pattern = '(?://|\.)(sexix\.net)/video([-\w]+)'

    def __init__(self):
        self.net = common.Net()

    def get_media_url(self, host, media_id):
        web_url = self.get_url(host, media_id)
        headers = {'User-Agent': common.RAND_UA}
        html = self.net.http_GET(web_url, headers=headers).content
            
        if html:
            try:
                headers.update({'Referer': web_url})
                iframe_url = re.search("""<iframe.+?src=["'](http://sexix\.net/v\.php\?u=.+?)['"]""", html).groups()[0]
                iframe_content = self.net.http_GET(iframe_url, headers=headers).content
                headers.update({'Referer': iframe_url})
                playlist_url = re.search("""playlist:\s*['"]([^'"]+)""", iframe_content).groups()[0]
                if playlist_url:
                    playlist_content = self.net.http_GET(playlist_url, headers=headers).content
                    sources = re.findall(r'''source\s*file=['"](?P<url>[^'"]+)['"]\s*type=['"]\w+['"]\s*label=['"](?P<label>(\w+))['"]''',playlist_content)
                    sources = [(i[1], i[0]) for i in sources if i]
                    return helpers.pick_source(sources)
                    
            except:
                raise ResolverError('File not found')
                
        raise ResolverError('File not found')

    def get_url(self, host, media_id):
        return self._default_get_url(host, media_id, template='http://{host}/video{media_id}/')

    @classmethod
    def _is_enabled(cls):
        return True
