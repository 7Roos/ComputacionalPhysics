**Personal Notes**
- [x] Write script for the video
- [x] Make animation in MANIM
- [x] Review the script
- [x] Record the audio
- [x] Adaptation of the time animations and audio generated
- [x] Write the code
- [x] Record the video
- [x] Edit the video
- [x] Upload the video
- [] Write the description
- [] Write the title
- [] Write the tags
- [] Draw the thumbnail
- [] Publish the video
- [] Create short resuming this content

# Integer
## Suggested Titles: 
- Variable Integers: Your Complete Beginner's Guide
- Mastering Integer Variables in Fortran (Easy Tutorial)
- Learn Integer Variables: A Step-by-Step Guide
- Unlocking the Power of Integers: A Beginner's Guide

## Future Videos
- Video 2 (Short): Order of Operations Hook: PEMDAS
    "Did you know that the order of operations in Fortran can lead to unexpected results? In this video, we’ll unravel the mysteries of operator precedence and how it affects your calculations." - The order of operations in Fortran: PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
- Video 3: Integer intrinsic functions
    - Video 3.1: Question Hook: kind and select_integer
        When 4 bytes are no longer sufficient. Expanding the size of an integer. Factors affecting data type selection: Memory usage and speed
    - Video 3.2: Intriguing Statement Hook: cubic root of a negative number
        "Choosing the right data type in Fortran can mean the difference between a flawless program and a frustrating bug. This video reveals the hidden complexities of integer and real variables and how to avoid common pitfalls." - cubic root of a negative number - if the number is integer, declare it as integer and not real.
    - Video 3.3: Contour periodic conditions with mod function
        "In Fortran, understanding contour periodic conditions is crucial for accurate simulations. This video will guide you through the intricacies of setting up and managing these conditions effectively through the mod function."

## Introduction
Unlock the potential of programming with a solid understanding of integer variables. This video provides a beginner-friendly guide, equipping you with the knowledge and confidence to build your coding skills.

## We need to count objects
Counting objects has been a fundamental task since the dawn of human civilization. From ancient societies to modern times, counting has been essential for trade, agriculture, and record-keeping. 

[V] Imagem salva em downloads

To accomplish this, we define the set of natural numbers, denoted by the letter N. There is considerable debate about whether the set of natural numbers includes zero or not. Some argue that natural numbers should start from 1, because they are used to count objects—you don't start counting "zero oranges, one orange, two oranges". In general convention, the set of natural numbers starts from 0, unless we indicate with an asterisk (*) that we are excluding zero.

**Animation created as NaturalNumbers**
```python
from manim import *
class NaturalNumbers(Scene):
    def construct(self):
         # Add a label for the set of natural numbers
        natural_numbers_label = MathTex(r"\mathbb{N}").scale(2).to_edge(UP, buff=1).set_color(AS2700.Y14_GOLDEN_YELLOW)
        self.play(Write(natural_numbers_label))

        # Create a number line
        number_line = NumberLine(x_range=[-1, 10, 1], length=10, color=BLUE)
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
            self.play(FadeIn(label, shift=0.1*DOWN), run_time=0.5)
        self.wait(2)
```

### Sum
Within this set, we can perform addition, the most basic operation in mathematics. For example, if we have 2 oranges and add 3 more, we will have a total of 5 oranges. In other words, addition is simple and intuitive, allowing us to count objects easily.

**Animation created in MANIM**
```python
from manim import *
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
        oranges = VGroup(two_oranges, three_oranges).arrange(
            RIGHT, buff=1, aligned_edge=DOWN
        ).to_edge(DOWN, buff=1)

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
                lag_ratio=0.3
            )
        )

        self.play(Write(plus), run_time=0.5)
        self.play(
            AnimationGroup(
                FadeIn(three_oranges[0], shift=DOWN),
                FadeIn(three_oranges[1], shift=DOWN),
                FadeIn(three_oranges[2], shift=DOWN),
                FadeIn(three),
                lag_ratio=0.3
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
            count_num = Text(str(i+1), font_size=25, color=BLACK, weight=BOLD)
            count_num.move_to(orange.get_center()).shift(0.1*DOWN)
            
            self.play(
                Create(circle),
                FadeIn(count_num, scale=1.5),
                run_time=0.5
            )
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
            run_time=2
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
            formatter_style=Code.get_styles_list()[16]
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
            run_time=0.8
        )
        
        # Destacar o resultado final
        self.play(
            result.animate.scale(1.5).set_color(GREEN),
            run_time=1
        )
        
        self.wait(3)

        # Final fade out de tudo
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )
        self.wait()
```

### Product
Specifically, we can organize objects in groups, where the result will be the multiplication of the number of objects in each group by the number of groups. For example, if we have 2 oranges in each group and 3 groups, we will have a total of 6 oranges. This is a simple and efficient way to count objects, especially when dealing with large quantities.

**Animation created in MANIM**
```python
from manim import *
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

        code.to_edge(LEFT, buff=0.4).shift(0.5*UP)

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
```

### Division
It is natural to define the division operation. For example, if we have 6 oranges and divide them into 2 groups, we will have 3 oranges in each group. This simple example might lead to the incorrect conclusion that division is the inverse of multiplication. In fact, division can seem like the inverse of multiplication in several situations. Let's look at another example: I can multiply 2 oranges by 0, resulting in 0. If I divide 0 by 2 oranges, I will also have 0. But if I divide 2 oranges by 0, I will have an undefined number of oranges. The key point is that division is not commutative—the order of numbers matters—while multiplication is commutative.

**Animation created in MANIM**
```python
from manim import *
class DivisionExample(Scene):
    def construct(self):
        # Import orange SVG image
        orange_image = SVGMobject("assets/orange-svgrepo-com.svg").scale(0.5)

        # Title of operation
        title = Text("Division", font_size=36, color=AS2700.Y14_GOLDEN_YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
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
            )
        )

        # Create labels for the division
        dividend = MathTex("6").to_edge(DOWN, buff=1).shift(LEFT)
        divide = MathTex("\\div").next_to(dividend, RIGHT, buff=0.6).scale(1.2)
        divisor = MathTex("2").next_to(divide, RIGHT, buff=0.6)
        equals = MathTex("=").next_to(divisor, RIGHT, buff=0.6).scale(1.2)
        result = MathTex("3").next_to(equals, RIGHT, buff=0.6).scale(1.2)
        self.play(Write(dividend), Write(divide), Write(divisor), run_time=0.5)

        # Divide oranges into groups
        groups = VGroup()
        for i in range(0, total_oranges, 3):  # Split into 2 groups of 3
            group = VGroup(*[orange_group[j].copy() for j in range(i, i + 3)])
            group.arrange(UP, buff=0.3)
            groups.add(group)

        groups.arrange(RIGHT, buff=1.5).to_edge(RIGHT, buff=1)

        # Animate division by showing groups
        self.play(Transform(orange_group, groups), run_time=2)

        # Add brackets to show the result of division (3 per group)
        for i, group in enumerate(groups):
            bracket = Brace(group, LEFT)
            self.play(GrowFromCenter(bracket), run_time=0.7)

        # Show the result
        self.play(FadeIn(equals), FadeIn(result))

        # Add programming example
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

        # Highlight the result
        self.play(result.animate.scale(1.4).set_color(GREEN), run_time=1)

        self.wait(3)

        # Final fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait()
```

### Integer Division with Remainder
While addition always produces a result within the set of natural numbers, division can lead to results outside this set. For example, if we divide 7 oranges by 3, we will have a fraction of oranges. You'd get zero whole oranges with a remainder of 1. In other words, we have a remainder from the division, which is very important in certain problems, and we'll return to this point in the future.

**Animation created in MANIM**
```python
from manim import *
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

        # Create labels for the division
        dividend = MathTex("7").to_edge(DOWN, buff=1).shift(LEFT)
        divide = MathTex("\\div").next_to(dividend, RIGHT, buff=0.6).scale(1.2)
        divisor = MathTex("3").next_to(divide, RIGHT, buff=0.6)
        equals = MathTex("=").next_to(divisor, RIGHT, buff=0.6).scale(1.2)
        result = MathTex("2 \\text{ R } 1").next_to(equals, RIGHT, buff=0.6).scale(1.2)
        self.play(Write(dividend), Write(divide), Write(divisor), run_time=0.5)

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

        # Show the result
        self.play(FadeIn(equals), FadeIn(result))

        # Add programming example
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

        # Highlight the result
        self.play(result.animate.scale(1.4).set_color(GREEN), run_time=1)

        self.wait(3)

        # Final fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait()
```

## Integer numbers - definition
Indeed, our problems require another operation: subtraction. However, not every subtraction yields natural numbers. We need to define a new set of numbers that includes negative values. This set is called the set of integers, usually denoted by the letter Z, which includes natural numbers, their negative counterparts, and zero.

**Animation created in MANIM**
```python
from manim import *
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
```

### Integer numbers - operations
In other words, we extend the set of natural numbers to include negative numbers; all operations valid for natural numbers remain valid for integers. The set of integers is a superset of natural numbers, meaning that all natural numbers are also integers, but the reciprocal is not always true. Therefore, in programming languages such as Fortran, the integer data type is used to represent whole numbers, both positive and negative. This allows us to perform arithmetic operations on integers, including addition, subtraction, multiplication, and division.

**Animation created in MANIM listing these operations**
```python
from manim import *
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
                Write(example_addition),
                Create(box_addition),
                FadeIn(operations[0][1], shift=0.1 * UP),
                Write(example_subtraction),
                FadeIn(operations[1], shift=0.1 * UP),
                Create(box_subtraction),
                Write(example_multiplication),
                FadeIn(operations[2], shift=0.1 * UP),
                Create(box_multiplication),
                Write(division_example),
                Create(box_division),
                lag_ratio=0.5,
                run_time=3,
            ),
            rate_functions=smooth,
        )
        self.wait(2)
```

