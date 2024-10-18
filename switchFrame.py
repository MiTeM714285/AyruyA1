import main


def switch_frame(self, frame_class):
    new_frame = frame_class(self)
    if self._frame is not None:
        self._frame.destroy()
    self._frame = new_frame
    self._frame.pack()
    print(main.entry.__str__())