import json
import os
import shutil
import datetime
from siprawn.metadata import default_copyright
import subprocess
import img2doku


def map_manifest_add_file(basedir, fn, collection, type_, copyright_year=None):
    """
    JSON with explicit copyright information
    """
    assert type_ in ("image", "map")
    jfn = os.path.join(basedir, ".manifest")
    if os.path.exists(jfn):
        j = json.load(open(jfn))
    else:
        j = {
            "files": {},
        }

    if not copyright_year:
        copyright_year = datetime.datetime.now().year

    if fn[0] == "/":
        raise ValueError("Require relative path")
    j["files"][fn] = {
        "collection": collection,
        "type": type_,
        "copyright_year": copyright_year,
    }

    # Be really careful not to corrupt records
    json.dump(j,
              open(jfn + ".tmp", "w"),
              sort_keys=True,
              indent=4,
              separators=(',', ': '))
    if os.path.exists(jfn):
        shutil.move(jfn, jfn + ".old")
    shutil.move(jfn + ".tmp", jfn)

def map_user(user, copyright_=None, files=[], run_img2doku=True):
    if not copyright_:
        copyright_ = default_copyright(user)
    print("Files")
    for f in files:
        print("  " + f)
    print("")
    print("")
    print("")
    copyright_ = "&copy; " + str(
        datetime.datetime.today().year) + " " + copyright_
    print("Copyright: " + copyright_)
    cmd = ["prawnmap", "--threads", "4", "-c", copyright_] + files
    print("Running: " + str(cmd))
    subprocess.check_call(cmd)
    print("")
    print("")
    print("")

    if run_img2doku:
        # Only write if the page doesn't already exist
        _out_txt, wiki_page, wiki_url, map_chipid_url, wrote, exists = img2doku.run(
            hi_fns=files, collect=user, write=True, write_lazy=True)
        print("wiki_page: " + wiki_page)
        print("wiki_url: " + wiki_url)
        print("map_chipid_url: " + map_chipid_url)
        print("wrote: " + str(wrote))
