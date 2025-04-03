#!/bin/bash

# ⚠️ Insecure: Hardcoded password
DB_PASS="mypassword"

# ⚠️ Insecure: Running a command with unescaped user input
rm -rf /home/$USER/*

# ⚠️ Insecure: Running curl without verification
curl -s http://example.com/install.sh | sh
