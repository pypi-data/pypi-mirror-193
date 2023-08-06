""" unit tests """
from conftest import skip_gitlab_ci

from kivy.uix.button import Button

from ae.kivy_file_chooser import FileChooserPopup


def test_declaration():
    assert FileChooserPopup


@skip_gitlab_ci
class TestFileChooserPopup:
    def test_open(self):
        # fcp = FileChooserPopup()
        # wid = Button(text='test')
        # fcp.open(wid)
        assert True

