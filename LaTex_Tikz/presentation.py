from manim import *  # or: from manimlib import *

# from manim_slides import Slide
from pathlib import Path
import os
from manim import AS2700  # Padrão australiano de cores

FLAGS = f"-qh"
SCENE = "Intro"
CLEAN = "--flush_cache  "


class Intro(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(orange_square)
        self.play(ReplacementTransform(orange_square, blue_circle, run_time=3))
        self.play(blue_circle.animate.shift(RIGHT))
        self.wait()
        self.play(FadeOut(blue_circle))

        vector = Arrow(ORIGIN, 2 * RIGHT, buff=0)
        vector2 = Arrow(ORIGIN, 2 * UP, buff=0)
        labels = VGroup(
            MathTex("\\vec{E}").next_to(vector, RIGHT),
            MathTex("\\vec{B}").next_to(vector2, UP),
        )
        vectors = VGroup(vector, vector2, labels)
        self.play(Write(vectors), run_time=3)
        self.play(
            Rotate(
                vectors,
                angle=0.3 * PI,
                about_point=ORIGIN,
                rate_func=linear,
            )
        )
        self.wait()
        self.play(FadeOut(vectors))

        t0 = Table(
            [["Inkscape"], ["Paint"]],
            row_labels=[Text("LaTex"), Text("Manim")],
            col_labels=[Text("non-programmable")],
            top_left_entry=Text("programmable"),
        )
        self.play(Create(t0), run_time=3)
        t0.add_highlighted_cell((2, 1), color=GREEN)
        self.wait()
        self.play(t0.animate.shift(15 * LEFT))

        title = (
            Text("Advantages", weight=BOLD)
            .to_edge(UP)
            .set_color_by_gradient(RED, GREEN)
        )
        self.play(FadeIn(title))
        list = BulletedList(
            "exactly positions",
            "highly scalable",
            "cooperative AI",
            "LMM coupling",
            color=AS2700.Y16_INCA_GOLD,
        ).to_edge(LEFT)
        for i in range(len(list)):
            self.play(Write(list[i]))
            self.wait()

        self.wait()
        self.play(list.animate.shift(10 * UP), title.animate.shift(5 * UP))
        self.remove(list)
        title = (
            Text("LaTex", weight=BOLD)
            .to_edge(UP)
            .set_color_by_gradient(RED, GREEN)
            .shift(LEFT)
        )
        self.play(FadeIn(title))
        list = BulletedList(
            "Cartesian coordinates",
            "define variables and parameters",
            "loops and logical conditions",
            "LaTex mathematical environment",
            "export to PDF",
            color=AS2700.Y16_INCA_GOLD,
        ).to_edge(LEFT)
        for i in range(len(list)):
            self.play(Write(list[i]))
            self.wait()

        self.wait()

        pgf = Text("PGF", color=AS2700.X41_BUFF).next_to(title, RIGHT).shift(RIGHT)
        tikz = Text("Tikz", color=AS2700.X41_BUFF).next_to(pgf, DOWN).shift(DOWN)
        pgfplots = (
            Text("pgfplots", color=AS2700.X41_BUFF).next_to(pgf, RIGHT).shift(RIGHT)
        )
        pgf_arrow = Arrow(title.get_right(), pgf.get_left())
        tikz_arrow = Arrow(pgf.get_bottom(), tikz.get_top())
        pgfplots_arrow = Arrow(pgf.get_right(), pgfplots.get_left())
        self.play(Write(pgf), Write(pgf_arrow))
        self.wait()
        self.play(Write(tikz), Write(tikz_arrow))
        self.wait()
        self.play(Write(pgfplots), Write(pgfplots_arrow))
        self.wait()

        self.play(
            FadeOut(title),
            FadeOut(pgf),
            FadeOut(pgf_arrow),
            FadeOut(list),
            FadeOut(tikz),
            FadeOut(tikz_arrow),
            FadeOut(pgfplots),
            FadeOut(pgfplots_arrow),
        )
        self.wait()

        lattice = ImageMobject("latticeSpins.png").to_edge(RIGHT).shift(5 * RIGHT)
        self.add(lattice)
        self.play(lattice.animate.shift(7 * LEFT))
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS} {SCENE}")
