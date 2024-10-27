from manim import *  # or: from manimlib import *

# from manim_slides import Slide
from pathlib import Path
import os
from manim import AS2700  # Padrão australiano de cores

# import random as rn

# Create animations
# manim presentation.py
# Flags:
# -q  quality: low(l), medium(m) and high(h),e.g, ql low quality

# Convert to html
# manim-slides convert BasicExample slides.html

# --flush_cache                  Remove cached partial movie files

FLAGS = f"-s -qh"
SCENE = "Intro"
CLEAN = "--flush_cache  "

########### Change background ###########
# config.background_color = AS2700.B62_MIDNIGHT_BLUE


class Presentation(Scene):
    def construct(self):
        # sections
        title = Text(
            "Computational methods",
            font="GFS Complutum",
            weight=BOLD,
            font_size=40,
            color=AS2700.X14_MANDARIN,
        ).to_edge(UP)
        self.add(title)
        self.wait()

        parts = (
            VGroup(
                Text(
                    "Numerical calculus",
                    font="GFS Complutum",
                    font_size=30,
                    color=AS2700.X14_MANDARIN,
                ),
                Text(
                    "Code",
                    font="GFS Complutum",
                    font_size=30,
                    color=AS2700.X14_MANDARIN,
                ),
            )
            .arrange(RIGHT, buff=2)
            .next_to(title, 3 * DOWN)
            .shift(1.4 * LEFT)
        )
        parts_box = VGroup(
            SurroundingRectangle(
                parts[0], buff=0.2, color=AS2700.G13_EMERALD, fill_opacity=0.5
            ),
            SurroundingRectangle(
                parts[1], buff=0.2, color=AS2700.G13_EMERALD, fill_opacity=0.5
            ),
        )
        parts_arrow = VGroup(
            Arrow([0, 3.05, 0], [-1.5, 2.5, 0]), Arrow([0, 3.05, 0], [1.5, 2.5, 0])
        )
        for i in 0, 1:
            self.play(Write(parts_arrow[i]), run_time=0.3)
            self.play(Write(parts_box[i]), run_time=0.3)
            self.play(FadeIn(parts[i]), run_time=0.3)
            self.wait(2)

        # formulas
        forward_text = (
            Text(
                "Formula 2 pts: forward",
                font_size=35,
            )
            .to_edge(LEFT)
            .set_color_by_gradient(
                AS2700.G37_BEANSTALK, AS2700.X14_MANDARIN, AS2700.G37_BEANSTALK
            )
        )
        forward_eq = MathTex(
            "f' = \\frac{f_{1} - f_{0}}{h} + \\mathcal{O}(h)", font_size=40
        ).next_to(forward_text, DOWN)
        self.play(FadeIn(forward_text), Write(forward_eq))
        self.wait(1)

        backward_text = (
            Text(
                "Formula 2 pts: backward",
                font_size=35,
            )
            .to_edge(RIGHT)
            .set_color_by_gradient(
                AS2700.G37_BEANSTALK, AS2700.X14_MANDARIN, AS2700.G37_BEANSTALK
            )
        )
        backward_eq = MathTex(
            "f' = \\frac{f_{0} - f_{-1}}{h} + \\mathcal{O}(h)", font_size=40
        ).next_to(backward_text, DOWN)
        self.play(FadeIn(backward_text), Write(backward_eq))
        self.wait(1)

        analytical = Text(
            "Analytical",
            font="GFS Complutum",
            font_size=30,
            color=AS2700.X14_MANDARIN,
        ).move_to(parts[0])
        self.remove(forward_text, backward_text, forward_eq, backward_eq)
        self.play(Transform(parts[0], analytical))
        self.wait()

        part_analytical = (
            VGroup(
                Text("Formula", font_size=30),
                Text("Pseudocode", font_size=30),
                Text("Flowchart", font_size=30),
            )
            .arrange(DOWN, buff=0.6, aligned_edge=LEFT)
            .next_to(parts[0], 5 * DOWN)
        )

        parts_analytical_arrow = Arrow(ORIGIN, DOWN).next_to(parts[0], DOWN)
        self.add(parts_analytical_arrow)

        part_analytical_box = SurroundingRectangle(
            part_analytical, buff=0.25, color=AS2700.G37_BEANSTALK
        )

        self.play(Write(part_analytical_box))
        for i in range(len(part_analytical)):
            self.play(FadeIn(part_analytical[i]))
            self.wait()

        part_code = (
            VGroup(
                Text("Fortran", font_size=30),
                Text("Python", font_size=30),
                Text("Julia", font_size=30),
            )
            .arrange(DOWN, buff=0.6, aligned_edge=LEFT)
            .next_to(parts[1], 5 * DOWN)
        )
        part_code_box = SurroundingRectangle(
            part_code, buff=0.25, color=AS2700.G37_BEANSTALK
        )

        parts_code_arrow = Arrow(ORIGIN, DOWN).next_to(parts[1], DOWN)
        self.add(parts_code_arrow)

        self.play(Write(part_code_box))
        for i in range(len(part_code)):
            self.play(FadeIn(part_code[i]), run_time=0.3)
            self.wait()
        self.wait()


