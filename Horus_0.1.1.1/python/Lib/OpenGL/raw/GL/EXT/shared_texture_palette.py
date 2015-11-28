'''OpenGL extension EXT.shared_texture_palette

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_shared_texture_palette'
_DEPRECATED = False
GL_SHARED_TEXTURE_PALETTE_EXT = constant.Constant( 'GL_SHARED_TEXTURE_PALETTE_EXT', 0x81FB )


def glInitSharedTexturePaletteEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )