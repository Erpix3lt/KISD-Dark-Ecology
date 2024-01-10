## Basic Setup
ssh max@crawler.local

<Enter PW>

sudo apt upgrade

sudo apt update

<Add new ssh passkey to github>

Clone Project

## Get Light Detection Running
First connect the camera to its dedicated port. If you are running on the latest raspberry pi os, there should be no additional configuration needed.

### Install CV2
https://askubuntu.com/questions/1330968/how-can-i-install-python-opencv-package-in-ubuntu-20-04
https://raspberrypi-guide.github.io/programming/install-opencv
sudo apt-get update

sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y

sudo apt-get install python3-opencv

### Install PiCamera2
https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
sudo apt install -y python3-picamera2

### Run the main.py



## Get Servo Running
Connect Servo to GPIO 26 and Ground, Power to 10V








