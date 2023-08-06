"""Create metadata of operations"""
import pydoc


def run_make_operations_meta(include):
    """Make metadata"""
    print(include)
    for include_module in include:
        pydoc.locate(include_module)
