from django.contrib import admin
import shopping.models  as sh
a = admin
# Register your models here.
a.site.register(sh.VitVit)
a.site.register(sh.On_Off)
a.site.register(sh.Type_job)
a.site.register(sh.Chop_prodect)
a.site.register(sh.Type_catigory)
a.site.register(sh.Type_prodect)
a.site.register(sh.Catigory)
a.site.register(sh.Prodect)
a.site.register(sh.Profile)