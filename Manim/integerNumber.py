from manim import *
from pathlib import Path
import os
import random
import subprocess
import sys
from manim import AS2700  # Padrão australiano de cores

FLAGS = f" "
SCENE = "OrderOfOperations"  # Change this to the desired scene name
CLEAN = "--flush_cache  "

# Vertical config
config.frame_rate = 25
config.frame_size = [1080, 1920]  # [WIDTH, HEIGHT]

# Script para executar automaticamente com os flags corretos
if __name__ == "__main__":
    if len(sys.argv) == 1:  # Se executado sem argumentos
        cmd = f"manim {FLAGS} {__file__} {SCENE}"
        subprocess.run(cmd.split())
        sys.exit(0)

# Padronizar tamanhos de fonte em todas as animações
title_size = 36
subtitle_size = 28
code_title_size = 28


class NaturalNumbers(Scene):
    def construct(self):
        # Add a label for the set of natural numbers
        natural_numbers_label = (
            MathTex(r"\mathbb{N}")
            .scale(2)
            .to_edge(UP, buff=1)
            .set_color(AS2700.Y14_GOLDEN_YELLOW)
        )
        self.play(Write(natural_numbers_label))

        # Create a number line
        number_line = NumberLine(x_range=[0, 10, 1], length=10, color=BLUE)
        self.play(Create(number_line), rate_functions=smooth)

        # Create labels for natural numbers
        # Create labels for natural numbers with color gradient from blue to purple
        labels = []
        for i in range(11):
            label = MathTex(str(i))
            # Calculate color gradient position (0 to 1)
            t = i / 10
            # Interpolate between BLUE and GREEN_E
            color = interpolate_color(BLUE_D, GREEN_E, t)
            label.set_color(color).next_to(number_line.n2p(i), UP)
            labels.append(label)
            self.play(FadeIn(label, shift=0.1 * DOWN), run_time=0.5)
        self.wait(2)


class AdditionExample(Scene):
    def construct(self):
        # Import orange SVG image
        orange_image = SVGMobject("assets/orange-svgrepo-com.svg").scale(0.5)
        two_oranges = (
            VGroup(orange_image, orange_image.copy()).arrange(UP, buff=0.3).shift(LEFT)
        )
        three_oranges = VGroup(
            orange_image.copy(), orange_image.copy(), orange_image.copy()
        ).arrange(UP, buff=0.3)
        oranges = (
            VGroup(two_oranges, three_oranges)
            .arrange(RIGHT, buff=1, aligned_edge=DOWN)
            .to_edge(DOWN, buff=1)
        )

        # Create labels for the oranges
        two = MathTex("2").next_to(two_oranges, DOWN, buff=0.5)
        plus = MathTex("+").next_to(oranges, DOWN, buff=0.5).scale(1.2)
        three = MathTex("3").next_to(three_oranges, DOWN, buff=0.5)
        equals = MathTex("=").next_to(three, RIGHT).scale(1.2)
        result = MathTex("5").next_to(equals, RIGHT).scale(1.3)

        # Adicionar título da operação
        title = Text("Count objects", font_size=36, color=AS2700.Y14_GOLDEN_YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)

        # Animate the addition
        self.play(
            AnimationGroup(
                FadeIn(two_oranges[0], shift=DOWN),
                FadeIn(two_oranges[1], shift=DOWN),
                FadeIn(two),
                lag_ratio=0.3,
            )
        )

        self.play(Write(plus), run_time=0.5)
        self.play(
            AnimationGroup(
                FadeIn(three_oranges[0], shift=DOWN),
                FadeIn(three_oranges[1], shift=DOWN),
                FadeIn(three_oranges[2], shift=DOWN),
                FadeIn(three),
                lag_ratio=0.3,
            )
        )
        self.play(FadeIn(equals), FadeIn(result))
        self.wait(1)

        # Animação de contagem - destacar cada laranja individualmente
        counting_text = Text("Let's count...", font_size=24)
        counting_text.next_to(title, DOWN, buff=0.3)
        self.play(Write(counting_text))

        # Destacar cada laranja com um círculo dourado
        all_oranges = [*two_oranges, *three_oranges]
        circles = []
        for i, orange in enumerate(all_oranges):
            circle = Circle(radius=0.6, color=AS2700.Y15_SUNFLOWER, stroke_width=3)
            circle.move_to(orange.get_center())
            circles.append(circle)

            # Mostrar número da contagem
            count_num = Text(str(i + 1), font_size=25, color=BLACK, weight=BOLD)
            count_num.move_to(orange.get_center()).shift(0.1 * DOWN)

            self.play(Create(circle), FadeIn(count_num, scale=1.5), run_time=0.5)
            self.play(FadeOut(circle), FadeOut(count_num), run_time=0.3)

        self.play(FadeOut(counting_text))

        # Criar o grupo final de 5 laranjas para mostrar o resultado visualmente
        result_oranges = VGroup()
        for i in range(5):
            orange_copy = orange_image.copy()
            result_oranges.add(orange_copy)

        # Posicionar as 5 laranjas em linha acima do número 5
        result_oranges.arrange(UP, buff=0.2).next_to(result, UP, buff=0.5)

        # Animar o movimento das laranjas para o resultado
        # Mover as 2 primeiras laranjas
        self.play(
            Transform(two_oranges[0], result_oranges[0]),
            Transform(two_oranges[1], result_oranges[1]),
            # Mover as 3 laranjas seguintes
            Transform(three_oranges[0], result_oranges[2]),
            Transform(three_oranges[1], result_oranges[3]),
            Transform(three_oranges[2], result_oranges[4]),
            run_time=2,
        )

        # Add a practical programming example on the left side
        example_code_orange = """i = 2  ! first group
j = 3  ! second group
sum = i + j

print *, "2 + 3 =", sum
# Output: 2 + 3 = 5
"""
        code = Code(
            code_string=example_code_orange,
            tab_width=4,
            background="window",
            language="Fortran",
            formatter_style=Code.get_styles_list()[16],
        )

        # Position the code on the left side
        code.to_edge(LEFT, buff=0.5).shift(DOWN)
        code.shift(UP)

        # Add a title for the code
        code_title = Text("Programming Implementation", font_size=28, color=BLUE_C)
        code_title.next_to(code, UP, buff=0.2)

        # Show the code with a typing animation
        self.play(Write(code_title), Write(code), run_time=2)

        # Highlight key parts of the code
        self.play(code.animate)  # a = 2

        # Fazer as laranjas "pularem" uma vez para enfatizar o resultado
        self.play(
            result_oranges.animate.shift(UP * 0.3).set_color(YELLOW),
            rate_func=there_and_back,
            run_time=0.8,
        )

        # Destacar o resultado final
        self.play(result.animate.scale(1.5).set_color(GREEN), run_time=1)

        self.wait(3)

        # Final fade out de tudo
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait()


