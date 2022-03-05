# MIT License 2021 Peter James Mangelsdorf
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files 
# (the "Software"), to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, 
# publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# https://opensource.org/licenses/MIT

# Bandcamp Song Renaming Utility
# 2021-09-16T19:13:00-04:00
# Peter-James-Mangelsdorf-201943
# Uses Peter's REPL Aid

from .repl import *

# Display Options (String)
if "opts" not in globals(): opts = ""
opts += """

## BandCamp Song Renaming

### Basics
rename_song       ( str ) Rename a Single File    ( None )
rename_all_songs  ( str ) Rename All Files in Dir ( None )
bc_pjm_rename     ( str ) Bandcamp -> Peter Name  ( str  )
"""

def rename_all_songs(filepath: str = ".") -> None:
    log("\n---\n")
    for filename_any in lsl(filepath):
        rename_song(filename_any)

def rename_song(filename_any: str) -> None:
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
    new_filename = bc_pjm_rename(filename_any)
    rename(filename_any, new_filename)

def log(any_obj: object) -> None:
    logfile = open("logfile.yaml",mode="a",encoding="utf-8")
    print(any_obj)
    logfile.write(str(any_obj) + "\n")
    logfile.close()

def test_pf_field(input_field,output_field) -> None:
    if output_field != input_field:
        log("    # ERROR: Does Not Match!")
        log("    # Should Be:")
        log("    #   \"" + str(input_field) + "\"")

def bc_pjm_rename(bc_name: str) -> str:

    # Log Metadata
    log("  gen:")
    log("    time: " + timenow())
    log("    method: rename_songs.bc_pjm_rename")
    log("    type: Actual")
    log("  type: SongName") 

    # Copy the Raw Name
    raw_str = bc_name
    log("  raw_str: |-\n    " + raw_str + "\"")
    
    # Split Name into Parts
    bc_comp_str = raw_str.split(" - ")
    log("  bc_comp_str:\n    " + str(bc_comp_str))

    # Artist 1
    bc_artist_1 = bc_comp_str[0]
    log("  bc_artist_1: \"" + bc_artist_1 + "\"")
    
    # Album
    bc_album = bc_comp_str[1]
    log("  bc_album: \"" + bc_album + "\"")
    
    # Track Number and Artist 2
    bc_track_number_artist_2 = bc_comp_str[2]
    log("  bc_track_number_artist_2: \"" + bc_track_number_artist_2 + "\"")
    
    # Track Name and Parenthized Text
    bc_track_name_metadata_filetype = bc_comp_str[-1]
    log("  bc_track_name_metadata_filetype: \"" + bc_track_name_metadata_filetype + "\"")
    
    # Check Unknowns
    bc_comp_str_len_over = len(bc_comp_str) - 4
    log("  bc_comp_str_len_over: \"" + str(bc_comp_str_len_over) + "\"")
    
    # Find Unknowns
    bc_unknowns = []
    for remaining_fields in range(bc_comp_str_len_over):
        bc_unknowns.append(bc_comp_str[3 + remaining_fields].strip())
    log("  bc_unknowns:\n    " + str(bc_unknowns))
    
    # Track Number
    pjm_track_number = bc_track_number_artist_2.split(" ")[0]
    log("  pjm_track_number: \"" + pjm_track_number + "\"")

    # Track Artist
    pjm_track_artist = "-".join(bc_track_number_artist_2.split(" ")[1:]).lower()
    log("  pjm_track_artist: \"" + pjm_track_artist + "\"")

    # Metadata; Filetype; Track Name (No Metadata)
    pjm_track_metadata = ""
    pjm_file_type =  bc_track_name_metadata_filetype[-3:]
    pjm_track_name = bc_track_name_metadata_filetype[0:-4]

    # Metadata; Filetype; Track Name (With Metadata)
    if "(" in bc_track_name_metadata_filetype:
        bc_track_name_metadata_filetype_split = bc_track_name_metadata_filetype[0:-4].split("(")
        pjm_track_name = bc_track_name_metadata_filetype_split[0]
        pjm_track_metadata = bc_track_name_metadata_filetype_split[1]
        pjm_track_metadata = "-".join(pjm_track_metadata.replace(")","").strip().split(" ")).lower()

    # Metadata; Filetype; Track Name (Common)
    log("  pjm_track_metadata: \"" + pjm_track_metadata + "\"")
    log("  pjm_file_type: \"" + pjm_file_type + "\"")

    # Track Name (No Unknowns)
    pjm_track_name = "-".join(pjm_track_name.strip().split(" ")).lower()

    # Track Name (With Unknowns)
    if len(bc_unknowns) != 0:
        for unknown_str in bc_unknowns:
            pjm_track_name = "-".join(unknown_str.split(" ")).lower() + "-" + pjm_track_name

    # Track Name (Common)
    log("  pjm_track_name: \"" + pjm_track_name + "\"")

    # Final String
    pjm_final_str = pjm_track_number + "." + pjm_track_artist + "." + pjm_track_name
    if pjm_track_metadata:
        pjm_final_str += "." + pjm_track_metadata
    pjm_final_str += "." + pjm_file_type
    log("  pjm_final_str: \"" + pjm_final_str + "\"")

    # Done
    log("  status: Done")
    return pjm_final_str

