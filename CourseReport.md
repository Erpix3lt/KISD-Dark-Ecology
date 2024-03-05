# Dark Ecology
Course Report - *Maximilian Schmalenbach* <br>
KISD, Th-Köln - Wintersemester 2023/24

### Objectives
The long-term project Dark Ecology, led by Prof. Dr. Lasse Scherrfig with the help of Laura Wagner, aimed to establish an understanding of the coherence between the worlds of artificial intelligence and botanical gardens. The aim was to introduce us students to the theoretical background of these worlds, while giving us the methods and knowledge to work on the production for an upcoming exhibition in the summer of 2024.
There was no clear product or artwork to be expected from this course.
However, we did visit an exhibition at the Max Ernst Museum. This would la **ter have a strong influence on the work of my project. We were also given the task of visiting the Flora Gardens and looking at the artificial nature that was there.

### Working-Progress
In this chapter, I will solely focus on the later stage of the course where we worked on our actual project. In this course, I teamed up with Luiz Sequira. Initially, we were quite intrigued by the works of Paul Duncombe, which we had seen at the exhibition "Surreal Futures", Max Ernst Museum.
Inspired by this, we wanted to add human attributes to a confined plant. This should be the next step in plant evolution. It struck us how people care about their houseplants. The details of these interactions are very complex. With our project we want to provide feedback from the plant. This feedback might range from a plant moving where the environment suits best, the plant reacting to people's emotions or even the plant communicating in text.
Further research revealed the powerful imagery of a walking plant. Conceptually, we paired this feature with a sunflower. The sunflower should lead itself into bright spots during the exhibition, creating a sense of autonomy.
In order to bring our idea to life, we used the mechanics of a Theo Janssen mechanism to create movement using only two servo motors. We used a laser cutter to cut out the parts required for four legs, a baseplate, and attachments for the motors. After this stage, we spent a lot of time in the workshop, refining each part further, experimenting with different motors, walking algorithms, and so on.
For our final prototype we printed each of the very detailed parts needed for the walking mechanism using a 3D printer. Besides that, we further refined the gears as well as the brackets holding our servo motors. The baseplate, as well as the plate above holding the plant, were made out of perforated metal plates. This gave us stability and durability, though it resulted in the walker being quite heavy.
Alongside the pure mechanical realisation of the project, we also worked on some code allowing for the autonomous navigation of the walker. For this, we used a Raspberry Pi paired with a camera. The code mainly relied on OpenCV for image analysis. We compared the left and right side of the image, navigating towards the side being brighter. Using a camera allowed us to implement further features, such as comparing different light averages. It will also allow us to implement more refined features in the future.
Talking about the feature, we still have to think about an exhibition concept. The following questions need answering: How do we maintain the walker? Where does the walker walk? How do we optimise the walker?

### Results
My work on this project resulted in the following:

A collection of photographs, working together with Felix Willen, we created a small website showcasing the images: https://flora-erpix3lt.vercel.app/.

The conceptualisation of our final project idea, as well as its technical and mechanical realisation, has resulted in a collection of code, the walker, imagery, setup tutorials, and more that can be found here: https://github.com/Erpix3lt/KISD-Dark-Ecology.
<br><br>
Tuesday, 05.03.2024 <br>
*Course conducted by Prof. Dr. Lasse Scherrfig*

