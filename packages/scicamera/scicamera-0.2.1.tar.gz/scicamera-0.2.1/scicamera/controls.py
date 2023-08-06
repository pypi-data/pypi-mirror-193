#!/usr/bin/python3
from __future__ import annotations

import threading
from typing import Set

from libcamera import ControlType, Rectangle, Size


# TODO(meawoppl) Bring the libcamera cohersion functions into this file
# currently in the root `__init__.py` Perform forward and backward
# type conversion in one place... here.
class Controls:
    def _framerates_to_durations_(framerates):
        if not isinstance(framerates, (tuple, list)):
            framerates = (framerates, framerates)
        return (int(1000000 / framerates[1]), int(1000000 / framerates[0]))

    def _durations_to_framerates_(durations):
        if durations[0] == durations[1]:
            return 1000000 / durations[0]
        return (1000000 / durations[1], 1000000 / durations[0])

    _VIRTUAL_FIELDS_MAP_ = {
        "FrameRate": (
            "FrameDurationLimits",
            _framerates_to_durations_,
            _durations_to_framerates_,
        )
    }

    def __init__(self, camera, controls={}):
        self._camera = camera
        self._controls = []
        self._lock = threading.Lock()
        self.set_controls(controls)

    def available_control_names(self) -> Set[str]:
        """Returns a set of all available control names"""
        return set(self._camera.camera_ctrl_info.keys())

    def __setattr__(self, name, value):
        if not name.startswith("_"):
            if name in Controls._VIRTUAL_FIELDS_MAP_:
                real_field = Controls._VIRTUAL_FIELDS_MAP_[name]
                name = real_field[0]
                value = real_field[1](value)
            if name not in self.available_control_names():
                raise RuntimeError(f"Control {name} is not advertised by libcamera")
            self._controls.append(name)
        self.__dict__[name] = value

    def __getattribute__(self, name):
        if name in Controls._VIRTUAL_FIELDS_MAP_:
            real_field = Controls._VIRTUAL_FIELDS_MAP_[name]
            real_value = self.__getattribute__(real_field[0])
            return real_field[2](real_value)
        return super().__getattribute__(name)

    def __repr__(self):
        return f"<Controls: {self.make_dict()}>"

    def set_controls(self, controls: dict | Controls):
        with self._lock:
            if isinstance(controls, dict):
                for k, v in controls.items():
                    self.__setattr__(k, v)
            elif isinstance(controls, Controls):
                for k in controls._controls:
                    v = controls.__dict__[k]
                    self.__setattr__(k, v)
            else:
                raise RuntimeError(f"Cannot update controls with {type(controls)} type")

    def get_libcamera_controls(self):
        libcamera_controls = {}
        with self._lock:
            for k in self._controls:
                v = self.__dict__[k]
                id = self._camera.camera_ctrl_info[k][0]
                if id.type == ControlType.Rectangle:
                    v = Rectangle(*v)
                elif id.type == ControlType.Size:
                    v = Size(*v)
                libcamera_controls[id] = v
        return libcamera_controls

    def make_dict(self):
        dict_ = {}
        with self._lock:
            for k in self._controls:
                v = self.__dict__[k]
                dict_[k] = v
        return dict_
