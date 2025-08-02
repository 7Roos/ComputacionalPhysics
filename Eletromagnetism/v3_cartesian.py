from manim import *  # or: from manimlib import *
from pathlib import Path
import os
import sys
from manim import AS2700

# Flags:
# -q  quality: low(l), medium(m) and high(h),e.g, ql low quality
# -sqh: save last frame hight quality

FLAGS = f"-ql"  # If Vertival, comment this line

# Configuração inteligente da cena
AVAILABLE_SCENES = {
    "1": "Unidimensional_vertical",
    "2": "Prob2",
    "3": "Prob3",
    "vertical": "Prob1_vertical",
    "summary": "Summary",
}

# Determinar qual cena executar
if len(sys.argv) > 1:
    scene_arg = sys.argv[1].lower()
    SCENE = AVAILABLE_SCENES.get(scene_arg, "Prob2")  # Default para Prob2
else:
    SCENE = "Prob2"  # Default quando nenhum argumento é fornecido

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


class Prob2(MovingCameraScene):
    def construct(self):
        # ========================================
        # SEÇÃO 1: DEFINIÇÃO DE OBJETOS
        # ========================================

        # Background e grid
        grid = NumberPlane(
            background_line_style={
                "stroke_color": GRAY_A,
                "stroke_width": 1,
                "stroke_opacity": 0.2,
            },
            axis_config={"stroke_opacity": 0},
            faded_line_style={
                "stroke_color": GRAY_A,
                "stroke_width": 1,
                "stroke_opacity": 0.2,
            },
            faded_line_ratio=1,
        )

        # Título e problema usando função utilitária
        problem_content = [
            MathTex(
                "\\text{Uma carga }",
                "q_{1}",
                "\\text{ está a uma distância }",
                "R",
                "\\text{ de uma segunda}",
            ).set_color_by_tex_to_color_map({"q_{1}": BLUE, "R": ORANGE}),
            MathTex(
                "\\text{carga }",
                "q_{2}",
                ".",
                "\\text{ Calcule a força }",
                "\\vec{F}_{12}",
                "\\text{ entre as cargas.}",
            ).set_color_by_tex_to_color_map({"q_{2}": BLUE, "\\vec{F}_{12}": GREEN}),
        ]

        exercise_box = create_exercise_statement(2, problem_content)

        # Livros usando função utilitária
        books = create_book_covers()

        # Partículas usando função simplificada
        q1 = create_charge_particle(1)  # q1 com cores avermelhadas
        q2 = create_charge_particle(2, position=3 * RIGHT)  # q2 com cores azuladas
        # Elementos de conexão
        line = Line(q1.get_right(), q2.get_left())
        line.set_color_by_gradient(AS2700.R32_APPLE_BLOSSOM, AS2700.B32_POWDER_BLUE)
        invisible_line = Line(q1.get_center(), q2.get_center())
        b1 = Brace(invisible_line, direction=UP, color=AS2700.Y13_VIVID_YELLOW, buff=0.6)
        b1text = b1.get_text("$R$")
        b1text.set_color(AS2700.Y13_VIVID_YELLOW)
        particles = VGroup(q1, line, q2, b1, b1text)

        # Lei de Coulomb
        law = Text("Lei de Coulomb", font="LobsterTwo", color=AS2700.Y13_VIVID_YELLOW)
        eq_law = MathTex(
            "\\vec{F}_{ij} = k_{0} \\frac{q_{i}q_{j}}{|\\vec{r}_{i} - \\vec{r}_{j}|^{3}} \\left( \\vec{r}_{i} - \\vec{r}_{j} \\right) "
        )
        coulomb_law = VGroup(law, eq_law)

        # Equações subsequentes
        eq_law_final = MathTex(
            "\\vec{F}_{12} = k_{0} \\frac{q_{1}q_{2}}{|\\vec{r}_{1} - \\vec{r}_{2}|^{3}} \\left( \\vec{r}_{1} - \\vec{r}_{2} \\right) "
        )

        location = MathTex(
            "\\vec{r}_{1} &= 0 \\hat{x} \\\\",
            "\\vec{r}_{2} &= R \\hat{x}",
        )
        location_brace = Brace(location, direction=LEFT, color=AS2700.Y13_VIVID_YELLOW)
        location_group = VGroup(location, location_brace)

        eq_replace_vals = MathTex(
            "\\vec{F}_{12} = k_{0} \\frac{q_{1}q_{2}}{|-R\\hat{x}|^{3}} \\left( -R\\hat{x} \\right) "
        )

        eq_signal_vector = MathTex(
            "\\vec{F}_{12} = -k_{0} \\frac{q_{1}q_{2}}{R^{3}}  R\\hat{x} "
        )

        eq_simplified_R = MathTex(
            "\\vec{F}_{12} = -k_{0} \\frac{q_{1}q_{2}}{R^{2}} \\hat{x} "
        )

        # Equações para F21
        eq_F12 = MathTex(
            "\\vec{F}_{21} = k_{0} \\frac{q_{2}q_{1}}{|\\vec{r}_{2} - \\vec{r}_{1}|^{3}} \\left( \\vec{r}_{2} - \\vec{r}_{1} \\right) "
        )

        location2 = MathTex(
            "\\vec{r}_{1} &= -R \\hat{x} \\\\",
            "\\vec{r}_{2} &= 0\\hat{x}",
        )
        location_brace2 = Brace(
            location2, direction=LEFT, color=AS2700.Y13_VIVID_YELLOW
        )
        location_group2 = VGroup(location2, location_brace2)

        eq_replace_vals2 = MathTex(
            "\\vec{F}_{21} = k_{0} \\frac{q_{2}q_{1}}{|-R\\hat{x}|^{3}} \\left( R\\hat{x} \\right) "
        )

        eq_signal_vector2 = MathTex(
            "\\vec{F}_{21} = k_{0} \\frac{q_{2}q_{1}}{R^{3}}  R\\hat{x} "
        )

        eq_simplified_R2 = MathTex(
            "\\vec{F}_{21} = k_{0} \\frac{q_{2}q_{1}}{R^{2}} \\hat{x} "
        )

        thirdLaw = MathTex("=-\\vec{F}_{21}")

        # Tabela de casos
        table_data = [
            ["\\text{Caso 1: }  q_{1}q_{2}> 0", "\\text{Caso 2: }  q_{1}q_{2}< 0"],
            ["\\text{Mesma polaridade}", "\\text{Polaridade oposta}"],
            [
                "\\begin{array}{c} \\vec{F}_{12} \\rightarrow - \\hat{x} \\\\ \\vec{F}_{21} \\rightarrow + \\hat{x} \\end{array} \\text{(repulsiva)}",
                "\\begin{array}{c} \\vec{F}_{12} \\rightarrow + \\hat{x} \\\\ \\vec{F}_{21} \\rightarrow - \\hat{x} \\end{array} \\text{(atrativa)}",
            ],
        ]

        cases_table = MathTable(
            table_data,
            include_outer_lines=False,
            line_config={"stroke_width": 3, "color": AS2700.Y13_VIVID_YELLOW},
            v_buff=0.4,
            h_buff=0.8,
        ).scale(0.9)

        # Ajustes da tabela
        first_horizontal_line = cases_table.get_horizontal_lines()[0]
        for line in cases_table.get_horizontal_lines():
            cases_table.remove(line)
        cases_table.add(first_horizontal_line)
        cases_table.get_entries((1, 1)).set_color(BLUE)
        cases_table.get_entries((1, 2)).set_color(RED)

        # ========================================
        # SEÇÃO 2: POSICIONAMENTO DE OBJETOS
        # ========================================

        # Posicionar elementos principais
        exercise_box.to_edge(UL).shift(0.3 * UP)

        # Posicionar partículas
        particles.to_corner(DL).shift(UP)

        # Posicionar Lei de Coulomb
        eq_law.next_to(law, DOWN)
        coulomb_law.next_to(particles, RIGHT)

        # Posicionar equações subsequentes
        eq_law_final.next_to(law, DOWN)
        location_group.next_to(eq_law, RIGHT).shift(0.3 * RIGHT)
        eq_replace_vals.next_to(law, DOWN)
        eq_signal_vector.next_to(eq_replace_vals, ORIGIN)
        eq_simplified_R.next_to(eq_replace_vals, ORIGIN)

        # Posicionar segunda análise
        eq_F12.next_to(law, DOWN).shift(DOWN)
        location_group2.next_to(eq_F12, RIGHT).shift(0.19 * RIGHT)
        eq_replace_vals2.next_to(eq_F12, ORIGIN)
        eq_signal_vector2.next_to(eq_replace_vals2, ORIGIN)
        eq_simplified_R2.next_to(eq_replace_vals2, ORIGIN)
        thirdLaw.next_to(eq_simplified_R, RIGHT)

        # Posicionar tabela
        cases_table.to_edge(LEFT).shift(5 * DOWN)

        # ========================================
        # SEÇÃO 3: ANIMAÇÕES
        # ========================================

        # Início da cena
        self.add(grid)
        self.add(exercise_box)
        self.add(books)
        self.add(particles)
        self.wait()

        # Animar saída dos livros
        self.play(
            books.animate.shift(10 * RIGHT),
            run_time=1,
            rate_func=smooth,
        )
        self.wait()

        # Introduzir Lei de Coulomb
        self.add(coulomb_law)
        self.wait()

        # Transformar equação geral para específica
        self.play(
            Transform(eq_law, eq_law_final),
            run_time=1,
            rate_func=smooth,
        )
        self.wait()

        # Mostrar localização das cargas
        self.add(location_group)
        self.wait()

        # Primeira substituição
        self.play(
            Transform(eq_law, eq_replace_vals),
            run_time=1,
            rate_func=smooth,
        )
        self.remove(location_group)
        self.wait()

        # Simplificação do sinal
        self.play(
            Transform(eq_law, eq_signal_vector),
            run_time=1,
            rate_func=smooth,
        )
        self.wait()

        # Simplificação final
        self.play(
            Transform(eq_law, eq_simplified_R),
            run_time=1,
            rate_func=smooth,
        )
        self.wait()

        # Mover câmera para análise adicional
        self.play(self.camera.frame.animate.move_to(3.8 * DOWN))
        self.wait()

        # Análise da força F21
        self.add(eq_F12)
        self.add(location_group2)
        self.wait()

        # Transformações para F21
        self.play(
            Transform(eq_F12, eq_replace_vals2),
            run_time=1,
            rate_func=smooth,
        )
        self.remove(location_group2)
        self.wait()

        self.play(
            Transform(eq_F12, eq_signal_vector2),
            run_time=1,
            rate_func=smooth,
        )
        self.wait()

        self.play(
            Transform(eq_F12, eq_simplified_R2),
            run_time=1,
            rate_func=smooth,
        )
        self.wait()

        # Mostrar terceira lei
        self.play(Transform(eq_F12, thirdLaw))
        self.wait()

        # Criar tabela de casos
        self.play(Create(cases_table), run_time=1.5)
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

        # Criação das partículas usando função simplificada
        q1 = create_charge_particle(1)  # q1 com cores avermelhadas
        q2 = create_charge_particle(2, position=3 * RIGHT)  # q2 com cores azuladas

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
            q1, line, q2, invisible_line, b1, b1text
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


