from manim import *  # or: from manimlib import *
#from manim_slides import Slide
from pathlib import Path
import os
from manim import AS2700 #Padrão australiano de cores
#import random as rn

# Create animations
# manim presentation.py
# Flags:
# -q  quality: low(l), medium(m) and high(h),e.g, ql low quality

# Convert to html
# manim-slides convert BasicExample slides.html

#--flush_cache                  Remove cached partial movie files

FLAGS = f"-ql"
SCENE = "BasicExample"

fonts = ['AR PL KaitiM Big5', 'AR PL KaitiM GB', 'AR PL Mingti2L Big5', 
         'AR PL SungtiL GB', 'AR PL UMing CN', 'AR PL UMing HK', 
         'AR PL UMing TW', 'AR PL UMing TW MBE', 'Abyssinica SIL', 
         'Accanthis ADF Std', 'Accanthis ADF Std No2', 'Accanthis ADF Std No3', 
         'Amiri', 'Amiri Quran', 'Amiri Quran Colored', 'Ani', 'AnjaliOldLipi', 
         'Arimo', 'Asana Math', 'Baekmuk Batang', 'Baekmuk Dotum', 
         'Baekmuk Gulim', 'Baekmuk Headline', 'Berenis ADF Pro', 
         'Berenis ADF Pro Math', 'C059', 'Cabin', 'Caladea', 'Cantarell', 
         'Carlito', 'Chandas', 'Charis SIL', 'Chilanka', 'Comfortaa', 'Cousine', 
         'D050000L', 'DejaVu Math TeX Gyre', 'DejaVu Sans', 'DejaVu Sans Mono', 
         'DejaVu Serif', 'Dhurjati', 'Droid Sans Fallback', 'Dyuthi', 
         'EB Garamond', 'EB Garamond 12 All SC', 'EB Garamond Initials', 
         'EB Garamond Initials Fill1', 'EB Garamond Initials Fill2', 
         'EB Garamond SC', 'FontAwesome', 'FoulisGreek', 'FreeMono', 'FreeSans', 
         'FreeSerif', 'GFS Artemisia', 'GFS Baskerville', 'GFS BodoniClassic', 
         'GFS Complutum', 'GFS Didot', 'GFS Didot Classic', 'GFS Gazis', 
         'GFS Neohellenic', 'GFS Olga', 'GFS Porson', 'GFS Solomos', 
         'GFS Theokritos', 'Gargi', 'Garuda', 'Gayathri', 'Gentium', 
         'Gentium Basic', 'Gentium Book Basic', 'Gentium Book Plus', 
         'Gentium Plus', 'Gentium Plus Compact', 'GentiumAlt', 'Gidugu', 
         'Gillius ADF', 'Gillius ADF No2', 'Go', 'Go Medium', 'Go Mono', 
         'Go Smallcaps', 'Gubbi', 'Gurajada', 'Hack', 'IPAGothic', 'IPAMincho', 
         'IPAPGothic', 'IPAPMincho', 'IPAexGothic', 'IPAexMincho', 'Jamrul', 'Junicode', 
         'KacstArt', 'KacstBook', 'KacstDecorative', 'KacstDigital', 'KacstFarsi', 'KacstLetter', 
         'KacstNaskh', 'KacstOffice', 'KacstOne', 'KacstPen', 'KacstPoster', 'KacstQurn', 
         'KacstScreen', 'KacstTitle', 'KacstTitleL', 'Kalapi', 'Kalimati', 'Karumbi', 'Keraleeyam', 
         'Khmer OS', 'Khmer OS System', 'Kinnari', 'LKLUG', 'LakkiReddy', 'Laksaman', 
         'Latin Modern Math', 'Latin Modern Mono', 'Latin Modern Mono Caps', 
         'Latin Modern Mono Light', 'Latin Modern Mono Light Cond', 'Latin Modern Mono Prop', 
         'Latin Modern Mono Prop Light', 'Latin Modern Mono Slanted', 'Latin Modern Roman', 
         'Latin Modern Roman Caps', 'Latin Modern Roman Demi', 'Latin Modern Roman Dunhill', 
         'Latin Modern Roman Slanted', 'Latin Modern Roman Unslanted', 'Latin Modern Sans', 
         'Latin Modern Sans Demi Cond', 'Latin Modern Sans Quotation', 'Lato', 'Liberation Mono', 
         'Liberation Sans', 'Liberation Sans Narrow', 'Liberation Serif', 'Likhan', 
         'Linux Biolinum Keyboard O', 'Linux Biolinum O', 'Linux Libertine Display O', 
         'Linux Libertine Initials O', 'Linux Libertine Mono O', 'Linux Libertine O', 'Lobster Two', 
         'Lohit Assamese', 'Lohit Bengali', 'Lohit Devanagari', 'Lohit Gujarati', 'Lohit Gurmukhi', 
         'Lohit Kannada', 'Lohit Malayalam', 'Lohit Odia', 'Lohit Tamil', 'Lohit Tamil Classical', 
         'Lohit Telugu', 'Loma', 'Mallanna', 'Mandali', 'Manjari', 'Meera', 'Mitra', 'Monospace', 
         'Mukti', 'NATS', 'NTR', 'Nakula', 'Navilu', 'Nimbus Mono PS', 'Nimbus Roman', 
         'Nimbus Sans', 'Nimbus Sans Narrow', 'Norasi', 'Noto Color Emoji', 'Noto Kufi Arabic', 
         'Noto Looped Lao', 'Noto Looped Thai', 'Noto Mono', 'Noto Music', 'Noto Naskh Arabic', 
         'Noto Nastaliq Urdu', 'Noto Rashi Hebrew', 'Noto Sans', 'Noto Sans Adlam', 
         'Noto Sans Adlam Unjoined', 'Noto Sans Anatolian Hieroglyphs', 'Noto Sans Arabic', 
         'Noto Sans Armenian', 'Noto Sans Avestan', 'Noto Sans Balinese', 'Noto Sans Bamum', 
         'Noto Sans Bassa Vah', 'Noto Sans Batak', 'Noto Sans Bengali', 'Noto Sans Bhaiksuki', 
         'Noto Sans Brahmi', 'Noto Sans Buginese', 'Noto Sans Buhid', 'Noto Sans CJK HK', 
         'Noto Sans CJK JP', 'Noto Sans CJK KR', 'Noto Sans CJK SC', 'Noto Sans CJK TC', 
         'Noto Sans Canadian Aboriginal', 'Noto Sans Carian', 'Noto Sans Caucasian Albanian', 
         'Noto Sans Chakma', 'Noto Sans Cham', 'Noto Sans Cherokee', 'Noto Sans Coptic', 
         'Noto Sans Cuneiform', 'Noto Sans Cypriot', 'Noto Sans Deseret', 'Noto Sans Devanagari', 
         'Noto Sans Display', 'Noto Sans Duployan', 'Noto Sans Egyptian Hieroglyphs', 
         'Noto Sans Elbasan', 'Noto Sans Elymaic', 'Noto Sans Ethiopic', 'Noto Sans Georgian', 
         'Noto Sans Glagolitic', 'Noto Sans Gothic', 'Noto Sans Grantha', 'Noto Sans Gujarati', 
         'Noto Sans Gunjala Gondi', 'Noto Sans Gurmukhi', 'Noto Sans Hanifi Rohingya', 
         'Noto Sans Hanunoo', 'Noto Sans Hatran', 'Noto Sans Hebrew', 'Noto Sans Imperial Aramaic', 
         'Noto Sans Indic Siyaq Numbers', 'Noto Sans Inscriptional Pahlavi', 
         'Noto Sans Inscriptional Parthian', 'Noto Sans Javanese', 'Noto Sans Kaithi', 
         'Noto Sans Kannada', 'Noto Sans Kayah Li', 'Noto Sans Kharoshthi', 'Noto Sans Khmer', 
         'Noto Sans Khojki', 'Noto Sans Khudawadi', 'Noto Sans Lao', 'Noto Sans Lepcha', 
         'Noto Sans Limbu', 'Noto Sans Linear A', 'Noto Sans Linear B', 'Noto Sans Lisu', 
         'Noto Sans Lycian', 'Noto Sans Lydian', 'Noto Sans Mahajani', 'Noto Sans Malayalam', 
         'Noto Sans Mandaic', 'Noto Sans Manichaean', 'Noto Sans Marchen', 
         'Noto Sans Masaram Gondi', 'Noto Sans Math', 'Noto Sans Mayan Numerals', 
         'Noto Sans Medefaidrin', 'Noto Sans Meetei Mayek', 'Noto Sans Mende Kikakui', 
         'Noto Sans Meroitic', 'Noto Sans Miao', 'Noto Sans Modi', 'Noto Sans Mongolian', 
         'Noto Sans Mono', 'Noto Sans Mono CJK HK', 'Noto Sans Mono CJK JP', 
         'Noto Sans Mono CJK KR', 'Noto Sans Mono CJK SC', 'Noto Sans Mono CJK TC', 
         'Noto Sans Mro', 'Noto Sans Multani', 'Noto Sans Myanmar', 'Noto Sans NKo', 
         'Noto Sans Nabataean', 'Noto Sans New Tai Lue', 'Noto Sans Newa', 'Noto Sans Nushu', 
         'Noto Sans Ogham', 'Noto Sans Ol Chiki', 'Noto Sans Old Hungarian', 
         'Noto Sans Old Italic', 'Noto Sans Old North Arabian', 'Noto Sans Old Permic', 
         'Noto Sans Old Persian', 'Noto Sans Old Sogdian', 'Noto Sans Old South Arabian', 
         'Noto Sans Old Turkic', 'Noto Sans Oriya', 'Noto Sans Osage', 'Noto Sans Osmanya', 
         'Noto Sans Pahawh Hmong', 'Noto Sans Palmyrene', 'Noto Sans Pau Cin Hau', 
         'Noto Sans PhagsPa', 'Noto Sans Phoenician', 'Noto Sans Psalter Pahlavi', 
         'Noto Sans Rejang', 'Noto Sans Runic', 'Noto Sans Samaritan', 'Noto Sans Saurashtra', 
         'Noto Sans Sharada', 'Noto Sans Shavian', 'Noto Sans Siddham', 'Noto Sans SignWriting', 
         'Noto Sans Sinhala', 'Noto Sans Sogdian', 'Noto Sans Sora Sompeng', 'Noto Sans Soyombo', 
         'Noto Sans Sundanese', 'Noto Sans Syloti Nagri', 'Noto Sans Symbols', 'Noto Sans Symbols2', 
         'Noto Sans Syriac', 'Noto Sans Tagalog', 'Noto Sans Tagbanwa', 'Noto Sans Tai Le', 
         'Noto Sans Tai Tham', 'Noto Sans Tai Viet', 'Noto Sans Takri', 'Noto Sans Tamil', 
         'Noto Sans Tamil Supplement', 'Noto Sans Telugu', 'Noto Sans Thaana', 'Noto Sans Thai', 
         'Noto Sans Tifinagh', 'Noto Sans Tifinagh APT', 'Noto Sans Tifinagh Adrar', 
         'Noto Sans Tifinagh Agraw Imazighen', 'Noto Sans Tifinagh Ahaggar', 'Noto Sans Tifinagh Air', 'Noto Sans Tifinagh Azawagh', 'Noto Sans Tifinagh Ghat', 'Noto Sans Tifinagh Hawad', 'Noto Sans Tifinagh Rhissa Ixa', 'Noto Sans Tifinagh SIL', 'Noto Sans Tifinagh Tawellemmet', 'Noto Sans Tirhuta', 'Noto Sans Ugaritic', 'Noto Sans Vai', 'Noto Sans Wancho', 'Noto Sans Warang Citi', 'Noto Sans Yi', 'Noto Sans Zanabazar Square', 'Noto Serif', 'Noto Serif Ahom', 'Noto Serif Armenian', 'Noto Serif Balinese', 'Noto Serif Bengali', 'Noto Serif CJK HK', 'Noto Serif CJK JP', 'Noto Serif CJK KR', 'Noto Serif CJK SC', 'Noto Serif CJK TC', 'Noto Serif Devanagari', 'Noto Serif Display', 'Noto Serif Dogra', 'Noto Serif Ethiopic', 'Noto Serif Georgian', 'Noto Serif Grantha', 'Noto Serif Gujarati', 'Noto Serif Gurmukhi', 'Noto Serif Hebrew', 'Noto Serif Hmong Nyiakeng', 'Noto Serif Kannada', 'Noto Serif Khmer', 'Noto Serif Khojki', 'Noto Serif Lao', 'Noto Serif Malayalam', 'Noto Serif Myanmar', 'Noto Serif Sinhala', 'Noto Serif Tamil', 'Noto Serif Tamil Slanted', 'Noto Serif Tangut', 'Noto Serif Telugu', 'Noto Serif Thai', 'Noto Serif Tibetan', 'Noto Serif Yezidi', 'Noto Traditional Nushu', 'Open Sans', 'Open Sans Condensed', 'OpenSymbol', 'P052', 'Padauk', 'Padauk Book', 'Pagul', 'Peddana', 'Phetsarath OT', 'Ponnala', 'Pothana2000', 'Potti Sreeramulu', 'Purisa', 'Rachana', 'RaghuMalayalamSans', 'Ramabhadra', 'Ramaraja', 'Rasa', 'RaviPrakash', 'Rekha', 'Roboto', 'Roboto Condensed', 'STIX', 'STIX Math', 'STIXGeneral', 'STIXIntegralsD', 'STIXIntegralsSm', 'STIXIntegralsUp', 'STIXIntegralsUpD', 'STIXIntegralsUpSm', 'STIXNonUnicode', 'STIXSizeFiveSym', 'STIXSizeFourSym', 'STIXSizeOneSym', 'STIXSizeThreeSym', 'STIXSizeTwoSym', 'STIXVariants', 'Saab', 'Sahadeva', 'Samanata', 'Samyak Devanagari', 'Samyak Gujarati', 'Samyak Malayalam', 'Samyak Tamil', 'Sans', 'Sarai', 'Sawasdee', 'Serif', 'Sree Krushnadevaraya', 'Standard Symbols PS', 'Suranna', 'Suravaram', 'Suruma', 'Syamala Ramana', 'System-ui', 'TeX Gyre Adventor', 'TeX Gyre Bonum', 'TeX Gyre Bonum Math', 'TeX Gyre Chorus', 'TeX Gyre Cursor', 'TeX Gyre DejaVu Math', 'TeX Gyre Heros', 'TeX Gyre Heros Cn', 'TeX Gyre Pagella', 'TeX Gyre Pagella Math', 'TeX Gyre Schola', 'TeX Gyre Schola Math', 'TeX Gyre Termes', 'TeX Gyre Termes Math', 'TenaliRamakrishna', 'Tibetan Machine Uni', 'Timmana', 'Tinos', 'Tlwg Mono', 'Tlwg Typewriter', 'Tlwg Typist', 'Tlwg Typo', 'URW Bookman', 'URW Gothic', 'Ubuntu', 'Ubuntu Condensed', 'Ubuntu Mono', 'Umpush', 'UnBatang', 'UnDinaru', 'UnDotum', 'UnGraphic', 'UnGungseo', 'UnJamoBatang', 'UnJamoDotum', 'UnJamoNovel', 'UnJamoSora', 'UnPen', 'UnPenheulim', 'UnPilgi', 'UnPilgia', 'UnShinmun', 'UnTaza', 'UnVada', 'UnYetgul', 'Universalis ADF Std', 'Uroob', 'Vemana2000', 'Waree', 'Yrsa', 'Z003', 'aakar', 'mry_KacstQurn', 'ori1Uni', 'padmaa', 'padmaa-Bold.1.1']

