#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback

try:
    import maya.cmds
except ImportError:
    traceback.print_exc()


class ScriptJob(object):
    """
    self._scriptJob = mutils.ScriptJob(e=['SelectionChanged', self.selectionChanged])
    """
    def __init__(self, *args, **kwargs):
        self.id = maya.cmds.scriptJob(*args, **kwargs)

    def kill(self):
        if self.id:
            maya.cmds.scriptJob(kill=self.id, force=True)
            self.id = None

    def __enter__(self):
        return self

    def __exit__(self, t, v, tb):
        if t is not None:
            self.kill()
