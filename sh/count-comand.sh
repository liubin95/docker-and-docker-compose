#!/bin/bash
# Count the number of commands in history
grep -E '^:' 0309 | awk -F ';' '{print $2}' | sort | uniq -c | sort -rn
grep -E '^:' 0309 | awk -F ';' '{print $2}' | awk '{print $1}' | sort | uniq -c | sort -rn
