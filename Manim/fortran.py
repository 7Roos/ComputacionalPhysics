from manim import *
from pathlib import Path
import os

# Flags:
# -q  quality: low(l), medium(m) and high(h),e.g, ql low quality
# --flush_cache     Remove cached partial movie files
# -s                save last frame

FLAGS = f"-qh"
SCENE = "FortranNameOrigin"
CLEAN = "--flush_cache  "


class FortranNameOrigin(Scene):
    def construct(self):
        # Create the full name "formula Translator"
        full_name = Text("FORMULA TRANSLATOR", font_size=72).shift(UP)

        # Create the contracted name "FORTRAN"
        fortran = Text("FORTRAN", font_size=72, color=BLUE).shift(UP)

        # Display the full name
        self.play(Write(full_name))
        self.wait(1)

        # Highlight the parts that form FORTRAN
        formula = full_name[0:3].copy().set_color(BLUE)
        tra = full_name[7:11].copy().set_color(BLUE)

        # Highlight the relevant letters
        self.play(
            AnimationGroup(
                full_name[0:3].animate.set_color(BLUE),
                full_name[7:11].animate.set_color(BLUE),
                lag_ratio=0.5,
            )
        )
        self.wait(1)

        # Create a copy of the highlighted parts
        formula_copy = formula.copy()
        tra_copy = tra.copy()

        # Move the copies to form FORTRAN
        # Fade out nas síbalas descartadas na sigla
        self.play(FadeOut(full_name[3:7]), FadeOut(full_name[11:]))
        self.wait(0.5)
        self.play(
            full_name[0:3].animate.move_to(fortran[0:3]),
            full_name[7:11].animate.move_to(fortran[3:]),
        )
        self.wait(1)

        # Add a subtitle explaining the significance
        subtitle = Text(
            "First high-level programming language (1957)", font_size=36, color=YELLOW
        ).next_to(fortran, DOWN, buff=0.5)

        # Show a brief explanation
        self.play(Write(subtitle))

        # Show additional context
        context = (
            VGroup(
                Text(
                    "• Designed for scientific calculations", font_size=30, color=WHITE
                ),
                Text(
                    "• Created by IBM for formula translation",
                    font_size=30,
                    color=WHITE,
                ),
                Text(
                    "• Still in use for numerical computation",
                    font_size=30,
                    color=WHITE,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(subtitle, DOWN, buff=0.5)
        )

        self.play(Write(context), run_time=2)
        self.wait(2)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS} {SCENE}")
