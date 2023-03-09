import math

class Engine:
    def __init__(self, rpm=0):
        self.rpm = rpm
        self.angle = 0
        self.piston_positions = [0, 0, 0, 0, 0, 0, 0, 0]
        self.crankshaft_rad = 0.05 
        self.connecting_rod_length = 0.15 

    def update(self, dt):
        self.angle += 2 * math.pi * self.rpm / 60 * dt

        for i in range(8):
            piston_angle = self.angle + i * math.pi / 4
            self.piston_positions[i] = self.crankshaft_rad * (1 - math.cos(piston_angle)) \
                + math.sqrt(self.connecting_rod_length ** 2 - self.crankshaft_rad ** 2 * (math.sin(piston_angle)) ** 2)

    def print_piston_positions(self):
        print('Piston positions (meters):')
        for i, position in enumerate(self.piston_positions):
            next_position = self.piston_positions[(i + 1) % 8]
            distance = abs(position - next_position)
            print(f'Piston {i + 1} to piston {i + 2}: {distance:.4f} meters')


engine = Engine(rpm=800)
engine.update(dt=0.01)
engine.print_piston_positions()