### Integer Numbers in Scientific Computing
But it doesn't stop there. Integer numbers are used for indexing loops, arrays, and other structures. A loop is a repetition structure — a way to repeat a set of instructions multiple times. For example, if we want to calculate the sum of the first 10 natural numbers, we can use a loop to iterate from 1 to 10 and add each number to a running total. The loop index is typically an integer variable that keeps track of the current iteration. In another example, we use integer variables to index a matrix, identifying the row and column of each element. This is important because matrices are often used to represent data in scientific computing, allowing us to perform complex calculations efficiently through vectorization. In general, a integer number occupies 4 bytes in memory, in some cases 8 bytes, depending on the architecture of the computer. This means that we can store a wide range of integer values. In constrast, the real number data type occupies 8 bytes in memory, which allows us to store decimal numbers, or 16 bytes for double precision in scientific computing. Because of this, that we say that the integer data type might offer better performance in some cases, especially when we are dealing with large datasets. 

**Animation created in MANIM**
```python
from manim import *
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
        self.play(FadeIn(max_label, scale=0.8))
        self.play(FadeIn(loop_label, scale=0.8))
        self.wait(2)
```

To sum up, although it may seem simple, the integer data type is a fundamental concept in programming, especially for representing discrete values within scientific computations.

## 🔔 Subscribe for More Scientific Computing! 

**Mid-Video Call to Action (CTA) - Perfect timing for engagement!**

Before we delve into the specifics of Fortran, if you find it useful: press the sign up button and give a like! We’re about to get into the actual programming part - and you won’t want to miss our upcoming videos on matrices, loops and advanced scientific computing techniques. What is your biggest challenge with programming languages? Leave in the comments!

**Quick CTA Animation in MANIM**
```python
from manim import *
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
```

---

## Arithmetic Operations with Scientific Computing Languages
In any scientific computing language decent, we can perform arithmetic operations with integers using the following operators: Addition, with the plus sign, as in mathematics. Subtraction, with the minus sign, as in mathematics too. Multiplication, with the asterisk, instead of the letter 'x' or dot. Division, with the forward slash, as in mathematics. And  Exponentiation, with the double asterisk, instead of the superscript notation used in mathematics.

**Animation created in MANIM about these operations**
```python
from manim import *
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
```

## PEMDAS - Order of Operations
Each language has its own syntax, but in general, the arithmetic operations are similar across languages. Just like in mathematics, we can combine these operations to perform more complex calculations. Then comes the question: what is the order of operations? In general, is obeyed the acronym PEMDAS, which stands for Parentheses, Exponents, Multiplication, Division (from left to right), Addition and Subtraction (from left to right too). 

**Animation created in MANIM about the PEMDAS**
```python
from manim import *
class OrderOfOperations(Scene):
    def construct(self):
        # Create a title
        title = (
            Text("Order of Operations: PEMDAS")
            .scale(0.8)
            .set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED)
            .to_edge(UP, buff=0.5)
        )
        self.play(Write(title))

        # Create the acronym PEMDAS vertically
        # Create labels for each operation
        DropCap = 70
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
                    Text("XPONENTS", font="Coelacanth", font_size=20),
                ).arrange(RIGHT, buff=DropCap_buff, aligned_edge=DOWN),
                VGroup(
                    Text(
                        "M",
                        font="Coelacanth",
                        font_size=DropCap,
                        color=AS2700.Y14_GOLDEN_YELLOW,
                    ),
                    Text("ULTIPLICATION", font="Coelacanth", font_size=20),
                ).arrange(RIGHT, buff=DropCap_buff, aligned_edge=DOWN),
                VGroup(
                    Text(
                        "D",
                        font="Coelacanth",
                        font_size=DropCap,
                        color=AS2700.Y14_GOLDEN_YELLOW,
                    ),
                    Text("IVISION", font="Coelacanth", font_size=20),
                ).arrange(RIGHT, buff=DropCap_buff, aligned_edge=DOWN),
                VGroup(
                    Text(
                        "A",
                        font="Coelacanth",
                        font_size=DropCap,
                        color=AS2700.Y14_GOLDEN_YELLOW,
                    ),
                    Text("DDITION", font="Coelacanth", font_size=20),
                ).arrange(RIGHT, buff=DropCap_buff, aligned_edge=DOWN),
                VGroup(
                    Text(
                        "S",
                        font="Coelacanth",
                        font_size=DropCap,
                        color=AS2700.Y14_GOLDEN_YELLOW,
                    ),
                    Text("UBTRACTION", font="Coelacanth", font_size=20),
                ).arrange(RIGHT, buff=DropCap_buff, aligned_edge=DOWN),
            )
            .arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            .to_edge(LEFT, buff=1.5)
        )

        for label in operations:
            self.play(FadeIn(label))

        # Wait before ending the scene
        self.wait(2)
```

### Note on Precedence
Despite this, the programming languages might have different order of precedence. There are the choose of memorize the rules. But, it is not good idea, the good practice is to use parentheses to impose your own order of operations. This avoids confusion and ensures that your calculations are performed in the intended order.

