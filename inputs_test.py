from modules.key_inputs import GTA5KeyboardEvent


def key_change_handler(keys):
    print("\r", keys, end='', flush=True)


def main():
    evt = GTA5KeyboardEvent(key_change_handler)
    evt.run()


# from inputs import get_gamepad
#
#
# def main():
#     while 1:
#         events = get_gamepad()
#         if events:
#             for event in events:
#                 print(event.ev_type, event.code, event.state)
#
#
if __name__ == "__main__":
    main()
