"""
library/pathlib

Documenations: https://docs.python.org/3/library/pathlib.html
"""

import os
import shutil
from pathlib import Path


def main() -> int:
    os.system("echo hello hello > file")

    # -------------------------------------------------------------------------
    # Following methods return 'Path' objects
    #

    cwd = Path.cwd()  # $PWD
    home = Path.home()  # ~/

    # -------------------------------------------------------------------------
    # Create your own 'Path' object.
    #
    # It does not check whether the path exists or not.

    path = Path(r"c:\Windows\System32\cmd.exe")
    path = Path("/usr/bin/python3")
    path = Path("/usr") / "bin" / "python3"  # Operator overload /

    # -------------------------------------------------------------------------
    # To check existence of path
    #

    path_exists = path.exists()

    # -------------------------------------------------------------------------
    # Open files: '.open()' returns a file object
    #

    path = Path.cwd() / "file"
    with path.open() as f:
        content = f.read()
        line = f.readline()

    # or equivalently:

    content = path.read_text()

    # -------------------------------------------------------------------------
    # To get absolute (full) path -> .resolve()
    # .resolve() returns a Path object.

    path = Path("file")
    print("(Possibly relative) path:", path)
    full_path = path.resolve()
    os.system("rm file")

    # -------------------------------------------------------------------------
    # Get the parent (directory) of a path
    #

    parent = path.parent  # returns a relative path: .
    full_path = path.resolve()
    parent_full_path = full_path.parent  # returns a relative path: .

    # -------------------------------------------------------------------------
    # Grand-parent: path.parent.parent (and so on)
    #

    grand_parent = full_path.parent.parent

    # -------------------------------------------------------------------------
    # Get the name of a path (equivalent to 'basename' command)
    #

    basename = full_path.parent.parent.name

    # -------------------------------------------------------------------------
    # Get the stem and suffix of a path
    #

    path = Path("snippet_pathlib.py")
    path_stem = path.stem
    path_suffix = path.suffix

    # -------------------------------------------------------------------------
    # To check if a path is a file or directory
    #

    path = Path("snippet_pathlib.py")
    path_is_file = path.is_file()

    mydir = Path.cwd() / "mydir"
    os.system("mkdir -p " + str(mydir))
    mydir_is_dir = mydir.is_dir()
    shutil.rmtree(mydir)  # rm -r build_dir

    # -------------------------------------------------------------------------
    # To create/write to/delete a file or directory
    #

    new_file = Path.cwd() / "new_file"

    new_file.touch()  # Create file
    new_file.write_text("Hello Hello, World!\n")  # Write text into the file
    new_file.unlink()  # Remove a file

    new_dir = Path.cwd() / "new_dir"

    new_dir.mkdir(exist_ok=True)  # Create (make) directory
    new_dir.rmdir()  # Remove a directory

    # -------------------------------------------------------------------------
    # cd into a directory (using os module)
    #

    new_dir = Path.cwd() / "new_dir"
    new_dir.mkdir()

    os.chdir(new_dir)

    print(f"cd into the '{new_dir.name}'; now cwd:", Path.cwd())
    os.chdir(new_dir.parent)
    new_dir.rmdir()

    # -------------------------------------------------------------------------
    # Listing subdirectories (iterating over items in a directory):
    #

    p = Path(".")
    [x for x in p.iterdir() if x.is_dir()]

    # -------------------------------------------------------------------------
    # Listing Python source files in this directory tree:
    #

    p = Path(".")
    list(p.glob("**/*.py"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
