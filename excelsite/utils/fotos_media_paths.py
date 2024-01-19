import os
from pathlib import Path

def go():

    def path_():
        rootfolder_ = os.path.dirname(os.path.abspath(__file__))
        rootfolder = Path(rootfolder_)
        media_path = Path(rootfolder.parent.parent, "media")
        return media_path

    media_path=path_()
    media_osn = Path(media_path, "photos","osn",)
    media_dop = Path(media_path, "photos", "dop", )
    media_osn_orig = Path(media_path, "orig", "osn", )
    media_dop_orig = Path(media_path, "orig", "dop", )
    result= {'media_osn': media_osn, 'media_dop':media_dop, 'media_osn_orig':media_osn_orig,  'media_dop_orig':media_dop_orig  }

    return  result