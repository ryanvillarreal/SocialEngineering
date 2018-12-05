#!/bin/bash

# change the password of the GoPhish server to something random and output to the screen.
sudo apt install -y sqlite

# create a random hash.  
$password=head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13 ; echo ''

$hash=echo -n $password | sha256sum

# place it in the SQLite Database
sudo sqlite3 gophish.db  'update users set hash=$hash where username="admin";'

# return the password to the screen:
echo "The password is:", $password

