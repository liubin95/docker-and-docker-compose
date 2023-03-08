#!/bin/bash
group_name=sanjutou
user_names="liubin openz caps"

groupadd $group_name
echo "group $group_name is created"

for user in $user_names; do
  useradd -m -g $group_name "$user"
  echo "$user" | passwd --stdin "$user"
  chage -d 0 "$user"
  echo "user $user is created"
done

exit 0
