from manim import *  # or: from manimlib import *

# from manim_slides import Slide
from pathlib import Path
import os
from manim import AS2700  # Padrão australiano de cores

# -sqh: save last frame hight quality
FLAGS = f" -sqh"
SCENE = "Table4"
CLEAN = "--flush_cache  "


class RoadMap(Scene):
    def construct(self):
        title = Title("Roadmap", width=40)
        self.play(Write(title))
        # self.wait()

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
        title = Text(
            "Unary operators: a = 3", font="ALM Fixed", font_size=40, color=RED_A
        )
        title.to_edge(UP)
        self.add(title)
        self.wait()

        table = MobjectTable(
            [
                [Text("-a = -3", font_size=35), Text("Overturned", font_size=35)],
                [Text("+a = 3", font_size=35), Text("Neutral", font_size=35)],
                [
                    Text("!a = F", font_size=35),
                    Text("Neg logical (here, a=T)", font_size=35),
                ],
                [Text("a! = 6", font_size=35), Text("factorial", font_size=35)],
                [
                    Text("$1", font_size=35),
                    Text("Select col.1 during 'using' manipulation", font_size=35),
                ],
            ],
            row_labels=[
                Text("-", font_size=40),
                Text("+", font_size=40),
                Text("!", font_size=40),
                Text("!", font_size=40),
                Text("$", font_size=40),
            ],
            col_labels=[
                Text("Example", font_size=40, weight=BOLD, color=AS2700.Y11_CANARY),
                Text("Explain", font_size=40, weight=BOLD, color=AS2700.Y11_CANARY),
            ],
            top_left_entry=Text(
                "Token", font_size=42, weight=BOLD, color=AS2700.Y11_CANARY
            ),
            include_outer_lines=True,
            line_config={"stroke_width": 2},
            arrange_in_grid_config={"cell_alignment": LEFT},
        )  # .arrange_in_grid(col_alignments="ccl")
        table.remove(*table.get_vertical_lines())
        table.scale(0.7)
        self.play(Create(table))
        self.wait()

        for i in range(1, 6):
            box = SurroundingRectangle(table.get_rows()[i])
            self.add(box)
            self.wait(2)
            self.remove(box)
            self.wait()


class Table2(Scene):
    def construct(self):
        title = Text(
            "Binary Operators (arithmetic): a=4, b=2",
            font="ALM Fixed",
            font_size=40,
            color=BLUE_B,
        )
        title.to_edge(UP)
        self.add(title)
        self.wait()

        table = MobjectTable(
            [
                [MathTex("a+b = 6", font_size=40), Text("Addition", font_size=35)],
                [MathTex("a-b = 2", font_size=40), Text("Subtration", font_size=35)],
                [
                    MathTex("a*b = 8", font_size=40),
                    Text("Multiplication", font_size=35),
                ],
                [MathTex("a/b = 2", font_size=40), Text("Division", font_size=35)],
                [
                    MathTex("a**b = 16", font_size=40),
                    Text("Exponentiation", font_size=35),
                ],
                [
                    MathTex("a=b; a=2, b=2", font_size=40),
                    Text("Assigment", font_size=35),
                ],
            ],
            row_labels=[
                Text("+", font_size=40),
                Text("-", font_size=40),
                Text("*", font_size=40),
                Text("/", font_size=40),
                Text("**", font_size=40),
                Text("=", font_size=40),
            ],
            col_labels=[
                Text("Example", font_size=40, weight=BOLD, color=AS2700.Y11_CANARY),
                Text("Explain", font_size=40, weight=BOLD, color=AS2700.Y11_CANARY),
            ],
            top_left_entry=Text(
                "Token", font_size=42, weight=BOLD, color=AS2700.Y11_CANARY
            ),
            include_outer_lines=True,
            line_config={"stroke_width": 2},
            arrange_in_grid_config={"cell_alignment": LEFT},
        )
        table.remove(*table.get_vertical_lines())
        table.scale(0.7).shift(0.3 * DOWN)
        self.play(Create(table))
        self.wait()

        for i in range(1, 7):
            box = SurroundingRectangle(table.get_rows()[i])
            self.add(box)
            self.wait()
            self.remove(box)
            self.wait()