class MultiplicationExample(Scene):
    def construct(self):
        # Import orange SVG image
        orange_image = SVGMobject("assets/orange-svgrepo-com.svg").scale(0.5)

        # Title of operation
        title = Text("Multiplication", font_size=36, color=AS2700.Y14_GOLDEN_YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)

        # Create 2 groups of 3 oranges each to show 2×3
        groups = VGroup()
        for _ in range(2):  # 2 groups
            group = VGroup()
            for _ in range(3):  # 3 oranges in each group
                group.add(orange_image.copy())
            group.arrange(UP, buff=0.3)
            groups.add(group)

        groups.arrange(RIGHT, buff=0.9).to_edge(DOWN, buff=0.8).shift(3.7 * RIGHT)

        # Create labels for the calculation
        group1_label = MathTex("2").next_to(groups[0], UP, buff=0.5)
        times = MathTex("\\times").next_to(group1_label, RIGHT, buff=0.6).scale(1.2)
        group2_label = MathTex("3").next_to(groups[1], UP, buff=0.5)
        equals = MathTex("=").next_to(group2_label, RIGHT, buff=0.6).scale(1.2)
        result = MathTex("6").next_to(equals, RIGHT, buff=0.6).scale(1.2)

        # Show the groups of oranges
        for i, group in enumerate(groups):
            self.play(
                AnimationGroup(
                    *[FadeIn(orange, shift=DOWN) for orange in group], lag_ratio=0.3
                )
            )
            # Add brackets to show grouping
            bracket = Brace(group, LEFT + 2 * i * RIGHT)
            group_text = Text(f"Group {i+1}", font_size=20).next_to(
                bracket, LEFT + 2 * i * RIGHT
            )
            self.play(GrowFromCenter(bracket), Write(group_text))

        # Animate the group appearance
        self.play(Write(group1_label), Write(times), Write(group2_label), run_time=0.5)

        # Show counting animation
        counting_text = Text("Let's count all oranges...", font_size=24)
        counting_text.next_to(title, DOWN, buff=0.3)
        self.play(Write(counting_text))

        # Count all oranges
        all_oranges = [orange for group in groups for orange in group]
        for i, orange in enumerate(all_oranges):
            circle = Circle(radius=0.6, color=AS2700.Y15_SUNFLOWER, stroke_width=3)
            circle.move_to(orange.get_center())

            count_num = Text(str(i + 1), font_size=25, color=BLACK, weight=BOLD)
            count_num.move_to(orange.get_center()).shift(0.1 * DOWN)

            self.play(Create(circle), FadeIn(count_num, scale=1.5), run_time=0.4)
            self.play(FadeOut(circle), FadeOut(count_num), run_time=0.2)

        # Add programming example
        example_code = """i = 2  
j = 3  
product = i * j

print *, i, 'x', j, '=', product
! Output: 2 × 3 = 6
"""
        code = Code(
            code_string=example_code,
            tab_width=4,
            background="window",
            language="Fortran",
            formatter_style=Code.get_styles_list()[16],
        )

        code.to_edge(LEFT, buff=0.4).shift(0.5 * UP)

        code_title = Text("Programming Implementation", font_size=28, color=BLUE_C)
        code_title.next_to(code, UP, buff=0.2)

        # Show result
        self.play(FadeIn(equals), FadeIn(result), FadeOut(counting_text))
        self.play(Write(code_title), Write(code), run_time=2)

        # Highlight the result
        self.play(result.animate.scale(1.4).set_color(GREEN), run_time=1)

        self.wait(3)

        # Final fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait()


class DivisionExample(Scene):
    def construct(self):
        # Import orange SVG image
        orange_image = SVGMobject("assets/orange-svgrepo-com.svg").scale(0.5)

        # Title of operation
        title = Text("Division", font_size=36, color=AS2700.Y14_GOLDEN_YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=2)
        self.wait(0.5)

        # Create a group of oranges (6 oranges)
        total_oranges = 6
        orange_group = VGroup()
        for _ in range(total_oranges):
            orange_group.add(orange_image.copy())

        # Arrange oranges in a grid (2×3)
        orange_group.arrange_in_grid(rows=2, buff=0.3).to_edge(LEFT, buff=1)

        # Show the oranges and the calculation
        self.play(
            AnimationGroup(
                *[FadeIn(orange, shift=DOWN) for orange in orange_group], lag_ratio=0.2
            ),
            run_time=2,
        )

        self.wait(2)  # Create labels for the division
        dividend = MathTex("6").to_edge(DOWN, buff=1).shift(LEFT)
        divide = MathTex("\\div").next_to(dividend, RIGHT, buff=0.6).scale(1.2)
        divisor = MathTex("2").next_to(divide, RIGHT, buff=0.6)
        equals = MathTex("=").next_to(divisor, RIGHT, buff=0.6).scale(1.2)
        result = MathTex("3").next_to(equals, RIGHT, buff=0.6).scale(1.2)
        self.play(Write(dividend), Write(divide), Write(divisor), run_time=0.5)

        self.wait(2)
        # Divide oranges into groups
        groups = VGroup()
        for i in range(0, total_oranges, 3):  # Split into 2 groups of 3
            group = VGroup(*[orange_group[j].copy() for j in range(i, i + 3)])
            group.arrange(UP, buff=0.3)
            groups.add(group)

        groups.arrange(RIGHT, buff=1.5).to_edge(RIGHT, buff=1)

        # Animate division by showing groups
        self.play(Transform(orange_group, groups), run_time=2)

        self.wait(2)
        # Add brackets to show the result of division (3 per group)
        for i, group in enumerate(groups):
            bracket = Brace(group, LEFT)
            self.play(GrowFromCenter(bracket), run_time=0.7)

        # Show the result
        self.play(FadeIn(equals), FadeIn(result), run_time=2)
        self.wait(3)
        example_code = """i = 6  ! total
j = 2  ! divisor
quotient = i / j

print *, i, '÷', j, '=', quotient
! Output: 6 ÷ 2 = 3
"""
        code = Code(
            code_string=example_code,
            tab_width=4,
            background="window",
            language="Fortran",
            formatter_style=Code.get_styles_list()[16],
        )

        code.to_edge(LEFT, buff=0.5).shift(0 * UP)

        code_title = Text("Programming Implementation", font_size=28, color=BLUE_C)
        code_title.next_to(code, UP, buff=0.2)

        # Show code
        self.play(Write(code_title), Write(code), run_time=2)

        self.wait(4)
        # Highlight the result
        self.play(result.animate.scale(1.4).set_color(GREEN), run_time=1)

        self.wait(3)

        # Final fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait()


