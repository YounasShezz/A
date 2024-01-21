import flet as ft
import android

from flet_django.pages import GenericApp
main = GenericApp(controls=[ft.Text(str(dir(android)))])