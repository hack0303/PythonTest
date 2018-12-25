# -*- coding: utf8 -*-
'''
Created on 2018��12��25��

@author: developorName
'''
import com.creating.www.main.moduleRela.Bmodule
import com.creating.www.main.moduleRela.Cmodule as c
from com.creating.www.main.moduleRela.Cmodule import func as c_func,func2 as c_func2
'''
6.4.1. Importing * From a Package
Now what happens when the user writes from sound.effects import *? Ideally, one would hope that this somehow goes out to the filesystem, finds which submodules are present in the package, and imports them all. This could take a long time and importing sub-modules might have unwanted side-effects that should only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the package. The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__, it is taken to be the list of module names that should be imported when from package import * is encountered. It is up to the package author to keep this list up-to-date when a new version of the package is released. Package authors may also decide not to support it, if they don’t see a use for importing * from their package. For example, the file sound/effects/__init__.py could contain the following code:

__all__ = ["echo", "surround", "reverse"]
This would mean that from sound.effects import * would import the three named submodules of the sound package.

If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package sound.effects into the current namespace; it only ensures that the package sound.effects has been imported (possibly running any initialization code in __init__.py) and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by __init__.py. It also includes any submodules of the package that were explicitly loaded by previous import statements. Consider this code:

import sound.effects.echo
import sound.effects.surround
from sound.effects import *
In this example, the echo and surround modules are imported in the current namespace because they are defined in the sound.effects package when the from...import statement is executed. (This also works when __all__ is defined.)

Although certain modules are designed to export only names that follow certain patterns when you use import *, it is still considered bad practice in production code.

Remember, there is nothing wrong with using from Package import specific_submodule! In fact, this is the recommended notation unless the importing module needs to use submodules with the same name from different packages.

'''
from com.creating.www.main.moduleRela import * 
#from com.creating.www.main.moduleRela.Cmodule import *
def func():
    print('Amodule')
if __name__ == '__main__':
    com.creating.www.main.moduleRela.Bmodule.func()
    print( com.creating.www.main.moduleRela.Bmodule.__name__)
    com.creating.www.main.moduleRela.Cmodule.func()
    c.func()
    c_func()
    c_func2()
    '''
    作为脚本运行
    6.1.1. Executing modules as scripts
When you run a Python module with

python fibo.py <arguments>
the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". That means that by adding this code at the end of your module:

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    '''
    '''
    6.1.2. The Module Search Path
When a module named spam is imported, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path. sys.path is initialized from these locations:

The directory containing the input script (or the current directory when no file is specified).
PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
The installation-dependent default.
Note On file systems which support symlinks, the directory containing the input script is calculated after the symlink is followed. In other words the directory containing the symlink is not added to the module search path.
After initialization, Python programs can modify sys.path. The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be loaded instead of modules of the same name in the library directory. This is an error unless the replacement is intended. See section Standard Modules for more information.
    '''
    '''
    关于编译：
    https://docs.python.org/3/tutorial/modules.html
    6.1.3
    说明指出，运行速度上脚本和编译后的没有多少区别，只有载入速度可能编译后的比脚本要快些
    '''
    import sys
    print(sys.api_version)
    print(dir(sys))
    print(dir())#列出已经定义的东西
    import builtins
    print(dir(builtins))
    print(com.creating.www.main.moduleRela.OtherModule.__name__)
    #全导入测试
    com.creating.www.main.moduleRela.OtherModule.printx()
    '''
    ValueError: attempted relative import beyond top-level package
      相对路径时有问题，好像和查找的路径有关,待解决
    '''
    from .. import XModule
    XModule.printx()
    '''
    6.4.2。Intra-package References
    6.4.3。Packages in Multiple Directories
      以后解决
    '''
    pass