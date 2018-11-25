AWK
====

filtering lines
----

ls -l  | awk '$11 ~ /Python.framework/ {split($9, a, "@"); print a[1]}'
