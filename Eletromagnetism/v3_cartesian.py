from manim import *  # or: from manimlib import *
from pathlib import Path
import os
from manim import AS2700

# Flags:
# -q  quality: low(l), medium(m) and high(h),e.g, ql low quality

# --flush_cache                  Remove cached partial movie files

FLAGS = f"-ql"
SCENE = "Unidimensional"


class Unidimensional(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        numberplane = NumberPlane()
        origin_text = MathTex("\\mathcal{O}").next_to(dot, DL)
        tip_text = MathTex("x", color=AS2700.Y13_VIVID_YELLOW, font_size=40).move_to(
            [5.9, 0.4, 0]
        )
        limit_inf = MathTex("-\\infty", color=AS2700.Y13_VIVID_YELLOW).move_to(
            [-6, -0.4, 0]
        )
        limit_sup = MathTex("+\\infty", color=AS2700.Y13_VIVID_YELLOW).move_to(
            [6, -0.4, 0]
        )

        self.add(numberplane, dot, origin_text, tip_text, limit_inf, limit_sup)

        versorA = Arrow(ORIGIN, [1, 0, 0], buff=0, color=AS2700.G31_VERTIGRIS)
        versorA_label = MathTex("\\hat{x}", font_size=40).next_to(
            versorA.get_center(), UP
        )

        vectorA = Arrow(ORIGIN, [3, 0, 0], buff=0, color=AS2700.R12_SCARLET)
        vectorA_label = MathTex(
            "\\vec{A} = a\\hat{x}", font_size=45, color=AS2700.R12_SCARLET
        ).next_to(vectorA.get_center(), UP)
        self.add(versorA, versorA_label, vectorA, vectorA_label)

        vectorB = Arrow(ORIGIN, [2, 0, 0], buff=0, color=AS2700.G56_SAGE_GREEN)
        vectorB_label = MathTex(
            "\\vec{B} = b\\hat{x}", font_size=45, color=AS2700.G56_SAGE_GREEN
        ).next_to(vectorB.get_center(), DOWN)
        self.add(vectorB, vectorB_label)

        add_vector = MathTex(
            "\\vec{A} + \\vec{B} &= a\\hat{x} + b\\hat{x} \\\\",
            "&= (a+b)\\hat{x} \\\\",
            "\\vec{C} &= c\\hat{x}",
        ).to_corner(UL)
        self.add(add_vector)

        vectorC = Arrow(ORIGIN, [5, 0, 0], buff=0, color=AS2700.X11_BUTTERSCOTCH)
        vectorC_label = MathTex(
            "\\vec{C} = c\\hat{x}", font_size=45, color=AS2700.X11_BUTTERSCOTCH
        ).next_to(vectorC.get_right(), DOWN)
        self.add(vectorC, vectorC_label)

        sub_vector = MathTex(
            "\\vec{A} - \\vec{B} &= a\\hat{x} - b\\hat{x} \\\\",
            "&= (a-b)\\hat{x} \\\\",
            "\\vec{C} &= c\\hat{x}",
        ).to_corner(UR)
        self.add(sub_vector)
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS}")
