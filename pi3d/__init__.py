from __future__ import absolute_import, division, print_function, unicode_literals
"""
Allows the use of:

  import pi3d

to drag in most of the important classes of pi3d.
"""

from pi3d.constants import *
from pi3d.constants import __version__

from pi3d import Display

from pi3d.Buffer import Buffer
from pi3d.Camera import Camera
from pi3d.Keyboard import Keyboard
from pi3d.Mouse import Mouse
from pi3d.Shader import Shader
from pi3d.Shape import Shape
from pi3d.Texture import Texture
from pi3d.Texture import TextureCache

from pi3d.Light import Light


if PLATFORM != PLATFORM_WINDOWS:
  from pi3d.event.Event import InputEvents

from pi3d.shape.Canvas import Canvas
from pi3d.shape.Cone import Cone
from pi3d.shape.Cuboid import Cuboid
from pi3d.shape.Cylinder import Cylinder
from pi3d.shape.Disk import Disk
from pi3d.shape.ElevationMap import ElevationMap
from pi3d.shape.Extrude import Extrude
from pi3d.shape.Helix import Helix
from pi3d.shape.Lathe import Lathe
from pi3d.shape.Lines import Lines
from pi3d.shape.LodSprite import LodSprite
from pi3d.shape.MergeShape import MergeShape
from pi3d.shape.Model import Model
from pi3d.shape.MultiSprite import MultiSprite
from pi3d.shape.Plane import Plane
from pi3d.shape.Points import Points
from pi3d.shape.Sphere import Sphere
from pi3d.shape.Sprite import Sprite, ImageSprite
from pi3d.shape.TCone import TCone
from pi3d.shape.Tetrahedron import Tetrahedron
from pi3d.shape.Torus import Torus
from pi3d.shape.Triangle import Triangle
from pi3d.shape.Tube import Tube

from pi3d.util import Log
from pi3d.util import Utility

from pi3d.sprite.Ball import Ball
from pi3d.util.Clashtest import Clashtest
from pi3d.util.Defocus import Defocus
from pi3d.shape.EnvironmentCube import EnvironmentCube, loadECfiles
from pi3d.util.Gui import Button
from pi3d.util.Gui import Gui
from pi3d.util.Gui import Radio
from pi3d.util.Gui import Scrollbar
from pi3d.util.Gui import MenuItem
from pi3d.util.Gui import Menu
from pi3d.util.Gui import TextBox
from pi3d.util.Pngfont import Pngfont
from pi3d.util.PointText import PointText
from pi3d.util.PostProcess import PostProcess
from pi3d.util.Screenshot import screenshot
from pi3d.util.ShadowCaster import ShadowCaster
from pi3d.util.StereoCam import StereoCam
from pi3d.util.String import String
from pi3d.util.TextBlock import TextBlock
from pi3d.util.TextBlock import TextBlockColour
from pi3d.util.TextBlock import TextBlockColourGradient

################################### only import these if PIL available
if PIL_OK:
  from pi3d.util.FixedString import FixedString
  from pi3d.util.Font import Font
  from pi3d.shape.Building import Building
  from pi3d.shape.Building import corridor
  from pi3d.shape.Building import Size
  from pi3d.shape.Building import Position
  from pi3d.shape.Building import SolidObject

