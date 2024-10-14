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

    import studiolibrary

    if studiolibrary.isMaya():
        import studiolibrarymaya
        libraryWindow = studiolibrarymaya.main(*args, **kwargs)
    else:
        libraryWindow = studiolibrary.LibraryWindow.instance(*args, **kwargs)

    return libraryWindow


if __name__ == "__main__":

    # Run the Studio Library in a QApplication instance
    with studiolibrary.app():
        studiolibrary.main()
