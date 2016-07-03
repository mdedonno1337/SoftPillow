#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image

class MyImage( Image.Image ):
    pass
    
Image.Image = MyImage