class DivisionRemainderExample(Scene):
    def construct(self):
        # Import orange SVG image
        orange_image = SVGMobject("assets/orange-svgrepo-com.svg").scale(0.5)

        # Title of operation
        title = Text(
            "Division with Remainder", font_size=36, color=AS2700.Y14_GOLDEN_YELLOW
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)

        # Create a group of oranges (7 oranges)
        total_oranges = 7
        orange_group = VGroup()
        for _ in range(total_oranges):
            orange_group.add(orange_image.copy())

        # Arrange oranges in a grid (3×3 but with only 7)
        orange_group.arrange_in_grid(
            rows=3, cols=3, buff=0.3, fill_rows_first=True
        ).to_edge(LEFT, buff=1)

        # Show the oranges and the calculation
        self.play(
            AnimationGroup(
                *[FadeIn(orange, shift=DOWN) for orange in orange_group], lag_ratio=0.2
            )
        )

        self.wait()  # Create labels for the division
        dividend = MathTex("7").to_edge(DOWN, buff=1).shift(LEFT)
        divide = MathTex("\\div").next_to(dividend, RIGHT, buff=0.6).scale(1.2)
        divisor = MathTex("3").next_to(divide, RIGHT, buff=0.6)
        equals = MathTex("=").next_to(divisor, RIGHT, buff=0.6).scale(1.2)
        result = MathTex("2 \\text{ R } 1").next_to(equals, RIGHT, buff=0.6).scale(1.2)
        self.play(Write(dividend), Write(divide), Write(divisor), run_time=0.5)

        self.wait()
        # Create groups of 3 oranges
        groups = VGroup()
        remainder_group = VGroup()

        # Two complete groups of 3
        for i in range(0, 6, 3):
            group = VGroup(*[orange_group[j].copy() for j in range(i, i + 3)])
            group.arrange(UP, buff=0.3)
            groups.add(group)

        # One orange as remainder
        remainder_group.add(orange_group[6].copy())

        # Arrange the groups and remainder
        groups.arrange(RIGHT, buff=1.5)
        remainder_group.next_to(groups, RIGHT, buff=1)

        # Position everything to the right
        VGroup(groups, remainder_group).to_edge(RIGHT, buff=1)

        # Animate division by showing groups
        self.play(Transform(orange_group, VGroup(groups, remainder_group)), run_time=2)

        self.wait()
        # Add brackets to show the result of division (3 per group)
        for i, group in enumerate(groups):
            bracket = Brace(group, LEFT)
            self.play(GrowFromCenter(bracket), run_time=0.7)

        # Label the remainder
        remainder_brace = Brace(remainder_group, LEFT)
        remainder_label = (
            Text("Remainder", font_size=20, color=AS2700.Y11_CANARY)
            .next_to(remainder_brace, DR)
            .shift(0.5 * LEFT)
        )
        self.play(GrowFromCenter(remainder_brace), Write(remainder_label), run_time=0.7)

        self.wait()
        # Show the result
        self.play(FadeIn(equals), FadeIn(result))

        self.wait()  # Add programming example
        example_code = """i = 7  ! total
j = 3  ! divisor
div = i / j  ! integer div
remainder = mod(i, j)

print *, i, '÷', j, '=', div, 
print *, 'R', remainder
! Output: 7 ÷ 3 = 2 
! R 1
"""
        code = Code(
            code_string=example_code,
            tab_width=4,
            background="window",
            language="Fortran",
            formatter_style=Code.get_styles_list()[16],
        )

        code.to_edge(LEFT, buff=0.5).shift(UP * 0)

        code_title = Text("Programming Implementation", font_size=28, color=BLUE_C)
        code_title.next_to(code, UP, buff=0.2)

        # Show code
        self.play(Write(code_title), Write(code), run_time=2)

        self.wait()  # Highlight the result
        self.play(result.animate.scale(1.4).set_color(GREEN), run_time=1)

        self.wait(3)

        # Final fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait()


class IntegerNumbers(Scene):
    def construct(self):
        # Create a number line
        RANGE_NUMBERS = 8
        number_line = NumberLine(
            x_range=[-RANGE_NUMBERS, RANGE_NUMBERS, 1],
            include_numbers=True,
            length=12,
            color=BLUE,
        )
        # Add a label for the set of integers
        integer_numbers_label = MathTex(r"\mathbb{Z}").scale(3).to_edge(UP)

        self.play(Create(number_line), FadeIn(integer_numbers_label))
        self.wait(2)


