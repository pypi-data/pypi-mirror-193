import signal
import psutil
import os

DESTRUCTORS = {}


def register_destructor(obj_id, dtor):
    DESTRUCTORS[obj_id] = dtor


def remove_destructor(obj_id):
    if obj_id in DESTRUCTORS:
        del DESTRUCTORS[obj_id]


def invoke_destructors():
    to_delete = []

    for obj_id, dtor in DESTRUCTORS.items():
        dtor()
        to_delete.append(obj_id)

    for obj_id in to_delete:
        remove_destructor(obj_id)


def terminate_all_subprocess():
    procs = psutil.Process().children()
    for p in procs:
        p.terminate()


def interrupt_handler(a, b):
    invoke_destructors()
    terminate_all_subprocess()
    os._exit(0)


def setup_interrupt_handlers():
    signal.signal(signal.SIGINT, interrupt_handler)
    signal.signal(signal.SIGTERM, interrupt_handler)
