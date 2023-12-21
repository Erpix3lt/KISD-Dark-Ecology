#include <AccelStepper.h>
// Define a stepper and the pins it will use
AccelStepper stepper(AccelStepper::DRIVER, 9, 8);

int pos = 10000;

void setup()
{ 
  stepper.setMaxSpeed(3500);
  stepper.setAcceleration(2000);
}

void loop()
{
  if (stepper.distanceToGo() == 0) {
    delay(500);
    pos = -pos;
    stepper.moveTo(pos);\
  }
  stepper.run();
}
