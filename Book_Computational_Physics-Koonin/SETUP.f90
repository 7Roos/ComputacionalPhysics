module io_all
   ! Apêndice D.2, pág. 584 do livro.
   ! Este módulo entra em substituição ao aruivo 'setup.for'
   ! Dessa forma, as subrotinas serão prodcedimentos de módulo, neste módulo
   ! e o arquivo 'io.all' estará declarado dentro do módulo se comunicando com algum código através de 'use io_all'.
   implicit none
   ! environment dependent parameters
   INTEGER :: IUNIT !unit number for input from screen
   INTEGER :: OUNIT !unit number for output to screen
   INTEGER :: TUNIT !unit number for text output to file
   INTEGER :: GUNIT !unit number for graphics output to file
   INTEGER :: DUNIT !unit number for data input from file
   INTEGER :: TRMLIN !number of lines on terminal screen
   INTEGER :: TRMWID !width of terminal screen
   !
   ! the following are default answers to i/o choices
   ! 1==yes 0 == no
   INTEGER :: TXTTRM !send text output to terminal?
   INTEGER :: TXTFIL !send text output to a file?
   INTEGER :: GRFTRM !send graphics to terminal?
   INTEGER :: GRFHRD !send graphics to a hard copy device?
   INTEGER :: GRFFIL !send graphics data to a file?
   !
   ! i/o input parameters for this run
   LOGICAL :: TTERM !write text output to terminal?
   LOGICAL :: TFILE !write text output to a file?
   CHARACTER(len=12) :: TNAME !name of text file
   LOGICAL :: GTERM !send graphics output to terminal?
   LOGICAL :: GHRDCP !send graphics output to hardcopy device?
   LOGICAL :: GFILE !send graphics data to a file?
   CHARACTER(len=12) :: GNAME !name of graphics data file
contains
   subroutine setup()
      !allows users to supply i/o parameters for their computing environment
      ! Global variables (já está inclusa pelo comando contains, sendo este um procedimento interno ao módulo,
      !todas as variaǘeis lá declarada são globais aqui.)
      implicit none
      !fortran unit numbers for i/o
      !unit for text output to a file
      TUNIT = 10
      !unit for graphics output to file
      GUNIT = 20
      !unit for input from keyboard
      IUNIT = 5
      !unit for output to screen
      OUNIT = 6
      !unit for input of data
      DUNIT = 11

      !how many lines and columns of text fit on your screen?
      TRMLIN = 58!24 (Original)
      TRMWID = 148!80 (Original)

      !!!!!!!!
      ! Para descobrir estes valores em seu terminal, digite no terminal:
      !clear
      !# Obter o número de linhas
      !tput lines

      !# Obter o número de colunas
      !tput cols
      !!!!!!!!


      !default output parameters
      ! There are five forms of output provided, here you are choosing
      !which forms of output you will want MOST of the time (any
      !combination is possible), you always have the option to change
      !your mind at run time.
      !0=no l=yes

      !do you want text sent to the screen?
      TXTTRM = 1

      !do you want text sent to a file?
      TXTFIL = 0

      !do you want graphics sent to the screen?
      GRFTRM = 0

      !do you want graphics sent to a hardcopy device?
      GRFHRD = 0

      !do you want graphics data sent to a file?
      GRFFIL = 0
      ! O comando 'return' ao final da subrotina é redundante em Fortran moderno.
   end subroutine

   subroutine clear()
      !clears text screen by sending an escape sequence;
      !check your terminal (operational system) manual for the correct sequence
      !THIS IS NOT AN ESSENTIAL ROUTINE - YOU CAN LEAVE IT BLANK
      implicit none
      ! Os códigos originais eram para computadores da década de 80 e 90.
      ! Atualmente podemos fazer algo bem mais simples que é passar os comandos para o terminal
      ! Através de uma sub-rotina intríseca

      ! Unix
      call system('clear')

      ! Windows
      !call system('cls')
   end subroutine

   subroutine gmode()
      !switches terminal from text to graphics mode
      ! by writing hardware dependent escape sequences to the terminal
      ! This routine contains the escape sequence for a Graphon terminal
      ! to switch between VT200 and TEK4014 modes
      implicit none
      ! Local variables:
      character(len=1), dimension(2) :: esc
      esc(1) = char(27)    !ascii codes for <ESC> 1
      esc(2) = char(49)

      !WRITE(OUNIT,10) ESC(1),ESCB(2)
      !10    format (1X, 2A1)
   end subroutine

   subroutine tmode()
      !switches terminal from graphics to text mode
      ! by writing hardware dependent escape sequences to the terminal
      ! This routine contains the escape sequence for a Graphon terminal
      ! to switch between TEK4014 and VT200 modes
      implicit none
      ! Local variables:
      character(len=1), dimension(2) :: esc

      esc(1) = char(27)       !ascii codes for <ESC> 2
      esc(2) = char(50)
      !WRITE(OUNIT,10) ESC(l),ESCB)
      !10    FORMAT (1X, 2A1)
   end subroutine
end module io_all
