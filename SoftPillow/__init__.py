#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image
from PIL.Image import NEAREST

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
        
    def chroma( self, color, tolerance = 0 ):
        """
            Change the color passed in argument to transparent.
        """
        datas = self.getdata()
        newData = []
        
        dstcolor = ( 0, 0, 0, 0 )
        
        if tolerance == 0:
            for r, g, b, a in datas:
                if ( r, g, b ) == color:
                    newData.append( dstcolor )
                else:
                    newData.append( ( r, g, b, a ) )
        
        else:
            tolerance *= tolerance
            keyr, keyg, keyb = color
            for r, g, b, a in datas:
                if pow( ( keyr - r ), 2 ) + pow( ( keyg - g ), 2 ) + pow( ( keyb - b ), 2 ) <= tolerance:
                    newData.append( dstcolor )
                else:
                    newData.append( ( r, g, b, a ) )
         
        ret = self.copy()
        ret.putdata( newData )
        return ret
    
    def transparency( self, alpha ):
        """
            Change the trasparency of the image (the new trasparency is alpha *
            the old trasparency).
        """
        datas = self.getdata()
        newData = []
        
        for r, g, b, a in datas:
            newData.append( ( r, g, b, int( a * alpha ) ) )
        
        ret = self.copy()
        ret.putdata( newData )
        return ret
    
