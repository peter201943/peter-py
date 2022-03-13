"""
Apple Song Renaming Utility

WARNING INCOMPLETE DO NOT USE
"""

from repl import *

# Display Options (String)
if "opts" not in globals(): opts = ""
opts += """

## Apple Music Song Renaming

### Basics
am_rename_song      ( str ) Rename a Single File    ( None )
am_rename_all_songs ( str ) Rename All Files in Dir ( None )
am_pjm_rename       ( str ) Bandcamp -> Peter Name  ( str  )
"""

def am_rename_all_songs(filepath: str = ".") -> None:
    log("\n---\n")
    for filename_any in lsl(filepath):
        am_rename_song(filename_any)

def am_rename_song(filename_any: str) -> None:
    log("\"" + filename_any + "\":")
    if not isfile(filename_any):
        log("  status: Skipped")
        return
    file_extension = filename_any.split(".")[-1]
    if file_extension in ["png", "jpg", "ico"]:
        log("  status: Skipped # (Image/Cover File)")
        return
    if file_extension in ["yaml", "yml", "py", "md", "txt"]:
        log("  status: Skipped # (Misc Supporting File)")
        return
    new_filename = am_pjm_rename(filename_any)
    rename(filename_any, new_filename)

def log(any_obj: object) -> None:
    logfile = open("logfile.yaml",mode="a",encoding="utf-8")
    print(any_obj)
    logfile.write(str(any_obj) + "\n")
    logfile.close()

def am_pjm_rename(am_name: str) -> str:

    # Log Metadata
    log("  gen:")
    log("    time: " + timenow())
    log("    method: rename_songs.am_pjm_rename")
    log("    type: Actual")
    log("  type: SongName") 

    # Copy the Raw Name
    raw_str = am_name
    log("  raw_str: |-\n    " + raw_str + "\"")
    
    # Split Name into Parts
    am_comp_str = raw_str.split(" ")
    log("  am_comp_str:\n    " + str(am_comp_str))
    
    # Track Number
    pjm_track_number = am_comp_str[0]
    log("  pjm_track_number: \"" + pjm_track_number + "\"")

    # Track Name and Extension
    am_track_name_filetype = "-".join(am_comp_str[1:])
    log("  am_track_name_filetype: \"" + am_track_name_filetype + "\"")
        
    # Filetype; Track Name
    pjm_file_type =  am_track_name_filetype.split(".")[-1]
    pjm_track_name = am_track_name_filetype.split(".")[0]
    log("  pjm_file_type: \"" + pjm_file_type + "\"")

    # Track Name
    pjm_track_name = "-".join(pjm_track_name.strip().split(" ")).lower()
    log("  pjm_track_name: \"" + pjm_track_name + "\"")

    # Final String
    pjm_final_str = pjm_track_number + "." + pjm_track_name + "." + pjm_file_type
    log("  pjm_final_str: \"" + pjm_final_str + "\"")

    # Done
    log("  status: Done")
    return pjm_final_str

