from jinja2 import Template
class HtmlH:
    page= Template(
        "<!DOCTYPE html>\n"
        "<html>\n"
        "<head>\n"
        "{% if this.title %}<title>{{this.title}}</title>{% endif %}"
        "    {{this.header.render(**kwargs)}}\n"
        "<script src=https://unpkg.com/htmx.org@1.9.4/dist/htmx.min.js></script>"
        "</head>\n"
        "<body>\n"
        "    {{this.html.render(**kwargs)}}\n"
        "</body>\n"
        "<script>\n"
        "    {{this.script.render(**kwargs)}}\n"
        "$(function() {\n"
        "   var xx = document.getElementById('afr_ava');\n"
        "   var xxx = xx.childNodes[1].childNodes[0].childNodes[1];\n"
        "   xxx.addEventListener('click', function(){alert('ok')})\n"
        "   var dt = window.parent.document.getElementById('FormData');\n"
        "   dt.setAttribute('hx-vals', `js:{'lat': '${getlocatttion_gps._event.latlng.lat}','lng': '${getlocatttion_gps._event.latlng.lng}'}`)\n"
        "});\n"
        "</script>\n"
        "</html>\n"
    )
    def __init__(self,page=page):
        self.page=page
    def add_jjs(self,variable):
        jjs = ""
        
        if variable==str("jjs"):
            return jjs