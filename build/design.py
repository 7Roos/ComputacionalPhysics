from manim import *  # or: from manimlib import *

# from manim_slides import Slide
from pathlib import Path
import os
from manim import AS2700  # Padrão australiano de cores
import manimpango  ## list fonts

# import random as rn

# Create animations
# manim presentation.py
# Flags:
# -q  quality: low(l), medium(m) and high(h),e.g, ql low quality

# Convert to html
# manim-slides convert BasicExample slides.html

# --flush_cache                  Remove cached partial movie files

FLAGS = f" -qh"
SCENE = "Design"
CLEAN = "--flush_cache  "


class Design(Scene):
    def construct(self):
        title = Title("Design", width=40)
        self.play(Create(title), run_time=4)
        self.wait()
        otherOp = Group(
            Text("Makefile", color=AS2700.Y11_CANARY, weight=BOLD),
            Text("Python", color=AS2700.Y12_WATTLE, weight=BOLD),
        )
        self.play(FadeIn(otherOp[0]))
        self.wait()
        self.play(Transform(otherOp[0], otherOp[1]))
        self.wait()
        self.play(FadeOut(otherOp[0]))
        self.wait()

        parts = (
            Group(
                Text("Definition", color=AS2700.Y13_VIVID_YELLOW, weight=BOLD),
                Text("Update", color=AS2700.Y13_VIVID_YELLOW, weight=BOLD),
                Text("Choose packages and package manager", font_size=25),
                Text("Update the system", font_size=25),
                Text("Installation", color=AS2700.Y13_VIVID_YELLOW, weight=BOLD),
                Text("Configuration", color=AS2700.Y13_VIVID_YELLOW, weight=BOLD),
                Text("Install packages", font_size=25),
                Text("Config packs and install complex packs", font_size=25),
            )
            .arrange_in_grid(rows=4, aligned_edge=LEFT, buff=1)
            .shift(0.5 * DOWN)
        )

        self.play(Create(parts[0]), run_time=0.5)
        self.play(Create(parts[1]), run_time=0.5)
        self.play(Create(parts[4]), run_time=0.5)
        self.play(Create(parts[5]), run_time=0.5)
        self.wait()

        grid = Group(
            Line([-6, 0, 0], [6, 0, 0], color=GREEN, stroke_width=5),
            Line([0, -2.5, 0], [0, 2.5, 0], color=GREEN, stroke_width=5),
        ).shift(0.3 * DOWN)
        self.play(Write(grid[0]), Write(grid[1]))
        self.wait()

        self.play(Create(parts[2]))
        self.wait()
        self.play(Create(parts[3]))
        self.wait()
        self.play(Create(parts[6]))
        self.wait()
        self.play(Create(parts[7]))
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS} {SCENE}")