# Três partículas carregadas repousam em uma linha reta e são separadas pela distância d. As cargas q1 e q2 são mantidas fixas. A carga q3, que é livre para mover-se, está em equilíbrio sobre a ação das forças elétricas. Ache q1 em função de q2.

#  Cada uma de duas pequenas esferas está carregada positivamente, com carga total de +52,6 E-6C. Cada esfera é repelida da outra com uma força de 1,19 N quando as esferas estão separadas de 1,94 m. Calcule a carga em cada esfera.


# Duas cargas fixas, +1,07 E-6 C e -3,28 E-6 C, estão separadas por 61,8 cm. Onde uma terceira carga pode ser posicionada para que a força resultante que age sobre ela seja nula?


def create_charge_particle(charge_number=1, radius=0.4, position=ORIGIN):
    """
    Função simplificada para criar partículas carregadas (q1 ou q2) com cores predefinidas.

    Args:
        charge_number: Número da carga (1 ou 2). Padrão: 1 (q1)
        radius: Raio da partícula. Padrão: 0.4
        position: Posição inicial da partícula. Padrão: ORIGIN

    Returns:
        VGroup: Grupo contendo a partícula, seu efeito de brilho e label
    """
    # Cores predefinidas para cada carga
    if charge_number == 1:
        # q1 - cores avermelhadas
        color_gradient_colors = [AS2700.R32_APPLE_BLOSSOM, AS2700.R41_SHELL_PINK]
        glow_color = AS2700.R32_APPLE_BLOSSOM
        label_text = "q_{1}"
        label_color = BLUE
    elif charge_number == 2:
        # q2 - cores azuladas
        color_gradient_colors = [AS2700.B32_POWDER_BLUE, AS2700.B41_BLUEBELL]
        glow_color = AS2700.B32_POWDER_BLUE
        label_text = "q_{2}"
        label_color = BLUE
    else:
        # Fallback para q1 se número inválido
        color_gradient_colors = [AS2700.R32_APPLE_BLOSSOM, AS2700.R41_SHELL_PINK]
        glow_color = AS2700.R32_APPLE_BLOSSOM
        label_text = "q_{1}"
        label_color = BLUE

    # Partícula principal
    particle = Circle(radius=radius)
    particle.set_fill(
        color=color_gradient(color_gradient_colors, 3),
        opacity=0.8,
    )
    particle.set_stroke(color=color_gradient_colors[0], width=2)

    # Efeito de brilho
    glow = Circle(radius=radius + 0.1)
    glow.set_fill(color=glow_color, opacity=0.2)
    glow.set_stroke(width=0)

    # Label da partícula
    label = MathTex(label_text, color=label_color)
    
    # Grupo da partícula
    particle_group = VGroup(glow, particle, label)
    particle_group.move_to(position)
    
    # Posicionar o label próximo à partícula
    if charge_number == 1:
        label.next_to(particle, 0.1 * DL)
    else:
        label.next_to(particle, 0.1 * DR)

    return particle_group


