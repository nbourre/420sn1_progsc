from manim import *
import random

class ExampleArray(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.array_len = 6
        self.random_seed = 1  # You can keep your other configuration options here

    def construct(self):
        #VGroup is a container for multiple mobjects
        labels = VGroup(*[
            Text(f"[{index}]", font_size=24)  # Set the font size here
            for index in range(self.array_len)
        ])
        text = VGroup(*[
            Text(str(random.randint(0, 10)), font_size=24)  # Set the font size here
            for i in range(self.array_len)
        ])
        # space it out
        text.arrange(RIGHT,buff=0.8)
        # See: https://github.com/3b1b/manim/blob/master/manimlib/mobject/mobject.py#L936

        for label,t in zip(labels,text): # I like to avoid using indexes
            label.scale(0.5)
            label.next_to(t,DOWN,buff=0.5)

        up_and_down_line = self.get_up_and_down_line(
            VGroup(text,labels),
            buff=0.7, # Distance between numbers and lines
            scale=1.4 # Scale of the line
        )

        self.play(
            *list(map(lambda x: Write(x,run_time=2),[text,labels])),
            *list(map(GrowFromCenter,up_and_down_line))
        )
        self.wait()

    def get_long_line(self,mob,y_direction,buff=0.5,scale=1):
        return Line(
            mob.get_corner(y_direction + LEFT), 
            mob.get_corner(y_direction + RIGHT)
        ).shift(y_direction*buff).scale(scale)

    def get_up_and_down_line(self,mob,**kwargs):
        return VGroup(
            self.get_long_line(mob,UP,**kwargs),
            self.get_long_line(mob,DOWN,**kwargs)
        )