#!/bin/bash

# Directory python3 is found in
dir="usr/local/bin"

# Add to path if not there
if [ -d "$dir" ] && [[ ":$PATH:" != *":$dir:"* ]]; then
  PATH="${PATH:+"$PATH:"}$dir"
fi

# Run program
python3 ~/Projects/instagram-bot/instagram_bot_weather.py
