#!/bin/bash
# Lancement du programme principal
export PYTHONPATH="$PYTHONPATH:/home/pi/jukebox/modules/"
cd /home/pi/jukebox
python 00_radioPlayerFull.py&
# Lancement du programme qui commande l'extinction avec appui sur le bouton
python shutdown_pi.py > /tmp/shutdown.log 2> /tmp/shutdown-error.log &
# Lancement du programme qui commande le volume sonore
python RotaryEncoderVolumeControl.py&
