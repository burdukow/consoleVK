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
          php config.php
          ;;
     *)
          echo "What?"
          ;;
      esac
