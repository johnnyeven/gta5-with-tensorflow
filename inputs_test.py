# from modules.key_inputs import GTA5KeyboardEvent
#
#
# def key_change_handler(keys):
#     print("\r", keys, end='', flush=True)
#
#
# evt = GTA5KeyboardEvent(key_change_handler)
# evt.run()

from inputs import get_key

while True:
    events = get_key()
    for event in events:
        if event.ev_type == "Key":
            print("\r", event.code, end='')
