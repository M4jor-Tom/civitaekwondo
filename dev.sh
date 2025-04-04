#!/bin/bash

export PROFILE=DEV
if [[ $PROFILE != "" ]]; then
  python main.py
  exit 0
else
  echo "Error:"
  if [[ $PROFILE == "" ]]; then
      echo "> $PROFILE is unset"
  fi
  exit 1
fi
