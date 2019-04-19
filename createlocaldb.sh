#!/bin/bash

# Verify if Postgres is installed
if ! type "psql" > /dev/null; then
    echo "Postgres is not installed."
    printf "To install:\t sudo apt-get install postgresql\n"
    echo "Then excute this script again"
fi

echo "Introduce your password..."
sudo echo "Password introduced."

echo "Configuring local data base..."

printf "\nCreating data base user\n"
sudo -u postgres createuser toDoList
echo "User created: toDoList"

printf "\nCreating data base\n"
sudo -u postgres createdb toDoListdb
echo "Created data base: toDoListdb" 

printf "\nAssigning privileges in the data base\n"
sudo -u postgres psql << EOF
alter user toDoList with encrypted password 'toDoList'; 
grant all privileges on database toDoListdb to toDoList;
\q
EOF
echo "Assigned privileges"
