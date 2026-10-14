from manim import *

class UnitCircleAnimation(Scene):
    def construct(self):
        title = Text("Unit Circle", font_size=32).to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[-1.5,1.5,1],
            y_range=[-1.5,1.5, 1],
            x_length=4.5,
            y_length=4.5,
            axis_config={"include_numbers": True, "font_size":20}
        ).shift(LEFT * 2.5 + DOWN * 0.5)

        unit_circle = Circle(
            radius=axes.coords_to_point(1,0)[0] - axes.coords_to_point(0,0)[0],
            color=BLUE
        ).move_to(axes.c2p(0,0))

        self.play(Create(axes), Create(unit_circle), run_time=2)

        theta = ValueTracker(0)
        radius_line = always_redraw(lambda: Line(
            axes.c2p(0,0),
            axes.c2p(np.cos(theta.get_value()), np.sin(theta.get_value())),
            color=YELLOW
        ))

        dot = always_redraw(lambda: Dot(
            axes.c2p(np.cos(theta.get_value()), np.sin(theta.get_value())),
            color=RED
        ))

        cos_line = always_redraw(lambda: Line(
            axes.c2p(0,0),
            axes.c2p(np.cos(theta.get_value()),0),
            color=GREEN
        ))

        sin_line = always_redraw(lambda:Line(
            axes.c2p(np.cos(theta.get_value()),0),
            axes.c2p(np.cos(theta.get_value()), np.sin(theta.get_value())),
            color=ORANGE
        ))

        # cos_label = Text(r"$\cos(\theta)$ (Eje X)", color=GREEN).scale(0.7).to_corner(UP_RIGHT).shift(UP * 0.2 + LEFT * 1.5)
        cos_label = Tex(r"$\cos(\theta)$ (Eje X)", color=GREEN).scale(0.7).to_corner(UR).shift(UP * 0.2 + LEFT * 1.5)
        sin_label = Text(r"$sin(\theta)$ (Eje Y)", color = YELLOW).scale(0.7).next_to(cos_label,DOWN, aligned_edge=LEFT)

        angel_label = always_redraw(lambda: MathTex(
            f"\\theta = {int(np.degrees(theta.get_value())% 360)}^\\circ",
            font_size=28
        ).to_corner(UR).shift(UP*1.5+LEFT*1.5))

        self.play(
            FadeIn(radius_line),
            FadeIn(dot),
            FadeIn(cos_line),
            FadeIn(sin_line),
            Write(cos_label),
            Write(sin_label),
            Write(angel_label)
        )

        self.play(
            theta.animate.set_value(2*PI),
            run_time=6,
            rate_func=linear
        )

        self.wait()