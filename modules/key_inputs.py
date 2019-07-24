from inputs import get_key

w = [1, 0, 0, 0, 0, 0, 0, 0, 0]
s = [0, 1, 0, 0, 0, 0, 0, 0, 0]
a = [0, 0, 1, 0, 0, 0, 0, 0, 0]
d = [0, 0, 0, 1, 0, 0, 0, 0, 0]
wa = [0, 0, 0, 0, 1, 0, 0, 0, 0]
wd = [0, 0, 0, 0, 0, 1, 0, 0, 0]
sa = [0, 0, 0, 0, 0, 0, 1, 0, 0]
sd = [0, 0, 0, 0, 0, 0, 0, 1, 0]
nk = [0, 0, 0, 0, 0, 0, 0, 0, 1]


class GTA5KeyboardEvent:
    key_w = False
    key_a = False
    key_s = False
    key_d = False
    key_change_handler = None

    def __init__(self, key_change_handler=None):
        if key_change_handler is not None:
            self.key_change_handler = key_change_handler

    def run(self):
        while True:
            events = get_key()
            for evt in events:
                if evt.ev_type == "Key":
                    if evt.state == 1:
                        print(evt.code)
                        if evt.code == "KEY_A":
                            self.key_a = True
                        elif evt.code == "KEY_S":
                            self.key_s = True
                        elif evt.code == "KEY_RESERVED":
                            self.key_d = True
                        elif evt.code == "KEY_W":
                            self.key_w = True
                    elif evt.state == 0:
                        if evt.code == "KEY_A":
                            self.key_a = False
                        elif evt.code == "KEY_S":
                            self.key_s = False
                        elif evt.code == "KEY_RESERVED":
                            self.key_d = False
                        elif evt.code == "KEY_W":
                            self.key_w = False
                    if self.key_change_handler is not None:
                        self.key_change_handler(self.get_keys_output())

    def get_keys_output(self):
        """
        Convert keys to a ...multi-hot... array
         0  1  2  3  4   5   6   7    8
        [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
        """
        if self.key_w and self.key_a:
            output = wa
        elif self.key_w and self.key_d:
            output = wd
        elif self.key_s and self.key_a:
            output = sa
        elif self.key_s and self.key_d:
            output = sd
        elif self.key_w:
            output = w
        elif self.key_s:
            output = s
        elif self.key_a:
            output = a
        elif self.key_d:
            output = d
        else:
            output = nk
        return output
