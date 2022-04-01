#!/bin/bash

PSQL="psql --username=freecodecamp --dbname=number_guess -t --no-align -c"

NUMBER=$(($RANDOM % 1000))
#prompt for username
echo "Enter your username:"
read USERNAME

BEST=$($PSQL "SELECT best_game FROM players WHERE username = '$USERNAME'")
#if username not in database
if [[ -z $BEST ]]
then
  echo "Welcome, $USERNAME! It looks like this is your first time here."
  GAMES=""
else
  GAMES=$($PSQL "SELECT games_played FROM players WHERE username = '$USERNAME'")
  echo "Welcome back, $USERNAME! You have played $GAMES games, and your best game took $BEST guesses."
fi

echo "Guess the secret number between 1 and 1000:"
read GUESS
COUNT=1
NUMBER=50
#until they guess the secret number
while [[ $(($GUESS != $NUMBER)) -ne 0 ]]
do
  COUNT=$(($COUNT+1))
  #if not a number
  if [[ ! $GUESS =~ ^[0-9]+$ ]]
  then
    echo "That is not an integer, guess again:"
  else
    #if > number
    if [[ $GUESS > $NUMBER ]]
    then
      echo "It's lower than that, guess again:"
    #if < number
    elif [[ $GUESS < $NUMBER ]]
    then
      echo "It's higher than that, guess again:"
    fi
  fi
  read GUESS
done

echo "You guessed it in $COUNT tries. The secret number was $NUMBER. Nice job!"

#check if num of games is empty
if [[ -z $GAMES ]]
then
  #insert player username, num_games=1, best=$COUNT
  INSERT_RESULT=$($PSQL "INSERT INTO players(username, games_played, best_game) VALUES('$USERNAME', 1, $COUNT)")
else
  #update database with num_games+1
  UPDATE_RESULT=$($PSQL "UPDATE players SET games_played=$(($GAMES+1)) WHERE username = '$USERNAME'")
  #check if $COUNT < best
  if [[ $COUNT < $BEST ]]
  then
    #update database with best = $COUNT
    HIGH_SCORE_RESULT=$($PSQL "UPDATE players SET best_game = $COUNT WHERE username = '$USERNAME'")
  fi
fi
    
