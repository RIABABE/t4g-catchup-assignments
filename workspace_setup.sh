#!/bin/bash

name="RASHIDAE"

echo "Hello, my name is $name"
echo "Current date and time: $(date)"

mkdir -p session_logs

logfile="session_logs/$(date +%F).log"

echo "Name: $name" >> $logfile
echo "This is my Week 2 workspace setup script." >> $logfile

echo "Setup complete!"
