from manim import *  # or: from manimlib import *

# from manim_slides import Slide
from pathlib import Path
import os
from manim import AS2700  # Padrão australiano de cores

FLAGS = f" -qm"
SCENE = "Table1"
CLEAN = "--flush_cache  "


class RoadMap(Scene):
    def construct(self):
        title = Title("Roadmap", width=40)
        self.play(Write(title))
        self.wait()

        list = BulletedList(
            "Data file",
            "Script .gnu",
            "Sintaxe Gnuplot for logical operators",
            "Plot with logical operators.",
            color=AS2700.Y11_CANARY,
        ).to_edge(LEFT)

        for i in range(len(list)):
            self.play(Write(list[i]))
        self.wait()


class Table1(Scene):
    def construct(self):
        title = Title("Operador unário", width=60)
        self.add(title)
        self.wait()

        operators = (
            VGroup(
                Text("Token", font_size=25, weight=BOLD),
                Text("Example", font_size=25, weight=BOLD),
                Text("Explain", font_size=25, weight=BOLD),
                Text("-", font_size=25),
                Text("-a = -3", font_size=25),
                Text("Overturned", font_size=25),
                Text("+", font_size=50),
                Text("+a = 3", font_size=25),
                Text("Neutral", font_size=25),
                Text("!", font_size=25),
                Text("!a = F", font_size=25),
                Text("Neg logical(here, a=T)", font_size=25),
                Text("!", font_size=25),
                Text("a! = 6", font_size=25),
                Text("factorial", font_size=25),
                Text("$", font_size=25),
                Text("$1", font_size=25),
                Text("Select col.1 durante uma manipulação 'using'", font_size=25),
            )
            .arrange_in_grid(rows=6, aligned_edge=LEFT, buff=0.5)
            .set_color(AS2700.Y12_WATTLE)
        )
        self.play(Write(operators))
        self.wait()

        self.play(
            FadeToColor(operators[3], GREEN),
            FadeToColor(operators[4], GREEN),
            FadeToColor(operators[5], GREEN),
            ratio_delay=1
        )
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS} {SCENE}")
