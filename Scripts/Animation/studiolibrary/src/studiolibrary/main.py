#!/usr/bin/env python
# -*- coding: utf-8 -*-

import studioqt
import studiolibrary


def main(*args, **kwargs):
    """
    Convenience method for creating/showing a library widget instance.

    return studiolibrary.LibraryWindow.instance(
        name="",
        path="",
        show=True,
        lock=False,
        superusers=None,
        lockRegExp=None,
        unlockRegExp=None
    )

    :rtype: studiolibrary.LibraryWindow
    """
    # Reload all Studio Library modules when Shift is pressed.
    # This is for developers to test their changes in a DCC application.
    if studioqt.isShiftModifier():
        import studiolibrary
        studiolibrary.reload()

    # Register all the items from the config file.
    import studiolibrary
    studiolibrary.registerItems()

    if studiolibrary.isMaya():
        from studiolibrarymaya import mayalibrarywindow
        libraryWindow = mayalibrarywindow.MayaLibraryWindow.instance(*args, **kwargs)
    else:
        from studiolibrary import librarywindow
        libraryWindow = librarywindow.LibraryWindow.instance(*args, **kwargs)

    return libraryWindow


if __name__ == "__main__":

    # Run the Studio Library in a QApplication instance
    import studioqt
    with studioqt.app():
        studiolibrary.main()
