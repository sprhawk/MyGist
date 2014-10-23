# rsync #

rsync -n -delete -CrutNS --size-only -v -h --progress  --exclude="xcuserdata" --exclude="*.xcworkspace" --exclude=".DS_Store"  Docs/ /Volumes/Macintosh/Docs/
rsync -O -vvv -C -ruN --size-only -h --progress  --exclude="xcuserdata" --exclude="*.xcworkspace" --exclude=".DS_Store"   Docs/ HONGBOs-MacBook-Pro.local::docs

-n, --dry-run               perform a trial run with no changes made

-C, --cvs-exclude           auto-ignore files in the same way CVS does
-S, --sparse                handle sparse files efficiently
--delete                delete extraneous files from dest dirs

-r, --recursive             recurse into directories
-u, --update                skip files that are newer on the receiver
-t, --times                 preserve modification times
-N, --crtimes               preserve create times (newness)

-h, --human-readable        output numbers in a human-readable format
--size-only             skip files that match in size