class IntegerOperations(Scene):
    def construct(self):
        title = Text(
            "Integer Operations", font_size=36, color=AS2700.Y14_GOLDEN_YELLOW
        ).to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=0.1 * DOWN))
        # Create labels for integer operations
        addition = MathTex("a + b")
        subtraction = MathTex("a - b")
        multiplication = MathTex("a \\times b")
        division = MathTex("a \\div b")

        operations = (
            VGroup(
                VGroup(addition, subtraction).arrange(DOWN, buff=3, aligned_edge=LEFT),
                multiplication,
                division,
            )
            .set_color(AS2700.Y14_GOLDEN_YELLOW)
            .arrange(RIGHT, buff=3, aligned_edge=UP)
            .next_to(title, DOWN, buff=0.5)
        )

        example_addition = (
            VGroup(MathTex("2 + 3 = 5"), MathTex("2 + (-5) = -3"))
            .arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            .next_to(operations[0][0], DOWN, buff=0.5)
        )

        example_subtraction = (
            VGroup(MathTex("5 - 2 = 3"), MathTex("(-3) - 2 = -5"))
            .arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            .next_to(operations[0][1], DOWN, buff=0.5)
        )

        example_multiplication = (
            VGroup(
                MathTex("2 \\times 3 = 6"),
                MathTex("(-2) \\times 3 = -6"),
                MathTex("2 \\times 0 = 0"),
            )
            .arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            .next_to(operations[1], DOWN, buff=0.5)
        )

        division_example = (
            VGroup(
                MathTex("6 / 3 = 2"),
                MathTex("(-6) / 3 = -2"),
                MathTex("0 / 2 = 0"),
                MathTex("7 / 2 = 3"),
                MathTex("2 / 7 = 0"),
                MathTex("2 / 0 = \\text{undefined}"),
            )
            .arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            .next_to(operations[2], DOWN, buff=0.5)
        )

        box_addition = SurroundingRectangle(
            VGroup(addition, example_addition), color=YELLOW, buff=0.2
        ).move_to(VGroup(addition, example_addition))
        box_subtraction = SurroundingRectangle(
            VGroup(subtraction, example_subtraction), color=ORANGE, buff=0.2
        ).move_to(VGroup(subtraction, example_subtraction))
        box_multiplication = SurroundingRectangle(
            VGroup(multiplication, example_multiplication), color=GREEN, buff=0.2
        ).move_to(VGroup(multiplication, example_multiplication))
        box_division = SurroundingRectangle(
            VGroup(division, division_example), color=RED, buff=0.2
        ).move_to(VGroup(division, division_example))

        # Animate the integer operations
        self.play(
            Succession(
                FadeIn(operations[0][0], shift=0.1 * UP),
                Write(example_addition[0]),
                Write(example_addition[1]),
                Create(box_addition),
                FadeIn(operations[0][1], shift=0.1 * UP),
                Write(example_subtraction[0]),
                Write(example_subtraction[1]),
                FadeIn(operations[1], shift=0.1 * UP),
                Create(box_subtraction),
                Write(example_multiplication[0]),
                Write(example_multiplication[1]),
                Write(example_multiplication[2]),
                FadeIn(operations[2], shift=0.1 * UP),
                Create(box_multiplication),
                Write(division_example[0]),
                Write(division_example[1]),
                Write(division_example[2]),
                Write(division_example[3]),
                Write(division_example[4]),
                Write(division_example[5]),
                Create(box_division),
                lag_ratio=0.5,
                run_time=20,
            ),
            rate_functions=smooth,
        )
        self.wait(2)


class LoopExample(Scene):
    def construct(self):
        # Create labels for the loop
        loop_label = (
            MathTex("& for \\ i = 1 \\ to \\ n: \\\\", "& \\quad sum = sum + i")
            .scale(2)
            .set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED)
            .shift(DOWN)
        )
        max_label = (
            MathTex("n = 10")
            .scale(2)
            .set_color(AS2700.Y14_GOLDEN_YELLOW)
            .to_edge(UP, buff=1)
        )

        # Animate the loop example
        self.play(FadeIn(max_label, scale=0.8), rate_functions=smooth)
        self.play(Write(loop_label, scale=0.8), run_time=2, rate_functions=smooth)
        self.wait(2)


class MidVideoCallToAction(Scene):
    def construct(self):
        # Quick subscribe reminder
        bell = SVGMobject("assets/bell-svgrepo-com.svg").scale(0.5).set_color("#FFD700")
        subscribe_reminder = VGroup(
            VGroup(
                bell, Text("Subscribe for More!", font_size=36, color="#FFD700")
            ).arrange(RIGHT, buff=0.5),
            Text("Coming up: Fortran Programming", font_size=24, color="#00FF00"),
        ).arrange(DOWN, buff=0.5)

        self.play(FadeIn(subscribe_reminder, scale=1.2))
        self.wait()
        self.play(Indicate(subscribe_reminder[0], color="#FF0000"))
        self.wait(15)
        self.play(FadeOut(subscribe_reminder))
        self.wait(0.5)


class ArithmeticOperations(Scene):
    def construct(self):
        # Create a title
        title = (
            Text("Arithmetic Operations in Programming")
            .scale(0.8)
            .set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED)
            .to_edge(UP, buff=0.5)
        )
        self.play(Write(title))
        self.wait(2)

        # Create a list of arithmetic operations
        operations = BulletedList(
            "Addition: a + b",
            "Subtraction: a - b",
            "Multiplication: a * b",
            "Division: a / b",
            "Exponentiation: a ** b",
        )
        operations.arrange(DOWN, buff=0.5, aligned_edge=LEFT).set_color(
            AS2700.Y14_GOLDEN_YELLOW
        )

        for label in operations:
            self.play(FadeIn(label))

        # Wait before ending the scene
        self.wait(2)


