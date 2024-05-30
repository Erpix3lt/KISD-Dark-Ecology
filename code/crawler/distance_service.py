from gpiozero import DistanceSensor

class DistanceService:
    
    def __init__(self):
        self.ultrasonic: DistanceSensor = DistanceSensor(echo=18, trigger=17, threshold_distance=0.2)
        self.is_colliding: bool = False
        self.ultrasonic.when_in_range = self.on_collision
        self.ultrasonic.when_out_of_range = self.on_no_collision
    
    def on_collision(self) -> None:
        print("Collision detected!")
        self.is_colliding = True

    def on_no_collision(self) -> None:
        print("No collision.")
        self.is_colliding = False

    def is_colliding(self) -> bool:
        return self.is_colliding
