#!/bin/bash

echo 'what do you use: '
echo '1) Linux'
echo '2) Termux'
read DISTR

case $DISTR in
     1|linux)
          if [ "$EUID" -ne 0 ]
               then echo "Пожалуйста, запустите программу через sudo"
               exit
          else
          echo "Linux install..."
          sudo apt-get update
          sudo apt-get upgrade
          sudo apt-get install php
          php config.php
          fi
          ;;
     2|termux)
          echo "Termux install..."
          pkg update
          pkg upgrade
          pkg install php
          php config.php
          ;;
     *)
          echo "Unknown value."
          ;;
      esac
