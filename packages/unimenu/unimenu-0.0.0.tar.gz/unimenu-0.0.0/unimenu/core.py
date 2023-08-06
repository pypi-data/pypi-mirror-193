"""
Core methods to generate custom menus.
"""

import importlib
import pkgutil
import unimenu.dccs._abstract
from unimenu.dccs import detect_dcc, DCC
from unimenu.utils import getattr_recursive, load_config
import os
from pathlib import Path


def setup_module(module,
                 parent_menu: str = None,
                 menu_name: str = None,
                 function_name: str = None,
                 icon: str = None,
                 tooltip: str = None,
                 dcc=None,
                 smart_spaces=True,
                 ):
    """
    Create a menu from a folder with modules,
    automatically keep your menu up to date with all tools in that folder

    note: ensure the folder is importable and in your environment path

    Args:
    module: the name of the module that contains all tools. e.g.: "cool_tools"
                        cool_tools
                        ├─ __init__.py   (import cool_tools)
                        ├─ tool1.py      (import cool_tools.tool1)
                        └─ tool2.py      (import cool_tools.tool2)
    parent: the name of the parent menu to add our menu entries to
    menu_name: optional kwars to overwrite the name of the menu to create, defaults to module name
    function_name: the function name to run on the module, e.g.: 'run', defaults to 'main'
                   if empty, call the module directly
    icon: the icon name to use for the menu entry, defaults to ''
    dcc: the dcc that contains the menu. if None, will try to detect dcc
    """

    function_name = function_name or "main"
    parent_module = importlib.import_module(module)

    # create dict for every module in the folder
    # label: the name of the module
    # callback: the function to run

    # todo support recursive folders -> auto create submenus

    items = []
    for module_finder, submodule_name, ispkg in pkgutil.iter_modules(parent_module.__path__):

        # skip private modules
        if submodule_name.startswith("_"):
            continue

        # to prevent issues with late binding
        # https://stackoverflow.com/questions/3431676/creating-functions-or-lambdas-in-a-loop-or-comprehension
        # first arg might be self, e.g. operator wrapped in blender
        def callback(self=None, _submodule_name=submodule_name, _function_name=function_name, *args, **kwargs):

            # only import the module after clicking in the menu
            # this prevents failed module imports breaking the menu setup
            # or menu generation taking a long time if the module imports are slow
            submodule = module_finder.find_spec(_submodule_name).loader.load_module()

            # run the user-provided function on the module, or call the module directly
            if _function_name:
                function = getattr_recursive(submodule, _function_name)
                function()
            else:
                submodule()

        # add spaces to the label. e.g.: "my_tool" -> "My Tool"
        submodule_label = submodule_name.replace('_', ' ').title() if smart_spaces else submodule_name

        submodule_dict = {
            "label": submodule_label,
            "command": callback,  # todo ensure this also works for dccs that only support strings
        }
        if icon:
            submodule_dict["icon"] = icon
        if tooltip:
            submodule_dict["tooltip"] = tooltip
        items.append(submodule_dict)

    data = {}
    if parent_menu:
        data["parent"] = parent_menu
    data["items"] = [{"label": menu_name or parent_module.__name__, "items": items}]

    # use the generated dict to set up the menu
    return setup(data, dcc)


def load(arg, dcc: DCC = None) -> unimenu.dccs._abstract.MenuNodeAbstract:
    """
    smart menu load from a dict, config file or module
    arg: a config (dict or str) or a module (to create a menu from a folder)
    """
    dcc = dcc or detect_dcc()
    return dcc.menu_node_class.load(arg)


def Node(**kwargs):
    """detect dcc and create a menu node from kwargs"""
    return load(kwargs)


def setup(arg, dcc: DCC = None, backlink=True, parent_app_node=None):
    """
    smart menu setup from a dict, config file or module
    arg: dict, str or module
    dcc: the dcc that contains the menu. if None, will try to detect dcc
    backlink: if True, add an attribute to the app node instance to the app node, doesn't work on all apps e.g. Unreal
    parent_app_node: if provided, use this node as the app parent node instead of the default root node
    returns the app menu node
    """
    menu_node = load(arg, dcc)
    app_node = menu_node.setup(parent_app_node=parent_app_node, backlink=backlink)
    return app_node


# def teardown_config(config_path):
#     """remove the created menu"""
#     # get all entries from a config, assume they are setup, and attempt a teardown
#     data = get_json_data(config_path) or get_yaml_data(config_path)
#     return teardown_dict(data)


# def teardown_dict(data, dcc=None):
#     """remove the created menu"""
#     # get all entries from a dict, assume they are setup, and attempt a teardown
#     dcc = dcc or detect_dcc()
#     return dcc.menu_module.teardown_menu(data)


def teardown_menu(name, dcc=None):
    """remove the created menu"""
    # get the top menu with name X, and delete it and all submenus
    dcc = dcc or detect_dcc()
    return dcc.menu_module.teardown_menu(name)


def config_paths() -> "list[Path]":
    raw_path = os.environ.get("UNIMENU_CONFIG_PATH", "")
    return [Path(x) for x in raw_path.split(os.pathsep) if x]


def discover_config_paths() -> "list[Path]":
    """discover all config files in the config paths"""
    paths = config_paths()
    configs = []
    for path in paths:
        configs.extend(path.rglob("*.json"))
        configs.extend(path.rglob("*.yaml"))
    return configs


def setup_all_configs():
    """setup all config files in the config paths"""
    config_paths = discover_config_paths()

    # register configs without parents first, to avoid creating the child before the parent.
    # note that this is not a perfect solution

    configs1 = []
    configs2 = []

    for config_path in config_paths:
        config_data = load_config(config_path)
        if not config_data.get("parent_path"):  # todo replace hard coded string, we could use Node.parent_path
            configs1.append(config_path)
        else:
            configs2.append(config_path)

    for p in configs1:
        setup(p)
    for p in configs2:
        setup(p)
