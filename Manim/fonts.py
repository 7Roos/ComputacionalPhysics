from manim import *  # or: from manimlib import *

# from manim_slides import Slide
from pathlib import Path
import os
from manim import AS2700  # Padrão australiano de cores
import manimpango  ## list fonts

# python3 file.py

# Flags:
# -q  quality: low(l), medium(m) and high(h),e.g, ql low quality
# --flush_cache     Remove cached partial movie files
# -s                save last frame

FLAGS = f"-s -qh"
SCENE = "Cover"
CLEAN = "--flush_cache  "

class Cover(Scene):
    def construct(self):
        # Intro
        question = Text(
            "What if we test all 496 \n fonts available in MANIM?",
            weight=BOLD,
            color=AS2700.X41_BUFF,
        ).shift(UP)
        letgo = (
            Text("LET'S GO!", weight=BOLD, color=AS2700.X41_BUFF)
            .next_to(question, 2 * DOWN)
            .scale(2)
        )
        self.add(question, letgo)

class Fonts(Scene):
    def construct(self):

        # Intro
        question = Text(
            "What if we test all 496 \n fonts available in MANIM?",
            weight=BOLD,
            color=AS2700.X41_BUFF,
        ).shift(UP)
        letgo = (
            Text("LET'S GO!", weight=BOLD, color=AS2700.X41_BUFF)
            .next_to(question, 2 * DOWN)
            .scale(2)
        )
        self.add(question)
        self.wait()
        self.play(FadeIn(letgo))
        self.wait(0.1)
        self.remove(question, letgo)
        self.wait()

        list_font = manimpango.list_fonts()

        lorem_latin = "'Lorem: ipsão - dólor (sit) amêt, cossectetur; à piscing. Elit!'"
        lorem = "'Lorem ipsum dolor ssit amett, consecur adipiscing elit. Sed do.'"
        math_example = "0123456789 +1-2/3*4,5.6=7<8{9*0[1] f(x), g(x, y)=|x-y|"

        slants = [NORMAL, ITALIC, OBLIQUE]
        wheights = [
            THIN,
            ULTRALIGHT,
            LIGHT,
            BOOK,
            NORMAL,
            MEDIUM,
            SEMIBOLD,
            BOLD,
            ULTRABOLD,
            HEAVY,
            ULTRAHEAVY,
        ]

        iter = 0
        item = 0
        fonts_in_screen = 5

        # Percorremos a lista de fontes
        while item < 495:
            item = iter * fonts_in_screen

            # Evitamos sair do range
            if item + fonts_in_screen > len(list_font) - 1:
                fonts_in_screen = len(list_font) - item

            # Imprimos o nome das fontes
            partial_fonts = VGroup()
            for i in range(fonts_in_screen):
                font = Text(list_font[item + i], font_size=30)
                partial_fonts.add(font)
            partial_fonts.arrange(DOWN, buff=1, aligned_edge=LEFT).to_corner(UL)

            self.add(partial_fonts)
            self.wait(0.1)

            for j in range(len(slants)):
                slant = Text(slants[j], color=YELLOW).to_corner(UR)
                self.add(slant)

                list_lorem_latin = VGroup()
                for i in range(fonts_in_screen):
                    frase = Text(
                        lorem_latin,
                        font=list_font[item + i],
                        font_size=30,
                        slant=slants[j],
                        color=AS2700.X41_BUFF,
                    ).next_to(partial_fonts[i], DOWN, aligned_edge=LEFT)
                    list_lorem_latin.add(frase)
                self.add(list_lorem_latin)
                self.wait(2)

                self.remove(list_lorem_latin, slant)

            for j in range(len(wheights)):
                weight = Text(wheights[j], color=ORANGE).to_corner(UR)
                self.add(weight)

                list_lorem = VGroup()
                for i in range(fonts_in_screen):
                    frase = Text(
                        lorem,
                        font=list_font[item + i],
                        font_size=30,
                        weight=wheights[j],
                        color=AS2700.X41_BUFF,
                    ).next_to(partial_fonts[i], DOWN, aligned_edge=LEFT)
                    list_lorem.add(frase)
                self.add(list_lorem)
                self.wait()

                self.remove(list_lorem, weight)

            list_math_example = VGroup()
            for i in range(fonts_in_screen):
                math = Text(
                    math_example,
                    font=list_font[item + i],
                    font_size=30,
                    color=AS2700.X41_BUFF,
                ).next_to(partial_fonts[i], DOWN, aligned_edge=LEFT)
                list_math_example.add(math)
            self.add(list_math_example)
            self.wait(2)

            self.remove(list_math_example, partial_fonts)
            self.wait(0.1)

            # self.remove(item_text)
            iter = iter + 1


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS} {SCENE}")
