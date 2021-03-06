#!/usr/bin/env python
import pygtk
pygtk.require("2.0")
import gtk

import random
import urllib

from settings import URL_FILE, DILBERT_IMG_URL


def pixbuf_from_url(url):
    image_data = urllib.urlopen(url)
    loader = gtk.gdk.PixbufLoader()
    loader.write(image_data.read())
    loader.close()
    return loader.get_pixbuf()


class RandomDilbert:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_default_size(670, 430)
        self.window.set_title("Random Dilbert")
        
        self.image = gtk.Image()
        self.show_random_image()
        
        self.random_button = gtk.Button("Random Image")
        self.random_button.connect("clicked", self.show_random_image)
        
        self.vbox = gtk.VBox()
        self.vbox.pack_start(self.image)
        self.vbox.pack_start(self.random_button)
        
        self.window.add(self.vbox)
        
        self.window.connect("destroy", self.destroy_window)
    
    def show(self):
        self.window.show_all()
        gtk.main()
    
    def destroy_window(self, widget=None, data=None):
        gtk.main_quit()

    def get_random_image(self):
        lines = open(URL_FILE).read().splitlines()
        image_hash =random.choice(lines)
        image_url = DILBERT_IMG_URL + image_hash
        return image_url

    def show_random_image(self, widget=None, data=None):
        self.image.set_from_pixbuf(pixbuf_from_url(self.get_random_image()))

if __name__ == "__main__":
    RandomDilbert().show()