class Table3(Scene):
    def construct(self):
        title = Text(
            "Binary Operators (relational): a=4, b=2",
            font="ALM Fixed",
            font_size=40,
            color=GREEN_A,
        )
        title.to_edge(UP)
        self.add(title)
        self.wait()

        table = MobjectTable(
            [
                [
                    MathTex("a>b \\rightarrow T", font_size=40),
                    Text("Greater than", font_size=35),
                ],
                [
                    MathTex("a < b \\rightarrow F", font_size=40),
                    Text("Less than", font_size=35),
                ],
                [
                    MathTex("a >= b \\rightarrow T", font_size=40),
                    Text("Greater than or equal to", font_size=35),
                ],
                [
                    MathTex("a <= b \\rightarrow F", font_size=40),
                    Text("Less than or equal to", font_size=35),
                ],
                [
                    MathTex("a==b \\rightarrow F", font_size=40),
                    Text("Equality", font_size=35),
                ],
                [
                    MathTex("a!=b \\rightarrow T", font_size=40),
                    Text("Inequality", font_size=35),
                ],
            ],
            row_labels=[
                Text(">", font_size=40),
                Text("<", font_size=40),
                Text(">=", font_size=40),
                Text("<=", font_size=40),
                Text("==", font_size=40),
                Text("!=", font_size=40),
            ],
            col_labels=[
                Text("Example", font_size=40, weight=BOLD, color=AS2700.Y11_CANARY),
                Text("Explain", font_size=40, weight=BOLD, color=AS2700.Y11_CANARY),
            ],
            top_left_entry=Text(
                "Token", font_size=42, weight=BOLD, color=AS2700.Y11_CANARY
            ),
            include_outer_lines=True,
            line_config={"stroke_width": 2},
            arrange_in_grid_config={"cell_alignment": LEFT},
        )
        table.remove(*table.get_vertical_lines())
        table.scale(0.7).shift(0.3 * DOWN)
        self.play(Create(table))
        self.wait()

        for i in range(1, 7):
            box = SurroundingRectangle(table.get_rows()[i])
            self.add(box)
            self.wait()
            self.remove(box)
            self.wait()


class Table4(Scene):
    def construct(self):
        title = Text(
            "Binary Operators (combinational): a=4, b=2",
            font="ALM Fixed",
            font_size=40,
            color=ORANGE,
        )
        title.to_edge(UP)
        self.add(title)
        self.wait()

        table = MobjectTable(
            [
                [
                    MathTex("a>b \\ \\&\\& \\ a>0 \\rightarrow T", font_size=40),
                    Text("Logical AND", font_size=35),
                ],
                [
                    MathTex("a>b \\ || \\ b>a \\rightarrow T", font_size=40),
                    Text("Logical OR", font_size=35),
                ],
            ],
            row_labels=[
                MathTex(" \\& \\& ", font_size=40),
                MathTex("||", font_size=40),
            ],
            col_labels=[
                Text("Example", font_size=40, weight=BOLD, color=AS2700.Y11_CANARY),
                Text("Explain", font_size=40, weight=BOLD, color=AS2700.Y11_CANARY),
            ],
            top_left_entry=Text(
                "Token", font_size=42, weight=BOLD, color=AS2700.Y11_CANARY
            ),
            include_outer_lines=True,
            line_config={"stroke_width": 2},
            arrange_in_grid_config={"cell_alignment": LEFT},
        )
        table.remove(*table.get_vertical_lines())
        table.scale(0.7).shift(1.4 * UP)
        self.play(Create(table))
        self.wait()

        t1 = (
            Table(
                [["T", "F"], ["F", "T"]],
                row_labels=[Text("T"), Text("F")],
                col_labels=[Text("T"), Text("F")],
                top_left_entry=Text("AND", font_size=40),
            )
            .scale(0.85)
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
            .scale(0.85)
            .to_corner(DR)
        )
        t2.add_highlighted_cell((2, 2), color=AS2700.G11_BOTTLE_GREEN)
        t2.add_highlighted_cell((2, 3), color=AS2700.G11_BOTTLE_GREEN)
        t2.add_highlighted_cell((3, 2), color=AS2700.G11_BOTTLE_GREEN)
        t2.add_highlighted_cell((3, 3), color=AS2700.R11_INTERNATIONAL_ORANGE)

        box = SurroundingRectangle(table.get_rows()[1])
        self.add(box)
        self.play(Write(t1))
        self.wait(4)
        self.remove(box)

        box = SurroundingRectangle(table.get_rows()[2])
        self.add(box)
        self.play(Write(t2))
        self.wait(4)


class Table5(Scene):
    def construct(self):
        title = Text(
            "Ternary Operator: if-else",
            font="ALM Fixed",
            font_size=40,
            color=PINK,
        )
        title.to_edge(UP)
        self.add(title)
        self.wait()

        table = MobjectTable(
            [
                [
                    Text(
                        "a?b:c",
                        font_size=40,
                        t2c={"[0:1]": YELLOW, "[2:3]": GREEN, "[4:5]": PURE_RED},
                    ),
                    Text(
                        "If a==T, do b, else do c",
                        font_size=40,
                        t2c={
                            "[0:2]": YELLOW,
                            "[2:7]": ORANGE,
                            "[7:11]": YELLOW,
                            "[15:23]": YELLOW,
                        },
                    ),
                ],
            ],
            row_labels=[
                Text("?:", font_size=40),
            ],
            col_labels=[
                Text("Example", font_size=40, weight=BOLD, color=AS2700.Y11_CANARY),
                Text("Explain", font_size=40, weight=BOLD, color=AS2700.Y11_CANARY),
            ],
            top_left_entry=Text(
                "Token", font_size=42, weight=BOLD, color=AS2700.Y11_CANARY
            ),
            include_outer_lines=True,
            line_config={"stroke_width": 2},
            arrange_in_grid_config={"cell_alignment": LEFT},
        )
        table.remove(*table.get_vertical_lines())
        table.scale(0.7).shift(1.4 * UP)
        self.play(Create(table))
        self.wait(2)

        explain = Text("(condition ? true_value : false_value)", color=AS2700.Y44_SAND)
        explain.shift(DOWN)
        self.play(FadeIn(explain))
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS} {SCENE}")
