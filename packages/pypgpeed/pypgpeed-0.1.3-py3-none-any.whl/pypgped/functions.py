import io
import os
import re

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter, QIcon
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtWidgets import QTextEdit


def get_box(*args, **kwargs):
    box = None
    for el in args:
        if isinstance(el, QTextEdit):
            box = el
    if "box" in kwargs:
        box = kwargs["box"]
    return box


def validate_password(password):
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return bool(re.match(regex, password))


def get_stored_keys(key_dir=None):
    # get the home directory path

    # set the keys directory path
    if not key_dir:
        key_dir = os.path.join(os.path.expanduser('~'), 'pgp_keys')

    # set the key file paths
    pub_key_path = os.path.join(key_dir, 'pub_key.key')
    pri_key_path = os.path.join(key_dir, 'pri_key.key')

    pub_key_str = ""
    pri_key_str = ""

    # check if the key files exist
    if os.path.exists(pub_key_path) and os.path.exists(pri_key_path):
        # load the public key file as a string
        with io.open(pub_key_path, 'r', encoding='utf-8') as pub_file:
            pub_key_str = pub_file.read()

        # load the private key file as a string
        with io.open(pri_key_path, 'r', encoding='utf-8') as pri_file:
            pri_key_str = pri_file.read()

    return pri_key_str, pub_key_str


def make_directory(path):
    """
    Create a directory and any necessary subdirectories if it doesn't already exist.
    """
    try:
        os.makedirs(path)
    except FileExistsError:
        # directory already exists
        pass
    except Exception as e:
        print(f"An error occurred while creating the directory: {str(e)}")


def set_logo(app):
    svg_data = """
<svg id="eCwKd6ihJFZ1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 300 300" shape-rendering="geometricPrecision" text-rendering="geometricPrecision"><g transform="matrix(1.013629 0 0 1-2.04435 0)"><rect width="304.033771" height="300" rx="0" ry="0" transform="matrix(.973465 0 0 1 2.016883 0.000001)" fill="#1de9b6" stroke-width="0"/></g><text dx="0" dy="0" font-family="&quot;eCwKd6ihJFZ1:::Oswald&quot;" font-size="15" font-weight="700" transform="matrix(5 0 0 5 29.85753 208.536589)" fill="#31363b" stroke="#fff" stroke-width="0.4"><tspan y="0" font-weight="700" stroke-width="0.4"><![CDATA[
PGPEED
]]></tspan></text><text dx="0" dy="0" font-family="&quot;eCwKd6ihJFZ1:::Oswald&quot;" font-size="15" font-weight="700" transform="matrix(5 0 0 5 31.181845 126.454039)" fill="#31363b" stroke="#fff" stroke-width="0.4"><tspan y="0" font-weight="700" stroke-width="0.4"><![CDATA[
PY_
]]></tspan><tspan x="0" y="30" font-weight="700" stroke-width="0.4"><![CDATA[
 
]]></tspan></text>
<style><![CDATA[
@font-face {font-family: 'eCwKd6ihJFZ1:::Oswald';font-style: normal;font-weight: 700;src: url(data:font/ttf;charset=utf-8;base64,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) format('truetype');}
]]></style>
</svg>
    """

    # Load the SVG data into a QPixmap
    renderer = QSvgRenderer(bytearray(svg_data, encoding='utf-8'))
    pixmap = QPixmap(100, 100)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()

    # Set the QPixmap as the application icon
    app.setWindowIcon(QIcon(pixmap))
    return