class Intro(Scene):
    def construct(self):
        ########### Cover ###########
        title = Text(
            "Numerical differentiation",
            font="GFS Complutum",
            weight=BOLD,
            font_size=40,
            color=AS2700.X14_MANDARIN,
        ).to_edge(UP)
        self.add(title)
        self.wait()

        axis = ParametricFunction(
            lambda t: [t, 0, 0], t_range=[-1.1 * PI, 1.1 * PI, 0.1], stroke_width=5
        )
        curve = ParametricFunction(
            lambda t: [t, np.sin(0.9 * t) + 1.5, 0],
            t_range=[-PI, PI, 0.01],
            stroke_width=5,
        )
        curve = CurvesAsSubmobjects(curve)
        curve.set_color_by_gradient(AS2700.B41_BLUEBELL, AS2700.G22_SERPENTINE)

        lines = VGroup()
        x_labels = VGroup()
        f_labels = VGroup()
        for i in range(-2, 3):
            dx = i * PI / 2.0
            line = Line(
                [dx, -0.2, 0],
                [dx, np.sin(0.9 * dx) + 1.5, 0],
                color=AS2700.R11_INTERNATIONAL_ORANGE,
                stroke_width=2,
            )
            x_label = MathTex(f"x_{{{i}}}").next_to(line, DOWN)
            f_label = MathTex(f"f_{{{i}}}").next_to(line, UP)
            lines.add(line)
            x_labels.add(x_label)
            f_labels.add(f_label)
        double_arrow = DoubleArrow(
            [-0.2, 0.5, 0], [1.75, 0.5, 0], tip_length=0.2, color=AS2700.X13_MARIGOLD
        )
        h_label = MathTex("h", color=AS2700.X13_MARIGOLD).next_to(double_arrow, UP)
        delta_h = VGroup(double_arrow, h_label)

        plot = (
            VGroup(lines, line, axis, curve, x_labels, f_labels, delta_h)
            .scale(1.0)
            .to_corner(DL)
        )

        f_approx = (
            MathTex(
                "f_{n} = f(x_{n}); \\ x_{n} = nh \\ (n=0, \\pm 1, \\pm2, ...).",
                font_size=35,
            )
            .next_to(title, DOWN)
            .shift(3.5 * LEFT)
        )
        self.play(Write(f_approx))
        self.wait()
        self.play(Write(plot))
        self.wait()

        taylor_eq = (
            MathTex(
                "f(x) \\approx \\sum_{n=0}^{\\infty} \\frac{1}{n!}",
                "\\left. \\frac{d^{n} f(x)}{dx^{n}} \\right|_{x = x_{0}}",
                "= f(x_{0}) + f'(x_{0})x + \\frac{1}{2} f''(x_{0})x^{2} + \\frac{1}{3!}f'''(x_{0})x^{3} + \\cdots",
                font_size=35,
            )
            .to_corner(UL)
            .shift(2 * DOWN)
        )
        taylor_label = (
            Text("Taylor-MacLaurin", font_size=35)
            .set_color_by_gradient(AS2700.B41_BLUEBELL, AS2700.G22_SERPENTINE)
            .next_to(taylor_eq, UP)
            .shift(4 * LEFT)
        )
        taylor_approx = VGroup(taylor_eq, taylor_label)

        deff_eq = (
            MathTex(
                "f_{0} & = x_{0} \\\\",
                "f_{1} & = x_{0} + h \\\\",
                "f_{-1} &= x_{0} - h \\\\",
                "& \\ \\ \\vdots \\\\",
                "f_{\\pm \\alpha} & = x_{0} \\pm \\alpha h",
                font_size=35,
            )
            .next_to(plot, RIGHT)
            .shift(2 * RIGHT)
        )
        framebox = SurroundingRectangle(
            deff_eq, buff=0.2, color=AS2700.G22_SERPENTINE, fill_opacity=0.3
        )
        deff = VGroup(deff_eq, framebox)
        self.play(FadeIn(deff))
        self.wait()

        self.play(Write(taylor_approx))
        self.wait()


