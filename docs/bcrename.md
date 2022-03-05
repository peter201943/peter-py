
# BandCamp RENAME utility

## Better Song Renaming Utility
- Current Utility is Broken
- Also not great documentation
  - an example would really be great
  - and function comments
- And not great imports either
- Logging needs to be better as well
  - the "pseudo yaml" is interesting, but not great
- it's also duplicating the filenames
- and there is no way of progressively updating
  - needs to check if filename matches pattern for a bandcamp songname
- may also want a "cut dupes" function (special function to )
- working medium should be better expressed
  - having a "rename_all" is not a great idea imo
  - there ought to be some way of saying "the files are the input"
  - so that it can instead be expressed as `map(rename_song,*)`
  - or `rename(".")


