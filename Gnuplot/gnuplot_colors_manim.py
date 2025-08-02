#!/usr/bin/env python3
"""
Script para gerar uma visualização das cores predefinidas do Gnuplot usando Manim
"""

import re
from manim import *

class GnuplotColors(Scene):
    def construct(self):
        # Ler e processar o arquivo de cores
        colors_data = self.parse_color_file()
        
        # Título principal
        title = Text("Cores Predefinidas do Gnuplot", font_size=36, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.add(title)
        
        # Configurar layout em grades
        colors_per_row = 8
        rows = 14
        start_y = 2.5
        box_size = 0.5
        spacing_x = 1.2
        spacing_y = 0.45
        
        # Criar visualização das cores
        color_group = VGroup()
        
        for i, (name, hex_color, rgb) in enumerate(colors_data[:colors_per_row * rows]):
            row = i // colors_per_row
            col = i % colors_per_row
            
            # Posição do retângulo
            x_pos = (col - colors_per_row/2 + 0.5) * spacing_x
            y_pos = start_y - row * spacing_y
            
            # Converter hex para cor do Manim
            try:
                # Remover # se presente
                clean_hex = hex_color.lstrip('#')
                # Converter para formato do Manim
                manim_color = f"#{clean_hex}"
                
                # Criar retângulo colorido
                color_rect = Rectangle(
                    width=box_size, 
                    height=box_size,
                    fill_color=manim_color,
                    fill_opacity=1.0,
                    stroke_width=1,
                    stroke_color=WHITE
                ).move_to([x_pos, y_pos, 0])
                
                # Nome da cor (texto pequeno abaixo do retângulo)
                color_name = Text(
                    name, 
                    font_size=8, 
                    color=WHITE
                ).next_to(color_rect, DOWN, buff=0.05)
                
                # Código RGB (texto ainda menor)
                rgb_text = Text(
                    f"RGB({rgb[0]},{rgb[1]},{rgb[2]})", 
                    font_size=6, 
                    color=GRAY
                ).next_to(color_name, DOWN, buff=0.02)
                
                color_group.add(color_rect, color_name, rgb_text)
                
            except Exception as e:
                print(f"Erro ao processar cor {name}: {e}")
                continue
        
        self.add(color_group)
        
        # Adicionar informação adicional
        info_text = Text(
            f"Total: {len(colors_data)} cores predefinidas", 
            font_size=20, 
            color=GRAY
        ).to_edge(DOWN, buff=0.3)
        self.add(info_text)
    
    def parse_color_file(self):
        """Lê e processa o arquivo colornames.md"""
        colors = []
        
        try:
            with open('colornames.md', 'r') as f:
                content = f.read()
            
            # Padrão regex para extrair as informações das cores
            # Formato: nome #hex = r g b
            pattern = r'(\S+)\s+#([0-9a-fA-F]{6})\s+=\s+(\d+)\s+(\d+)\s+(\d+)'
            
            matches = re.findall(pattern, content)
            
            for match in matches:
                name, hex_color, r, g, b = match
                colors.append((name, hex_color, (int(r), int(g), int(b))))
            
            print(f"Encontradas {len(colors)} cores")
            return colors
            
        except FileNotFoundError:
            print("Arquivo colornames.md não encontrado")
            # Cores de fallback
            return [
                ("red", "ff0000", (255, 0, 0)),
                ("green", "00ff00", (0, 255, 0)),
                ("blue", "0000ff", (0, 0, 255)),
                ("yellow", "ffff00", (255, 255, 0)),
                ("cyan", "00ffff", (0, 255, 255)),
                ("magenta", "ff00ff", (255, 0, 255)),
                ("white", "ffffff", (255, 255, 255)),
                ("black", "000000", (0, 0, 0))
            ]

# Classe alternativa para criar uma imagem estática
class GnuplotColorsStatic(Scene):
    def get_text_color(self, hex_color):
        """Determina se o texto deve ser branco ou preto baseado na luminosidade da cor de fundo"""
        # Converter hex para RGB
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        
        # Calcular luminosidade usando a fórmula padrão
        # Luminosity = 0.299*R + 0.587*G + 0.114*B
        luminosity = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        
        # Se a luminosidade for maior que 0.5, usar texto preto, senão branco
        return BLACK if luminosity > 0.5 else WHITE
    
    def construct(self):
        # Similar ao anterior, mas otimizado para imagem estática
        colors_data = self.parse_color_file()
        
        # Configuração da cena
        self.camera.background_color = "#1e1e1e"  # Fundo escuro
        
        # Título
        #title = Text(f"Gnuplot - {len(colors_data)} available colors", font_size=35, color=WHITE, weight=BOLD)
        #title.to_edge(UP, buff=0.1)
        
        # Layout em grid mais compacto
        colors_per_row = 9
        max_colors = 108  # Múltiplo de 9 para layout limpo
        start_y = 3.67
        box_size = 0.61
        spacing_x = 1.55
        spacing_y = 0.66
        
        color_elements = VGroup()
        
        for i, (name, hex_color, rgb) in enumerate(colors_data[:max_colors]):
            row = i // colors_per_row
            col = i % colors_per_row
            
            x_pos = (col - colors_per_row/2 + 0.5) * spacing_x
            y_pos = start_y - row * spacing_y
            
            try:
                # Retângulo colorido
                color_rect = Rectangle(
                    width=2.49*box_size, 
                    height=box_size,
                    fill_color=f"#{hex_color}",
                    fill_opacity=1.0,
                    stroke_width=0.5,
                    stroke_color=WHITE
                ).move_to([x_pos, y_pos, 0])
                
                # Nome da cor (agora no centro do retângulo)
                text_color = self.get_text_color(hex_color)
                color_name = Text(
                    name.replace('-', '-\n') if len(name) > 17 else name, 
                    font_size=13, 
                    font='AlgolRevived',
                    color=text_color,
                    line_spacing=0.8
                ).move_to(color_rect.get_center())
                
                color_elements.add(color_rect, color_name)
                
            except Exception as e:
                print(f"Erro ao processar {name}: {e}")
                continue
        
        # Adicionar todos os elementos
        self.add(color_elements)
    
    def parse_color_file(self):
        """Método auxiliar para ler cores"""
        colors = []
        
        try:
            with open('colornames.md', 'r') as f:
                content = f.read()
            
            pattern = r'(\S+)\s+#([0-9a-fA-F]{6})\s+=\s+(\d+)\s+(\d+)\s+(\d+)'
            matches = re.findall(pattern, content)
            
            for match in matches:
                name, hex_color, r, g, b = match
                colors.append((name, hex_color, (int(r), int(g), int(b))))
            
            return colors
            
        except FileNotFoundError:
            print("Arquivo colornames.md não encontrado")
            return []

if __name__ == "__main__":
    # Executar a cena
    pass