class Interpolation(Scene):
    def construct(self):
        # Formula 2pts forward and backward
        axis = ParametricFunction(
            lambda t: [t, 0, 0], t_range=[-1.1 * PI, 1.1 * PI, 0.1], stroke_width=5
        )
        curve = ParametricFunction(
            lambda t: [t, np.sin(0.9 * t) + 1.5, 0],
            t_range=[-PI, PI, 0.01],
            stroke_width=5,
        )
        curve = CurvesAsSubmobjects(curve)
        curve.set_color_by_gradient(AS2700.B41_BLUEBELL, AS2700.G22_SERPENTINE)

        lines = VGroup()
        x_labels = VGroup()
        f_labels = VGroup()
        for i in range(-2, 3):
            dx = i * PI / 2.0
            line = Line(
                [dx, -0.2, 0],
                [dx, np.sin(0.9 * dx) + 1.5, 0],
                color=AS2700.R11_INTERNATIONAL_ORANGE,
                stroke_width=2,
            )
            x_label = MathTex(f"x_{{{i}}}").next_to(line, DOWN)
            f_label = MathTex(f"f_{{{i}}}").next_to(line, UP)
            lines.add(line)
            x_labels.add(x_label)
            f_labels.add(f_label)
        delta_h = PI / 2.0
        margin = 0.04
        # f1
        p1 = [0 + margin, 0 + margin, 0]
        p2 = [delta_h - margin, 0 + margin, 0]
        p3 = [delta_h - margin, np.sin(0.9 * delta_h) + 1.5 - margin, 0]
        p4 = [0 + margin, np.sin(0) + 1.5 - margin, 0]
        trapezio = Polygon(p1, p2, p3, p4, color=AS2700.X13_MARIGOLD, fill_opacity=1)
        dash_line = DashedLine(p3, p4, stroke_width=5)

        # f2
        p1 = [-delta_h + margin, 0 + margin, 0]
        p2 = [0 - margin, 0 + margin, 0]
        p3 = [0 - margin, np.sin(0) + 1.5 - margin, 0]
        p4 = [-delta_h + margin, np.sin(-0.9 * delta_h) + 1.5 - margin, 0]
        trapezio2 = Polygon(p1, p2, p3, p4, color=AS2700.X13_MARIGOLD, fill_opacity=1)
        dash_line2 = DashedLine(p3, p4, stroke_width=5)

        plot = (
            VGroup(
                axis,
                curve,
                lines,
                line,
                x_labels,
                f_labels,
                trapezio,
                dash_line,
                trapezio2,
                dash_line2,
            )
            .scale(1.0)
            .to_corner(UL)
            .shift(0.4 * UP + 0.4 * LEFT)
        )
        self.play(Write(plot[0:6]))
        self.wait()
        self.play(FadeIn(plot[6:8]))
        self.wait()

        x_0_zero = MathTex("x = 0", color=AS2700.Y12_WATTLE)
        taylor_eq = MathTex(
            "f(x) = ",
            "f_{0} + xf' + \\frac{x^{2}}{2} f'' + \\frac{x^{3}}{3!}f''' + \\cdots",
            font_size=34,
        )

        taylor_approx = VGroup(x_0_zero, taylor_eq).arrange(DOWN, buff=0.7).to_edge(UR)
        framebox = SurroundingRectangle(taylor_eq, buff=0.2, color=AS2700.R43_RED_DUST)
        self.play(Write(taylor_approx), Write(framebox))
        self.wait()

        f1 = MathTex(
            "f_{\\pm 1} \\equiv f(x \\pm h) = f_{0} \\pm hf' + \\frac{h^{2}}{2} f'' \\pm \\frac{ h^{3}}{6}f''' ",
            "+ \\mathcal{O}(h^{4})",
            font_size=35,
        )
        f2 = MathTex(
            "f_{\\pm 2} \\equiv f(x \\pm 2h) = f_{0} \\pm 2hf' + \\frac{(2h)^{2}}{2} f'' \\pm \\frac{(2h)^{3}}{2(3)}f'''",
            "+ \\mathcal{O}(h^{4})",
            font_size=35,
        )
        f_eqs = VGroup(f1, f2).arrange(DOWN, buff=0.7).to_edge(DOWN).shift(0.5 * UP)
        self.play(Write(f_eqs))
        self.wait()

        f2_new = MathTex(
            "f_{\\pm 2} \\equiv f(x \\pm 2h) = f_{0} \\pm 2hf' + 2h^{2} f'' \\pm \\frac{4h^{3}}{3}f'''",
            "+ \\mathcal{O}(h^{4})",
            font_size=35,
        ).move_to(f_eqs[1])
        self.play(Transform(f_eqs[1], f2_new))
        self.wait()
        self.play(f_eqs[1].animate.shift(12 * LEFT))
        self.wait()

        f_eqs_new = (
            MathTex(
                "f_{1} & = f_{0} + hf' + \\frac{h^{2}}{2} f'' + \\frac{h^{3}}{6}f''' + \\mathcal{O}(h^{4}) \\\\ ",
                "f_{- 1} & = f_{0} - hf' + \\frac{h^{2}}{2} f'' - \\frac{h^{3}}{6}f''' + \\mathcal{O}(h^{4})",
                font_size=35,
            )
            .move_to(f_eqs[0])
            .shift(0.5 * DOWN)
        )
        self.play(Transform(f_eqs[0], f_eqs_new))
        self.wait()
        f_eqs[0][0:1].set_color(AS2700.X13_MARIGOLD)
        self.wait()

        self.play(FadeOut(plot[6:8]))
        self.wait()

        f_eqs[0][0:1].set_color(WHITE)
        f_eqs[0][1:2].set_color(AS2700.X13_MARIGOLD)
        self.play(FadeIn(plot[8:10]))
        self.wait()


class Formula2Pts(Scene):
    def construct(self):
        # Formula 2pts forward and backward
        f_eqs = (
            MathTex(
                "f_{1} & = f_{0} + hf' + \\frac{h^{2}}{2} f'' + \\frac{h^{3}}{6}f''' + \\mathcal{O}(h^{4}) \\\\ ",
                "f_{- 1} & = f_{0} - hf' + \\frac{h^{2}}{2} f'' - \\frac{h^{3}}{6}f''' + \\mathcal{O}(h^{4})",
                font_size=35,
            )
        ).to_corner(UR)
        forward_framebox = SurroundingRectangle(
            f_eqs[0][0:8], buff=0.25, color=AS2700.G22_SERPENTINE
        )
        forward_text = (
            Text(
                "Formula 2 pts: forward",
                font_size=35,
            )
            .set_color_by_gradient(
                AS2700.B22_HOMEBUSH_BLUE, AS2700.B33_MIST_BLUE, AS2700.B21_ULTRAMARINE
            )
            .to_corner(UL)
        )
        forward_eq = MathTex(
            "f_{+}' = \\frac{f_{1} - f_{0}}{h} + \\mathcal{O}(h)", font_size=40
        ).next_to(forward_text, DOWN)

        self.play(Write(f_eqs))
        self.wait()
        self.play(Write(forward_framebox), FadeIn(forward_text))
        self.play(FadeIn(forward_eq), run_time=0.3)
        self.wait()

        self.play(forward_framebox.animate.shift(0.99 * DOWN))
        backward_text = (
            Text("Formula 2 pts: backward", font_size=35)
            .set_color_by_gradient(
                AS2700.B22_HOMEBUSH_BLUE, AS2700.B33_MIST_BLUE, AS2700.B21_ULTRAMARINE
            )
            .next_to(forward_eq, DOWN)
        )
        backward_eq = MathTex(
            "f_{-}' = \\frac{f_{0} - f_{-1}}{h} + \\mathcal{O}(h)", font_size=40
        ).next_to(backward_text, DOWN)

        self.play(FadeIn(backward_text), FadeIn(backward_eq), run_time=0.3)
        self.wait()
        self.remove(forward_framebox)
        self.wait()

        axis = ParametricFunction(
            lambda t: [t, 0, 0], t_range=[-1.1 * PI, 1.1 * PI, 0.1], stroke_width=5
        )
        curve = ParametricFunction(
            lambda t: [t, np.sin(0.9 * t) + 1.5, 0],
            t_range=[-PI, PI, 0.01],
            stroke_width=5,
        )
        curve = CurvesAsSubmobjects(curve)
        curve.set_color_by_gradient(AS2700.B41_BLUEBELL, AS2700.G22_SERPENTINE)

        lines = VGroup()
        x_labels = VGroup()
        f_labels = VGroup()
        for i in range(-2, 3):
            dx = i * PI / 2.0
            line = Line(
                [dx, -0.2, 0],
                [dx, np.sin(0.9 * dx) + 1.5, 0],
                color=AS2700.R11_INTERNATIONAL_ORANGE,
                stroke_width=2,
            )
            x_label = MathTex(f"x_{{{i}}}").next_to(line, DOWN)
            f_label = MathTex(f"f_{{{i}}}").next_to(line, UP)
            lines.add(line)
            x_labels.add(x_label)
            f_labels.add(f_label)
        delta_h = PI / 2.0
        margin = 0.04
        # f1
        p1 = [0 + margin, 0 + margin, 0]
        p2 = [delta_h - margin, 0 + margin, 0]
        p3 = [delta_h - margin, np.sin(0.9 * delta_h) + 1.5 - margin, 0]
        p4 = [0 + margin, np.sin(0) + 1.5 - margin, 0]
        trapezio = Polygon(p1, p2, p3, p4, color=GREEN_D, fill_opacity=1)

        sec_x0 = [0 - 0.5, 1.5 + -0.5 * ((np.sin(0.9 * delta_h)) / delta_h), 0]
        sec_x1 = [
            delta_h + 0.7,
            1.5 + (delta_h + 0.7) * ((np.sin(0.9 * delta_h)) / delta_h),
            0,
        ]
        sec_line_forward = Line(
            sec_x0, sec_x1, stroke_width=5, color=AS2700.Y13_VIVID_YELLOW
        )
        sec_line_forward_label = (
            MathTex("f_{+}'", font_size=35, color=AS2700.Y13_VIVID_YELLOW)
            .next_to(sec_line_forward, UR)
            .shift(0.5 * DOWN)
        )

        # f2
        p1 = [-delta_h + margin, 0 + margin, 0]
        p2 = [0 - margin, 0 + margin, 0]
        p3 = [0 - margin, np.sin(0) + 1.5 - margin, 0]
        p4 = [-delta_h + margin, np.sin(-0.9 * delta_h) + 1.5 - margin, 0]
        trapezio2 = Polygon(p1, p2, p3, p4, color=AS2700.X13_MARIGOLD, fill_opacity=1)

        sec_x0 = [
            -delta_h - 0.5,
            1.5 + (-delta_h - 0.5) * ((np.sin(0.9 * delta_h)) / delta_h),
            0,
        ]
        sec_x1 = [
            0.7,
            1.5 + (0.7) * ((np.sin(0.9 * delta_h)) / delta_h),
            0,
        ]
        sec_line_backward = Line(
            sec_x0, sec_x1, stroke_width=5, color=AS2700.P21_SUNSET_PINK
        )
        sec_line_backward_label = (
            MathTex("f_{-}'", font_size=35, color=AS2700.P21_SUNSET_PINK)
            .next_to(sec_line_backward, DL)
            .shift(0.55 * UP)
        )

        sec_x0 = [-1.4, 1.5 + (-1.4) * 0.9, 0]
        sec_x1 = [
            1.3,
            1.5 + (1.3) * 0.9,
            0,
        ]
        f_prime_exact = Line(sec_x0, sec_x1, stroke_width=5, color=MAROON_E)
        f_prime_exact_label = (
            Text("Exact", font_size=25, color=MAROON)
            .next_to(f_prime_exact, UR)
            .shift(1.3 * LEFT + 0.3 * DOWN)
        )

        plot = (
            VGroup(
                lines,
                line,
                axis,
                curve,
                x_labels,
                f_labels,
                trapezio,
                sec_line_forward,
                sec_line_forward_label,
                trapezio2,
                sec_line_backward,
                sec_line_backward_label,
                f_prime_exact,
                f_prime_exact_label,
            )
            .scale(1.3)
            .to_corner(DR)
            .shift(0.0 * UP + 0.0 * RIGHT)
        )
        self.play(Write(plot[0:6]))
        self.wait()

        self.play(Write(plot[6:9]))
        self.wait()

        self.play(FadeOut(plot[6]))
        self.play(Write(plot[9:12]))
        self.wait()

        self.play(FadeOut(plot[9]))
        self.play(Write(plot[12:14]))
        # self.add(plot[9:14])

        self.wait()


class Flowchart(Scene):
    def construct(self):
        ## Box 1
        title = Text("Flowcharts", weight="BOLD", font="DejaVu Sans").to_edge(UP)
        self.add(title)
        self.wait()

        subsection = (
            VGroup(
                Text(
                    "From function", font="DejaVu Sans", weight="BOLD", font_size=25
                ).set_color_by_gradient(RED_E, AS2700.R32_APPLE_BLOSSOM, RED_E),
                Text(
                    "From datafile", font="DejaVu Sans", weight="BOLD", font_size=25
                ).set_color_by_gradient(RED_E, AS2700.R32_APPLE_BLOSSOM, RED_E),
                Text(
                    "From array", font="DejaVu Sans", weight="BOLD", font_size=25
                ).set_color_by_gradient(RED_E, AS2700.R32_APPLE_BLOSSOM, RED_E),
            )
            .arrange(RIGHT, buff=2.9)
            .next_to(title, DOWN)
        )
        self.play(Write(subsection[0]), Write(subsection[1]), Write(subsection[2]))

        # From function
        flowchart_function = (
            VGroup(
                MathTex("f(x), h, x", font_size=30),
                MathTex("f' = \\frac{f(x + h) - f(x)}{h}", font_size=30),
                Text("Result", font_size=30),
            )
            .arrange(DOWN, buff=1.5)
            .next_to(subsection[0], 2 * DOWN)
        )

        boxes_function = VGroup()
        for i in range(len(flowchart_function)):
            color_box = GREEN_A
            fill_color = GREEN_E
            if i == 1:
                color_box = MAROON_A
                fill_color = MAROON_E
            box = SurroundingRectangle(
                flowchart_function[i],
                corner_radius=0.2,
                color=color_box,
                fill_color=fill_color,
                fill_opacity=1,
                buff=0.3,
            )
            boxes_function.add(box)

        self.play(FadeIn(boxes_function[0]), FadeIn(flowchart_function[0]))
        self.wait()

        # Criar uma seta que liga os dois blocos
        arrows = VGroup()
        for i in range(0, len(flowchart_function) - 1):
            arrow = Arrow(
                boxes_function[i].get_bottom(),
                boxes_function[i + 1].get_top(),
                buff=0.01,
                color=AS2700.X11_BUTTERSCOTCH,
            )
            arrows.add(arrow)
        for i in 1, 2:
            self.play(Write(arrows[i - 1]))
            self.play(FadeIn(boxes_function[i]), FadeIn(flowchart_function[i]))
            self.wait()

        # Legend
        legend = (
            VGroup(
                Circle(0.2, color=GREEN_A, fill_color=GREEN_E, fill_opacity=1),
                Circle(
                    0.2,
                    color=MAROON_A,
                    fill_color=MAROON_E,
                    fill_opacity=1,
                ),
                Circle(
                    0.2,
                    color=GOLD_A,
                    fill_color=GOLD_E,
                    fill_opacity=1,
                ),
            )
            .arrange(direction=RIGHT, buff=1.4)
            .to_corner(DL)
            .shift(0.2 * LEFT)
        )
        legend_text = VGroup(
            Text("I/O", font="EB Garamond", font_size=25),
            Text("Process", font="EB Garamond", font_size=25),
            Text("Decision", font="EB Garamond", font_size=25),
        )
        for i in range(len(legend)):
            legend_text[i].next_to(legend[i], RIGHT)
        self.add(legend, legend_text)
        self.wait()

        # From function
        flowchart_datafile = (
            VGroup(
                Text("filename", font_size=25),
                MathTex(
                    "& \\text{read x, y} \\\\ f[i] &= y, \\ h[i] = x", font_size=30
                ),
                MathTex(
                    "f' &= \\frac{f[i] - f[i-1]}{h[i] - h[i-1]} \\\\",
                    "&\\text{write x, f'}",
                    font_size=30,
                ),
                Text("End file", font_size=25),
            )
            .arrange(DOWN, buff=1)
            .next_to(subsection[1], 2 * DOWN)
        )

        boxes_datafile = VGroup()
        for i in range(len(flowchart_datafile)):
            color_box = GREEN_A
            fill_color = GREEN_E
            if i == 1 or i == 2:
                color_box = MAROON_A
                fill_color = MAROON_E
            box = SurroundingRectangle(
                flowchart_datafile[i],
                corner_radius=0.2,
                color=color_box,
                fill_color=fill_color,
                fill_opacity=1,
                buff=0.3,
            )
            boxes_datafile.add(box)

        arrows_datafile = VGroup()
        for i in range(0, len(flowchart_datafile) - 1):
            arrow = Arrow(
                boxes_datafile[i].get_bottom(),
                boxes_datafile[i + 1].get_top(),
                buff=0.01,
                color=AS2700.X11_BUTTERSCOTCH,
                stroke_width=5,
            )
            arrows_datafile.add(arrow)

        self.play(FadeIn(boxes_datafile[0], flowchart_datafile[0]))
        self.wait()

        for i in range(1, len(flowchart_datafile)):
            self.play(Write(arrows_datafile[i - 1]))
            self.play(FadeIn(boxes_datafile[i]), FadeIn(flowchart_datafile[i]))
            self.wait()

        # From array
        flowchart_array = (
            VGroup(
                MathTex("f(x),n, dx", font_size=30),
                MathTex(
                    "f' &= \\frac{f[i+1] - f[i]}{dx} \\\\",
                    font_size=30,
                ),
                MathTex("i == n", color=BLACK),
                Text("Stop", font_size=25),
            )
            .arrange(DOWN, buff=1.25)
            .next_to(subsection[2], 2 * DOWN)
        )

        boxes_array = VGroup()
        for i in range(len(flowchart_array)):
            color_box = GREEN_A
            fill_color = GREEN_E
            if i == 1:
                color_box = MAROON_A
                fill_color = MAROON_E
            if i == 2:
                box = Circle(
                    0.8,
                    color=GOLD_A,
                    fill_color=GOLD_E,
                    fill_opacity=1,
                ).move_to(flowchart_array[i])
            else:
                box = SurroundingRectangle(
                    flowchart_array[i],
                    corner_radius=0.2,
                    color=color_box,
                    fill_color=fill_color,
                    fill_opacity=1,
                    buff=0.3,
                )
            boxes_array.add(box)

        arrows_array = VGroup()
        for i in range(0, len(flowchart_array) - 1):
            arrow = Arrow(
                boxes_array[i].get_bottom(),
                boxes_array[i + 1].get_top(),
                buff=0.01,
                color=AS2700.X11_BUTTERSCOTCH,
                stroke_width=5,
            )
            arrows_array.add(arrow)

        self.play(FadeIn(boxes_array[0], flowchart_array[0]))
        self.wait()

        for i in range(1, len(flowchart_array) - 1):
            self.play(Write(arrows_array[i - 1]))
            self.play(FadeIn(boxes_array[i]), FadeIn(flowchart_array[i]))
            self.wait()

        yes = Text("yes", font_size=25).next_to(arrows_array[2], RIGHT)
        self.add(yes)
        self.play(Write(arrows_array[2]))
        self.play(FadeIn(boxes_array[3]), FadeIn(flowchart_array[3]))
        self.wait()

        arrow_curve = CubicBezier(
            start_anchor=flowchart_array[2].get_center() - 0.8 * RIGHT,
            end_anchor=flowchart_array[1].get_center() + 1.4 * LEFT + 0.9 * DOWN,
            start_handle=flowchart_array[2].get_center()
            + 1.8 * LEFT
            + 0.1 * DOWN,  # Adjust control points for
            end_handle=flowchart_array[1].get_center() + 1.3 * LEFT + 0.8 * DOWN,
            color=AS2700.X11_BUTTERSCOTCH,
        )  # Adjust control points for curvature
        arrow_tip = Triangle(
            stroke_width=0.5, color=AS2700.X11_BUTTERSCOTCH, fill_opacity=1
        ).scale(0.15)
        arrow_tip.move_to(arrow_curve.points[-1])  # Move to the last point of the curve
        arrow_no = VGroup(arrow_curve, arrow_tip)
        no = Text("no", font_size=25).next_to(arrow_tip, LEFT)
        self.add(no)
        self.play(Write(arrow_no))
        self.wait()


