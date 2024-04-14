from manim import *

# default text rendering
class MyText(Scene):
    def construct(self):
        text = Text("This is so cool!")
        self.play(Write(text), run_time=2)


class CircleAnim(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle), run_time=2)
        self.play(Transform(circle, circle.copy().shift(2*UP + 2*RIGHT)), run_time=2)
        self.play(Transform(circle, circle.copy().scale(0.5)), run_time=2)
        self.wait(1)
        self.play(circle.animate.set_color(RED), run_time=2)  
        self.wait(1)
        self.play(circle.animate.set_opacity(0.5), run_time=2)  

# Render the animation
if __name__ == "__main__":
    my_text_scene = MyText()
    my_text_scene.render(preview=True)

    # Start the second animation
    circle_anim_scene = CircleAnim()
    circle_anim_scene.render(preview=True)
