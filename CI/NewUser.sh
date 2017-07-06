#!/bin/bash

sudo deluser --remove-home testuser

echo -n "Username? "
read varuser

echo -n "Password? "
read varpass

sudo useradd -U $varuser -G sudo -d /home/$varuser -p $varpass -m