## Even or Odd Numbers
These arithmetic operations are very basic, but that's exactly why they are so important and we need to understand them well, because they are in the heart of several more complex operations. For example, the rest of the division might be used to determine if a number is even or odd, or then to apply the contour periodic condition vital for simulation of physical systems. Exist many other examples and operations, but to go to into details, we should choose a language.

**Animation created in Manim: even or odd**
```python
from manim import *
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
        even_label = Text("Even: n % 2 == 0").scale(0.8).next_to(title, DOWN, buff=1)
        odd_label = Text("Odd: n % 2 != 0").scale(0.8).next_to(even_label, DOWN)

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
```

## Arithmetic Operations in Fortran
For example, we perform these operations in this code:
```fortran
! This is a comment line in Fortran, which is ignored by the compiler.
! The exclamation mark is a reserved symbol for comments in Fortran.
program arithmeticOperations
   print *, "|| Arithmetic Operations with Integers in Fortran ||"
   print *, " - Addition: 2 + 3 =       ", 2 + 3
   print *, " - Subtraction: 5 - 2 =    ", 5 - 2
   print *, " - Multiplication: 4 * 3 = ", 4 * 3
   print *, " - Division: 10 / 2 =      ", 10 / 2
   print *, " - Exponentiation: 2 ** 3 =", 2 ** 3

   print *, " | Special cases: |"
   print *, " This is a continuation line in 'Fortran' &
   & which is used to split long lines."
   print 10, "Exp negative base: -2 ** 2 =", -2 ** 2
   print 10, "Exp negative base: (-2) ** 2 =", (-2) ** 2
   print 11, "Denominator > numerator: 3 / 4 =", 3 / 4, &
   & ', rest =', mod(3, 4)
   print 11, "Denominator = numerator: 4 / 4 =", 4 / 4, &
   & ', rest =', mod(4, 4)
   print 11, "Denominator < numerator(not multiple): 5 / 4 =", 5 / 4, &
   & ', rest =', mod(5, 4)
   print 11, "Denominator < numerator(multiple): 8 / 4 =", 8 / 4, &
   & ', rest =', mod(8, 4)

   print *, " | Error cases: |"
   print *, " - Division by zero: 10 / 0 = ", 10 / 0
   print *, " - Multiplication: 4 * -3 = ", 4 * -3
   print *, " - Undefined variable: 2 + j =", 2 + j
10 format ('->', A47, I3)
11 format ('->', A47, I3, A8, I3)
end program arithmeticOperations
```
We define a program called 'arithmeticOperations' through the 'program' keyword and end it with the 'end program' statement. 

### Basic operations
In the first block, we demonstrate the basic arithmetic operations using integers in Fortran. The 'print' statement is used to display the output, and we can see how each operation works with integer values. The asterisk after 'print' indicates that we are using the formatting standard.

To see the result, we need to compile and run the program. In the terminal, we can use the command 'gfortran Fortran_InDepth.f90' to compile the program; use the Tab key to autocomplete the name of the file. If there are no errors, an executable file named 'a.out' will be created. To run the program, we simply type './a.out' in the terminal and press 'Enter'. The output will display the results of the arithmetic operations. As we can see on the screen, all operations are performed correctly, and the results are displayed as expected with integer values.

### Special cases 
#### Reserved Words and Symbols in Fortran
It is important to point out that not all tokens are allowed in programming languages, and Fortran is not exempt from this rule. For example, there are reserved symbols that cannot be used as variable names, such as the exclamation mark, which is used to indicate a comment. As we see at the top of our code, everything written to the right of this symbol is ignored by the compiler. 

In the second block, we explore some special cases in arithmetic operations. Another example of reserved symbols is the ampersand, which is used to indicate a continuation line when a statement is too long to fit on a single line. Another example is the use of double quotation marks, which are used to indicate a string when used in pairs. If you want to use quotation marks within a string, you can use single quotation marks instead and leave the double quotation marks for the string delimiter, and vice-versa. We're going to see this by compiling and running the program again, but commenting out the first block and uncommenting some lines in the second block.

