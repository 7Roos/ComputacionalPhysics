from manim import *  # or: from manimlib import *

# from manim_slides import Slide
from pathlib import Path
import os
from manim import AS2700  # Padrão australiano de cores

FLAGS = f" -qh"
SCENE = "Table5"
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
        title = Title("Unary operators: a = 3", width=60)
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
                Text("+", font_size=25),
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
                Text("Select col.1 during 'using' manipulation ", font_size=25),
            )
            .arrange_in_grid(rows=6, aligned_edge=LEFT, buff=0.5)
            .set_color(AS2700.Y12_WATTLE)
        )
        self.play(Write(operators))
        self.wait()

        for i in range(5):
            self.play(
                FadeToColor(operators[3 + 3 * i], GREEN),
                FadeToColor(operators[4 + 3 * i], GREEN),
                FadeToColor(operators[5 + 3 * i], GREEN),
                lag_ratio=0.9,
            )
            self.wait(2)
            self.play(
                FadeToColor(operators[3 + 3 * i], AS2700.Y12_WATTLE),
                FadeToColor(operators[4 + 3 * i], AS2700.Y12_WATTLE),
                FadeToColor(operators[5 + 3 * i], AS2700.Y12_WATTLE),
            )
            self.wait()


class Table2(Scene):
    def construct(self):
        title = Text(
            "Binary Operators (arithmetic): a=4, b=2", weight=BOLD, font_size=20
        ).to_edge(UP)
        line = Line(
            title.get_left(), title.get_right(), color=AS2700.B11_RICH_BLUE
        ).next_to(title, DOWN)
        self.add(title, line)
        self.wait()

        operators = (
            VGroup(
                Text("Token", font_size=25, weight=BOLD),
                Text("Example", font_size=25, weight=BOLD),
                Text("Explain", font_size=25, weight=BOLD),
                MathTex("+", font_size=35),
                MathTex("a+b = 6", font_size=35),
                Text("Addition", font_size=25),
                MathTex("-", font_size=35),
                MathTex("a - b = 2", font_size=35),
                Text("Subtration", font_size=25),
                MathTex("*", font_size=35),
                MathTex("a * b = 8", font_size=35),
                Text("Multiplication", font_size=25),
                MathTex("/", font_size=35),
                MathTex("a / b = 2", font_size=35),
                Text("division", font_size=25),
                MathTex("**", font_size=35),
                MathTex("a**b = 16", font_size=35),
                Text("Exponentiation", font_size=25),
                MathTex("=", font_size=35),
                MathTex("a=b; a=2, b=2", font_size=35),
                Text("Assigment", font_size=25),
            )
            .arrange_in_grid(rows=6, aligned_edge=LEFT, buff=0.5)
            .set_color(AS2700.Y12_WATTLE)
        )
        self.play(Write(operators))
        self.wait(2)


class Table3(Scene):
    def construct(self):
        title = Text(
            "Binary Operators (relational): a=4, b=2", weight=BOLD, font_size=20
        ).to_edge(UP)
        line = Line(
            title.get_left(), title.get_right(), color=AS2700.B11_RICH_BLUE
        ).next_to(title, DOWN)
        self.add(title, line)
        self.wait()

        operators = (
            VGroup(
                Text("Token", font_size=25, weight=BOLD),
                Text("Example", font_size=25, weight=BOLD),
                Text("Explain", font_size=25, weight=BOLD),
                MathTex(">", font_size=35),
                MathTex("a>b \\rightarrow T", font_size=35),
                Text("Greater than", font_size=25),
                MathTex("<", font_size=35),
                MathTex("a < b \\rightarrow F", font_size=35),
                Text("Less than", font_size=25),
                MathTex(">=", font_size=35),
                MathTex("a >= b \\rightarrow T", font_size=35),
                Text("Greater than or equal to", font_size=25),
                MathTex("<=", font_size=35),
                MathTex("a <= b \\rightarrow F", font_size=35),
                Text("Less than or equal to", font_size=25),
                MathTex("==", font_size=35),
                MathTex("a==b \\rightarrow F", font_size=35),
                Text("Equality", font_size=25),
                MathTex("!=", font_size=35),
                MathTex("a!=b \\rightarrow T", font_size=35),
                Text("Inequality", font_size=25),
            )
            .arrange_in_grid(rows=8, aligned_edge=LEFT, buff=0.5)
            .set_color(AS2700.Y12_WATTLE)
        )
        self.play(Write(operators))
        self.wait()

        for i in range(6):
            self.play(
                FadeToColor(operators[3 + 3 * i], GREEN),
                FadeToColor(operators[4 + 3 * i], GREEN),
                FadeToColor(operators[5 + 3 * i], GREEN),
                lag_ratio=0.9,
            )
            self.wait(0.5)
            self.play(
                FadeToColor(operators[3 + 3 * i], AS2700.Y12_WATTLE),
                FadeToColor(operators[4 + 3 * i], AS2700.Y12_WATTLE),
                FadeToColor(operators[5 + 3 * i], AS2700.Y12_WATTLE),
            )
            self.wait(0.5)


