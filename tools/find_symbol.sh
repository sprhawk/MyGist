if [ $# -lt 3 ]; then
    name=$(basename $0);
    echo "$name UUID arch addr";
    echo "eg: $name 75B26654-010D-356A-B185-29F8F6290822 armv7s 0x43623";
    exit 1;
fi

dSYMPath="$(find ~/Library/Developer/Xcode -iname '*.dSYM' -print0 | xargs -0 dwarfdump -u | grep $1 | sed -E 's/^[^/]+//' | head -n 1)";dwarfdump --arch=$2 --lookup $3 "$dSYMPath"
