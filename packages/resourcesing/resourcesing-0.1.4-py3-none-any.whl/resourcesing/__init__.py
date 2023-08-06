import pathlib as __pathlib
import inspect as __inspect
from daemonprocessing import rerun as __rerun

def get_exe_path() -> __pathlib.Path:
    return __pathlib.Path(__rerun.current_executable().split()[-1])

def get_obj_path(object) -> __pathlib.Path:
    return __pathlib.Path(__inspect.getfile(object))