class Table4(Scene):
    def construct(self):
        title = Text(
            "Binary Operators (combinational): a=4, b=2", weight=BOLD, font_size=20
        ).to_edge(UP)
        line = Line(
            title.get_left(), title.get_right(), color=AS2700.B11_RICH_BLUE
        ).next_to(title, DOWN)
        self.add(title, line)
        self.wait()

        operators = (
            VGroup(
                Text("Token", font_size=25, weight=BOLD),
                Text("Example", font_size=25, weight=BOLD),
                Text("Explain", font_size=25, weight=BOLD),
                MathTex(" \\& \\& ", font_size=35),
                MathTex("a>b \\ \\&\\& \\ a>0 \\rightarrow T", font_size=35),
                Text("Logical AND", font_size=25),
                MathTex("||", font_size=35),
                MathTex("a>b \\ || \\ b>a \\rightarrow T", font_size=35),
                Text("Logical OR", font_size=25),
            )
            .arrange_in_grid(rows=3, aligned_edge=LEFT, buff=0.5)
            .set_color(AS2700.Y12_WATTLE)
            .next_to(line, DOWN)
        )
        self.play(Write(operators))
        self.wait()

        t1 = (
            Table(
                [["T", "F"], ["F", "T"]],
                row_labels=[Text("T"), Text("F")],
                col_labels=[Text("T"), Text("F")],
                top_left_entry=Text("AND", font_size=40),
            )
            .scale(0.95)
            .to_corner(DL)
        )
        t1.add_highlighted_cell((2, 2), color=AS2700.G11_BOTTLE_GREEN)
        t1.add_highlighted_cell((3, 3), color=AS2700.G11_BOTTLE_GREEN)
        t1.add_highlighted_cell((2, 3), color=AS2700.R11_INTERNATIONAL_ORANGE)
        t1.add_highlighted_cell((3, 2), color=AS2700.R11_INTERNATIONAL_ORANGE)

        t2 = (
            Table(
                [["T", "T"], ["T", "F"]],
                row_labels=[Text("T"), Text("F")],
                col_labels=[Text("T"), Text("F")],
                top_left_entry=Text("OR", font_size=40),
            )
            .scale(0.95)
            .to_corner(DR)
        )
        t2.add_highlighted_cell((2, 2), color=AS2700.G11_BOTTLE_GREEN)
        t2.add_highlighted_cell((2, 3), color=AS2700.G11_BOTTLE_GREEN)
        t2.add_highlighted_cell((3, 2), color=AS2700.G11_BOTTLE_GREEN)
        t2.add_highlighted_cell((3, 3), color=AS2700.R11_INTERNATIONAL_ORANGE)

        self.play(Write(t1))
        self.wait(4)
        self.play(Write(t2))
        self.wait(4)


class Table5(Scene):
    def construct(self):
        title = Text("Ternary Operator: if-else", weight=BOLD, font_size=25).to_edge(UP)
        line = Line(
            title.get_left(), title.get_right(), color=AS2700.B11_RICH_BLUE
        ).next_to(title, DOWN)
        self.add(title, line)
        self.wait()

        operators = (
            VGroup(
                Text("Token", font_size=25, weight=BOLD, color=AS2700.Y12_WATTLE),
                Text("Example", font_size=25, weight=BOLD, color=AS2700.Y12_WATTLE),
                Text("Explain", font_size=25, weight=BOLD, color=AS2700.Y12_WATTLE),
                Text("?:", font_size=25),
                Text(
                    "a?b:c",
                    font_size=25,
                    t2c={"[0:1]": YELLOW, "[2:3]": GREEN, "[4:5]": RED},
                ),
                Text(
                    "If a=T, plot b, else then c",
                    font_size=25,
                    t2c={
                        "[0:2]": YELLOW,
                        "[2:6]": GREEN,
                        "[7:12]": YELLOW,
                        "[16:25]": YELLOW,
                    },
                ),
            )
            .arrange_in_grid(rows=2, aligned_edge=LEFT, buff=0.5)
            .next_to(line, DOWN)
        )
        self.play(Write(operators))
        self.wait(4)

        explain = Text("(condition ? true_value : false_value)", color=AS2700.Y44_SAND)
        self.play(FadeIn(explain))
        self.wait(2)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS} {SCENE}")
