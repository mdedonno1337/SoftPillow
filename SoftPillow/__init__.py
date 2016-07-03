#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image
from Image import NEAREST

class MyImage( Image.Image ):
    def scale( self, factor, resample = NEAREST ):
        """
            Returns a rescaled image by a specific factor given in parameter. A
            factor greater than 1 expands the image, between 0 and 1 contracts
            the image.
        """
        self.load()
        
        if factor == 1:
            return self._new( self.im )
        
        elif factor <= 0:
            raise ValueError( "the factor must be greater than 0" )
        
        else:
            size = ( int( round( factor * self.width ) ), int( round( factor * self.height ) ) )
            return self.resize( size, resample )
    
Image.Image = MyImage