class Summary(Scene):
    """
    Cena de resumo que consolida os principais conceitos aprendidos.
    """

    def construct(self):
        # Título da seção
        title = Text("Resumo", font="LobsterTwo", color=YELLOW, font_size=60)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Pontos principais
        key_points = VGroup(
            Text("1. Sistema de coordenadas: cartesiano 1D", font_size=36),
            Text("2. Sistema de referência: uma carga na origem", font_size=36),
            Text("3. Lei de Coulomb aplicada com vetores posição", font_size=36),
            Text("4. Análise de sinais emerge da matemática", font_size=36),
            Text("5. Terceira Lei de Newton é automática", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        key_points.next_to(title, DOWN, buff=1)

        # Anima cada ponto aparecendo
        for point in key_points:
            self.play(FadeIn(point, shift=UP), run_time=1)
            self.wait(0.5)

        self.wait(2)

        # Equação final destacada
        final_equation = MathTex(
            "\\vec{F}_{12} = -k_0 \\frac{q_1 q_2}{R^2} \\hat{x}", font_size=48
        ).set_color(GREEN)

        equation_box = SurroundingRectangle(final_equation, color=WHITE, buff=0.3)

        equation_group = VGroup(final_equation, equation_box)
        equation_group.to_edge(DOWN, buff=1)

        self.play(Create(equation_box), Write(final_equation), run_time=2)
        self.wait(3)

        # Função utilitária para criar enunciados de exercícios


def create_exercise_statement(
    exercise_number, problem_content, box_colors=[BLUE, AS2700.Y15_SUNFLOWER]
):
    """
    Cria um enunciado de exercício padronizado com caixa, número e conteúdo.

    Args:
        exercise_number (int): Número do exercício
        problem_content (VGroup): Conteúdo do problema (VGroup com MathTex)
        box_colors (list): Lista de cores para o gradiente da caixa

    Returns:
        VGroup: Grupo contendo caixa e problema formatado
    """
    # Título do exercício
    numberOfExercise = Text(
        f"Exercício {exercise_number}",
        color=YELLOW,
        font="LobsterTwo",
        weight="BOLD",
        font_size=80,
    )

    # Organizar conteúdo do problema
    if isinstance(problem_content, list):
        problem_statement = VGroup(*problem_content)
        problem_statement.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
    else:
        problem_statement = problem_content

    # Agrupar título e enunciado
    problem = VGroup(numberOfExercise, problem_statement).arrange(
        DOWN, aligned_edge=LEFT, buff=0.5
    )

    # Criar caixa com bordas arredondadas e gradiente
    box = SurroundingRectangle(
        problem,
        color=WHITE,
        buff=0.5,
        corner_radius=0.3,
        fill_opacity=0.2,
    )
    box.set_fill(color=color_gradient(box_colors, 2))

    # Retornar grupo completo
    return VGroup(box, problem)


class Prob3(Scene):
    """
    Exemplo de uso da função create_exercise_statement para um terceiro exercício
    """

    def construct(self):
        # Exemplo de uso da função utilitária
        problem_content = [
            MathTex(
                "\\text{Duas cargas fixas, }",
                "+1{,}07 \\times 10^{-6}",
                "\\text{ C e }",
                "-3{,}28 \\times 10^{-6}",
                "\\text{ C,}",
            ).set_color_by_tex_to_color_map(
                {"+1{,}07 \\times 10^{-6}": RED, "-3{,}28 \\times 10^{-6}": BLUE}
            ),
            MathTex(
                "\\text{estão separadas por }",
                "61{,}8",
                "\\text{ cm. Onde uma terceira carga pode ser}",
            ).set_color_by_tex_to_color_map({"61{,}8": ORANGE}),
            MathTex("\\text{posicionada para que a força resultante seja nula?}"),
        ]

        # Cores personalizadas para a caixa
        custom_colors = [GREEN, PURPLE]

        # Criar o enunciado usando a função
        exercise_box = create_exercise_statement(3, problem_content, custom_colors)
        exercise_box.to_edge(UP)

        # Adicionar à cena
        self.add(exercise_box)
        self.wait(2)


# Execução principal
if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"

    # Exibir ajuda se solicitado
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help", "help"]:
        print("\n=== SISTEMA DE CENAS v3_cartesian.py ===")
        print("Uso: python v3_cartesian.py [numero_da_cena]")
        print("\nCenas disponíveis:")
        for key, scene in AVAILABLE_SCENES.items():
            print(f"  {key:8} -> {scene}")
        print(f"\nPadrão: {SCENE} (quando nenhum argumento é fornecido)")
        print(f"Flags: {FLAGS}")
        print("\nExemplos:")
        print("  python v3_cartesian.py 2      # Executa Prob2")
        print("  python v3_cartesian.py 3      # Executa Prob3")
        print("  python v3_cartesian.py 1      # Executa Unidimensional_vertical")
        print("  python v3_cartesian.py summary # Executa Summary")
        exit(0)

    # Executar animação
    print(f"Executando cena: {SCENE}")
    os.system(f"manim {script_name} {SCENE} {FLAGS}")


def create_book_covers():
    """
    Cria um grupo de capas dos livros hallidayEd5 e hallidayEd12 posicionados no canto inferior direito.
    Função simplificada específica para estes dois livros.

    Returns:
        Group: Grupo contendo as capas dos livros hallidayEd5 e hallidayEd12 formatadas
    """
    books = []

    # Livro hallidayEd5
    try:
        hallidayEd5 = ImageMobject("media/images/hallidayEd5Vol3.png")
        hallidayEd5.scale(1.5)
        hallidayEd5.to_corner(DR)
        hallidayEd5.shift(0.5 * DOWN + 0.4 * RIGHT)
        books.append(hallidayEd5)
    except Exception as e:
        print(f"Erro ao carregar hallidayEd5: {e}")
        # Placeholder para hallidayEd5
        hallidayEd5_placeholder = Rectangle(
            width=1, height=1.5, fill_color=BLUE, fill_opacity=0.3, stroke_color=WHITE
        )
        hallidayEd5_placeholder.add(Text("hallidayEd5", font_size=16))
        hallidayEd5_placeholder.to_corner(DR).shift(0.5 * DOWN + 0.4 * RIGHT)
        books.append(hallidayEd5_placeholder)

    # Livro hallidayEd12
    try:
        hallidayEd12 = ImageMobject("media/images/hallidayEd12Vol3.jpg")
        hallidayEd12.scale(0.173)
        hallidayEd12.to_corner(DR)
        hallidayEd12.shift(0.5 * DOWN + 1.73 * LEFT)
        books.append(hallidayEd12)
    except Exception as e:
        print(f"Erro ao carregar hallidayEd12: {e}")
        # Placeholder para hallidayEd12
        hallidayEd12_placeholder = Rectangle(
            width=1.5, height=2, fill_color=RED, fill_opacity=0.3, stroke_color=WHITE
        )
        hallidayEd12_placeholder.add(Text("hallidayEd12", font_size=16))
        hallidayEd12_placeholder.to_corner(DR).shift(0.5 * DOWN + 1.7 * LEFT)
        books.append(hallidayEd12_placeholder)

    return Group(*books)
