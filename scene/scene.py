import typing as tp

import numpy as np
from numpy.random import uniform

from field import field
from swarm import swarm


class Scene:
    def __init__(self, field_height: float, field_width: float,
                 field_target_function: tp.Callable[[float, float, tuple[float, float]], float],
                 swarm_n_particles: int, swarm_n_iterations: int = 1000, spawn_type: str = "full location"):
        self.spawn_type = spawn_type

        if self.spawn_type == "small area":
            self.edge: int = np.random.randint(4)
            self.factor: float = 20
            if self.edge == 0:    # left
                self.spawn_start_location: np.ndarray = np.array([0, uniform(field_height/self.factor,
                                                                             field_height-field_height/self.factor)])
            elif self.edge == 1:  # right
                self.spawn_start_location: np.ndarray = np.array([field_width,
                                                                  uniform(field_height/self.factor,
                                                                          field_height - field_height/self.factor)])
            elif self.edge == 2:  # top
                self.spawn_start_location: np.ndarray = np.array([uniform(field_width/self.factor,
                                                                          field_width-field_width/self.factor), 0])
            elif self.edge == 3:  # bottom
                self.spawn_start_location: np.ndarray = np.array([uniform(field_width/self.factor,
                                                                          field_width-field_width/self.factor),
                                                                  field_height])
        self.field: field.Field = field.Field(field_height, field_width, field_target_function)
        self.swarm: swarm.Swarm = swarm.Swarm(swarm_n_particles, swarm_n_iterations, self)

    def run(self):
        print(self.swarm.best_global_score)
        self.swarm.release_the_swarm()
        print(self.swarm.best_global_score)


if __name__ == "__main__":
    my_scene = Scene(10, 10, field.gaussian, 5, 1000, spawn_type="small area")
    my_scene.run()
