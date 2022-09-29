#!/usr/bin/env bash

# sudo not needed for windows git bash shell
sudo chmod +rwx run.sh
sudo chmod +rwx wpe_merge


python --version
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Installation Complete"

export PATH=$PATH:$pwd
# echo $PATH