Other cases concern formatting, such as special characters like hash (#), percent (%), and dollar ($). Other languages are more flexible in this regard, such as Julia, which allows the use of LaTeX syntax, for example. Indeed, it's worth noting that there are other rules, such as maximum line length and number of lines in a program, but we are not going to cover them in this video and will leave them for future content.

#### Negative Base in Exponentiation
If we use a negative base in exponentiation, we can have different results depending on whether we use parentheses or not. For example, if we write minus 2 double asterisk 2 without parentheses, we will have a negative result, which is minus 4. This is because the exponentiation operator (double asterisk) has higher precedence than the negation operator, so it's interpreted as minus (2 to the power of 2) equals minus 4. However, if we use parentheses around the base, (minus 2) double asterisk 2, we will have a positive result, which is 4. Thus, to avoid ambiguity, it is good practice to use parentheses to clarify the intended operation. This is especially important with exponentiation operations.

The number 10 in the print statement identifies label 10 in the format statement, which is used to format the output. The letter 'A' indicates that we are printing a string, and the number 47 indicates the field width for the string. The letter 'I' indicates that we are printing an integer, and the number 3 indicates the field width for the integer. Therefore, we can automatically format the output of several print statements in the program, which is good practice to ensure that the output is consistent and easy to read.

#### Division with Integer Numbers
Now, we explore four cases of division with integer numbers. When the denominator is greater than the numerator, we will have a result of zero because we are performing integer division. So, be careful! Indeed, we see a marking on the number 3. If we hover the mouse over it, we can read the warning: 'Integer division truncated to constant 0'. This warning is also present in the 'Problems' tab. When we click on it, we can read the same message. What's generating this? It's the 'Modern Fortran' extension, which precompiles our code, searches for syntax errors, and warns us before compilation. In this case, as we can see on the screen, the remainder of the division is the numerator itself.

The second example shows that if the denominator is equal to the numerator, we will have a result of one with a remainder of zero, as expected. 

The third example shows that if the numerator is greater than the denominator and not a multiple of it, we will have a result of one (the integer part). Again, the 'Modern Fortran' linter warns us: 'Integer division truncated to constant 1'.

The last example of division shows that if the numerator is greater than the denominator and is a multiple of it, we will have a result greater than one, which is the exact result of the division, and a remainder of zero. 

In these examples, we use the label formatting 11 defined at line 30.

### Error cases
But trouble in paradise has appeared! In the last block, we're going to see some error cases. In other words, declarations that are illegal or problematic.

Division by Zero: To begin with an undefined mathematical operation, division by zero is not allowed. The linter warns us: 'Division by zero'. When we try to compile, it results in an error. The compiler informs us why it stopped: 'Error: Division by zero at 1' and marks it with a red number below line 10, indicating the line and specifically the column where the error occurred.

Invalid Token Sequences: Now that we know how to read this kind of error, let's go to the next example: two or more conflicting tokens in the same operation. In this case, we have a multiplication symbol followed by a minus symbol, which creates ambiguity in Fortran - it's not immediately clear whether this is multiplication followed by a negative number or some other intended operation. The linter warns us: 'Extension: Unary operator following arithmetic operator (use parentheses) at (1)'. In this case, not only does it warn us about the error, but it also shows us how to resolve it: 'use parentheses'. 

Undefined Variables: In the last example, we try to use an undefined variable (J) in an arithmetic operation. In this case, no error is triggered during compilation, but when running the program, the result is a random number. This error is more subtle. What is the J variable? We don't know, and neither does the compiler initially. It's a variable that was not explicitly defined in the program. Due to Fortran's implicit typing rules, the compiler assumes 'J' is an integer variable (since it starts with a letter between I-N) and assigns it some arbitrary value from memory. Therefore, always define your variables before using them to avoid unexpected results. In Fortran, there's a good practice of using the 'implicit none' command, which might be challenging for beginners. Therefore, we will explain it in the next video, due to the importance of this command in Fortran programming.

## Summing: why Fortran?
To sum up.
- Why Fortran? Its enduring legacy in scientific computing and continued relevance today? Firstly, Fortran is a language that has been around for decades and has a strong presence in the scientific computing community. It is known for its efficiency and performance, making it a popular choice for numerical simulations and high-performance computing tasks. In great part, this is due to the early limitations and the importance of efficient memory usage in the context of limited computer resources at the beginning of programming. There are more than 5 decades of history and improvement of the language. 
- Despite being a simple type, the integer data type is fundamental in programming, serving as the foundation for more complex operations, data structures, and providing key performance optimizations in several cases. 
- The linting tools, such as the 'Modern Fortran' extension, are essential for catching potential errors and improving code quality. They help ensure that the code adheres to best practices and standards, making it easier to maintain and understand.
- Knowing how to interpret the output of the compiler and the linter is crucial for resolving errors and warnings effectively. Understanding the error messages and warnings helps programmers identify: potential runtime errors at compile time, deprecated or dangerous practices, performance optimization opportunities, and standards compliance issues.
We are done!
**Create an animation in Manim: summarize the video**
```python
from manim import *
class SummaryAnimation(Scene):
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
        key_points.arrange(DOWN, buff=0.5, aligned_edge=LEFT).set_color(AS2700.Y14_GOLDEN_YELLOW)
        self.play(FadeIn(key_points, scale=0.8))
        self.wait(2)
        # Highlight each key point
        for point in key_points:
            self.play(point.animate.set_color(RED), run_time=0.5)
            self.wait(1)
            self.play(point.animate.set_color(AS2700.Y14_GOLDEN_YELLOW), run_time=0.5)
        self.wait(2)
        # Depois do último loop de destaque, você poderia adicionar:
        self.play(key_points.animate.scale(1.1).set_color(GREEN), run_time=1)
        self.play(key_points.animate.scale(1).set_color(AS2700.Y14_GOLDEN_YELLOW), run_time=0.5)
        self.wait(2)
```

# Short: PEMDAS as rule of precedence
Title: Order of Operations in Programming: PEMDAS 
Description: In this short video, we explore the order of operations in programming languages, following the PEMDAS rule. We explain how parentheses, exponents, multiplication, division, addition, and subtraction are prioritized in calculations. Understanding this order is crucial for writing correct and efficient code.


# Understanding the implicit none command
Title: Fortran's implicit none: Why Every Beginner NEEDS This Command
## Implicit Declaration of Integer Variables
In the last video, we discussed the integer data type in Fortran. We also performed basic arithmetic operations with integers, as we see on the screen.
```fortran
program arithmeticOperations
    print *, "Arithmetic Operations with Integers in Fortran"
    print *, "Addition: 2 + 3 =", 2 + 3
    print *, "Subtraction: 5 - 2 =", 5 - 2
    print *, "Multiplication: 4 * 3 =", 4 * 3
    print *, "Division: 10 / 2 =", 10 / 2
    print *, "Exponentiation: 2 ** 3 =", 2 ** 3
end program arithmeticOperations
```
However, we didn't discuss how to declare variables in Fortran. In fact, we didn't even mention the concept of variables. In this video, we will explore the concept of variables and how they are used in Fortran. Indeed, we will clarify the concept of implicit none in Fortran and why it is a good practice. Of course, in general we can't program directly using only print statements. We can use variables, which are essentially labels for memory addresses. In other words, we store values in memory as integer numbers. But we don't need to know or manipulate these memory addresses directly. We can use variable names to refer to the values stored in those memory locations, and Fortran takes care of memory management for us. This is a fundamental concept in programming, as it allows us to focus on the logic of our code rather than the underlying details of the hardware, which was the main goal of the Fortran language. 

**Animation created in Manim: illustrate the memory and address**
```python
from manim import *
class VariableMemoryExample(Scene):
    def construct(self):
        # Create a title
        title = Text("Variable Memory Example", font_size=36)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)

        # Create a variable 'i' and show its memory address
        i_label = Text("i", font_size=28).shift(LEFT)
        i_value = Text("2", font_size=28).next_to(i_label, RIGHT)
        i_memory = Text("Memory: 0x1234", font_size=28).next_to(i_value, RIGHT)
        self.play(Write(i_label), Write(i_value), Write(i_memory))
        self.wait(1)

        # Create a variable 'j' and show its memory address
        j_label = Text("j", font_size=28).shift(LEFT)
        j_value = Text("3", font_size=28).next_to(j_label, RIGHT)
        j_memory = Text("Memory: 0x5678", font_size=28).next_to(j_value, RIGHT)
        self.play(Write(j_label), Write(j_value), Write(j_memory))
        self.wait(1)

        # Show the addition operation
        addition = Text("i + j", font_size=28).next_to(j_memory, DOWN)
        self.play(Write(addition))
        self.wait(1)

        # Show the result
        result = Text("Result: 5", font_size=28).next_to(addition, DOWN)
        self.play(Write(result))
        self.wait(1)

        # Fade out all elements
        self.play(FadeOut(title), FadeOut(i_label), FadeOut(i_value), FadeOut(i_memory),
                  FadeOut(j_label), FadeOut(j_value), FadeOut(j_memory),
                  FadeOut(addition), FadeOut(result))
        self.wait(1)
```

For example, we can assign the value 2 to the variable 'i' and the value 3 to the variable 'j', and then use these variables in our calculations. Reorganizing the code:
```fortran
program arithmeticOperations
    i = 2
    j = 3
    print *, "Arithmetic Operations with Integers in Fortran"
    print *, "Addition: ", i + j
    print *, "Subtraction: ", i - j
    print *, "Multiplication: ", i * j
    print *, "Division: ", i / j
    print *, "Exponentiation: ", i ** j
end program arithmeticOperations
``` 
Now, to update the values, we just change the values of 'i' and 'j', without needing to change the rest of the code. This is a powerful feature of programming languages, allowing us to write more flexible and maintainable code. Another issue we need to pay attention to is the equal sign, which does not have the same meaning as the mathematical equal sign. In general, in programming languages, the equal sign is used to assign a value to a variable, not to indicate equality. This will become clearer in the future when we discuss logical operations and repetition structures. This difference is necessary in programming because the nature of the work is different. In mathematics, we abstract the problem and work with variables, and only at the end do we assign values. However, analytical solutions are not always possible, and we need to use numerical methods to perform calculations or simulate problems. Computers are specially designed to work with numbers: storing, reading, and performing arithmetic operations on numerical values. In Fortran, it is not possible to use symbolic operations as humans do, though Python, for example, allows this. In Fortran, we need to use variables to store values and then perform operations with them. This represents a fundamental difference between programming languages and mathematics.

## Explicit Declaration of Integer Variables
### Replace Variable Names
Consistent variable names and coding conventions are crucial in programming for several reasons. They enhance code readability, making it easier for developers to understand and maintain the code. When variable names are descriptive and follow a consistent naming scheme, it reduces confusion and helps prevent errors. Additionally, adhering to coding conventions promotes collaboration among team members, as everyone can quickly grasp the code structure and logic. Let's consider replacing the variable names 'i' and 'j' with more meaningful names, such as 'a' and 'b'. When we compile and run the program again, we see that the results are the same mathematically, but now there are several zeros on the screen, meaning that the output is now a real number. 

## Implicit Declaration of Variables
This is not random. What's happening is that Fortran is implicitly assuming that these variables are real numbers. In other words, all variables that start with letters of the alphabet from 'i' to 'n' are considered integer numbers, while all other letters are considered real numbers. This convention was established in the early days of Fortran and has been carried over into modern versions of the language. However, this implicit declaration can lead to confusion and errors, especially for beginners. To avoid this, it is recommended to use explicit declarations for all variables, specifying their data types clearly. This not only improves code readability but also helps prevent unintended type conversion, errors during runtime, and allows more freedom in the choice of variable names. In Fortran, we can use the 'implicit none' statement at the beginning of our program to disable implicit declarations. This forces us to explicitly declare all variables, which is a good practice for writing clear and maintainable code. For example, we can declare the variables 'a' and 'b' as integers using the 'integer' keyword and separate them by double colons:
```fortran
program arithmeticOperations
    implicit none
    integer :: a, b
    a = 2
    b = 3
    print *, "Arithmetic Operations with Integers in Fortran"
    print *, "Addition: ", a + b
    print *, "Subtraction: ", a - b
    print *, "Multiplication: ", a * b
    print *, "Division: ", a / b
    print *, "Exponentiation: ", a ** b
end program arithmeticOperations
```
When we compile and run the program again, we see that now the output is an integer number, as it was with the 'i' and 'j' variables. In this sense, we can say that Fortran is a strongly typed language, meaning that variables must be declared with their specific data types before they can be used. Indeed, this typing is static, meaning that the data type of a variable is determined at compile time and cannot change during program execution. In contrast, dynamically typed languages like Python allow variables to change types at runtime, which can lead to more flexibility but also potential errors if not managed carefully. The introduction of the "INTEGER" keyword in Fortran 4 marked a significant advancement in the language's ability to handle integer variables. This enhancement allowed programmers to explicitly declare integer variables, providing greater control over data types and improving code clarity. By using the "INTEGER" keyword, developers could specify the exact nature of their variables, reducing ambiguity and potential errors in calculations. This change laid the foundation for more robust programming practices in Fortran, enabling developers to write clearer and more maintainable code.

To sum up, the 'implicit none' statement is a good practice in Fortran programming because it avoids ambiguity and potential errors in variable declarations. On one hand, it forces us to explicitly declare all variables. On the other hand, it gives us more freedom in the choice of variable names, as we can use any letter of the alphabet without worrying about implicit declarations. This is particularly useful when we want to use descriptive variable names that are not limited to the letters 'i' to 'n'. 
We are done!

# Constants in Fortran
## Resume last video
In the last video, we addressed the concept of implicit none, the famous command in Fortran and maybe strange for beginner students/programmers. Fortran is a language of freedom; the user decides how to use it. You can choose whether to declare all variables or not. Indeed, the Fortran language offers many tools to manipulate variables. 

## Introduction
For example, we can use the 'parameter' keyword to define constants, which are variables that cannot be changed during program execution. This is useful for defining fixed values that are used throughout the program, such as physical constants or configuration parameters (array size, loop index limits). Indeed, it is helpful to calculate some parameters of a system. For example, in a system of spins with two states, we can define the number of spins and the number of accessible states for the system using parameters, without the need to change the code every time and/or calculate it manually (that leads to errors). 

## Example of Constants in Fortran: spins
In this example, we define a constant 'minConfig' with a value of 2, representing the number of states of a single spin (up and down), and 'Ns' with a value of 4, representing the number of spins. To determine the number of accessible states for the system, we raise 'minConfig' to the power of 'Ns', which results in 16. Note that we use the 'write' statement to print the result, which is a more flexible way to format the output. The 'write' statement allows us to specify the format of the output and the device to which we want to write the output, which might be the screen or a data file. In this case, we use the asterisk symbol to indicate that we want to write to the default output device, which is usually the screen, with standard formatting.
```fortran
program arithmeticOperations
    implicit none
    integer, parameter :: minConfig = 2
    integer, parameter :: Ns = 4
    integer, parameter :: Nc = minConfig ** Ns

    write(*,*) "For a system of spins with two states and", Ns, "spins"
    print *, "The number of accessible states for the system is", Nc
end program arithmeticOperations
```
## Parameter can't be changed
Now, we test a functionality of the parameter attribute that is very useful: protecting the value of a variable against changes. If we try to change the value of 'minConfig' or 'Ns' after the declaration, we will get an error, as we see on the screen. 
This is because the 'parameter' keyword indicates that these variables are constants and cannot be modified. This is a good practice in programming, as it helps to avoid accidental changes to important values in the code, which can lead to unexpected behavior or errors.

## Parameters have to be initialized
It is important to note that the 'parameter' keyword requires the variable to be initialized at the time of declaration. This means that we cannot declare a parameter without assigning it a value. If we try to declare a parameter without initializing it, we will get an error. This is because the 'parameter' keyword is used to define constants, and constants must have a fixed value that does not change during program execution. If we attempt to declare a parameter without initializing it, the compiler will not know what value to assign to it, leading to ambiguity. Thus, our friend, the compiler, warns us about this mistake before we run the program.

## Resume
To sum up, the 'parameter' keyword together with type declaration of variables in Fortran allows us to define constants that cannot be changed during program execution, which helps to avoid accidental changes to important values in the code. Therefore, the 'parameter' keyword requires the variable to be initialized at the time of declaration. This is useful for defining fixed values that are used throughout the program, such as physical constants or configuration parameters like array size, loop index limits, etc. This is a good practice in programming, as it helps to avoid accidental changes to important values in the code, which can lead to unexpected behavior or errors that are very hard to find.
We are done!

# Intrinsic Functions
## Introduction
Many programming languages offer built-in functions to manipulate variables. 

## Module of the number
For example, in Fortran, we have the 'abs' function, which returns the absolute value of an integer. This is useful when we want to ensure that a number is positive, regardless of its original sign.
```fortran
program absoluteValue
    implicit none
    integer :: a, b
    a = -5
    b = abs(a)
    print *, "The absolute value of", a, "is", b
end program absoluteValue
```
In this example, we assign the value minus 5 to the variable 'a', and then we use the 'abs' function to calculate its absolute value, which is stored in the variable 'b'. The output will show that the absolute value of minus 5 is 5. This functionality is similar to the modulus function in mathematics, indicated by a pair of vertical bars, which also returns the absolute value of a number.

## Remainder of Division
Another useful function is the 'mod' function, which returns the remainder of a division operation. This is particularly useful when we want to determine if a number is even or odd, as we mentioned earlier.
```fortran
program modulusExample
    implicit none
    integer :: a, b, c
    a = 10
    b = 3
    c = mod(a, b)
    print *, "The remainder of", a, "divided by", b, "is", c
end program modulusExample
```
In this example, we assign the value 10 to the variable 'a' and 3 to the variable 'b'. We then use the 'mod' function to calculate the remainder of the division of 'a' by 'b', which is stored in the variable 'c'. The output will show that the remainder of 10 divided by 3 is 1. This is useful for determining if a number is even or odd, as we can check if the remainder is 0 (even) or 1 (odd).

## Maximum Value Between Two Integers
We can also use the 'max' function to find the maximum value between two or more integers. This is useful when we want to compare values and determine the largest one. 
```fortran
program maxExample
    implicit none
    integer :: a, b, c
    a = 5
    b = 10
    c = max(a, b)
    print *, "The maximum value between", a, "and", b, "is", c
end program maxExample
```
In this example, we assign the value 5 to the variable 'a' and 10 to the variable 'b'. We then use the 'max' function to find the maximum value between 'a' and 'b', which is stored in the variable 'c'. The output will show that the maximum value between 5 and 10 is 10. This is useful for comparing values and determining the largest one. The analogous function to find the minimum value is 'min', which works similarly to 'max'.

## Summary
To sum up: Built-in functions like 'abs', 'mod', and 'max' enhance code functionality and simplify common operations. We are done!

# Learning as choose the kind appropriate
📺 "Integer Kind in Fortran: Memory, Performance & Portability"


# Video 2: PEMDAS it is wrong
## Define the problem
The set integer, we can perform the addition operation, which is the most basic operation in mathematics. For example, if we have 2 oranges and add 3 more, we will have a total of 5 oranges. In other words, the addition operation is simple and intuitive, allowing us to count objects easily. Specially, we can organize the objects in a group, thus the result will be the multiplication of the number of objects in the group by the number of groups. For example, if we have 2 oranges in each group and 3 groups, we will have a total of 6 oranges. This is a simple and efficient way to count objects, especially when dealing with large quantities. It is natural define the division operation, that more people call it the inverse of the multiplication. But it is errorneous to think about it. For example, if we have 6 oranges and divide them into 3 groups, we will have 2 oranges in each group. This is a simple example might conduct to the wrong conclusion that the division is the inverse of the multiplication. In fact, the division operation can sound like the inverse of multiplication in several situations. Let's take a look another example, I can multiply 2 oranges by 0, it is result 0. If I divide 0 by 2 oranges, I will have 0 oranges too. But, if I divide 2 oranges by 0, I will have an undefined number of oranges. The central key point is that the division operation is not commutative, that is, the order of the numbers matters, while the multiplication operation is commutative. This misconception can lead to confusion and errors in mathematical calculations. For example, the famous rule of the order of operations, which states that multiplication and division should be performed before addition and subtraction, putting the division operation in the same level of the multiplication, but it is not true, because these operations are not inverse of each other which subtration and addition are.  

Nevertheless, the people use this rule without reflect about it to solve the problems, but it is important to understand the underlying principles to avoid mistakes.

Now, since the commutative property of the multiplication, I prove that rule of the order of operations is not true. Before, it is worth to mention that this problem is far of being new, rather, it dates back to the early twentieth century.