class BasicExample(Scene):
    def construct(self):
        ########### Change background ###########
        self.camera.background_color = "#00060D"
        

        ########### Capa ###########
        title = (
            Text(
                "Lei de Coulomb",
                font="GFS Complutum",
                weight=BOLD,
                font_size=40
            )
            .to_edge(UL)
        )
        subtitle = Text("Definição", font=fonts[8], font_size=35).to_edge(UL).shift(DOWN)
        self.add(title, subtitle)
        self.wait()

        system = VGroup(Dot(DOWN), 
                     Dot(2*LEFT + 1.5*UP, radius=0.2, color=BLUE),
                     Dot(RIGHT + 0.7*UP, radius=0.2, color=RED),
                     Arrow(DOWN, 2*LEFT + 1.5*UP, stroke_width=4, max_tip_length_to_length_ratio=0.15),
                     Arrow(DOWN, RIGHT + 0.7*UP, stroke_width=4, max_tip_length_to_length_ratio=0.15),
                     Arrow(RIGHT + 0.7*UP, 2*LEFT + 1.5*UP, stroke_width=4, max_tip_length_to_length_ratio=0.15),
                     MathTex("\\mathcal{O}").next_to(DOWN, DOWN),
                     MathTex("q_{2}").next_to(2*LEFT + 1.5*UP, UP),
                     MathTex("q_{1}").next_to(RIGHT + 0.7*UP, UP),
                     MathTex("\\vec{r^{\\prime}}", color=YELLOW_E).next_to(ORIGIN, 4.1*LEFT + 0.1*DOWN),
                     MathTex("\\vec{r}", color=YELLOW_E).next_to(ORIGIN, 2.9*RIGHT + DOWN),
                     MathTex("\\vec{r} - \\vec{r^{\\prime}", color=YELLOW_E).next_to(ORIGIN, 5*UP))
        system.scale(1.9).to_edge(RIGHT)

        eq = VGroup(MathTex("\\vec{F}_{12} = k \\frac{q_{1}q_{2}}{\\left|\\vec{r} - \\vec{r^{\\prime}}\\right|^{3}} \\left( \\vec{r} - \\vec{r^{\\prime}} \\right)", color='#95B43B'), 
                    MathTex("\\vec{F}_{12} = \\vec{F}_{21}", color='#95B43B'),
                    MathTex("\\left|\\vec{r} - \\vec{r^{\\prime}}\\right| = \\sqrt{ \\left( \\vec{r} - \\vec{r^{\\prime}} \\right) \\cdot \\left( \\vec{r} - \\vec{r^{\\prime}} \\right) }", color='#95B43B'))
        eq.arrange(direction=DOWN, buff=0.9, aligned_edge=LEFT).to_edge(DL)
        self.add(system, eq)
        self.wait()
        self.remove(title, subtitle, system, eq)
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS}")
    #os.system(f"manim-slides convert {SCENE} slides1080.html")