#!/bin/bash

PSQL="psql -X --username=freecodecamp --dbname=periodic_table --tuples-only -c"

if [[ -z $1 ]]
then
  echo "Please provide an element as an argument."
else
  #try to find data where $1 is atomic_number or symbol or name
  if [[ $1 =~ ^[0-9]+$ ]]
  then
	#input contains numbers
	RESULT=$($PSQL "SELECT atomic_number FROM elements WHERE atomic_number = $1")
  else
  #input contains letters
	RESULT=$($PSQL "SELECT atomic_number FROM elements WHERE symbol = '$1' OR name = '$1'")
  fi
  if [[ -z $RESULT ]]
  then
	echo "I could not find that element in the database."
  else
	echo $($PSQL "SELECT atomic_number, name, symbol, type, atomic_mass, melting_point_celsius, boiling_point_celsius FROM properties INNER JOIN types USING(type_id) INNER JOIN elements USING(atomic_number) WHERE atomic_number = $RESULT") | while read NUM BAR NAME BAR SYMBOL BAR TYPE BAR MASS BAR MP BAR BP
	do
	  echo "The element with atomic number $NUM is $NAME ($SYMBOL). It's a $TYPE, with a mass of $MASS amu. $NAME has a melting point of $MP celsius and a boiling point of $BP celsius."
	done
  fi

fi
