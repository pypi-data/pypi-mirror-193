from magicgui import magic_factory
import qrcode

import numpy as np


@magic_factory(
    call_button="Generate",
)
def qrcode_widget(
    viewer: "napari.viewer.Viewer",
    text: str = "Check out napari: https://napari.org",
    box_size=3,
    border=4,
):
    qr = qrcode.QRCode(box_size=box_size, border=border)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    viewer.add_image(np.asarray(img), name=text)


if __name__ == "__main__":
    import napari

    viewer = napari.Viewer()
    viewer.window.resize(800, 600)

    widget = qrcode_widget()

    viewer.window.add_dock_widget(widget, name="QR-Code")
    # widget_demo.show()