def test_generate_filename(input_song:Obj) -> str:

    # Log Metadata
    log("  gen:")
    log("    time: " + timenow())
    log("    method: rename_songs.test_generate_filename")
    log("    type: Test")
    log("  type: SongName")

    # Create Local Comparator
    output_song = Obj()

    # Copy the Raw Name
    output_song.raw_str = input_song.raw_str
    log("  raw_str: |-\n    " + output_song.raw_str + "\"")
    
    # Split Name into Parts
    output_song.bc_comp_str = output_song.raw_str.split(" - ")
    log("  bc_comp_str:\n    " + str(output_song.bc_comp_str))
    test_pf_field(input_song.bc_comp_str, output_song.bc_comp_str)

    # Artist 1
    output_song.bc_artist_1 = output_song.bc_comp_str[0]
    log("  bc_artist_1: \"" + output_song.bc_artist_1 + "\"")
    test_pf_field(input_song.bc_artist_1, output_song.bc_artist_1)
    
    # Album
    output_song.bc_album = output_song.bc_comp_str[1]
    log("  bc_album: \"" + output_song.bc_album + "\"")
    test_pf_field(input_song.bc_album, output_song.bc_album)
    
    # Track Number and Artist 2
    output_song.bc_track_number_artist_2 = output_song.bc_comp_str[2]
    log("  bc_track_number_artist_2: \"" + output_song.bc_track_number_artist_2 + "\"")
    test_pf_field(input_song.bc_track_number_artist_2, output_song.bc_track_number_artist_2)
    
    # Track Name and Parenthized Text
    output_song.bc_track_name_metadata_filetype = output_song.bc_comp_str[-1]
    log("  bc_track_name_metadata_filetype: \"" + output_song.bc_track_name_metadata_filetype + "\"")
    test_pf_field(input_song.bc_track_name_metadata_filetype, output_song.bc_track_name_metadata_filetype)
    
    # Check Unknowns
    output_song.bc_comp_str_len_over = len(output_song.bc_comp_str) - 4
    log("  bc_comp_str_len_over: \"" + str(output_song.bc_comp_str_len_over) + "\"")
    test_pf_field(input_song.bc_comp_str_len_over, output_song.bc_comp_str_len_over)
    
    # Find Unknowns
    output_song.bc_unknowns = []
    for remaining_fields in range(output_song.bc_comp_str_len_over):
        output_song.bc_unknowns.append(output_song.bc_comp_str[3 + remaining_fields].strip())
    log("  bc_unknowns:\n    " + str(output_song.bc_unknowns))
    test_pf_field(input_song.bc_unknowns, output_song.bc_unknowns)
    
    # Track Number
    output_song.pjm_track_number = output_song.bc_track_number_artist_2.split(" ")[0]
    log("  pjm_track_number: \"" + output_song.pjm_track_number + "\"")
    test_pf_field(input_song.pjm_track_number, output_song.pjm_track_number)

    # Track Artist
    output_song.pjm_track_artist = "-".join(output_song.bc_track_number_artist_2.split(" ")[1:]).lower()
    log("  pjm_track_artist: \"" + output_song.pjm_track_artist + "\"")
    test_pf_field(input_song.pjm_track_artist, output_song.pjm_track_artist)

    # Metadata; Filetype; Track Name (No Metadata)
    output_song.pjm_track_metadata = ""
    output_song.pjm_file_type =  output_song.bc_track_name_metadata_filetype[-3:]
    output_song.pjm_track_name = output_song.bc_track_name_metadata_filetype[0:-4]

    # Metadata; Filetype; Track Name (With Metadata)
    if "(" in output_song.bc_track_name_metadata_filetype:
        bc_track_name_metadata_filetype_split = output_song.bc_track_name_metadata_filetype[0:-4].split("(")
        output_song.pjm_track_name = bc_track_name_metadata_filetype_split[0]
        output_song.pjm_track_metadata = bc_track_name_metadata_filetype_split[1]
        output_song.pjm_track_metadata = "-".join(output_song.pjm_track_metadata.replace(")","").strip().split(" ")).lower()

    # Metadata; Filetype; Track Name (Common)
    log("  pjm_track_metadata: \"" + output_song.pjm_track_metadata + "\"")
    test_pf_field(input_song.pjm_track_metadata, output_song.pjm_track_metadata)
    log("  pjm_file_type: \"" + output_song.pjm_file_type + "\"")
    test_pf_field(input_song.pjm_file_type, output_song.pjm_file_type)

    # Track Name (No Unknowns)
    output_song.pjm_track_name = "-".join(output_song.pjm_track_name.strip().split(" ")).lower()

    # Track Name (With Unknowns)
    if len(output_song.bc_unknowns) != 0:
        for unknown_str in output_song.bc_unknowns:
            output_song.pjm_track_name = "-".join(unknown_str.split(" ")).lower() + "-" + output_song.pjm_track_name

    # Track Name (Common)
    log("  pjm_track_name: \"" + output_song.pjm_track_name + "\"")
    test_pf_field(input_song.pjm_track_name, output_song.pjm_track_name)

    # Final String
    output_song.pjm_final_str = output_song.pjm_track_number + "." + output_song.pjm_track_artist + "." + output_song.pjm_track_name
    if output_song.pjm_track_metadata:
        output_song.pjm_final_str += "." + output_song.pjm_track_metadata
    output_song.pjm_final_str += "." + output_song.pjm_file_type
    log("  pjm_final_str: \"" + output_song.pjm_final_str + "\"")
    test_pf_field(input_song.pjm_final_str, output_song.pjm_final_str)

    # Done
    log("  status: Done")
    return output_song.pjm_final_str

