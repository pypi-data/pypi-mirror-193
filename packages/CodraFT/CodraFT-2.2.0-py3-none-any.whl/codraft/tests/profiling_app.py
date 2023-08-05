# -*- coding: utf-8 -*-
#
# Licensed under the terms of the BSD 3-Clause or the CeCILL-B License
# (see codraft/__init__.py for details)

"""
Profiling
"""

from codraft.env import execenv
from codraft.tests import codraft_app_context

SHOW = False  # Show test in GUI-based test launcher


def test():
    """Dictionnary/List in metadata (de)serialization test"""
    execenv.unattended = True
    with codraft_app_context() as win:
        win.open_h5_files(
            [
                "C:/Dev/Projets/X-GRID_data/Projets_Oasis/XGRID5/VS000001-blobs_doh_profiling.h5"
            ],
            import_all=True,
        )


if __name__ == "__main__":
    test()