class OrderOfOperations(Scene):
    def construct(self):
        # Config for short Youtube video
        # Create a title
        title = (
            Text("Order of Operations: PEMDAS")
            .scale(1.3)
            .set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED)
            .to_edge(UP, buff=0.5)
            .shift(5 * UP)
        )
        self.play(Write(title), run_time=0.5)
        self.wait()

        # Mathematical expression with fraction (non compatible
        # with programing languages)
        original_expr = (
            MathTex("6 + 2 \\times (3 + 1)^{2} - \\frac{8}{4}", font_size=48)
            .scale(2)
            .shift(1.5 * UP)
        )
        warning_text = Text(
            "Not compatible with programming languages!", font_size=40, color=RED
        )
        warning_text.next_to(original_expr, DOWN, buff=0.5)
        inline_text = Text(
            "We need to write inline", font_size=55, color=AS2700.Y14_GOLDEN_YELLOW
        )
        inline_text.next_to(warning_text, DOWN, buff=1)
        self.play(Write(original_expr), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(warning_text), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(inline_text), run_time=0.5)
        self.wait(2)

        self.remove(original_expr, warning_text, inline_text)
        self.wait()

        # Create the acronym PEMDAS vertically
        # Create labels for each operation
        DropCap = 75
        DropCap_buff = 0.05
        operations = (
            VGroup(
                VGroup(
                    Text(
                        "P",
                        font="Coelacanth",
                        font_size=DropCap,
                        color=AS2700.Y14_GOLDEN_YELLOW,
                    ),
                    Text("ARENTHESES", font="Coelacanth", font_size=0.4 * DropCap),
                ).arrange(RIGHT, buff=DropCap_buff, aligned_edge=DOWN),
                VGroup(
                    Text(
                        "E",
                        font="Coelacanth",
                        font_size=DropCap,
                        color=AS2700.Y14_GOLDEN_YELLOW,
                    ),
                    Text("XPONENTS", font="Coelacanth", font_size=0.4 * DropCap),
                ).arrange(RIGHT, buff=DropCap_buff, aligned_edge=DOWN),
                VGroup(
                    Text(
                        "M",
                        font="Coelacanth",
                        font_size=DropCap,
                        color=AS2700.Y14_GOLDEN_YELLOW,
                    ),
                    Text("ULTIPLICATION", font="Coelacanth", font_size=0.4 * DropCap),
                ).arrange(RIGHT, buff=DropCap_buff, aligned_edge=DOWN),
                VGroup(
                    Text(
                        "D",
                        font="Coelacanth",
                        font_size=DropCap,
                        color=AS2700.Y14_GOLDEN_YELLOW,
                    ),
                    Text("IVISION", font="Coelacanth", font_size=0.4 * DropCap),
                ).arrange(RIGHT, buff=DropCap_buff, aligned_edge=DOWN),
                VGroup(
                    Text(
                        "A",
                        font="Coelacanth",
                        font_size=DropCap,
                        color=AS2700.Y14_GOLDEN_YELLOW,
                    ),
                    Text("DDITION", font="Coelacanth", font_size=0.4 * DropCap),
                ).arrange(RIGHT, buff=DropCap_buff, aligned_edge=DOWN),
                VGroup(
                    Text(
                        "S",
                        font="Coelacanth",
                        font_size=DropCap,
                        color=AS2700.Y14_GOLDEN_YELLOW,
                    ),
                    Text("UBTRACTION", font="Coelacanth", font_size=0.4 * DropCap),
                ).arrange(RIGHT, buff=DropCap_buff, aligned_edge=DOWN),
            )
            .arrange(DOWN, buff=1.1, aligned_edge=LEFT)
            .to_edge(LEFT, buff=1.)
        )

        # Use a clearer expression without ambiguity
        SCALE_EQ = 1.4
        parenthesis_expr = (
            (MathTex("6 + 2 \\times", "(3 + 1)", "^{2} - 8 \\div 4", font_size=48))
            .scale(SCALE_EQ)
            .next_to(operations[0].get_left(), RIGHT, buff=5)
        )
        parenthesis_expr[1].set_color(AS2700.Y14_GOLDEN_YELLOW)

        exponential_expr = (
            MathTex("6 + 2 \\times", "4^{2}", "- 8 \\div 4", font_size=48)
            .scale(SCALE_EQ)
            .next_to(operations[1].get_left(), RIGHT, buff=5)
        )
        exponential_expr[1].set_color(AS2700.Y14_GOLDEN_YELLOW)

        product_expr = (
            MathTex("6 +", "2 \\times 16", "- 8 \\div 4", font_size=48)
            .scale(SCALE_EQ)
            .next_to(operations[2].get_left(), RIGHT, buff=5)
        )
        product_expr[1].set_color(AS2700.Y14_GOLDEN_YELLOW)

        division_expr = (
            MathTex("6 + 32 - ", "8 \\div 4", font_size=48)
            .scale(SCALE_EQ)
            .next_to(operations[3].get_left(), RIGHT, buff=5)
        )
        division_expr[1].set_color(AS2700.Y14_GOLDEN_YELLOW)

        add_expr = (
            MathTex("6 + 32", "- 2", font_size=48)
            .scale(SCALE_EQ)
            .next_to(operations[4].get_left(), RIGHT, buff=5)
        )
        add_expr[0].set_color(AS2700.Y14_GOLDEN_YELLOW)

        minus_expr = (
            MathTex("38 - 2", font_size=48)
            .scale(SCALE_EQ)
            .next_to(operations[5].get_left(), RIGHT, buff=5)
            .set_color(AS2700.Y14_GOLDEN_YELLOW)
        )

        expressions_eqs = VGroup(
            parenthesis_expr,
            exponential_expr,
            product_expr,
            division_expr,
            add_expr,
            minus_expr,
        )

        # Animate each PEMDAS operation with its corresponding expression
        for i, (label, expression) in enumerate(zip(operations, expressions_eqs)):
            # Then reveal the PEMDAS operation label
            self.play(
                LaggedStart(FadeIn(label), Write(expression), lag_ratio=0.25),
                run_time=2,
            )
            self.wait(1)

        # Wait before ending the scene
        self.wait(4)


