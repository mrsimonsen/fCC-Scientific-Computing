#!/bin/bash

PSQL="psql -X --username=freecodecamp --dbname=salon --tuples-only -c"

MAIN_MENU(){
  echo "$($PSQL "SELECT service_id, name FROM services ORDER BY service_id")" | while read SERVICE_ID BAR NAME
  do
	echo "$SERVICE_ID) $NAME"
  done
  read SERVICE_ID_SELECTED
  SERVICE_NAME_SELECTED=$($PSQL "SELECT name FROM services WHERE service_id = $SERVICE_ID_SELECTED")
  if [[ -z $SERVICE_NAME_SELECTED ]]
  then
	echo -e "\nI could not find that service. What would you like today?"
	MAIN_MENU
  else
	echo -e "\nWhat's your phone number?"
	read CUSTOMER_PHONE
	CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE phone = '$CUSTOMER_PHONE'")
	if [[ -z $CUSTOMER_NAME ]]
	then
	  echo -e "\nI don't have a record for that phone number, what's your name?"
	  read CUSTOMER_NAME
	  INSERT_CUSTOMER_RESULT=$($PSQL "INSERT INTO customers(name, phone) VALUES('$CUSTOMER_NAME', '$CUSTOMER_PHONE')")
	fi
	CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone = '$CUSTOMER_PHONE'")
	echo -e "\nWhat time would you like your $SERVICE_NAME_SELECTED, $CUSTOMER_NAME?"
	read SERVICE_TIME
	INSER_APPT_RESULT=$($PSQL "INSERT INTO appointments(customer_id, service_id, time) VALUES($CUSTOMER_ID, $SERVICE_ID_SELECTED, '$SERVICE_TIME')")
	echo -e "\nI have put you down for a $SERVICE_NAME_SELECTED at $SERVICE_TIME, $CUSTOMER_NAME."
  fi
}




echo -e "\n~~~~~ MY SALON ~~~~~\n"
echo -e "Welcome to My Salon, how can I help you?\n"
MAIN_MENU
