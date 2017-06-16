# coding=utf8
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

ventana= Gtk.Window()
ventana.set_title("Hola mundo ")
ventana.connect("delete-event", Gtk.main_quit)
ventana.show()

caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
caja.show()
ventana.add(caja)


def boton_click(widget):
    print "esta bien"

etiqueta = Gtk.Label("hello my friends!!")
etiqueta.show()
caja.pack_start(etiqueta, True, True, 0)
#ventana.add(etiqueta)

boton = Gtk.Button("salir")
boton.connect("clicked", Gtk.main_quit)
#boton.connect("clicked", boton_click)
boton.show()
caja.pack_start(boton, True, True, 0)
#ventana.add(boton)

Gtk.main()