def test_pf_filename_1() -> None:
    log("\n\ntest_bc_filename_1:")
    test_generate_filename(
      Obj(
        raw_str = "Various Artists - Thank You For Holding - 19 회사AUTO - カスタマーサービスLine✆NE - 09 。。。分21 .ogg",
        bc_comp_str = [
          "Various Artists",
          "Thank You For Holding",
          "19 회사AUTO",
          "カスタマーサービスLine✆NE",
          "09 。。。分21 .ogg"
        ],
        bc_artist_1                     = "Various Artists",
        bc_album                        = "Thank You For Holding",
        bc_track_number_artist_2        = "19 회사AUTO",
        bc_track_name_metadata_filetype = "09 。。。分21 .ogg",
        bc_comp_str_len_over            = 1,
        bc_unknowns                     = ["カスタマーサービスLine✆NE"],
        pjm_track_number                = "19",
        pjm_track_artist                = "회사auto",
        pjm_track_name                  = "カスタマーサービスline✆ne-09-。。。分21",
        pjm_track_metadata              = "",
        pjm_file_type                   = "ogg",
        pjm_final_str                   = "19.회사auto.カスタマーサービスline✆ne-09-。。。分21.ogg"
      )
    )
    # This filename is a real clusterfuck
    # It comes from here:
    #   album:        カスタマーサービスLine✆NE
    #   artist:       회사AUTO
    #   track number: 09
    #   track name:    。。。分21
    #   url:          https://ailanthusrecordings.bandcamp.com/album/line-ne
    # The total composite is as such:
    #   - host artist:          Various Artists
    #   - host album:           Thank You For Holding
    #   - host track number:    19
    #   - host track artist:    회사AUTO
    #   - source album:         カスタマーサービスLine✆NE
    #   - source track number:  09
    #   - source track name:    "。。。分21 "
    #   - host filetype:        .ogg
    # The problem is fundamentally not having access to recursion specifiers
    # Since we only have flat-specifiers (` - ` on bandcamp, `.` on peter's files)
    # We cannot specify that this is actually: (types)
    #   `(host-artist host-track track-name)`
    #   `(host-artist host-track (source-album source-track))`
    #   `(host-artist host-track (source-album (source-track-number source-track-name)))`
    # To handle this, will simply always set `track_name_metadata_filetype` to be `bc_comp_str[-1]`

def test_pf_filename_2() -> None:
    log("\n\ntest_bc_filename_2:")
    test_generate_filename(
      Obj(
        raw_str = "Various Artists - Thank You For Holding - 07 Limousine - Rainforest Cafe Customer Review Hotline (Call Now For $10 Off Next Alligator Avocado Appetizer).ogg",
        bc_comp_str = [
          "Various Artists",
          "Thank You For Holding",
          "07 Limousine",
          "Rainforest Cafe Customer Review Hotline (Call Now For $10 Off Next Alligator Avocado Appetizer).ogg"
        ],
        bc_artist_1                     = "Various Artists",
        bc_album                        = "Thank You For Holding",
        bc_track_number_artist_2        = "07 Limousine",
        bc_track_name_metadata_filetype = "Rainforest Cafe Customer Review Hotline (Call Now For $10 Off Next Alligator Avocado Appetizer).ogg",
        bc_comp_str_len_over            = 0,
        bc_unknowns                     = [],
        pjm_track_number                = "07",
        pjm_track_artist                = "limousine",
        pjm_track_name                  = "rainforest-cafe-customer-review-hotline",
        pjm_track_metadata              = "call-now-for-$10-off-next-alligator-avocado-appetizer",
        pjm_file_type                   = "ogg",
        pjm_final_str                   = "07.limousine.rainforest-cafe-customer-review-hotline.call-now-for-$10-off-next-alligator-avocado-appetizer.ogg"
      )
    )

def test_all():
    log("\n---\n")
    test_pf_filename_1()
    test_pf_filename_2()

if __name__ == "__main__":
    # cls && py rename_songs.py
    test_all()
