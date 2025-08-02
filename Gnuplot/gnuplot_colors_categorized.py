#!/usr/bin/env python3
"""
Script para gerar uma visualização categorizada das cores predefinidas do Gnuplot
"""

import re
from manim import *

class GnuplotColorsCategorized(Scene):
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
        # Ler e processar o arquivo de cores
        colors_data = self.parse_color_file()
        
        # Categorizar as cores
        categorized_colors = self.categorize_colors(colors_data)
        
        # Configuração da cena
        self.camera.background_color = "#1a1a1a"  # Fundo escuro
        
        # Título principal
        #title = Text("Gnuplot - Cores por Categoria", font_size=36, color=WHITE, weight=BOLD)
        #title.to_edge(UP, buff=0.2)
        #self.add(title)
        
        # Layout das categorias
        start_y = 3.85
        category_spacing = 1.
        box_size = 0.5
        color_spacing = 1.01
        
        y_offset = 0
        
        for category_name, colors in categorized_colors.items():
            if not colors:  # Pular categorias vazias
                continue
                
            # Título da categoria
            category_title = Text(
                category_name, 
                font_size=20, 
                color=YELLOW,
                weight=BOLD
            ).move_to([0, start_y - y_offset, 0])
            self.add(category_title)
            
            # Cores da categoria
            colors_group = VGroup()
            actual_colors_count = min(14, len(colors))  # Número real de cores a exibir
            
            for i, (name, hex_color, rgb) in enumerate(colors[:14]):  # Máximo 14 cores por categoria
                col = i
                
                # Centralizar baseado no número real de cores
                x_pos = (col - actual_colors_count/2 + 0.5) * color_spacing
                y_pos = start_y - y_offset - 0.5
                
                try:
                    # Retângulo colorido
                    color_rect = Rectangle(
                        width=2.1*box_size, 
                        height=box_size,
                        fill_color=f"#{hex_color}",
                        fill_opacity=1.0,
                        stroke_width=0.5,
                        stroke_color=WHITE
                    ).move_to([x_pos, y_pos, 0])
                    
                    # Nome da cor (texto pequeno)
                    text_color = self.get_text_color(hex_color)
                    color_name = Text(
                        name, 
                        font_size=9, 
                        font='AlgolRevived',
                        color=text_color
                    ).move_to(color_rect.get_center())
                    
                    colors_group.add(color_rect, color_name)
                    
                except Exception as e:
                    print(f"Erro ao processar {name}: {e}")
                    continue
            
            self.add(colors_group)
            y_offset += category_spacing
            
            # Evitar que as categorias saiam da tela
            if y_offset > 10:
                break
    
    def parse_color_file(self):
        """Lê e processa o arquivo colornames.md"""
        colors = []
        
        try:
            with open('colornames.md', 'r') as f:
                content = f.read()
            
            # Padrão regex para extrair as informações das cores
            pattern = r'(\S+)\s+#([0-9a-fA-F]{6})\s+=\s+(\d+)\s+(\d+)\s+(\d+)'
            matches = re.findall(pattern, content)
            
            for match in matches:
                name, hex_color, r, g, b = match
                colors.append((name, hex_color, (int(r), int(g), int(b))))
            
            return colors
            
        except FileNotFoundError:
            print("Arquivo colornames.md não encontrado")
            return []
    
    def categorize_colors(self, colors_data):
        """Categoriza as cores por tipos"""
        categories = {
            "Básicas": [],
            "Vermelhos": [],
            "Verdes": [],
            "Azuis": [],
            "Amarelos/Dourados": [],
            "Rosas/Magentas": [],
            "Cinzas": [],
            "Marrons/Terrosas": [],
            "Outras": []
        }
        
        for name, hex_color, rgb in colors_data:
            name_lower = name.lower()
            
            # Categorização baseada no nome
            if any(x in name_lower for x in ['red', 'crimson', 'coral', 'salmon']):
                categories["Vermelhos"].append((name, hex_color, rgb))
            elif any(x in name_lower for x in ['green', 'lime', 'chartreuse', 'olive', 'forest']):
                categories["Verdes"].append((name, hex_color, rgb))
            elif any(x in name_lower for x in ['blue', 'navy', 'royal', 'steel', 'sky', 'cyan']):
                categories["Azuis"].append((name, hex_color, rgb))
            elif any(x in name_lower for x in ['yellow', 'gold', 'khaki', 'lemon', 'beige']):
                categories["Amarelos/Dourados"].append((name, hex_color, rgb))
            elif any(x in name_lower for x in ['pink', 'magenta', 'violet', 'purple', 'orchid', 'plum']):
                categories["Rosas/Magentas"].append((name, hex_color, rgb))
            elif any(x in name_lower for x in ['grey', 'gray', 'white', 'black']):
                categories["Cinzas"].append((name, hex_color, rgb))
            elif any(x in name_lower for x in ['brown', 'tan', 'sienna', 'bisque', 'antique']):
                categories["Marrons/Terrosas"].append((name, hex_color, rgb))
            elif name_lower in ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white', 'black']:
                categories["Básicas"].append((name, hex_color, rgb))
            else:
                categories["Outras"].append((name, hex_color, rgb))
        
        # Remover categorias vazias e ordenar por número de cores
        filtered_categories = {k: v for k, v in categories.items() if v}
        return dict(sorted(filtered_categories.items(), key=lambda x: len(x[1]), reverse=True))

# Classe para gerar uma paleta compacta com todas as cores
class GnuplotColorsCompact(Scene):
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
        return BLACK if luminosity > 0.4 else WHITE
    
    def construct(self):
        colors_data = self.parse_color_file()
        
        # Configuração
        self.camera.background_color = "#0f0f0f"
        
        # Título
        title = Text("Gnuplot - Pallet colors", font_size=32, color=WHITE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        
        # Informações
        info = Text(f"{len(colors_data)} predefined colors", font_size=18, color=GRAY)
        info.next_to(title, DOWN, buff=0.1)
        
        # Grid compacto
        colors_per_row = 15
        max_rows = 8
        start_y = 2.4
        box_size = 0.8
        spacing = box_size + 0.05
        
        colors_group = VGroup()
        
        for i, (name, hex_color, rgb) in enumerate(colors_data[:colors_per_row * max_rows]):
            row = i // colors_per_row
            col = i % colors_per_row
            
            x_pos = (col - colors_per_row/2 + 0.5) * spacing
            y_pos = start_y - row * spacing
            
            try:
                # Retângulo da cor
                color_rect = Rectangle(
                    width=box_size, 
                    height=box_size,
                    fill_color=f"#{hex_color}",
                    fill_opacity=1.0,
                    stroke_width=0.3,
                    stroke_color="#666666"
                ).move_to([x_pos, y_pos, 0])
                
                colors_group.add(color_rect)
                
                # A cada 15 cores, adicionar o nome de uma cor representativa
                text_color = self.get_text_color(hex_color)
                if i % 15 == 7:  # Meio da linha
                    sample_name = Text(
                        name, 
                        font_size=10, 
                        font='AlgolRevived',
                        color=text_color
                    ).move_to(color_rect)
                    colors_group.add(sample_name)
                
            except Exception as e:
                print(f"Erro: {name}")
                continue
        
        self.add(title, info, colors_group)
    
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
            
            return sorted(colors, key=lambda x: x[0])  # Ordenar por nome
            
        except FileNotFoundError:
            return []

if __name__ == "__main__":
    pass
