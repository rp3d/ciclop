'''OpenGL extension APPLE.transform_hint

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_APPLE_transform_hint'
_DEPRECATED = False
GL_TRANSFORM_HINT_APPLE = constant.Constant( 'GL_TRANSFORM_HINT_APPLE', 0x85B1 )


def glInitTransformHintAPPLE():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )