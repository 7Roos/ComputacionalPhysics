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

FLAGS = f"-qh"
SCENE = "Symmetry"


class Motivation(Scene):
    def construct(self):
        ########### Change background ###########
        self.camera.background_color = AS2700.G61_DARK_GREEN

        ########### Cover ###########
        title = Text(
            "The physics and mathematics: Vectors",
            font="GFS Complutum",
            weight=BOLD,
            font_size=40,
        ).to_edge(UP)
        subtitle = (
            Text(
                '"Physics, is more mathematics than physics!"',
                font="GFS Complutum",
                slant=ITALIC,
                font_size=30,
                color=YELLOW,
            )
            .next_to(title, DOWN)
            .shift(2 * LEFT + 0.5 * DOWN)
        )
        self.add(title, subtitle)
        self.wait(2)

        # Define the rectangle dimensions
        width = 7
        height = width / 2

        # Add the sections to the rectangle group
        rectangle_group = (
            VGroup(
                Rectangle(width=width / 5, height=height, color=BLACK),
                Rectangle(width=3 * width / 5, height=height, color=BLACK),
                Rectangle(width=width / 5, height=height, color=BLACK),
            )
            .arrange(buff=0)
            .shift(0.5 * LEFT + DOWN)
        )

        text1 = Paragraph(
            "Physics: \npropose \nthe model",
            font="C059",
            font_size=35,
            weight=SEMIBOLD,
            alignment="right",
        ).next_to(rectangle_group[0], LEFT)
        text2 = Paragraph(
            "Mathematics and \ncomputing:" "\nobtaining \nthe results",
            font="Amiri",
            font_size=35,
            weight=SEMIBOLD,
            alignment="center",
        ).next_to(rectangle_group[1], ORIGIN)
        text3 = Paragraph(
            "Physics: \ninterpretation \nof results",
            font="C059",
            font_size=35,
            weight=SEMIBOLD,
        ).next_to(rectangle_group[2], RIGHT)

        # Add the rectangle group to the scene
        self.add(rectangle_group)
        self.wait()
        self.add(text1)
        self.play(rectangle_group[0].animate.set_fill(RED, 0.8))
        self.wait()
        self.add(text2)
        self.play(rectangle_group[1].animate.set_fill(DARK_BLUE, 0.8))
        self.wait()
        self.add(text3)
        self.play(rectangle_group[2].animate.set_fill(RED, 0.8))
        self.wait()


class Intro(Scene):
    def construct(self):
        ########### Change background ###########
        self.camera.background_color = AS2700.G61_DARK_GREEN
        self.wait()

        title2 = Text(
            "Physical quantities", font="GFS Complutum", weight=BOLD, font_size=40
        ).to_edge(UP)
        subtitle2 = (
            Text(
                "Scalars",
                font="GFS Complutum",
                weight=BOLD,
                font_size=30,
                color=AS2700.B34_PARADISE_BLUE,
            )
            .to_edge(LEFT)
            .shift(2.5 * UP)
        )
        self.add(title2, subtitle2)
        self.wait()

        mass = VGroup(
            Square(fill_color="#925629", fill_opacity=1),
            MathTex("m = 2 \\ Kg", font_size=40),
        )

        # Define the dimensions of the thermometer
        tube_width = 0.2
        tube_height = 3
        bulb_radius = 0.3
        scale_length = 6
        scale_ticks = 5

        # Create the thermometer tube
        tube = RoundedRectangle(
            width=tube_width, height=tube_height, color=GRAY, corner_radius=0.1
        )

        # Create the thermometer bulb
        bulb = Circle(
            radius=bulb_radius, color="#CE482A", fill_color="#CE482A", fill_opacity=1
        )

        # Position the bulb at the bottom of the tube
        bulb.next_to(tube.get_corner(DOWN), ORIGIN)

        # Create the scale ticks
        scale_ticks_group = VGroup()
        for i in range(1, scale_ticks + 1):
            tick_height = scale_length / scale_ticks
            tick_position = (0, tick_height * i, 0)
            tick = Line([0, 0, 0], [0.2, 0, 0], color=GRAY)
            tick.to_corner(tick_position)
            scale_ticks_group.add(tick)

        # Position the scale to the right of the tube
        scale_ticks_group.next_to(tube, ORIGIN)
        line_temp = Line([0, -1.2, 0], [0, 0.9, 0], color="#CE482A")
        temp = MathTex("T = 35^{\\circ} C").next_to(tube, RIGHT).shift(0.9 * UP)

        # Combine the thermometer parts
        thermometer = VGroup(tube, scale_ticks_group, bulb, line_temp, temp)

        charge = VGroup(
            Circle(radius=0.4, color="#858F88", fill_color="#28304D", fill_opacity=1),
            MathTex("e"),
            MathTex("q = 1.6\\times10^{-6} C").shift(UP),
        )

        examples = VGroup(mass, thermometer, charge).arrange(direction=RIGHT, buff=2)

        self.play(FadeIn(examples[0]))
        self.play(FadeIn(examples[1]))
        self.play(FadeIn(examples[2]))
        self.wait()

        subtitle = (
            Text(
                "Vectors",
                font="GFS Complutum",
                weight=BOLD,
                font_size=30,
                color=AS2700.B34_PARADISE_BLUE,
            )
            .to_edge(LEFT)
            .shift(2.5 * UP)
        )

        self.remove(examples[0], examples[1], examples[2])
        self.play(Transform(subtitle2, subtitle))
        eq = MathTex("\\vec{v} = 2 \\hat{r} \\ m/s  ").next_to(subtitle, DOWN)
        eq.shift(0.1 * RIGHT)
        self.play(Write(eq))
        self.wait()

        system2 = VGroup(
            Dot(DOWN + 0.05 * RIGHT),
            Arrow(
                1.2 * DOWN,
                UP + 0.5 * RIGHT,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.1,
            ),
            MathTex("\\mathcal{O}").next_to(DOWN, DOWN),
        ).to_edge(3 * LEFT)
        eq2 = MathTex("\\vec{r} = r \\hat{r}", color="#95B43B").next_to(system2, DOWN)
        self.play(FadeIn(system2, eq2))
        self.wait()

        system = VGroup(
            Dot(DOWN),
            Arrow(
                1.2 * DOWN + 0.15 * RIGHT,
                2 * LEFT + 1.5 * UP,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.1,
            ),
            Arrow(
                1.2 * DOWN + 0.125 * LEFT,
                RIGHT + 0.7 * UP,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.1,
            ),
            Arrow(
                1.1 * RIGHT + 0.4 * UP,
                2.1 * LEFT + 1.4 * UP,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.1,
            ),
            MathTex("\\mathcal{O}").next_to(DOWN, DOWN),
            MathTex("\\vec{C}", color=YELLOW_E).next_to(
                ORIGIN, 4.1 * LEFT + 0.1 * DOWN
            ),
            MathTex("\\vec{A}", color=YELLOW_E).next_to(ORIGIN, 2.9 * RIGHT + DOWN),
            MathTex("\\vec{B}", color=YELLOW_E).next_to(ORIGIN, 5 * UP),
        )
        system.scale(1.1).next_to(system2, 10 * RIGHT)

        eq3 = MathTex("\\vec{C} = \\vec{A} + \\vec{B}", color="#95B43B").next_to(
            system, DOWN
        )
        self.play(FadeIn(system, eq3))
        self.wait()


class OpVectorials(Scene):
    def construct(self):
        ########### Change background ###########
        self.camera.background_color = AS2700.G61_DARK_GREEN
        self.wait()

        title = Text(
            "Vector operations", font="GFS Complutum", weight=BOLD, font_size=40
        ).to_edge(UP)
        self.add(title)
        self.wait()

        subtitle = (
            VGroup(
                Text("Sum", font="GFS Complutum", weight=BOLD, font_size=23),
                Text("Subtraction", font="GFS Complutum", weight=BOLD, font_size=23),
                Text(
                    "Multiplication by a scalar",
                    font="GFS Complutum",
                    weight=BOLD,
                    font_size=23,
                ),
                Text(
                    "Division by a scalar",
                    font="GFS Complutum",
                    weight=BOLD,
                    font_size=23,
                ),
            )
            .arrange(RIGHT, buff=1)
            .to_edge(3 * UP)
        )

        self.add(subtitle[0])

        system = VGroup(
            Dot(DOWN),
            Arrow(
                1.2 * DOWN + 0.15 * RIGHT,
                2 * LEFT + 1.5 * UP,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.1,
            ),
            Arrow(
                1.2 * DOWN + 0.125 * LEFT,
                RIGHT + 0.7 * UP,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.1,
            ),
            Arrow(
                1.1 * RIGHT + 0.4 * UP,
                2.1 * LEFT + 1.4 * UP,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.1,
            ),
            MathTex("\\mathcal{O}").next_to(DOWN, DOWN),
            MathTex("\\vec{C}", color=YELLOW_E).next_to(
                ORIGIN, 4.1 * LEFT + 0.1 * DOWN
            ),
            MathTex("\\vec{A}", color=YELLOW_E).next_to(ORIGIN, 2.9 * RIGHT + DOWN),
            MathTex("\\vec{B}", color=YELLOW_E).next_to(ORIGIN, 5 * UP),
        ).next_to(subtitle, 2 * DOWN)
        system.scale(1.1)

        eq = MathTex("C = A + B").to_edge(2 * LEFT)
        subtitle[0].set_color(color="YELLOW")
        self.play(Write(eq), Write(system))
        self.wait(2)

        minus_b_vec = Arrow(
            1.8 * LEFT + 1.35 * UP,
            1.6 * RIGHT + 0.3 * UP,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.1,
        )
        minus_b = MathTex("-\\vec{B}", color=YELLOW_E).next_to(ORIGIN, 5 * UP)
        c_to_d = MathTex("\\vec{D}", color=YELLOW_E).next_to(
            ORIGIN, 4.1 * LEFT + 0.1 * DOWN
        )

        eq2 = MathTex("D = A - B").to_edge(2 * LEFT)

        subtitle[0].set_color(color="WHITE")
        self.add(subtitle[1])
        subtitle[1].set_color(color="YELLOW")
        self.wait()

        self.play(Transform(system[3], minus_b_vec))
        self.play(Transform(system[7], minus_b))
        self.play(TransformMatchingTex(system[5], c_to_d))
        self.play(TransformMatchingTex(eq, eq2))
        self.wait()

        subtitle[1].set_color(color="WHITE")
        self.add(subtitle[2])
        subtitle[2].set_color(color="YELLOW")
        self.wait()

        self.remove(
            system[0],
            system[1],
            system[2],
            system[3],
            system[4],
            system[5],
            system[6],
            system[7],
            eq2,
            c_to_d,
        )
        self.wait()

        system2 = VGroup(
            Dot(DOWN + 0.05 * RIGHT),
            Arrow(
                1.2 * DOWN,
                UP + 0.5 * RIGHT,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.1,
            ),
            MathTex("\\vec{A}").next_to(DOWN, UP + RIGHT),
            MathTex("\\mathcal{O}").next_to(DOWN, DOWN),
        ).next_to(subtitle, 2 * DOWN)

        eq = MathTex("\\vec{E} = k \\vec{A}").to_edge(2 * LEFT)

        self.play(Write(eq), Write(system2))
        self.wait()

        # Dilatar o vetor
        system2_expand = VGroup(
            Dot(DOWN + 0.05 * RIGHT),
            Arrow(
                1.2 * DOWN,
                2 * (UP + 0.5 * RIGHT),
                stroke_width=4,
                max_tip_length_to_length_ratio=0.1,
            ),
            MathTex("k\\vec{A}").next_to(DOWN, 2 * (UP + RIGHT)),
            MathTex("\\mathcal{O}").next_to(DOWN, DOWN),
        ).next_to(subtitle, 2 * DOWN)

        self.play(Transform(system2, system2_expand))
        self.wait()

        # Divisão por um escalar
        subtitle[2].set_color(color="WHITE")
        self.add(subtitle[3])
        subtitle[3].set_color(color="YELLOW")
        self.wait()

        eq2 = MathTex("\\vec{E} = \\frac{\\vec{A}}{k}").to_edge(2 * LEFT)

        self.play(Transform(eq, eq2))
        self.wait()

        divide_vec_by_k = VGroup(
            Dot(DOWN + 0.05 * RIGHT),
            Arrow(
                1.2 * DOWN,
                2 * (UP + 0.5 * RIGHT),
                stroke_width=4,
                max_tip_length_to_length_ratio=0.1,
            ),
            MathTex("\\frac{\\vec{A}}{k}").next_to(DOWN, 2 * (UP + RIGHT)),
            MathTex("\\mathcal{O}").next_to(DOWN, DOWN),
        ).next_to(subtitle, 2 * DOWN)

        self.play(Transform(system2, divide_vec_by_k))
        self.wait()

        # versor
        k_equal_one = MathTex("\\vec{E} = \\frac{\\vec{A}}{A}").to_edge(2 * LEFT)
        versor = VGroup(
            Dot(DOWN + 0.05 * RIGHT),
            Arrow(
                1.2 * DOWN,
                (UP + 0.5 * RIGHT),
                stroke_width=4,
                max_tip_length_to_length_ratio=0.1,
            ),
            MathTex("\\frac{\\vec{A}}{A}").next_to(DOWN, 2 * (0.5 * UP + RIGHT)),
            MathTex("\\mathcal{O}").next_to(DOWN, DOWN),
        ).next_to(subtitle, 2 * DOWN)

        self.play(Transform(eq, k_equal_one))
        self.play(Transform(system2, versor))
        versor_eq = MathTex("\\hat{A} = \\frac{\\vec{A}}{A}").next_to(eq, ORIGIN)
        self.play(Transform(eq, versor_eq))
        self.wait()

        versor_text = Text(
            "versor or unit vector",
            font="GFS Didot",
            font_size=30,
            color=AS2700.B34_PARADISE_BLUE,
        ).next_to(eq, DOWN + 0.5 * RIGHT)

        self.add(versor_text)
        self.wait()


class DotProduct(Scene):
    def construct(self):
        ########### Change background ###########
        self.camera.background_color = AS2700.G61_DARK_GREEN
        self.wait()

        subtitle = Text(
            "Dot product",
            font="GFS Complutum",
            weight=BOLD,
            font_size=25,
            color=AS2700.Y11_CANARY,
        ).to_edge(UP)
        self.add(subtitle)
        self.wait()

        vec_a = Arrow(ORIGIN, [2, 2, 0], buff=0, color=AS2700.T11_TROPICAL_BLUE)
        vec_b = Arrow(ORIGIN, [3, 0, 0], buff=0, color=AS2700.R54_RASPBERRY)
        angle = Angle(vec_b, vec_a, radius=0.5, other_angle=False)

        decomp_vec_a = Brace(vec_a)
        label_decomp_vec_a = MathTex("A\\cos \\theta").next_to(decomp_vec_a, DOWN)
        dashed = DashedLine([2, 0.1, 0], [2, 2, 0])

        system = VGroup(
            vec_a,
            vec_b,
            angle,
            MathTex("\\theta").next_to(angle, 0.5 * RIGHT).shift(0.15 * UP),
            MathTex("\\vec{A}").next_to(vec_a, ORIGIN).shift(0.5 * LEFT),
            MathTex("\\vec{B}").next_to(vec_b, 0.1 * DOWN).shift(0.9 * RIGHT),
            MathTex("\\mathcal{O}").next_to(ORIGIN, 0.5 * LEFT),
            decomp_vec_a,
            label_decomp_vec_a,
            dashed,
        ).to_edge(LEFT)
        self.add(system[0:6])
        self.wait()

        eq = (
            MathTex("\\vec{A}\\cdot\\vec{B} = AB\\cos\\theta")
            .set_color(AS2700.X13_MARIGOLD)
            .next_to(system, 2 * DOWN)
        )

        self.add(system[7:])
        self.play(Write(eq))
        self.wait()

        # Properties of the dot product
        property_title = (
            Text(
                "Properties",
                font="GFS Complutum",
                weight=BOLD,
                font_size=25,
                color=AS2700.X41_BUFF,
            )
            .next_to(subtitle, DOWN)
            .shift(1.2 * LEFT)
        )

        self.add(property_title)
        self.wait()

        property = (
            VGroup(
                Text("Symmetry", font_size=25),
                MathTex(
                    "\\vec{A}\\cdot\\vec{B} = \\vec{B}\\cdot\\vec{A} ",
                    color=AS2700.Y42_MUSTARD,
                ),
                Text("Orthogonality", font_size=25),
                MathTex(
                    "\\vec{A}\\cdot\\vec{B} = 0",
                    color=AS2700.Y42_MUSTARD,
                ),
                Text("Module", font_size=25),
                MathTex(
                    "|\\vec{A}| = \\sqrt{\\vec{A}\\cdot\\vec{A}} = A",
                    color=AS2700.Y42_MUSTARD,
                ),
                Text("Direction Cosine", font_size=25),
                MathTex(
                    "\\vec{A} &= \\hat{e}_{x} (\\vec{A}\\cdot \\hat{e}_{x}) + \\hat{e}_{y} (\\vec{A}\\cdot \\hat{e}_{y}) \\\\ &= \\hat{e}_{x}A_{x} + \\hat{e}_{y}A_{y} ",
                    color=AS2700.Y42_MUSTARD,
                ),
            )
            .arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            .next_to(subtitle, 2.5 * DOWN)
            .shift(2 * RIGHT)
        )
        for i in range(0, len(property), 2):
            self.play(FadeIn(property[i]), Write(property[i + 1]))
            self.wait()


class CrossProduct(Scene):
    def construct(self):
        ########### Change background ###########
        self.camera.background_color = AS2700.G61_DARK_GREEN
        self.wait()

        subtitle = Text(
            "Cross product",
            font="GFS Complutum",
            weight=BOLD,
            font_size=25,
            color=AS2700.Y11_CANARY,
        ).to_edge(UP)
        self.add(subtitle)
        self.wait()

        axis = VGroup(
            Arrow(ORIGIN, [2, 0, 0], buff=0),
            Arrow(ORIGIN, [0, 2, 0], buff=0),
            Arrow(ORIGIN, [-1, -1, 0], buff=0),
        ).to_edge(LEFT)
        system = VGroup(
            axis,
            Angle(axis[2], axis[0], radius=0.2, other_angle=False),
            MathTex("\\theta").next_to(axis[1], ORIGIN).shift(1.5 * DOWN),
            MathTex("\\vec{A}").next_to(axis[2], ORIGIN).shift(0.5 * UP),
            MathTex("\\vec{B}").next_to(axis[0], ORIGIN).shift(0.4 * UP),
            MathTex("\\vec{C}").next_to(axis[1], ORIGIN).shift(0.3 * LEFT),
        )
        eq = (
            MathTex("\\vec{A}\\times\\vec{B} = \\vec{C} = AB\\sin\\theta \\hat{C}")
            .set_color(AS2700.X13_MARIGOLD)
            .next_to(system, 2 * DOWN)
            .shift(RIGHT)
        )
        self.play(Write(system), Write(eq))
        self.wait()

        # Properties of the cross product
        property_title = (
            Text(
                "Properties",
                font="GFS Complutum",
                weight=BOLD,
                font_size=25,
                color=AS2700.X41_BUFF,
            )
            .next_to(subtitle, DOWN)
            .shift(LEFT)
        )

        self.add(property_title)
        self.wait()

        property = (
            VGroup(
                Text("Antisymmetry", font_size=25),
                MathTex(
                    "\\vec{A}\\times\\vec{B} = - \\vec{B}\\times\\vec{A} ",
                    color=AS2700.Y42_MUSTARD,
                ),
                Text("Parallel vectors", font_size=25),
                MathTex(
                    "\\vec{A}\\times\\vec{B} = \\vec{0}",
                    color=AS2700.Y42_MUSTARD,
                ),
                Text("Orthogonal result", font_size=25),
                MathTex(
                    "\\vec{A}\\cdot(\\vec{A}\\times\\vec{B}) &= 0 = \\vec{B}\\cdot(\\vec{A}\\times\\vec{B})",
                    color=AS2700.Y42_MUSTARD,
                ),
                Text("Area", font_size=25),
                MathTex(
                    "\\text{Area} = |\\vec{A}\\times\\vec{B} | = AB\\sin\\theta",
                    color=AS2700.Y42_MUSTARD,
                ),
            )
            .arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            .next_to(subtitle, 2.5 * DOWN)
            .shift(2.2 * RIGHT)
        )
        for i in range(0, len(property), 2):
            self.play(FadeIn(property[i]), Write(property[i + 1]))
            self.wait()


class Symmetry(Scene):
    def construct(self):
        ########### Change background ###########
        self.camera.background_color = AS2700.G61_DARK_GREEN
        self.wait()

        # Symetrics
        title = Text(
            "Symmetries", font="GFS Complutum", weight=BOLD, font_size=40
        ).to_edge(UP)
        self.add(title)
        self.wait()

        subtitle = (
            Text(
                "Translation invariance",
                font="GFS Complutum",
                weight=BOLD,
                font_size=25,
                color=AS2700.Y11_CANARY,
            )
            .to_edge(LEFT)
            .shift(2.5 * UP)
        )
        self.add(subtitle)

        axis = VGroup(
            Dot(ORIGIN),
            Arrow([0, 0, 0], [1, 1, 0], buff=0),
            Arrow(stroke_width=20, max_stroke_width_to_length_ratio=10).set_color(
                AS2700.X13_MARIGOLD
            ),
            Dot([3.5, 0, 0]),
            Arrow([5, 0, 0], [6, 1, 0], buff=0),
            DashedLine([3.6, 0, 0], [5, 0, 0]).set_color(AS2700.T11_TROPICAL_BLUE),
        )
        system = (
            VGroup(
                axis[0],
                axis[1],
                axis[2].next_to(axis[1], RIGHT),
                MathTex("\\vec{r}").next_to(axis[1], ORIGIN).shift(0.5 * UP),
                MathTex("\\mathcal{O}").next_to(axis[0], ORIGIN).shift(0.4 * LEFT),
                axis[4],
                axis[3],
                MathTex("\\mathcal{O}").next_to(axis[3], ORIGIN).shift(0.4 * LEFT),
                MathTex("\\vec{r'}").next_to(axis[4], ORIGIN).shift(0.5 * UP),
                axis[5],
                MathTex("\\alpha").next_to(axis[5], ORIGIN).shift(0.2 * UP),
            )
            .next_to(subtitle, DOWN)
            .shift(1 * RIGHT)
        )

        self.play(
            Write(system[0]),
            Write(system[1]),
            Write(system[3]),
            Write(system[4]),
        )
        self.wait()
        self.play(
            Write(system[2]),
            Write(system[5]),
            Write(system[6]),
            Write(system[7]),
            Write(system[8]),
            Write(system[9]),
            Write(system[10]),
        )
        self.wait()

        eq = (
            MathTex("\\vec{r} \\equiv \\vec{r'} = \\vec{r} + \\vec{\\alpha}")
            .next_to(system, DOWN)
            .shift(DOWN)
        )
        self.add(eq)
        self.wait()

        subtitle2 = (
            Text(
                "Rotation invariance",
                font="GFS Complutum",
                weight=BOLD,
                font_size=25,
                color=AS2700.Y11_CANARY,
            )
            .to_edge(RIGHT)
            .shift(2.5 * UP + LEFT)
        )
        self.add(subtitle2)
        self.wait()

        axis2 = VGroup(
            Dot(ORIGIN),
            Arrow(ORIGIN, [1, 1, 0], buff=0),
            Arrow(ORIGIN, [-1, 1, 0], buff=0),
        )
        system2 = (
            VGroup(
                axis2[0],
                axis2[1],
                axis2[2],
                Angle(axis2[1], axis2[2]),
                MathTex("\\theta").next_to(axis2[0], UP).shift(0.1 * UP),
                MathTex("\\vec{r}")
                .next_to(axis2[1], RIGHT)
                .shift(0.5 * LEFT + 0.3 * DOWN),
                MathTex("\\vec{r'}")
                .next_to(axis2[2], LEFT)
                .shift(0.5 * RIGHT + 0.3 * DOWN),
            )
            .next_to(subtitle2, DOWN)
            .shift(0.5 * DOWN)
        )
        self.add(system2)
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS} {SCENE}")
