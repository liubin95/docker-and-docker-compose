#!/bin/bash
# Count the number of commands in history
grep -E '^:' ~/.zsh_history | awk -F ';' '{print $2}' | sort | uniq -c | sort -rn
grep -E '^:' ~/.zsh_history | awk -F ';' '{print $2}' | awk '{if($1 == "sudo"){print $2}else{print $1}}' | sort | uniq -c | sort -rn