class PEMDASControversyExample(Scene):
    def construct(self):
        # Create title
        title = Text(
            "The Famous PEMDAS Controversy",
            font_size=36,
            color=AS2700.Y14_GOLDEN_YELLOW,
        ).to_edge(UP, buff=0.3)

        subtitle = Text(
            "8 ÷ 2(2+2) = ?", font_size=48, color=WHITE, weight=BOLD
        ).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)

        # Show the controversy - two different interpretations
        controversy_text = Text(
            "This expression creates two different answers!", font_size=24, color=RED
        ).next_to(subtitle, DOWN, buff=0.5)

        self.play(Write(controversy_text))
        self.wait(2)

        # Create two columns for different interpretations
        interpretation1_title = (
            Text("Interpretation 1: Strict Left-to-Right", font_size=20, color=BLUE)
            .to_edge(LEFT, buff=0.5)
            .shift(UP * 1.5)
        )

        interpretation2_title = (
            Text("Interpretation 2: Implied Multiplication", font_size=20, color=GREEN)
            .to_edge(RIGHT, buff=0.5)
            .shift(UP * 1.5)
        )

        self.play(Write(interpretation1_title), Write(interpretation2_title))

        # Left side - Interpretation 1 (Result = 16)
        left_steps = VGroup()

        step1_left = MathTex("8 \\div 2(2+2)").set_color(WHITE)
        step2_left = MathTex("8 \\div 2(4)").set_color(WHITE)
        step3_left = MathTex("8 \\div 2 \\times 4").set_color(BLUE)
        step4_left = MathTex("4 \\times 4").set_color(BLUE)
        step5_left = MathTex("16").set_color(BLUE).scale(1.5)

        left_steps = VGroup(step1_left, step2_left, step3_left, step4_left, step5_left)
        left_steps.arrange(DOWN, buff=0.4).next_to(
            interpretation1_title, DOWN, buff=0.5
        )

        # Right side - Interpretation 2 (Result = 1)
        right_steps = VGroup()

        step1_right = MathTex("8 \\div 2(2+2)").set_color(WHITE)
        step2_right = MathTex("8 \\div 2(4)").set_color(WHITE)
        step3_right = MathTex("8 \\div [2 \\times 4]").set_color(GREEN)
        step4_right = MathTex("8 \\div 8").set_color(GREEN)
        step5_right = MathTex("1").set_color(GREEN).scale(1.5)

        right_steps = VGroup(
            step1_right, step2_right, step3_right, step4_right, step5_right
        )
        right_steps.arrange(DOWN, buff=0.4).next_to(
            interpretation2_title, DOWN, buff=0.5
        )

        # Animate left side
        for i, step in enumerate(left_steps):
            self.play(Write(step), run_time=0.8)
            if i == 2:  # Highlight the key difference
                explanation_left = Text(
                    "Division and multiplication\nhave equal priority",
                    font_size=14,
                    color=BLUE,
                ).next_to(step, DOWN, buff=0.2)
                self.play(Write(explanation_left))
            self.wait(0.5)

        # Animate right side
        for i, step in enumerate(right_steps):
            self.play(Write(step), run_time=0.8)
            if i == 2:  # Highlight the key difference
                explanation_right = Text(
                    "Implied multiplication\nbinds more tightly",
                    font_size=14,
                    color=GREEN,
                ).next_to(step, DOWN, buff=0.2)
                self.play(Write(explanation_right))
            self.wait(0.5)

        # Show the conflict
        conflict_text = Text(
            "Which is correct? Both follow PEMDAS rules!", font_size=20, color=RED
        ).to_edge(DOWN, buff=1.5)

        self.play(Write(conflict_text))
        self.wait(3)

        # Clear everything for the solution
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Show the solution - proper mathematical notation
        solution_title = Text(
            "The Solution: Use Clear Notation!",
            font_size=36,
            color=AS2700.Y14_GOLDEN_YELLOW,
        ).to_edge(UP, buff=0.5)

        self.play(Write(solution_title))

        # Show clear notation examples
        clear_notation = VGroup(
            Text("Ambiguous:", font_size=24, color=RED),
            MathTex("8 \\div 2(2+2)", font_size=32),
            Text("Clear Option 1:", font_size=24, color=BLUE),
            MathTex("(8 \\div 2) \\times (2+2) = 16", font_size=32, color=BLUE),
            Text("Clear Option 2:", font_size=24, color=GREEN),
            MathTex("8 \\div [2(2+2)] = 1", font_size=32, color=GREEN),
        ).arrange(DOWN, buff=0.4)

        for item in clear_notation:
            self.play(Write(item), run_time=0.8)
            self.wait(0.3)

        # Programming advice
        programming_advice = (
            VGroup(
                Text("In Programming:", font_size=24, color=YELLOW, weight=BOLD),
                Text("• Always use parentheses for clarity", font_size=18),
                Text("• Avoid implied multiplication", font_size=18),
                Text("• Make your intentions explicit", font_size=18),
            )
            .arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            .to_edge(DOWN, buff=1)
        )

        for advice in programming_advice:
            self.play(Write(advice), run_time=0.6)

        self.wait(4)


