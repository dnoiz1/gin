#!/usr/bin/env python

import distutils.core
import os.path
import sys

if __name__ == "__main__":
    README = "https://github.com/dnoiz1/gin2/blob/master/README.md"

    if os.path.isfile("gin2/gin2.py"):
        with open("gin2/gin2.py", "r+") as f:
            # this is actually wot pls no
            f.seek(108)
            version = f.read(7)

            if os.path.isdir(".git") and ("sdist" in sys.argv):
                patch = int(version[-3:]) + 1
                if patch > 999:
                   raise ValueError("Update major/minor version")
                version = version[:-3] + "%03i" % patch

                f.seek(108)
                f.write(version)
    else:
        print("Unable to find gin script: refusing to install")
        sys.exit(1)

    distutils.core.setup(
        name="gin",
        version=version,
        author=["Sean B. Palmer", "Tim Noise"],
        url="https://github.com/dnoiz1",
        description="Git index file parser",
        long_description="Documented in `@dnoiz1/gin2/README.md <%s>`_" % README,
        packages=["gin2"],
        platforms="Linux and OS X",
        classifiers=[
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX",
            "Programming Language :: Python :: 2"
        ]
    )
