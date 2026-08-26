from manim import *

class Trigonometria(Scene):
    def construct(self):
        # titulo de la identidad
        title = MathTex(r"\sin^2(\theta) + \cos^2(\theta) = 1")
        title.to_edge(UP)
        self.play(Write(title))

        # configurar circulo unitario
        axes = Axes(
            x_range = [-1.5, 1.5,1],
            y_range = [-1.5, 1.5, 1],
            x_length = 5,
            y_length = 5,

        ).shift(DOWN * 0.5)

        # radio de 2.5
        r_pixel=2.5
        circle = Circle(radius=r_pixel, color=GRAY_B).move_to(axes.c2p(0,0))
        self.play(Create(axes), Create(circle))

        # angulo teta
        theta_tracker = ValueTracker(35*DEGREES)

        # elementos dinamicos del triangulo
        hypotenuse = always_redraw(lambda: Line(
            start = axes.c2p(0,0),
            end=axes.c2p(np.cos(theta_tracker.get_value()), np.sin(theta_tracker.get_value())),
            color = WHITE,
            stroke_width = 4
        ))

        # cateto adyacente
        adjacent = always_redraw(lambda: Line(
            start= axes.c2p(0,0),
            end = axes.c2p(np.cos(theta_tracker.get_value()),0),
            color = RED,
            stroke_width = 5
        ))

        #cateto opuesto
        opposite = always_redraw(lambda: Line(
            start = axes.c2p(np.cos(theta_tracker.get_value()),0),
            end = axes.c2p(np.cos(theta_tracker.get_value()),np.sin(theta_tracker.get_value())),
            color = GREEN,
            stroke_width = 5
        ))

        cos_label = always_redraw(lambda: MathTex(r"\cos(\theta)", color=RED).scale(0.7).next_to(adjacent, DOWN, buff=0.1))
        sin_label = always_redraw(lambda: MathTex(r"\sin(\theta)", color=GREEN).scale(0.7).next_to(opposite,RIGHT,buff = 0.1))

        angle_arc = always_redraw(lambda: Arc(
            radius=0.4,
            start_angle=0,
            angle=theta_tracker.get_value(),
            arc_center=axes.c2p(0, 0),
            color=YELLOW
        ))

        # 6. Mostrar el triángulo en pantalla
        self.play(Create(hypotenuse), Create(adjacent), Create(opposite))
        self.play(Create(angle_arc), Write(cos_label), Write(sin_label))
        self.wait(1)

        # 7. Animación del movimiento (Variar el ángulo de 35 a 120 grados)
        self.play(
            theta_tracker.animate.set_value(120 * DEGREES),
            run_time=4,
            rate_func=linear
        )
         # Regresar a 10 grados para observar el cambio en sentido opuesto
        self.play(
            theta_tracker.animate.set_value(10 * DEGREES),
            run_time=3,
            rate_func=smooth
        )
        self.wait(1)