class PEMDASExample(Scene):
    def construct(self):
        # Create title
        title = Text(
            "PEMDAS in Action: Clear Example",
            font_size=36,
            color=AS2700.Y14_GOLDEN_YELLOW,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Use a clearer expression without ambiguity
        original_expr = MathTex(
            "6 + 2 \\times (3 + 1)^2 - 8 \\div 4", font_size=48
        ).next_to(title, DOWN, buff=1)

        self.play(Write(original_expr))
        self.wait(2)

        # Create step-by-step breakdown
        steps_title = Text("Following PEMDAS Order:", font_size=24, color=BLUE).next_to(
            original_expr, DOWN, buff=1
        )
        self.play(Write(steps_title))

        # Step 1: Parentheses
        step1_title = Text("1. Parentheses first:", font_size=20, color=RED).next_to(
            steps_title, DOWN, buff=0.5
        )
        step1_expr = MathTex("6 + 2 \\times ", "(3 + 1)", "^2 - 8 \\div 4").next_to(
            step1_title, DOWN, buff=0.3
        )
        step1_result = MathTex("6 + 2 \\times ", "4", "^2 - 8 \\div 4").next_to(
            step1_expr, DOWN, buff=0.3
        )

        # Highlight parentheses
        step1_expr[1].set_color(RED)
        step1_result[1].set_color(RED)

        self.play(Write(step1_title))
        self.play(Write(step1_expr))
        self.wait(1)
        self.play(Transform(step1_expr[1], step1_result[1]))
        self.wait(2)

        # Step 2: Exponents
        step2_title = Text("2. Exponents next:", font_size=20, color=ORANGE).next_to(
            step1_result, DOWN, buff=0.5
        )
        step2_expr = MathTex("6 + 2 \\times ", "4^2", " - 8 \\div 4").next_to(
            step2_title, DOWN, buff=0.3
        )
        step2_result = MathTex("6 + 2 \\times ", "16", " - 8 \\div 4").next_to(
            step2_expr, DOWN, buff=0.3
        )

        # Highlight exponent
        step2_expr[1].set_color(ORANGE)
        step2_result[1].set_color(ORANGE)

        self.play(Write(step2_title))
        self.play(Write(step2_expr))
        self.wait(1)
        self.play(Transform(step2_expr[1], step2_result[1]))
        self.wait(2)

        # Clear previous steps for space
        self.play(
            FadeOut(step1_title),
            FadeOut(step1_expr),
            FadeOut(step1_result),
            FadeOut(step2_title),
            FadeOut(step2_expr),
            FadeOut(step2_result),
        )

        # Step 3: Multiplication and Division (left to right)
        step3_title = Text(
            "3. Multiplication and Division (left to right):",
            font_size=20,
            color=YELLOW,
        ).next_to(steps_title, DOWN, buff=0.5)
        step3a_expr = MathTex("6 + ", "2 \\times 16", " - ", "8 \\div 4").next_to(
            step3_title, DOWN, buff=0.3
        )
        step3a_result = MathTex("6 + ", "32", " - ", "8 \\div 4").next_to(
            step3a_expr, DOWN, buff=0.3
        )

        # Highlight multiplication
        step3a_expr[1].set_color(YELLOW)
        step3a_result[1].set_color(YELLOW)

        self.play(Write(step3_title))
        self.play(Write(step3a_expr))
        self.wait(1)
        self.play(Transform(step3a_expr[1], step3a_result[1]))
        self.wait(1)

        # Continue with division
        step3b_expr = MathTex("6 + 32 - ", "8 \\div 4").next_to(
            step3a_result, DOWN, buff=0.3
        )
        step3b_result = MathTex("6 + 32 - ", "2").next_to(step3b_expr, DOWN, buff=0.3)

        # Highlight division
        step3b_expr[1].set_color(YELLOW)
        step3b_result[1].set_color(YELLOW)

        self.play(Write(step3b_expr))
        self.wait(1)
        self.play(Transform(step3b_expr[1], step3b_result[1]))
        self.wait(2)

        # Step 4: Addition and Subtraction (left to right)
        step4_title = Text(
            "4. Addition and Subtraction (left to right):", font_size=20, color=GREEN
        ).next_to(step3b_result, DOWN, buff=0.5)
        step4a_expr = MathTex("6 + 32", " - 2").next_to(step4_title, DOWN, buff=0.3)
        step4a_result = MathTex("38", " - 2").next_to(step4a_expr, DOWN, buff=0.3)

        # Highlight addition
        step4a_expr[0].set_color(GREEN)
        step4a_result[0].set_color(GREEN)

        self.play(Write(step4_title))
        self.play(Write(step4a_expr))
        self.wait(1)
        self.play(Transform(step4a_expr[0], step4a_result[0]))
        self.wait(1)

        # Final subtraction
        final_expr = MathTex("38 - 2").next_to(step4a_result, DOWN, buff=0.3)
        final_result = MathTex(
            "36", font_size=60, color=AS2700.Y14_GOLDEN_YELLOW
        ).next_to(final_expr, DOWN, buff=0.5)

        final_expr.set_color(GREEN)

        self.play(Write(final_expr))
        self.wait(1)
        self.play(Write(final_result))

        # Add emphasis to final result
        self.play(final_result.animate.scale(1.3), rate_func=there_and_back, run_time=1)

        # Show Fortran code implementation
        code_title = (
            Text("Fortran Implementation:", font_size=24, color=BLUE_C)
            .to_edge(LEFT, buff=0.5)
            .shift(UP)
        )

        fortran_code = """program pemdas_clear_example
    implicit none
    integer :: result
    
    ! Clear expression: 6 + 2*(3+1)^2 - 8/4
    result = 6 + 2 * (3 + 1)**2 - 8 / 4
    
    print *, "Expression: 6 + 2*(3+1)^2 - 8/4"
    print *, "Result:", result
    ! Output: Result: 36
end program pemdas_clear_example"""

        code = (
            Code(
                code_string=fortran_code,
                tab_width=4,
                background="window",
                language="Fortran",
            )
            .next_to(code_title, DOWN, buff=0.3)
            .to_edge(LEFT, buff=0.5)
            .scale(0.7)
        )

        self.play(Write(code_title))
        self.play(Write(code), run_time=3)

        # Add warning box
        warning = VGroup(
            Text(
                "✓ This example is unambiguous!", font_size=20, color=GREEN, weight=BOLD
            ),
            Text("Fortran follows PEMDAS correctly!", font_size=16, color=WHITE),
            Text("Always use parentheses for clarity!", font_size=16, color=WHITE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        warning_box = SurroundingRectangle(warning, color=GREEN, buff=0.3)
        warning_group = (
            VGroup(warning_box, warning).to_edge(RIGHT, buff=0.5).shift(DOWN)
        )

        self.play(Create(warning_box))
        self.play(Write(warning))

        self.wait(5)

        # Final fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)

        self.play(Write(step4_title))
        self.play(Write(step4a_expr))
        self.wait(1)
        self.play(Transform(step4a_expr[0], step4a_result[0]))
        self.wait(1)

        # Final subtraction
        final_expr = MathTex("53 - 4").next_to(step4a_result, DOWN, buff=0.3)
        final_result = MathTex(
            "49", font_size=60, color=AS2700.Y14_GOLDEN_YELLOW
        ).next_to(final_expr, DOWN, buff=0.5)

        final_expr.set_color(GREEN)

        self.play(Write(final_expr))
        self.wait(1)
        self.play(Write(final_result))

        # Add emphasis to final result
        self.play(final_result.animate.scale(1.3), rate_func=there_and_back, run_time=1)

        # Show Fortran code implementation
        code_title = (
            Text("Fortran Implementation:", font_size=24, color=BLUE_C)
            .to_edge(LEFT, buff=0.5)
            .shift(UP)
        )

        fortran_code = """program pemdas_example
    implicit none
    integer :: result
    
    ! Following PEMDAS order automatically
    result = 3 + 2 * (4 + 1)**2 - 8 / 2
    
    print *, "Expression: 3 + 2*(4+1)^2 - 8/2"
    print *, "Result:", result
    ! Output: Result: 49
end program pemdas_example"""

        code = (
            Code(
                code_string=fortran_code,
                tab_width=4,
                background="window",
                language="Fortran",
            )
            .next_to(code_title, DOWN, buff=0.3)
            .to_edge(LEFT, buff=0.5)
            .scale(0.7)
        )

        self.play(Write(code_title))
        self.play(Write(code), run_time=3)

        # Add warning box
        warning = VGroup(
            Text("⚠️ Important:", font_size=20, color=RED, weight=BOLD),
            Text("Fortran follows PEMDAS automatically!", font_size=16, color=WHITE),
            Text("Use parentheses for clarity!", font_size=16, color=WHITE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        warning_box = SurroundingRectangle(warning, color=RED, buff=0.3)
        warning_group = (
            VGroup(warning_box, warning).to_edge(RIGHT, buff=0.5).shift(DOWN)
        )

        self.play(Create(warning_box))
        self.play(Write(warning))

        self.wait(5)

        # Final fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)


class EvenOddExample(Scene):
    def construct(self):
        # Create a title
        title = (
            Text("Even or Odd Numbers")
            .scale(0.8)
            .set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED)
            .to_edge(UP, buff=0.5)
        )
        self.play(FadeIn(title, scale=0.8))

        # Create labels for even and odd numbers
        even_label = (
            Text("Even: mod(n, 2) == 0").scale(0.8).next_to(title, DOWN, buff=1)
        )
        odd_label = Text("Odd: mod(n, 2) /= 0").scale(0.8).next_to(even_label, DOWN)

        even_example = (
            MathTex("\\frac{4}{2} = 2 \\\\ \\text{ Remainder } = 0")
            .scale(1)
            .next_to(odd_label, DOWN, buff=1.2)
        ).set_color(RED)
        odd_example = (
            MathTex("\\frac{5}{2} = 2 \\\\ \\text{ Remainder } = 1")
            .scale(1)
            .next_to(odd_label, DOWN, buff=1.2)
        ).set_color(BLUE)

        # Animate the labels
        self.play(Succession(FadeIn(even_label), Write(even_example)))
        self.wait(2)

        # Animate the examples
        self.play(FadeOut(even_example, shift=0.1 * UP))
        self.play(Succession(FadeIn(odd_label), Write(odd_example)))
        self.wait(2)

        # Wait before ending the scene
        self.wait(2)


class CallToAction(Scene):
    def construct(self):
        # Create animated title
        title = Text(
            "Ready to Master Fortran?", font_size=42, color="#FFD700"
        )  # GOLD color
        title.to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=1.5)

        # Create subscribe button animation
        subscribe_button = RoundedRectangle(
            width=4,
            height=1.2,
            corner_radius=0.3,
            fill_color="#FF0000",
            fill_opacity=1,
            stroke_color="#FFFFFF",
            stroke_width=3,  # RED and WHITE
        )
        subscribe_text = Text(
            "SUBSCRIBE", font_size=32, color="#FFFFFF", font="Arial Bold"
        )  # WHITE, bold font
        subscribe_group = VGroup(subscribe_button, subscribe_text)
        subscribe_group.move_to(ORIGIN)

        # Bell icon animation (using text emoji)
        bell = Text("🔔", font_size=40).next_to(subscribe_group, RIGHT, buff=0.5)

        # Animate subscribe button with pulsing effect
        self.play(GrowFromCenter(subscribe_button), Write(subscribe_text), run_time=1.2)
        self.play(FadeIn(bell, scale=1.5), run_time=0.8)

        # Pulsing animation for emphasis
        self.play(
            subscribe_group.animate.scale(1.1).set_color("#FFFF00"),  # YELLOW
            bell.animate.scale(1.2),
            run_time=0.5,
        )
        self.play(
            subscribe_group.animate.scale(1 / 1.1).set_color("#FF0000"),  # RED
            bell.animate.scale(1 / 1.2),
            run_time=0.5,
        )

        # Next video preview
        next_video = (
            VGroup(
                Text("Next Video:", font_size=24, color="#0000FF"),  # BLUE
                Text(
                    "Order of Operations in Fortran", font_size=28, color="#FFFFFF"
                ),  # WHITE
                Text(
                    "(Avoid Calculation Mistakes!)", font_size=20, color="#FFA500"
                ),  # ORANGE
            )
            .arrange(DOWN, buff=0.2)
            .next_to(subscribe_group, DOWN, buff=1)
        )

        self.play(FadeIn(next_video, shift=UP), run_time=1.5)

        # Engagement prompts
        engagement = (
            VGroup(
                Text("👍 Like this video", font_size=24, color="#00FF00"),  # GREEN
                Text(
                    "💬 Share your Fortran questions", font_size=24, color="#0000FF"
                ),  # BLUE
                Text(
                    "🚀 Let's code together!", font_size=24, color="#800080"
                ),  # PURPLE
            )
            .arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            .to_edge(DOWN, buff=1)
        )

        self.play(
            AnimationGroup(
                *[FadeIn(item, shift=LEFT) for item in engagement], lag_ratio=0.3
            ),
            run_time=2,
        )

        # Final emphasis on subscribe
        self.play(
            Indicate(subscribe_group, color="#FFFF00", scale_factor=1.2),  # YELLOW
            run_time=1,
        )

        self.wait(3)

        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)


class Summary(Scene):
    def construct(self):
        # Create a title
        title = (
            Text("Summary of Fortran Basics")
            .scale(0.8)
            .set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED)
            .to_edge(UP, buff=0.5)
        )
        self.play(Write(title))
        self.wait()
        # Create a list of key points
        key_points = BulletedList(
            "Why Fortran? Legacy in scientific computing",
            "Integer data type: fundamental in programming",
            "Linting tools: catch potential errors",
            "Understanding compiler output: resolve errors effectively",
        )
        key_points.arrange(DOWN, buff=0.5, aligned_edge=LEFT).set_color(
            AS2700.Y14_GOLDEN_YELLOW
        )
        # Show first key point with a nice animation
        self.play(FadeIn(key_points[0], scale=0.8))

        # Instead of just waiting, animate the color of the first point
        # cycling through a range of colors to make it more engaging
        colors = [BLUE, GREEN, PURPLE, ORANGE, RED, YELLOW]

        for i in range(10):  # 10 color cycles, each taking 3 seconds total
            for color in colors:
                self.play(
                    key_points[0].animate.set_color(color),
                    run_time=0.6,
                    rate_func=smooth,
                )

        self.play(FadeIn(key_points[1], scale=0.8))

        for i in range(2):
            for color in colors:
                self.play(
                    key_points[1].animate.set_color(color),
                    run_time=0.7,
                    rate_func=smooth,
                )

        self.play(FadeIn(key_points[2], scale=0.8))

        for i in range(4):
            for color in colors:
                self.play(
                    key_points[2].animate.set_color(color),
                    run_time=0.8,
                    rate_func=smooth,
                )

        self.play(FadeIn(key_points[3], scale=0.8))

        for i in range(1):
            for color in colors:
                self.play(
                    key_points[3].animate.set_color(color),
                    run_time=0.8,
                    rate_func=smooth,
                )

        # Highlight each key point
        for point in key_points:
            self.play(point.animate.set_color(RED), run_time=0.5)
            self.wait(1)
            self.play(point.animate.set_color(AS2700.Y14_GOLDEN_YELLOW), run_time=0.5)
        self.wait()
        # Depois do último loop de destaque, você poderia adicionar:
        self.play(key_points.animate.scale(1.1).set_color(GREEN), run_time=1)
        self.play(
            key_points.animate.scale(1).set_color(AS2700.Y14_GOLDEN_YELLOW),
            run_time=0.5,
        )
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS} {SCENE}")
