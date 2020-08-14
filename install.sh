#!/bin/bash

echo 'what do you use: '
echo '1) Linux'
echo '2) Termux'
read DISTR

case $DISTR in
     1|linux)
          echo "Linux install..."
          ;;
     2|termux)
          echo "Termux install..."
          pkg update
          pkg upgrade
          pkg install php
          echo "enter the authorization token VK: "
          read token
          jq -n --arg name-is $token '{"token": $ARGS.named["name-is"]}'
          ;;
     *)
          echo "What?"
          ;;
      esac