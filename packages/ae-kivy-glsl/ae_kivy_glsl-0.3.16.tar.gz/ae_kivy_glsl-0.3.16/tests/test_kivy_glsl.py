""" unit tests """
from conftest import skip_gitlab_ci

from kivy.uix.boxlayout import BoxLayout

from ae.kivy_glsl import ShadersMixin


def test_declaration():
    assert ShadersMixin


class ShaderBoxLayout(ShadersMixin, BoxLayout):
    """ test class """


@skip_gitlab_ci
class TestShadersMixin:
    def test_add_shader(self):
        sbl = ShaderBoxLayout()
        sid = sbl.add_shader()
        assert isinstance(sid, dict)        # silly mypy does not support to use ShaderIdType
        assert not sbl.running_shaders      # not added because ShaderBoxLayout has no parent
