from modules.key_inputs import GTA5KeyboardEvent


def key_change_handler(keys):
    print(keys)


evt = GTA5KeyboardEvent(key_change_handler)
evt.run()
