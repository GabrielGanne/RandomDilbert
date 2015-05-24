#!/usr/bin/env python
import pygtk
pygtk.require("2.0")
import gtk

import random
import urllib
import re


DILBERT_URL_PATTERN = "http://www.dilbert.com/strip/%s-%s-%s/"
DILBERT_IMG_URL = "http://assets.amuniversal.com/"

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
        self.window.set_title("RandomDilbert Client by GKBRK")
        
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
        year = random.choice(range(2009, 2015))
        month = random.choice(range(1, 13))
        day = random.choice(range(1, 29))
        url_to_dilbert_page = DILBERT_URL_PATTERN % (year, month, day)
        page_contents = urllib.urlopen(url_to_dilbert_page).read()
        image_hash = re.search('<meta property="og:image" content="http://assets.amuniversal.com/([0-9a-fA-F]*)"/>', page_contents).group(1)
        image_url = DILBERT_IMG_URL + image_hash

        return image_url

    def show_random_image(self, widget=None, data=None):
        self.image.set_from_pixbuf(pixbuf_from_url(self.get_random_image()))

if __name__ == "__main__":
    RandomDilbert().show()