class PseudoCode(Scene):
    def construct(self):
        title = Text("Pseudocode", weight="BOLD", font="DejaVu Sans").to_edge(UP)
        self.add(title)
        self.wait()

        # Sections
        subsection = VGroup(
            Text(
                "From function", font="DejaVu Sans", weight="BOLD", font_size=25
            ).set_color_by_gradient(RED_E, AS2700.R32_APPLE_BLOSSOM, RED_E),
            Text(
                "From datafile", font="DejaVu Sans", weight="BOLD", font_size=25
            ).set_color_by_gradient(RED_E, AS2700.R32_APPLE_BLOSSOM, RED_E),
            Text(
                "From array", font="DejaVu Sans", weight="BOLD", font_size=25
            ).set_color_by_gradient(RED_E, AS2700.R32_APPLE_BLOSSOM, RED_E),
        ).next_to(title, DL)
        self.play(Write(subsection[0]))

        # funciton
        code = """Define f(x) = cos(x)
read h, x

f_prime = (f(x+h) - f(x)) / h

print f_prime
        """
        rendered_code = (
            Code(
                code=code,
                tab_width=0,
                background="window",
                language="Fortran",
                font="Monospace",
                line_spacing=0.4,
                margin=0.3,
            )
            .next_to(subsection[0], DOWN)
            .shift(RIGHT)
        )
        self.play(Write(rendered_code))
        self.wait(2)

        # dataile
        code2 = """read datafile_name
open datafile, newDatafile
i = 0

loop while
    read(datafile) x, y
    f[i] = y
    h[i] = x
    i = i + 1
    if i == 2
        f_prime = (f[1] - f[0]) / (h[1] - h[0])
        write(newDataFile) h[1], f_prime
        f[0] = f[1]
        h[0] = h[1]
        i = 2
    end if
    if end datafile
        stop
    end if
end loop
        """
        rendered_code2 = (
            Code(
                code=code2,
                tab_width=0,
                background="window",
                language="Fortran",
                font="Monospace",
                line_spacing=0.4,
                margin=0.3,
                font_size=15,
            )
            .next_to(subsection[1], DOWN)
            .shift(RIGHT)
        )
        self.play(
            subsection[0].animate.shift(9*LEFT),
            rendered_code.animate.shift(9*LEFT),
        )
        self.play(FadeIn(subsection[1]), FadeIn(rendered_code2))
        self.wait(2)

        # Array
        self.play(
            subsection[1].animate.shift(9*LEFT),
            rendered_code2.animate.shift(9*LEFT),
        )
        code3 = """Define f(x) = cos(x)
read n, dx

loop i = 1, n - 1
    f_prime[i] = (f[i+1] - f[i]) / dx
end loop
        """
        rendered_code3 = (
            Code(
                code=code3,
                tab_width=0,
                background="window",
                language="Fortran",
                font="Monospace",
                line_spacing=0.4,
                margin=0.3,
            )
            .next_to(subsection[2], DOWN)
            .shift(2*RIGHT)
        )
        self.play(FadeIn(subsection[2]), FadeIn(rendered_code3))
        self.wait(2)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS} {SCENE}")
