# KISD-Dark-Ecology
Archive of everything surrounding the course.

## Dates
- Exhibition in Summer (around June)

## TODOs
- Build a handheld navigation towars light device. Attach two light sensors to a raspberry pi. Compare both values, let the raspberry pi navigate you by telling either left or right. This might also be possible with a camera.

## Course-Works
- Flora <br> https://github.com/Erpix3lt/Flora

## Project Ideas
### Visualize Plant Data (Electrical Current..) and train a model on the visualized images, in order to give some feedback
### The next Step in Gardening
Withing this project we want to add human attributes to a confined plant. This shall be the next step in the plant evolution. It struck us, how people care about their houseplant.   The detail of these interaction are sometimes very complex. With our project we want to give feedback from the plant. This feedback might range from a plant moving where the environment suits best, the plant reacting to peoples emotions or even the plant communicatin in text.
### How do you like plants
A series of different plant in confined environments, ranging from beautiful to ugly. People shall display their connection to these plants in emotions. Based on a map of happy - grim the terrariums will either try to destroy or keep the plants alive.
Have a setup of where to put faces ("Röntgenraum Zahnarzt") scane emotions, display live data of terrarium.
  
## References
### 18.10.2023
- Max Ernst Museum, Exhibition <br> https://maxernstmuseum.lvr.de/de/ausstellungen/surreal_futures_16nv2a6w00cbh/surreal_futures.html
- Virtual Herbaria, Archive.org <br> https://archive.org/details/texts?query=Herbaria
- ImageNet Dataset Categories <br> https://www.image-net.org/
- Ernst Haekel Zoologe <br> https://de.wikipedia.org/wiki/Ernst_Haeckel

### 19.10.2023
- Voynich Manuskript, Plant Chapter <br> http://www.edithsherwood.com/voynich_botanical_plants/ <br> https://www.holybooks.com/wp-content/uploads/Voynich-Manuscript.pdf
- WordNet Relations of words, also API available <br> https://wordnet.princeton.edu/
- OpenAI Microscope <br> https://microscope.openai.com/models

### 31.10.2023
- Objects and texture <br> https://www.cytter-datalab.com/

### 09.11.2023
- What do Vision Transformers Learn? A Visual Exploration <br>https://arxiv.org/abs/2212.06727
- AI Art without text to image - Myriad Tulips <br>https://annaridler.com/myriad-tulips
- Telegarden <br> https://goldberg.berkeley.edu/garden/Ars/

### 14.11.2023
- Dust I <br> https://arambartholl.com/de/dust-winter-prison/

### 16.11.2023
- Nooscope Manifeterd <br> https://link.springer.com/article/10.1007/s00146-020-01097-6

### 21.12.2023
- Raspi and Camera <br> https://magpi.raspberrypi.com/articles/add-navigation-to-a-low-cost-robot

### 10.01.2024
Logic architecture approach 1:
- Scan for the brightest point in the image
- Trigger a rotating motion until the brightest point is centered.
- Move for a given time forward
- Scan again, should the brightest point be still in the center continue

Logic architecture approach 2:
- Continously scan and move for the brightest point
- there is no centering of the brightest point
- either move the left or right motor slower/faster depending of where you want to go

Problems arising:
- Due to the narrow fov, only the viewable is scanned for the brightest light. Implement an algorythm to scan 360° for the brightest point and compare.
- When do we settle? Should the robot be in continuos motion? Attach a light sensor to the bottom of the robot, If a certain treshhold of brightness is reach settle for a while.

### 30.01.2024
- Object avoidance <br> https://littlebirdelectronics.com.au/guides/163/obstacle-avoidance-robot-with-raspberry-pi-4

## 14.02.2025
- PDF exhibiton: https://spaces.kisd.de/app/uploads/sites/5471/2024/06/in_06-2024-web-2-HL.pdf
