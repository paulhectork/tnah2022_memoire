# delete all tex aux files and the `_minted` folder
# (but not tex, pdf or bash files, aka this script)
for f in *; do
	if test -f "$f" && [[ ! "$f" =~ .*\.(tex|pdf|sh)$ ]]; then
		rm "$f"
	fi;
done;
rm -r _minted-*
echo "auxiliary files deleted"
