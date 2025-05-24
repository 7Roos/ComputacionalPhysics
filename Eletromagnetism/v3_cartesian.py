from manim import *  # or: from manimlib import *
from pathlib import Path
import os
from manim import AS2700

# Flags:
# -q  quality: low(l), medium(m) and high(h),e.g, ql low quality
# -sqh: save last frame hight quality

FLAGS = f"-ql"  # If Vertival, comment this line
SCENE = "Prob2"
CLEAN = "--flush_cache  "  # Remove cached partial movie files

# Vertical config
# config.frame_rate = 25
# config.frame_size = [1080, 1920]  # [WIDTH, HEIGHT]


class Unidimensional_vertical(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        grid = NumberPlane(
            background_line_style={
                "stroke_color": GRAY_A,
                "stroke_width": 2,
                "stroke_opacity": 0.2,
            }
        )
        origin_text = MathTex("\\mathcal{O}").next_to(dot, DL)
        tip_text = MathTex("x", color=AS2700.Y13_VIVID_YELLOW, font_size=60).move_to(
            [6, 0.4, 0]
        )
        limit_inf = MathTex("-\\infty", color=AS2700.Y13_VIVID_YELLOW).move_to(
            [-6.5, -0.4, 0]
        )
        limit_sup = MathTex("+\\infty", color=AS2700.Y13_VIVID_YELLOW).move_to(
            [6.5, -0.4, 0]
        )

        self.play(Create(grid, run_time=2, lag_ratio=0.1))
        self.play(
            FadeIn(dot, run_time=2, lag_ratio=0.1),
            FadeIn(origin_text, run_time=2, lag_ratio=0.2),
            FadeIn(tip_text, run_time=2, lag_ratio=0.3),
            FadeIn(limit_sup, run_time=2, lag_ratio=0.4),
            FadeIn(limit_inf, run_time=2, lag_ratio=0.4),
        )
        self.wait()  # 5

        versorA = Arrow(ORIGIN, [1, 0, 0], buff=0, color=AS2700.G31_VERTIGRIS)
        versorA_label = MathTex("\\hat{x}", font_size=40).next_to(
            versorA.get_center(), UP
        )

        vectorA = Arrow(ORIGIN, [3, 0, 0], buff=0, color=AS2700.B45_SKY_BLUE)
        vectorA_label = MathTex(
            "\\vec{A} = a\\hat{x}", font_size=45, color=AS2700.B45_SKY_BLUE
        ).next_to(vectorA.get_center(), UP)
        self.play(Create(versorA), Write(versorA_label))
        self.wait()  # 3
        self.play(Create(vectorA), Write(vectorA_label))
        self.wait()  # 5

        vectorB = Arrow(ORIGIN, [2, 0, 0], buff=0, color=AS2700.N12_PASTEL_GREY)
        vectorB_label = MathTex(
            "\\vec{B} = b\\hat{x}", font_size=45, color=AS2700.N12_PASTEL_GREY
        ).next_to(vectorB.get_center(), DOWN)
        self.play(Create(vectorB), Write(vectorB_label))
        self.wait()  # 5

        add_vector = (
            MathTex(
                "\\vec{A} + \\vec{B} &= a\\hat{x} + b\\hat{x} \\\\",
                "&= (a+b)\\hat{x} \\\\",
                "\\vec{C} &= c\\hat{x}",
            )
            .to_corner(UL)
            .shift(DOWN)
        )
        self.play(Write(add_vector))
        self.wait()  # 5

        vectorC = Arrow(ORIGIN, [5, 0, 0], buff=0, color=AS2700.X11_BUTTERSCOTCH)
        vectorC_label = MathTex(
            "\\vec{C} = c\\hat{x}", font_size=45, color=AS2700.X11_BUTTERSCOTCH
        ).next_to(vectorC.get_right(), DOWN)
        self.play(Create(vectorC), Write(vectorC_label))
        self.wait()  # 5

        # invert b vector
        vectorBInvert = Arrow(ORIGIN, [-2, 0, 0], buff=0, color=AS2700.N12_PASTEL_GREY)
        vectorB_labelInvert = MathTex(
            "\\vec{B} = -b\\hat{x}", font_size=45, color=AS2700.N12_PASTEL_GREY
        ).next_to(vectorBInvert.get_center(), UP)
        self.play(
            Transform(vectorB, vectorBInvert),
            Transform(vectorB_label, vectorB_labelInvert),
        )
        self.wait()  # 3

        sub_vector = (
            MathTex(
                "\\vec{A} - \\vec{B} &= a\\hat{x} - b\\hat{x} \\\\",
                "&= (a-b)\\hat{x} \\\\",
                "\\vec{C} &= d\\hat{x}",
            )
            .to_corner(UR)
            .shift(DOWN)
        )
        self.play(Write(sub_vector))
        self.wait()  # 3

        vectorCInvert = Arrow(ORIGIN, [1, 0, 0], buff=0, color=AS2700.X11_BUTTERSCOTCH)
        vectorC_label.next_to(vectorCInvert.get_right(), DOWN)
        self.play(Transform(vectorC, vectorCInvert))
        self.wait()  # 5

        # Remove desnecessary
        self.remove(limit_inf, limit_sup)
        self.play(FadeOut(vectorC), FadeOut(vectorC_label))
        vectorBRestore = Arrow(ORIGIN, [2, 0, 0], buff=0, color=AS2700.N12_PASTEL_GREY)
        vectorB_label = MathTex(
            "\\vec{B} = b\\hat{x}", font_size=45, color=AS2700.N12_PASTEL_GREY
        ).next_to(vectorB.get_center(), DOWN)
        self.play(Transform(vectorB, vectorBRestore))
        self.wait()  # 3

        dotProduct = (
            MathTex(
                "\\vec{A} \\cdot \\vec{B} &= a\\hat{i} \\cdot b\\hat{i} \\\\ &= ab(\\hat{i}\\cdot\\hat{i}) \\\\ &= ab"
            )
            .to_edge(DL)
            .shift(UP)
        )
        self.add(dotProduct)
        self.wait()

        dotProduct2 = MathTex("\\vec{A} \\cdot \\vec{B} = ab \\cos(\\theta)").next_to(
            dotProduct, DOWN
        )
        self.add(dotProduct2)
        self.wait()

        cosZero = MathTex("\\vec{A} \\cdot \\vec{B} = ab \\cos(0)").next_to(
            dotProduct2, ORIGIN
        )
        self.play(Transform(dotProduct2, cosZero))
        self.wait()

        ab = MathTex("\\vec{A} \\cdot \\vec{B} = ab").next_to(dotProduct2, ORIGIN)
        self.play(Transform(dotProduct2, ab))
        self.wait()

        cosUm = MathTex("\\vec{A} \\cdot \\vec{B} = ab \\cos(180)").next_to(
            dotProduct2, ORIGIN
        )
        self.play(Transform(dotProduct2, cosUm))
        self.wait()

        abMinus = MathTex("\\vec{A} \\cdot \\vec{B} = -ab").next_to(dotProduct2, ORIGIN)
        self.play(Transform(dotProduct2, abMinus))
        self.wait()

        module = (
            MathTex(
                "|\\vec{A}\\cdot\\vec{A}| &= \\sqrt{(\\vec{A}\\cdot\\vec{A})} \\\\ &= \\sqrt{(a)^{2}} \\\\ &= a"
            )
            .to_edge(DR)
            .shift(UP)
        )
        self.add(module)
        self.wait()

        self.remove(dotProduct2)

        sum_label = Text("Soma", color=YELLOW).to_corner(UL)
        subtraction_label = Text("Subtração", color=YELLOW).to_corner(UR)
        dot_label = Text("Produto escalar", color=YELLOW).to_corner(DL)
        module_label = Text("Módulo", color=YELLOW).to_corner(DR)
        self.add(sum_label, subtraction_label, dot_label, module_label)
        self.wait()

        # Replace numerical
        replace = (
            Text("Substituindo")
            .to_edge(UP)
            .set_color_by_gradient(RED, BLUE)
            .scale(3)
            .shift(6 * UP)
        )
        replaceText = (
            MathTex("a = 3, b=2")
            .set_color(AS2700.Y14_GOLDEN_YELLOW)
            .next_to(replace, DOWN)
            .scale(3)
            .shift(DOWN)
        )
        self.play(
            Write(replace, run_time=4, lag_ratio=0.1),
            Write(replaceText, run_time=4, lag_ratio=0.3),
        )
        add_vectorNums = MathTex(
            "\\vec{A} + \\vec{B} &= 3\\hat{x} + 2\\hat{x} \\\\",
            "&= (3+2)\\hat{x} \\\\",
            "\\vec{C} &= 5\\hat{x}",
        ).move_to(add_vector, ORIGIN)
        sub_vectorNums = MathTex(
            "\\vec{A} - \\vec{B} &= 3\\hat{x} - 2\\hat{x} \\\\",
            "&= (3-2)\\hat{x} \\\\",
            "\\vec{C} &= 1\\hat{x}",
        ).move_to(sub_vector, ORIGIN)
        dotProductNums = MathTex(
            "\\vec{A} \\cdot \\vec{B} &= 3\\hat{i} \\cdot 2\\hat{i} \\\\ &= 3(2)(\\hat{i}\\cdot\\hat{i}) \\\\ &= 6"
        ).move_to(dotProduct, ORIGIN)
        moduleNums = MathTex(
            "|\\vec{A}\\cdot\\vec{A}| &= \\sqrt{(\\vec{A}\\cdot\\vec{A})} \\\\ &= \\sqrt{(3)^{2}} \\\\ &= 3"
        ).move_to(module, ORIGIN)
        self.play(
            Transform(add_vector, add_vectorNums, run_time=4, lag_ratio=0.1),
            Transform(sub_vector, sub_vectorNums, run_time=4, lag_ratio=0.2),
            Transform(dotProduct, dotProductNums, run_time=4, lag_ratio=0.3),
            Transform(module, moduleNums, run_time=4, lag_ratio=0.4),
        )
        self.wait()


class Prob1_vertical(MovingCameraScene):
    def construct(self):
        # blackboard
        grid = NumberPlane(
            background_line_style={
                "stroke_color": GRAY_A,
                "stroke_width": 1,
                "stroke_opacity": 0.2,
            }
        )
        self.play(Create(grid, run_time=2, lag_ratio=0.1))
        self.wait()

        # law's Coulomb
        coulomb_law = VGroup()

        law = Text("Lei de Coulomb").to_edge(UL)
        eq_law = (
            MathTex(
                "\\vec{F}_{ij} = k_{0} \\frac{q_{i}q_{j}}{|\\vec{r}_{i} - \\vec{r}_{j}|^{3}} \\left( \\vec{r}_{i} - \\vec{r}_{j} \\right) "
            )
            .next_to(law, DOWN)
            .shift(0.6 * RIGHT)
        )
        cte = MathTex("k0 = \\frac{1}{4\\pi\\epsilon_{0}}").next_to(eq_law, DOWN)

        # Adiciona os elementos ao grupo
        coulomb_law.add(law, eq_law, cte)

        self.add(coulomb_law)
        self.wait()

        # particles
        particles = VGroup()

        # Criação das partículas com efeitos visuais
        q1 = Circle(radius=0.4)
        q1.set_fill(
            color=color_gradient([AS2700.R32_APPLE_BLOSSOM, AS2700.R41_SHELL_PINK], 3),
            opacity=0.8,
        )
        q1.set_stroke(color=AS2700.R32_APPLE_BLOSSOM, width=2)

        # Efeito de brilho para q1
        q1_glow = Circle(radius=0.5)
        q1_glow.set_fill(color=AS2700.R32_APPLE_BLOSSOM, opacity=0.2)
        q1_glow.set_stroke(width=0)

        q2 = Circle(radius=0.4)
        q2.set_fill(
            color=color_gradient([AS2700.B32_POWDER_BLUE, AS2700.B41_BLUEBELL], 3),
            opacity=0.8,
        )
        q2.set_stroke(color=AS2700.B32_POWDER_BLUE, width=2)
        q2.shift(3 * RIGHT)

        # Efeito de brilho para q2
        q2_glow = Circle(radius=0.5)
        q2_glow.set_fill(color=AS2700.B32_POWDER_BLUE, opacity=0.2)
        q2_glow.set_stroke(width=0)
        q2_glow.shift(3 * RIGHT)

        # Labels com fonte mais elegante
        q1label = MathTex("q_{1}", color=WHITE).next_to(q1, 0.1 * DL)
        q2label = MathTex("q_{2}", color=WHITE).next_to(q2, 0.1 * DR)

        # Linhas com gradiente
        line = Line(q1.get_right(), q2.get_left())
        line.set_color_by_gradient(AS2700.R32_APPLE_BLOSSOM, AS2700.B32_POWDER_BLUE)

        # Linha invisível para o Brace (mede distância entre centros)
        invisible_line = Line(q1.get_center(), q2.get_center())
        invisible_line.set_opacity(0)  # Torna a linha invisível

        # Brace com estilo mais elegante
        b1 = Brace(invisible_line, direction=UP, color=AS2700.Y13_VIVID_YELLOW).shift(
            0.5 * UP
        )
        b1text = b1.get_text("$r$")
        b1text.set_color(AS2700.Y13_VIVID_YELLOW)

        # Adiciona todos os elementos ao grupo
        particles.add(
            q1_glow, q1, q1label, line, q2_glow, q2, q2label, invisible_line, b1, b1text
        )

        # Move o grupo inteiro para o canto inferior esquerdo
        particles.to_edge(LEFT).shift(1.5 * DOWN + 1.2 * RIGHT)

        self.add(particles)
        self.wait()

        # Define vectors
        r2 = Vector(3 * RIGHT).shift(DOWN).set_color(GREEN_C)
        r2label = MathTex("\\vec{r}_{2}").next_to(r2, DOWN).set_color(GREEN_C)

        self.play(
            Create(line, run_time=2, lag_ratio=0.1),
            Create(b1, run_time=2, lag_ratio=0.2),
            FadeIn(b1text, run_time=2, lag_ratio=0.3),
            Create(r2, run_time=2, lag_ratio=0.4),
            FadeIn(r2label, run_time=2, lag_ratio=0.4),
        )
        self.wait()

        # Solution
        eqNew = MathTex(
            "\\vec{F}_{0} &= k_{0} \\frac{q_{1}q_{2}}{| - \\vec{r}_{2}|^{3}} \\left( - \\vec{r}_{2} \\right) \\\\ ",
            " &=k_{0} \\frac{q_{1}q_{2}}{r^{3}} \\left( - r \\hat{x} \\right) \\\\ ",
            " &= -k_{0} \\frac{q_{1}q_{2}}{r^{2}} \\hat{x}",
        ).to_edge(DL)
        self.play(Write(eqNew[0]))
        self.wait()
        self.play(Write(eqNew[1]))
        self.wait()
        self.play(Write(eqNew[2]))
        self.wait()

        # Force result
        forceResult = Vector(2 * LEFT).set_color(AS2700.G45_CHARTREUSE)
        forceResultText = (
            MathTex("\\vec{F}_{12}")
            .next_to(forceResult, UP)
            .set_color(AS2700.G45_CHARTREUSE)
        )
        self.play(
            Create(forceResult, run_time=2, lag_ratio=0.1),
            FadeIn(forceResultText, run_time=2, lag_ratio=0.2),
        )
        self.wait()

        forceResult2 = Vector(2 * RIGHT).set_color(AS2700.G36_KIKUYU).shift(3 * RIGHT)
        forceResult2Text = (
            MathTex("\\vec{F}_{21} = - \\vec{F}_{12}")
            .next_to(forceResult2, UP)
            .set_color(AS2700.G36_KIKUYU)
            .shift(RIGHT)
        )
        self.play(
            Create(forceResult2, run_time=2, lag_ratio=0.1),
            FadeIn(forceResult2Text, run_time=2, lag_ratio=0.2),
        )
        self.wait()

        moduleForce = MathTex(
            "\\left|\\vec{F}_{0} \\right| &= \\left|-k_{0} \\frac{q_{1}q_{2}}{r^{2}} \\hat{x} \\right| \\\\ ",
            " F_{0} &= k_{0} \\frac{q_{1}q_{2}}{r^{2}}",
        ).next_to(eqNew, DOWN)
        self.play(self.camera.frame.animate.move_to(5 * DOWN))
        self.play(Write(moduleForce[0]))
        self.wait()
        self.play(Write(moduleForce[1]))
        self.wait()

        replace = MathTex(
            "r^{2} &= k_{0} \\frac{q_{1}q_{2}}{F_{0}} \\\\",
            " r &= \\sqrt{k_{0}\\frac{q_{1}q_{2}}{F_{0}}}",
        ).next_to(moduleForce, DOWN)
        self.play(Write(replace[0]))
        self.wait()
        self.play(Write(replace[1]))
        self.wait()

        box = SurroundingRectangle(replace[1])
        self.play(Create(box))
        self.wait()

        replaceValsText = (
            Text("Substituindo os valores", color=AS2700.Y11_CANARY)
            .next_to(moduleForce, RIGHT)
            .shift(RIGHT)
        )
        replaceVals = MathTex(
            " r &= \\sqrt{9\\times 10^{9} \\frac{Nm^{2}}{C^{2}} \\frac{26.3\\mu C (47.1\\mu C)}{5.66 N}} \\\\",
            "r &= 1.96 m",
        ).next_to(replaceValsText, DOWN)
        self.play(FadeIn(replaceValsText))
        self.play(Write(replaceVals[0]))
        self.wait()
        self.play(Write(replaceVals[1]))
        self.wait()
        boxResult = SurroundingRectangle(replaceVals[1], color=AS2700.B21_ULTRAMARINE)
        self.play(Create(boxResult))
        self.wait()

        # Adiciona os elementos ao grupo
        coulomb_law.add(law, eq_law)
        coulomb_law.next_to(particles, RIGHT)

        self.add(coulomb_law)
        self.wait()

        # Cria a equação com índices substituídos
        eq_law_final = MathTex(
            "\\vec{F}_{12} = k_{0} \\frac{q_{1}q_{2}}{|\\vec{r}_{1} - \\vec{r}_{2}|^{3}} \\left( \\vec{r}_{1} - \\vec{r}_{2} \\right) "
        ).next_to(law, DOWN)

        # Anima a substituição dos índices
        self.play(
            Transform(eq_law, eq_law_final),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait()


# Uma carga pontual de +3,12 E-6 C está 12,3 cm de distância de uma segunda carga pontual de -1,48 E-6 C. Calcule a intensidade da força em cada carga.


class Prob2(MovingCameraScene):
    def construct(self):
        # blackboard com grid suave sem eixos principais
        grid = NumberPlane(
            background_line_style={
                "stroke_color": GRAY_A,
                "stroke_width": 1,
                "stroke_opacity": 0.2,
            },
            # Remove os eixos principais
            axis_config={
                "stroke_opacity": 0,
            },
            # Configura o grid
            faded_line_style={
                "stroke_color": GRAY_A,
                "stroke_width": 1,
                "stroke_opacity": 0.2,
            },
            faded_line_ratio=1,
        )
        self.add(grid)

        # Cria o grupo principal do problema
        problem = VGroup()

        # Exercise number with bold font
        numberOfExercise = Text(
            "Exercício 2",
            color=YELLOW,
            font="LobsterTwo",  # Fonte mais chamativa e disponível
            weight="BOLD",  # Negrito
            font_size=80,  # Tamanho um pouco maior
        )

        # Problem statement with highlighted variables
        problem_statement = VGroup(
            MathTex(
                "\\text{Uma carga }",
                "q_{1}",
                "\\text{ está a uma distância }",
                "R",
                "\\text{ de uma segunda carga }",
            ).set_color_by_tex_to_color_map({"q_{1}": BLUE, "R": ORANGE}),
            MathTex(
                "q_{2}",
                ".",
                "\\text{ Calcule a força }",
                "\\vec{F}_{12}",
                "\\text{ entre as cargas.}",
            ).set_color_by_tex_to_color_map({"q_{2}": BLUE, "\\vec{F}_{12}": GREEN}),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        # Adiciona os elementos ao grupo principal
        problem.add(numberOfExercise, problem_statement)

        # Organiza o grupo principal
        problem.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # Posiciona o grupo na cena
        problem.to_edge(UL)

        # Cria a caixa ao redor do problema
        box = SurroundingRectangle(
            problem,
            color=WHITE,
            buff=0.5,  # Padding ao redor do conteúdo
            corner_radius=0.3,
            fill_opacity=0.2,  # Preenchimento suave
        )
        # Adiciona o gradiente ao preenchimento
        box.set_fill(color=color_gradient([BLUE, AS2700.Y15_SUNFLOWER], 2))

        # Adiciona elementos à cena
        self.add(box, problem)  # Adiciona a caixa primeiro para ficar atrás

        # Cria um grupo para as imagens dos livros
        books = Group()

        # Adiciona as imagens dos livros ao grupo
        book1 = (
            ImageMobject("./media/images/hallidayEd12Vol3.jpg")
            .scale(0.22)
            .to_corner(DR)
            .shift(0.5 * DOWN + 0.4 * RIGHT)
        )
        book2 = (
            ImageMobject("./media/images/hallidayEd5Vol3.png")
            .scale(1.92)
            .to_corner(DR)
            .shift(0.5 * DOWN + 1.7 * LEFT)
        )

        books.add(book1, book2)
        self.add(books)

        # particles
        # Criação das partículas com efeitos visuais
        # Create group for particle 1
        q1_group = VGroup()
        
        q1 = Circle(radius=0.4)
        q1.set_fill(
            color=color_gradient([AS2700.R41_SHELL_PINK, AS2700.G31_VERTIGRIS], 3),
            opacity=0.8,
        )
        q1.set_stroke(color=AS2700.R41_SHELL_PINK, width=2)

        # Efeito de brilho para q1
        q1_glow = Circle(radius=0.5)
        q1_glow.set_fill(color=AS2700.R32_APPLE_BLOSSOM, opacity=0.2)
        q1_glow.set_stroke(width=0)
        
        # Add elements to particle1_group
        q1_group.add(q1, q1_glow)
        
        # Position the group at ORIGIN
        r1 = 6*LEFT + 2*DOWN
        q1_group.move_to(r1)

        # Create group for particle 2
        q2_group = VGroup()

        q2 = Circle(radius=0.4)
        q2.set_fill(
            color=color_gradient([AS2700.B32_POWDER_BLUE, AS2700.B41_BLUEBELL], 3),
            opacity=0.8,
        )
        q2.set_stroke(color=AS2700.B32_POWDER_BLUE, width=2)

        # Efeito de brilho para q2
        q2_glow = Circle(radius=0.5)
        q2_glow.set_fill(color=AS2700.B32_POWDER_BLUE, opacity=0.2)
        q2_glow.set_stroke(width=0)

        # Add elements to particle2_group
        q2_group.add(q2, q2_glow).move_to(r1 + 3 * RIGHT)

        # Labels com fonte mais elegante
        q1label = MathTex("q_{1}", color=BLUE).next_to(q1_group, 0.1 * DL)
        q2label = MathTex("q_{2}", color=BLUE).next_to(q2_group, 0.1 * DR)

        # Linhas com gradiente
        line = Line(q1_group.get_right(), q2_group.get_left())
        line.set_color_by_gradient(AS2700.R32_APPLE_BLOSSOM, AS2700.B32_POWDER_BLUE)

        # Linha invisível para o Brace (mede distância entre centros)
        invisible_line = Line(q1_group.get_center(), q2_group.get_center())

        # Brace com estilo mais elegante
        b1 = Brace(invisible_line, direction=UP, color=AS2700.Y13_VIVID_YELLOW).shift(
            0.5 * UP
        )
        b1text = b1.get_text("$R$")
        b1text.set_color(AS2700.Y13_VIVID_YELLOW)

        particles = VGroup()
        # Adiciona todos os elementos ao grupo
        particles.add(q1_group, q1label, line, q2_group, q2label, b1, b1text)

        self.add(particles)
        self.wait()

        # Anima o grupo de livros para a direita até sair da tela
        self.play(
            books.animate.shift(10 * RIGHT),  # Move 10 unidades para a direita
            run_time=1,  # Duração da animação em segundos
            rate_func=smooth,  # Função de interpolação suave
        )
        self.wait()

        # law's Coulomb
        coulomb_law = VGroup()

        law = Text("Lei de Coulomb", font="LobsterTwo", color=AS2700.Y13_VIVID_YELLOW)
        eq_law = MathTex(
            "\\vec{F}_{ij} = k_{0} \\frac{q_{i}q_{j}}{|\\vec{r}_{i} - \\vec{r}_{j}|^{3}} \\left( \\vec{r}_{i} - \\vec{r}_{j} \\right) "
        ).next_to(law, DOWN)

        # Adiciona os elementos ao grupo
        coulomb_law.add(law, eq_law)
        coulomb_law.next_to(particles, RIGHT)

        self.add(coulomb_law)
        self.wait()

        # Cria a equação com índices substituídos
        eq_law_final = MathTex(
            "\\vec{F}_{12} = k_{0} \\frac{q_{1}q_{2}}{|\\vec{r}_{1} - \\vec{r}_{2}|^{3}} \\left( \\vec{r}_{1} - \\vec{r}_{2} \\right) "
        ).next_to(law, DOWN)

        # Anima a substituição dos índices
        self.play(
            TransformMatchingTex(eq_law, eq_law_final),
            run_time=1,
            rate_func=smooth,
        )
        self.wait()


        # location of charges
        location_group = VGroup()

        location = MathTex(
            "\\vec{r}_{1} &= 0 \\hat{x} \\\\",
            "\\vec{r}_{2} &= R \\hat{x}",
        )

        # Cria o brace para as equações de localização
        location_brace = Brace(location, direction=LEFT, color=AS2700.Y13_VIVID_YELLOW)

        # Adiciona os elementos ao grupo
        location_group.add(location, location_brace)
        location_group.next_to(eq_law, RIGHT).shift(0.3 * RIGHT)
        self.add(location_group)
        self.wait()

        # Cria a equação com os vetores posição substituídos
        eq_replace_vals = MathTex(
            "\\vec{F}_{12} = k_{0} \\frac{q_{1}q_{2}}{|-R\\hat{x}|^{3}} \\left( -R\\hat{x} \\right) "
        ).next_to(law, DOWN)

        # Anima a substituição dos vetores posição
        self.play(
            TransformMatchingTex(eq_law_final, eq_replace_vals),
            run_time=1,
            rate_func=smooth,
        )
        self.remove(location_group)
        self.wait()

        # Signal vector
        eq_signal_vector = MathTex(
            "\\vec{F}_{12} = -k_{0} \\frac{q_{1}q_{2}}{R^{3}}  R\\hat{x} "
        ).next_to(eq_replace_vals, ORIGIN)
        self.play(
            TransformMatchingTex(eq_replace_vals, eq_signal_vector),
            run_time=1,
            rate_func=smooth,
        )
        self.wait()

        # Simplified R factor
        eq_simplified_R = MathTex(
            "\\vec{F}_{12} = -k_{0} \\frac{q_{1}q_{2}}{R^{2}} \\hat{x} "
        ).next_to(eq_replace_vals, ORIGIN)
        self.play(
            TransformMatchingTex(eq_signal_vector, eq_simplified_R),
            run_time=1,
            rate_func=smooth,
        )
        self.wait()
        

        # advanced for cases
        self.play(self.camera.frame.animate.move_to(3.8 * DOWN))
        self.wait()

        # F21
        eq_F12 = MathTex(
            "\\vec{F}_{21} = k_{0} \\frac{q_{2}q_{1}}{|\\vec{r}_{2} - \\vec{r}_{1}|^{3}} \\left( \\vec{r}_{2} - \\vec{r}_{1} \\right) "
        ).next_to(law, DOWN).shift(DOWN)
        self.add(eq_F12)

        location2 = MathTex(
            "\\vec{r}_{1} &= -R \\hat{x} \\\\",
            "\\vec{r}_{2} &= 0\\hat{x}",
        ).next_to(eq_F12, RIGHT).shift(0.3 * RIGHT)
        location_brace2 = Brace(location2, direction=LEFT, color=AS2700.Y13_VIVID_YELLOW)
        location_group2 = VGroup(location2, location_brace2)
        self.add(location_group2)
        self.wait()
        

        # Cria a equação com os vetores posição substituídos
        eq_replace_vals2 = MathTex(
            "\\vec{F}_{21} = k_{0} \\frac{q_{2}q_{1}}{|-R\\hat{x}|^{3}} \\left( R\\hat{x} \\right) "
        ).next_to(eq_F12, ORIGIN)
        # Anima a substituição dos vetores posição
        self.play(
            TransformMatchingTex(eq_F12, eq_replace_vals2),
            run_time=1,
            rate_func=smooth,
        )
        self.remove(location_group2)
        self.wait()

        # Signal vector
        eq_signal_vector2 = MathTex(
            "\\vec{F}_{21} = k_{0} \\frac{q_{2}q_{1}}{R^{3}}  R\\hat{x} "
        ).next_to(eq_replace_vals2, ORIGIN)
        self.play(
            TransformMatchingTex(eq_replace_vals2, eq_signal_vector2),
            run_time=1,
            rate_func=smooth,
        )
        self.wait() 
        # Simplified R factor
        eq_simplified_R2 = MathTex(
            "\\vec{F}_{21} = k_{0} \\frac{q_{2}q_{1}}{R^{2}} \\hat{x} "
        ).next_to(eq_replace_vals2, ORIGIN)
        self.play(
            TransformMatchingTex(eq_signal_vector2, eq_simplified_R2),
            run_time=1,
            rate_func=smooth,
        )
        self.wait()
        # F12 = -F21
        thirdLaw = MathTex(
            "=-\\vec{F}_{21}"
            ).next_to(eq_simplified_R, RIGHT)
        self.play(TransformMatchingTex(eq_simplified_R2, thirdLaw))
        self.wait()
        
        # Cria a tabela usando o objeto MathTable do Manim
        table_data = [
            ["\\text{Caso 1: }  q_{1}q_{2}> 0", "\\text{Caso 2: }  q_{1}q_{2}< 0"],
            ["\\text{Mesma polaridade}", "\\text{Polaridade oposta}"],
            [
            "\\begin{array}{c} \\vec{F}_{12} \\rightarrow - \\hat{x} \\\\ \\vec{F}_{21} \\rightarrow + \\hat{x} \\end{array} \\text{(repulsiva)}",
            "\\vec{F}_{12} \\rightarrow + \\hat{x} \\text{ atrativa}",
            ],
        ]
        
        # Cria a tabela
        cases_table = MathTable(
            table_data,
            include_outer_lines=False,
            line_config={"stroke_width": 3, "color": AS2700.Y13_VIVID_YELLOW},
            v_buff=0.4,
            h_buff=0.8,
        ).scale(0.9)
        
        # Salva a primeira linha horizontal
        first_horizontal_line = cases_table.get_horizontal_lines()[0]
        
        # Remove todas as linhas horizontais
        for line in cases_table.get_horizontal_lines():
            cases_table.remove(line)
        
        # Adiciona a primeira linha de volta
        cases_table.add(first_horizontal_line)
        
        # Aplica cores específicas para as cargas
        cases_table.get_entries((1, 1)).set_color(BLUE)
        cases_table.get_entries((1, 2)).set_color(RED)
        
        # Posiciona a tabela abaixo da equação simplificada
        cases_table.to_edge(LEFT).shift(4 * DOWN)
        
        # Adiciona a tabela à cena
        self.play(Create(cases_table), run_time=1.5)
        self.wait()


# Duas partículas igualmente carregadas, mantidas separadas pela distância de 3,20 mm, são liberadas do repouso. Observa-se que a aceleração inicial da primeira partícula é de 7,22 m/s2 e que da segunda é 9,16 m/s2. A massa da primeira partícula é de 6.31 e-7 kg. Ache (a) a massa da segunda partícula e (b) a intensidade da carga comum destas.


# Três partículas carregadas repousam em uma linha reta e são separadas pela distância d. As cargas q1 e q2 são mantidas fixas. A carga q3, que é livre para mover-se, está em equilíbrio sobre a ação das forças elétricas. Ache q1 em função de q2.

#  Cada uma de duas pequenas esferas está carregada positivamente, com carga total de +52,6 E-6C. Cada esfera é repelida da outra com uma força de 1,19 N quando as esferas estão separadas de 1,94 m. Calcule a carga em cada esfera.


# Duas cargas fixas, +1,07 E-6 C e -3,28 E-6 C, estão separadas por 61,8 cm. Onde uma terceira carga pode ser posicionada para que a força resultante que age sobre ela seja nula?


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
