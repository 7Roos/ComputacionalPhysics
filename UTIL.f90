module menu_all
   ! Apêndice D3, pág. 588 do livro.
   ! Este módulo substitui o arquivo 'util.for'
   implicit none
   !menu data types
   INTEGER, parameter :: FLOAT = 0  !floating point number
   INTEGER, parameter :: NUM = 1    !integer
   INTEGER, parameter :: BOOLEN = 2 !yes or no user input
   INTEGER, parameter :: YESKIP = 3 !yes or no, skip on YES
   INTEGER, parameter :: NOSKIP = 4 !yes or no, skip on NO
   INTEGER, parameter :: SKIP = 5   !Unconditional goto
   INTEGER, parameter :: QUIT = 6   !abort current ASK call
   INTEGER, parameter :: TITLE = 7  !print prompt (in ASK or PRTAGS)
   INTEGER, parameter :: WAIT = 8   !print prompt and invoke PAUSE
   INTEGER, parameter :: CHSTR = 9  !character string
   INTEGER, parameter :: MTITLE = 10    !print MPRMPT() during ASK only
   INTEGER, parameter :: MCHOIC = 11    !print prompt, get choice, branch
   INTEGER, parameter :: PPRINT = 12    !print out parameters
   INTEGER, parameter :: CLRTRM = 13    !clear screen

   !menu entries which are the same for all programs
   INTEGER, parameter :: IMAIN = 10     !main menu choice
   INTEGER, parameter :: STOP = -7      !flag to stop
   INTEGER, parameter :: ITTERM = 73    !text to terminal
   INTEGER, parameter :: ITFILE = 74    !text to file
   INTEGER, parameter :: ITNAME = 75    !text file name
   INTEGER, parameter :: IGTERM = 83    !graphics to terminal
   INTEGER, parameter :: IGHRD = 84     !graphics hardcopy
   INTEGER, parameter :: IGFILE = 85    !graphics to file
   INTEGER, parameter :: IGNAME = 86    !graphics file name
   INTEGER, parameter :: ISTOP = 98     !last entry

   !data arrays for menu
   CHARACTER(len=60), dimension(100) :: MPRMPT  !prompt string
   CHARACTER(len=60), dimension(100) :: MTAG    !terse description
   INTEGER, dimension(100) :: MTYPE             !data type
   INTEGER, dimension(100) :: MINTS             !default value for integer
   REAL, dimension(100) :: MREALS               !default value for real
   REAL, dimension(100) :: MLOLIM               !lower limit on input
   REAL, dimension(100) :: MHILIM               !high limit on input
   CHARACTER(len=40), dimension(100) :: MSTRNG  !default value for string
contains
   subroutine header(descrp, nhead, ntext, ngraph)
      ! Global variables:
      use io_all
      implicit none
      ! Input variables:
      character(len=*), dimension(20) :: descrp !description of program and output
      integer :: nhead, ntext, ngraph           !number of lines for each description
      ! Local variables:
      integer :: n                        !current line number
      integer :: LENGTH                   !true length of character strings
      integer :: NBLNKS                   !num of blanks needed to center string
      character(len=80) :: BLANKS = ' '   !array of blanks for centering
      ! Function (O tipo das funções são acessíveis a todo o escopo, não havenod necessidade de declarar novamente aqui):
      !integer :: lentru    !true length of character string

      call clear()      !vertically center output
      do n = 1, (TRMLIN-18-nhead-ngraph-ntext)/2
         write(OUNIT, 20)
      end do

      !write out constant part of header
      write(OUNIT, 40)
      write(OUNIT, 50)
      write(OUNIT, 60)
      write(OUNIT, 80)
      write(OUNIT, 20)
      write(OUNIT, 20)

      !write out chapter dependent section of the header
      do n = 1, nhead + ntext + ngraph
         if ( n == nhead + 1 ) then !text output header
            write(OUNIT,110)
         end if

         if ( n == nhead+ntext+1 ) then
            write(OUNIT,115) !graphics output header
         end if

         LENGTH = lentru(descrp(n)) !horizontally center output
         NBLNKS = (80 - LENGTH) / 2
         WRITE (OUNIT,120) BLANKS(1:NBLNKS),DESCRP(N)(1:LENGTH)
      end do

      call PAUSE(' to begin the program...', 1)
      call clear()

20    format (' ')
40    format (1/, 30x, 'Computational Physics')
50    format (1/, 32x, '(FORTRAN VERSION)')
60    format (1/, 20x, 'by Steven E. Koonin and Dawn C. Meredith')
80    format (1/, 14x, 'Copyright 1989, Benjamin/Cummings Publishing Company')
110   format (1/, 30x, 'Text output displays')
115   format (1/, 28x, 'Graphics output displays')
120   format (A,A)
   end subroutine

   subroutine menu()
      ! sets up the part of the menu that is the same for all programs
      !
      ! Global variables:
      use io_all
      implicit none
      ! main menu

      MTYPE(1) = CLRTRM

      MTYPE(2) = MTITLE
      MPRMPT(2) = 'MAIN MENU'
      MLOLIM(2) = 2
      MHILIM(2) = 1

      MTYPE(3) = MTITLE
      MPRMPT(3) = '1) Change physical parameters'
      MLOLIM(3) = 0
      MHILIM(3) = 0

      MTYPE(4) = MTITLE
      MPRMPT(4) = '2) Change numerical parameters'
      MLOLIM(4) = 0
      MHILIM(4) = 0

      MTYPE(5) = MTITLE
      MPRMPT(5) = '3) Change output parameters'
      MLOLIM(5) = 0
      MHILIM(5) = 0

      MTYPE(6) = MTITLE
      MPRMPT(6) = '4) Display physical and numerical parameters'
      MLOLIM(6) = 0
      MHILIM(6) = 0

      MTYPE(7) = MTITLE
      MPRMPT(7) = '5) Display output parameters'
      MLOLIM(7) = 0.
      MHILIM(7) = 0.

      MTYPE(8) = MTITLE
      MPRMPT(8) = '6) Run program'
      MLOLIM(8) = 0
      MHILIM(8) = 0

      MTYPE(9) = MTITLE
      MPRMPT(9) = '7) Stop program'
      MLOLIM(9) = 0
      MHILIM(9) = 1

      MTYPE(10) = MCHOIC
      MPRMPT(10) = 'Make a menu choice'
      MTAG(10) = '11 36 61 91 94 99 99'
      MLOLIM(10) = 1
      MHILIM(10) = 7
      MINTS(10) = 6
      MREALS(10) = -6

      !physical parameters
      MTYPE(11) = CLRTRM

      MTYPE(12) = TITLE
      MPRMPT(12) = 'PHYSICAL PARAMETERS'
      MLOLIM(12) = 2.
      MHILIM(12) = 1.

      MTYPE(35) = SKIP
      MREALS(35) = 1.

      !numerical parameters
      MTYPE(36) = CLRTRM

      MTYPE(37) = TITLE
      MPRMPT(37) = 'NUMERICAL PARAMETERS'
      MLOLIM(37) = 2.
      MHILIM(37) = 1.

      MTYPE(60) = SKIP
      MREALS(60) = 1.

      !output menu
      MTYPE(61) = CLRTRM

      MTYPE(62) = MTITLE
      MPRMPT(62) = 'OUTPUT MENU'
      MLOLIM(62) = 0.
      MHILIM(62) = 1.

      MTYPE(63) = MTITLE
      MPRMPT(63) = 'Change text output parameters'
      MLOLIM(63) = 0.
      MHILIM(63) = 0.

      MTYPE(64) = MTITLE
      MPRMPT(64) = 'Change graphics output parameters'
      MLOLIM(64) = 0.
      MHILIM(64) = 0.

      MTYPE(65) = MTITLE
      MPRMPT(65) = 'Return to main menu'
      MLOLIM(65) = 0.
      MHILIM(65) = 1.

      MTYPE(66) = MCHOIC
      MPRMPT(66) = 'Make menu choice and press Return'
      MTAG(66) = '71 81 01'
      MLOLIM(66) = 1.
      MHILIM(66) = 3.
      MINTS(66) = 3.

      !text output parameters
      MTYPE(71) = CLRTRM

      MTYPE(72) = TITLE
      MPRMPT(72) = 'TEXT OUTPUT PARAMETERS'
      MLOLIM(72) = 2.
      MHILIM(72) = 1.

      MTYPE(73) = BOOLEN
      MPRMPT(73) = 'Do you want text output displayed on screen?'
      MTAG(73) = 'Text output to screen'
      MINTS(73) = TXTTRM

      MTYPE(74) = NOSKIP
      MPRMPT(74) = 'Do you want text output sent to a file?'
      MTAG(74) = 'Text output to file'
      MREALS(74) = 76.
      MINTS(74) = TXTFIL

      MTYPE(75) = CHSTR
      MPRMPT(75) = 'Enter name of file for text output'
      MTAG(75) = 'File name for text output'
      MLOLIM(75) = 1.
      MHILIM(75) = 12.
      MINTS(75) = 1
      MSTRNG(MINTS(75)) = 'cmphys.txt'

      MTYPE(80) = SKIP
      MREALS(80) = 61.

      !graphics output parameters
      MTYPE(81) = CLRTRM

      MTYPE(82) = TITLE
      MPRMPT(82) = 'GRAPHICS OUTPUT PARAMETERS'
      MLOLIM(82) = 2.
      MHILIM(82) = 2.
      MHILIM(82) = 1.

      MTYPE(83) = BOOLEN
      MPRMPT(83) = 'Do you want graphics sent to the terminal?'
      MTAG(83) = 'Graphics output to terminal'
      MINTS(83) = GRFTRM

      MTYPE(84) = BOOLEN
      MPRMPT(84) = 'Do you want graphics sent to the hardcopy device?'
      MTAG(84) = 'Graphics output to hardcopy device'
      MINTS(84) = GRFHRD

      MTYPE(85) = NOSKIP
      MPRMPT(85) = 'Do you want data for graphing sent to a file?'
      MTAG(85) = 'Data for graphing sent to file'
      MREALS(85) = 87.
      MINTS(85) = GRFFIL

      MTYPE(86) = CHSTR
      MPRMPT(86) = 'Enter name of file for graphics data'
      MTAG(86) = 'File for graphics data'
      MLOLIM(86) = 2.
      MHILIM(86) = 12.
      MINTS(86) = 2.
      MSTRNG(MINTS(86)) = 'cmphys.grf'

      MTYPE(90) = SKIP
      MREALS(90) = 61.

      !printing numerical and physical parameters
      MTYPE(91) = PPRINT
      MLOLIM(91) = 11.
      MHILIM(91) = 60.

      MTYPE(92) = SKIP
      MREALS(92) = 1.

      !printing output parameters
      MTYPE(94) = PPRINT
      MLOLIM(94) = 71.
      MHILIM(94) = 90.

      MTYPE(95) = SKIP
      MREALS(95) = 1.
   end subroutine

   subroutine ask(start, end)
      !executes menu items from START to END;
      !see Appendix A for a description of the menu
      !
      ! Global variables:
      use io_all
      implicit none
      ! Input variables:
      integer :: start, end         !starting/ending menu items to execute
      ! Local variables:
      integer :: i                  !current menu item
      integer :: ilow, ihigh        !integer limits for NUM type
      integer :: numskp            !number of blank lines to print
      integer :: ichoic             !current menu choice
      ! Functions:
      ! Coments, internal procedure!
      !character(len=40) :: charac   !character input
      !real :: getflt                !real input
      !integer :: getint             !integer input
      !integer :: parse              !determines menu branching
      !integer :: yesno              !boolean input

      i = start

      do
         if ( MTYPE(i) == float ) then
            MREALS(i) = getflt(MREALS(i), MLOLIM(i), MHILIM(i), MPRMPT(i))
         else if ( MTYPE(I) == NUM ) then
            ILOW = int(MLOLIM(I))
            IHIGH = int(MHILIM(I))
            MINTS(I) = GETINT(MINTS(I), ILOW, IHIGH, MPRMPT(I))
         else if (MTYPE(I) == BOOLEN) then
            MINTS(I) = YESNO(MINTS(I), MPRMPT(I))
         else if (MTYPE(I) == CHSTR) then
            MSTRNG(MINTS(I)) = CHARAC(MSTRNG(MINTS(I)),INT(MHILIM(I)),MPRMPT(I))

         else if (MTYPE(I) == MCHOIC) then
            ILOW = int(MLOLIM(I))
            IHIGH = int(MHILIM(I))
            ICHOIC = GETINT(MINTS(I), ILOW, IHIGH, MPRMPT(I))

            !if MREALS is > 0, save ICHOIC and change default
            IF (MREALS(I) > 0) THEN
               MREALS(I) = REAL(ICHOIC)
               MINTS(I) = ICHOIC
               ! if MREALS is < 0, save ICHOIC but leave default the same
            ELSE IF (MREALS(I) < 0) THEN
               MREALS(I) = -REAL(ICHOIC)
            END IF

            I = PARSE(MTAG(I), ICHOIC) - 1

         else if (MTYPE(I) == TITLE .OR. MTYPE(I) == MTITLE) then
            NUMSKP = int(MLOLIM(I))
            CALL PRBLKS(NUMSKP)
            WRITE (OUNIT, 10) MPRMPT(I)
            NUMSKP = int(MHILIM(I))
            CALL PRBLKS(NUMSKP)
         ELSE IF (MTYPE(I) == YESKIP) THEN
            MINTS(I) = YESNO(MINTS(I), MPRMPT(I))
            IF (MINTS(I) /= 0) THEN
               I = int(MREALS(I) - 1)
            END IF
         ELSE IF (MTYPE(I) == NOSKIP) THEN
            MINTS(I) =YESNO(MINTS(I), MPRMPT(I))
            IF (MINTS(I) == 0) THEN
               I = int(MREALS(I) - 1)
            END IF
         ELSE IF (MTYPE(I) == SKIP) THEN
            I = int(MREALS(I) - 1)
         ELSE IF (MTYPE(I) == WAIT) THEN
            WRITE(OUNIT, 10) MPRMPT(I)
            CALL PAUSE('to continue',1)
         ELSE IF (MTYPE(I) == CLRTRM) THEN
            CALL CLEAR
         ELSE IF (MTYPE(I) == QUIT) THEN
            I = END
         ELSE IF (MTYPE(I) == PPRINT) THEN
            ILOW = int(MLOLIM(I))
            IHIGH = int(MHILIM(I))
            CALL CLEAR
            CALL PRTAGS(ILOW,IHIGH)
            CALL PAUSE(' to see the Main Menu...',1)
            CALL CLEAR
         end if

         !display info about defaults
         IF (I == 1) THEN
            WRITE (OUNIT,*) ' '
            WRITE (OUNIT,100)
            WRITE (OUNIT,101)
         END IF

         I = I + 1

         if (i > end) exit
      end do

10    format (1x, A)
100   format (' To accept the default value [in brackets] for any item')
101   format (' just press Return at the prompt')
   end subroutine

   subroutine PRTAGS(START, END)
      ! prints menu prompts and default values for items START to END
      !
      ! Global variables:
      use io_all
      implicit none
      ! Input variables:
      integer :: start, end      !limiting indices of printed menu items
      ! Local variables:
      integer :: i               !menu items index
      integer :: numskp          !number of lines to skip
      integer :: index           !subindex for menu items
      integer :: plen            !length of prompt
      integer :: ichoic          !menu/parameter choice
      ! Function
      !integer :: lentru (replace by len_trim)
      !integer :: parse           !menu choice

      I=START
      do
         IF (MTYPE(I) == FLOAT) THEN
            WRITE (OUNIT, 11) MTAG(I), MREALS(I)

         ELSE IF (MTYPE(I) == NUM) THEN
            WRITE (OUNIT, 12) MTAG(I), MINTS(I)

         ELSE IF (MTYPE(I) == BOOLEN) THEN
            CALL PRYORN(MTAG(I), MINTS(I))

         ELSE IF (MTYPE(I) == CHSTR) THEN
            WRITE( OUNIT, 13) MTAG(I), MSTRNG(MINTS(I))

         ELSE IF (MTYPE(I) == TITLE) THEN
            NUMSKP = int(MLOLIM(I))
            CALL PRBLKS(NUMSKP)
            WRITE (OUNIT, 10) MPRMPT(I)
            NUMSKP = int(MHILIM(I))
            CALL PRBLKS(NUMSKP)

         ELSE IF (MTYPE(I) == YESKIP) THEN
            CALL PRYORN(MTAG(I), MINTS(I))
            IF (MINTS(I) /= 0 .AND. MREALS(I) > I) THEN
               I = int(MREALS(I) - 1)
            END IF

         ELSE IF (MTYPE(I) == NOSKIP) THEN
            CALL PRYORN(MTAG(I), MINTS(I))
            IF (MINTS(I) == 0 .AND. MREALS(I) > I) THEN
               I = int(MREALS(I) - 1)
            END IF
         ELSE IF (MTYPE(I) == SKIP) THEN
            IF (MREALS(I) > I) I = int(MREALS(I) - 1) !don't skip backwards

         ELSE IF (MTYPE(I) == MCHOIC) THEN
            IF (MREALS(I) > 0) THEN
               ! for menu choices that are parameter choices, print out
               ! choice, but first you must find it
               DO INDEX = int(I - MHILIM(I)),I - 1
                  IF (int(I + MREALS(I) - MHILIM(I) - 1) == INDEX) THEN
                     PLEN = len_trim(MPRMPT(INDEX))
                     WRITE (OUNIT,10) MPRMPT(INDEX)(4:PLEN)
                  END IF
               end do
            END IF
            IF (MREALS(I) /= 0) THEN
               !branch to chosen parameter
               ICHOIC = ABS(INT(MREALS(I) ) )
               I = PARSE(MTAG(I),ICHOIC) - 1
            END IF
         end if

         i = i + 1
         if (i > end) exit
      end do

10    format (1X, A)
11    format (1x, A, 1PE11.3)
12    FORMAT (1x, A, I6)
13    format (1x, A, 5x, A)
   end subroutine

   subroutine pryorn(PMPT, YORN)
      !print a 'yes' or 'no'
      !
      ! Global variables:
      use io_all
      implicit none
      ! Input variables:
      integer :: yorn               !1 == 'YES', '0' == 'NO'
      character(len=*) :: pmpt      !string to print before y/n
      ! functions:(replace by len_trim)
      ! integer :: lentru

      IF (YORN == 0) THEN
         WRITE(OUNIT, 10) PMPT(1:len_trim(PMPT))
      ELSE
         WRITE(OUNIT, 11) PMPT(1:len_trim(PMPT))
      END IF
10    FORMAT( 1X, A, ': no')
11    FORMAT( 1X, A, ': yes')
   end subroutine

   subroutine prblks(NUMLIN)
      !prints NUMLIN blank lines on terminal
      !
      ! Global variables:
      use io_all
      implicit none
      ! Passed variables:
      integer :: numlin    !number of blank lines to print
      ! Local variables:
      integer :: i         !dummy index

      do i = 1, numlin
         write(OUNIT, *) ' '
      end do
   end subroutine

   subroutine pause(phrase, nskip)
      !gives user time to read screen by waiting for dummy input;
      !allows for printing of PHRASE to screen;
      !skips NSKIP lines before printing PHRASE
      !
      ! Global variables:
      use io_all
      implicit none
      ! Passed variables:
      character(len=*) phrase    !phrase to be printed
      integer :: nskip           !number of lines to skip
      ! Local variables:
      character(len=1) :: dummy  !dummy variable
      integer :: iskip           !NSKIP index

      do iskip = 1, nskip
         write(OUNIT, 5)
      end do
5     format (' ')
      write(OUNIT, 15) phrase    !write phrase
      read(IUNIT, 20) dummy      !wait for dummy input
15    format (' Press return', A)
20    format(A1)
   end subroutine

   subroutine flopen(fname, funit)
      !opens a new file, unless one by the same name already exists
      !
      ! Global variables:
      use io_all
      implicit none
      ! Input variables:
      character(len=*) :: fname     !file name
      integer :: funit              !unit number
      ! Local variables:
      logical :: opn                !is the file open?
      logical :: exst               !does it exist?
      !character(len=40) :: charac   !function that return character input (already disponible in module)
      !integer :: lentru (replace by len_trim)

      do
         INQUIRE(FILE=FNAME,EXIST=EXST,OPENED=OPN)

         IF (OPN) exit

         IF (EXST) THEN
            WRITE (OUNIT,20) FNAME(1:len_trim(FNAME))
20          FORMAT (' Output file ', A, ' already exists')
            FNAME=CHARAC(FNAME,12, 'Enter another filename')
         ELSE
            OPEN(UNIT=FUNIT,FILE=FNAME,STATUS='NEW')
            exit
         END IF
      end do
   end subroutine

   subroutine flopn2()
      implicit none
      print *, 'preencher!'
   end subroutine

   subroutine flclos(fname, funit)
      !checks on file status of file, and closes if open
      !
      ! Global variables:
      use io_all
      implicit none
      ! Input variables:
      character(len=*) :: fname     !file name
      integer :: funit              !unit number
      ! Local variables:
      logical opn                   !is the file open

      INQUIRE(FILE=FNAME, OPENED=OPN)
      IF (OPN) CLOSE(UNIT=FUNIT)
   end subroutine

   subroutine finish()
      !closes files and stops execution
      !
      ! Global variables:
      use io_all
      implicit none
      call flclos(tname, tunit)
      call flclos(gname, gunit)
      stop
   end subroutine

   subroutine fltdef(xprmpt, X)
      !prints prompt for floating number
      ! and displays default X in a format dictated by size of X
      !
      ! Global variables:
      use io_all
      implicit none
      ! Input variables:
      character(len=*) :: xprmpt    !prompt string
      real :: x                     !default value
      ! Function(replace by len_trim):
      ! Integer: lentru             !true length of string

      !positive numbers (leave no room for a sign)
      IF (X > 0) THEN
         IF ((ABS(X) < 999.49) .AND. (ABS(X) >= 99.949)) THEN
            WRITE (OUNIT,5) XPRMPT(1:len_trim(XPRMPT)),X
         ELSE IF ((ABS(X) < 99.949) .AND. (ABS(X) >= 9.9949)) THEN
            WRITE (OUNIT,10) XPRMPT(1:len_trim(XPRMPT)),X
         ELSE IF ((ABS(X) < 9.9949) .AND. (ABS(X) >= .99949)) THEN
            WRITE (OUNIT,15) XPRMPT(1:len_trim(XPRMPT)),X
         ELSE IF ((ABS(X) < .99949) .AND. (ABS(X) >= .099949)) THEN
            WRITE (OUNIT,20) XPRMPT(1:len_trim(XPRMPT)),X
         ELSE
            WRITE (OUNIT,25) XPRMPT(1:len_trim(XPRMPT)),X
         END IF
         !negative numbers (leave room for the sign)
      ELSE
         IF ((ABS(X) < 999.49) .AND. (ABS(X) >= 99.949)) THEN
            WRITE (OUNIT,105) XPRMPT(1:len_trim(XPRMPT)),X
         ELSE IF ((ABS(X) < 99.949) .AND. (ABS(X) >= 9.9949)) THEN
            WRITE (OUNIT,110) XPRMPT(1:len_trim(XPRMPT)),X
         ELSE IF ((ABS(X) < 9.9949) .AND. (ABS(X) >= .99949)) THEN
            WRITE (OUNIT,115) XPRMPT(1:len_trim(XPRMPT)),X
         ELSE IF ((ABS(X) < .99949) .AND. (ABS(X) >= .099949)) THEN
            WRITE (OUNIT,120) XPRMPT(1:len_trim(XPRMPT)),X
         ELSE
            WRITE (OUNIT,125) XPRMPT(1:len_trim(XPRMPT)),X
         END IF
      END IF

5     format (1x, A, 1X, '[', F4.0, ']')
10    format (1x, A, 1X, '[', F4.1, ']')
15    format (1x, A, 1X, '[', F4.2, ']')
20    format (1x, A, 1X, '[', F4.3, ']')
      ! Recommended relationship between field width 'W' and the number of fractional digits 'D' in this edit descriptor is 'W>=D+7'.
25    format (1x, A, 1X, '[', 1PE9.2, ']')
105   format (1x, A, 1X, '[', F5.0, ']')
110   format (1x, A, 1X, '[', F5.1, ']')
115   format (1x, A, 1X, '[', F5.2, ']')
120   format (1x, A, 1X, '[', F5.3, ']')
125   format (1x, A, 1X, '[', 1PE9.2, ']')
   end subroutine

   subroutine intdef(kprmpt, k)
      !prints prompt for integer input from screen
      !and default value in appropriate format
      !
      ! Global variables:
      use io_all
      implicit none
      ! Input variables:
      character(len=*) :: kprmpt    !prompt string
      integer :: k                  !default values
      ! Function(replace by len_trim):
      !integer :: lentru

      !positive numbers (leave no room for a sign)
      IF (K >= 0 ) THEN
         IF ((IABS(K) <= 9999) .AND. (IABS(K) >= 1000)) THEN
            WRITE (OUNIT,10) KPRMPT(1:len_trim(KPRMPT)),K
         ELSE IF ((IABS(K) <= 999) .AND. (IABS(K) >= 100)) THEN
            WRITE (OUNIT,20) KPRMPT(1:len_trim(KPRMPT)),K
         ELSE IF ((IABS(K) <= 99) .AND. (IABS(K) >= 10)) THEN
            WRITE (OUNIT,30) KPRMPT(1:len_trim(KPRMPT)),K
         ELSE IF ((IABS(K) <= 9) .AND. (IABS(K) >= 0)) THEN
            WRITE (OUNIT,40) KPRMPT(1:len_trim(KPRMPT)),K
         ELSE
            WRITE (OUNIT,50) KPRMPT(1:len_trim(KPRMPT)),K
         END IF
         !negative numbers (leave room for the sign)
      ELSE
         IF ((IABS(K) <= 9999) .AND. (IABS(K) >= 1000)) THEN
            WRITE (OUNIT,110) KPRMPT(1:len_trim(KPRMPT)),K
         ELSE IF ((IABS(K) <= 999) .AND. (IABS(K) >= 100)) THEN
            WRITE (OUNIT,120) KPRMPT(1:len_trim(KPRMPT)),K
         ELSE IF ((IABS(K) <= 99) .AND. (IABS(K) >= 10)) THEN
            WRITE (OUNIT,130) KPRMPT(1:len_trim(KPRMPT)),K
         ELSE IF ((IABS(K) <= 9) .AND. (IABS(K) >= 1)) THEN
            WRITE (OUNIT,140) KPRMPT(1:len_trim(KPRMPT)),K
         ELSE
            WRITE (OUNIT,150) KPRMPT(1:len_trim(KPRMPT)),K
         END IF

      END IF

10    format (1x, a, 1x, 1x, '[', I4, ']')
20    format (1x, a, 1x, 1x, '[', I3, ']')
30    format (1x, a, 1x, 1x, '[', I2, ']')
40    format (1x, a, 1x, 1x, '[', I1, ']')
50    format (1x, a, 1x, 1x, '[', I10, ']')
110   format (1x, a, 1x, 1x, '[', I5, ']')
120   format (1x, a, 1x, 1x, '[', I4, ']')
130   format (1x, a, 1x, 1x, '[', I3, ']')
140   format (1x, a, 1x, 1x, '[', I2, ']')
150   format (1x, a, 1x, 1x, '[', I10, ']')
   end subroutine

   subroutine convrt(x, string, len)
      !converts a real number x to a character variable string of length LEN
      ! for printing; the format is chosen according to the value of X,
      ! taking roundoff into account
      implicit none
      ! Passed variables:
      character(len=9) :: string    !routine output
      real :: x                     !routine input
      integer :: len                !string length
      ! Function (relace by len_trim)
      !integer :: lentru !gets string length

      !positive numbers (leave no room for a sign)

      if ( x > 0 ) then
         if ( abs(x) < 999.4 .AND. (abs(x) >= 99.94)) then
            WRITE(STRING, 5) X
         else if ( abs(x) < 99.94 .AND. (abs(x) >= 9.994)) then
            WRITE(STRING, 10) x
         else if ( abs(x) < 9.994 .AND. (abs(x) >= .9994)) then
            WRITE (STRING, 15) x
         else if ( abs(x) < .9994 .AND. (abs(x) >= .09994)) then
            WRITE (STRING, 20) x
         else
            WRITE (STRING, 25) x
         end if

         !negative numbers (leave room for a sign)
      else
         if ( abs(x) < 999.4 .AND. (abs(x) >= 99.94)) then
            WRITE(STRING, 105) X
         else if ( abs(x) < 99.94 .AND. (abs(x) >= 9.994)) then
            WRITE(STRING, 110) x
         else if ( abs(x) < 9.994 .AND. (abs(x) >= .9994)) then
            WRITE (STRING, 115) x
         else if ( abs(x) < .9994 .AND. (abs(x) >= .09994)) then
            WRITE (STRING, 120) x
         else
            WRITE (STRING, 125) x
         end if
      end if

      len = len_trim(string)

5     format (F4.0)
10    format (F4.1)
15    format (F4.2)
20    format (F4.3)
      !Recommended relationship between field width 'W' and the number of fractional digits 'D' in this edit descriptor is 'W>=D+7'
25    format (1PE9.2)
105   format (F5.0)
110   format (F5.1)
115   format (F5.2)
120   format (F5.3)
125   format (1PE9.2)
   end subroutine

   subroutine icnvrt(i, string, len)
      !converts an integer I to a character variable STRING for
      ! printing; the format is chosen according to the value of I
      implicit none
      ! Passed variables:
      character(len=9) :: string    !routine output
      integer :: i                  !routine input
      integer :: len                !length of string

      !positive numbers (leave no room for a sign)
      if ( i >= 0 ) then
         if ( (abs(i) <= 9) .AND. (abs(i) >= 10)) then
            WRITE(STRING, 5) I
            len = 1
         else if ((abs(i) <= 99) .AND. (abs(i) >= 10)) then
            WRITE(STRING, 10) I
            len = 2
         else if ((abs(i) <= 999) .AND. (abs(i) >= 100)) then
            WRITE(STRING, 15) I
            len = 3
         else if ((abs(i) <= 9999) .AND. (abs(i) >= 1000)) then
            WRITE(STRING, 20) I
            len = 4
         else
            WRITE(STRING, 25) real(I)
         end if
         !negative numbers (leave room for the sign)
      else
         if ( (abs(i) <= 9) .AND. (abs(i) >= 10)) then
            WRITE(STRING, 105) I
            len = 1
         else if ((abs(i) <= 99) .AND. (abs(i) >= 10)) then
            WRITE(STRING, 110) I
            len = 2
         else if ((abs(i) <= 999) .AND. (abs(i) >= 100)) then
            WRITE(STRING, 115) I
            len = 3
         else if ((abs(i) <= 9999) .AND. (abs(i) >= 1000)) then
            WRITE(STRING, 120) I
            len = 4
         else
            WRITE(STRING, 125) real(I)
         end if
      end if
5     format (I1)
10    format (I2)
15    format (I3)
20    format (I4)
      !Recommended relationship between field width 'W' and the number of fractional digits 'D' in this edit descriptor is 'W>=D+7'
25    format (1PE9.2)
105   format (I2)
110   format (I3)
115   format (I4)
120   format (I5)
125   format (1PE9.2)
   end subroutine

   integer function parse(string, choice)
      ! determines branching in menu list
      !
      ! breaks STRING (of the form 'nn nn nn nn nn nn ....') into pieces, and
      ! returns the integer value represented by the CHOICE group of digits
      implicit none
      ! Input variables:
      character(len=*) :: string    !string to look at
      integer :: choice             !specific number to look at
      ! Local variables:
      integer :: ipos               !current character position in string
      integer :: igroup             !current group of digits in string

      IPOS = 1
      DO IGROUP = 1, CHOICE - 1
         DO WHILE (STRING(IPOS:IPOS) /= ' ')
            IPOS = IPOS + 1
         END DO
         IPOS = IPOS + 1
      END DO
      read (string(ipos:ipos + 2), 10) parse
10    format (I2)
   end function

   integer function lentru(charactere)
      ! finds the true length of a character string by searching
      ! backward for first nonblank character
      implicit none
      ! Input variables:
      character(len=*) :: charactere    !string whose length we are finding
      ! Local variables:

      ! Em Fortran moderno podemos utilizar uma função intríseca.
      lentru = len_trim(charactere)
   end function

   real function getflt(x, xmin, xmax, xprmpt)
      ! get a floating point number GETFLT; make sure it is between XMIN
      ! and XMAX and prompt with XPRMPT
      !
      ! If your compiler accepts (FMT=*) to an internal unit, comment out
      ! lines 3 and 5, and uncomment lines 2 and 4
      !
      !Global variables:
      use io_all
      implicit none
      !Input variables:
      character(len=*) :: xprmpt    !prompt
      real :: x                     !default value
      real :: xmin, xmax            !limits on input
      !Local variables:
      character(len=40) :: string   !internal unit
      ! Function (len_trim replaces this function)
      !integer :: lentru             !returns true length of string
      integer :: err_string, err_getflt ! Para tratar erros de leitura

      flt: do
         str: do
            !prompt for float, display default value
            call fltdef(xprmpt, x)
            read(IUNIT, 35, iostat = err_string) string
            if (err_string == 0) exit
         end do str

         ! accept default value X if STRING is empty
         if ( len_trim(string) == 0 ) then
            getflt = x
         else
            !read(unit=string, fmt=*, err=10) getflt  ! Line 2
            read(unit=string, fmt=1, iostat = err_getflt) getflt   ! Line 3
1           format (E9.2)
         end if
         if ( err_getflt == 0 ) exit
      end do flt

      ! make sure GETFLT is between XMIN and XMAX
      do while ( (getflt < xmin) .OR. (getflt > xmax))
         do
            str2: do
               write(OUNIT, 60) xmin, xmax
               read(IUNIT, 35, iostat = err_string) string
               if (err_string == 0) exit
            end do str2
            if ( len_trim(string) == 0 ) then
               getflt = x
            else
               !read(unit=string, fmt=*, err=50) getflt  ! Line 4
               read(unit=string, fmt=1, iostat=err_getflt) getflt   ! Line 5
            end if
            if (err_getflt == 0 ) exit
         end do
      end do

35    format (A40)
60    format(' Try again: input outside of range = [', 1PE11.3, 1PE11.3, ']')
      !100   format (1PE9.2)     ! defined but not used
   end function

   integer function getint(k, kmin, kmax, kprmpt)
      !get an integer value GETINT;
      !check that it lies between KMIN and KMAX and prompt with KPRMPT
      !
      !This function allows input of integers in a natural way (i.e., without
      !preceding blanks or decimal points) even though we cannot use list
      !directed READ (i.e., FMT=*) from internal units
      !
      ! Global variables:
      use io_all
      implicit none
      ! Input variables:
      character(len=*) :: kprmpt    !string prompt
      integer :: k                  !default value
      integer :: kmin, kmax         !upper and lower limits
      ! local variables:
      character(len=40) :: string   !internal unit
      real :: temp                  !temp var to allow for easier input
      ! Function(replace by len_trim):
      ! integer :: lentru
      integer :: err_string, err_temp

      !prompt for input; display default

      do
         do
            CALL INTDEF(KPRMPT,K)
            READ (IUNIT,35, iostat = err_string) STRING
            if (err_string == 0) exit
         end do

         !accept default value K if STRING is empty
         IF (len_trim(STRING) == 0) THEN
            GETINT = K
         ELSE
            !change the integer into a real number
            STRING = STRING(1:len_trim(STRING)) // '.'
            !read the real number from string
            READ (UNIT=STRING,FMT=1, iostat = err_temp) TEMP
            !change it to an integer
            GETINT = INT(TEMP)
         END IF
         if (err_temp == 0) exit
      end do

      !check that GETINT lies between KMIN and KMAX
      do while ((getint < kmin) .OR. (getint > kmax))
         tem: do
            str: do
               WRITE (OUNIT,60) KMIN,KMAX
               READ (IUNIT,35, iostat= err_string) STRING
               if (err_string == 0) exit
            end do str
            IF (len_trim(STRING) == 0) THEN
               GETINT=K
            ELSE
               STRING = STRING(1:len_trim(STRING)) // '.'
               READ (UNIT=STRING,FMT=1, iostat = err_temp) TEMP
               GETINT = INT(TEMP)
            END IF
            if (err_temp == 0) exit
         end do tem
      end do
1     FORMAT(F7.0)
35    format (A40)
60    format (' Try again: input is outside of range = [', I6, I6, ']')
   end function

   character(len=40) function charac(c, clngth, cprmpt)
      !gets character string CHARAC no longer than CLNGTH from the screen
      ! Global variables:
      use io_all
      implicit none
      ! INput variables:
      character(len=*) :: c         !default value
      character(len=*) :: cprmpt    !prompt
      integer :: clngth             !max length
      ! Local variables:
      character(len=40) :: string   !internal unit
      ! Function(replace by len_trim)
      ! integer :: lentru
      integer :: err_string, err_charac

      !data can't be longer than 40 characters due to fixed format
      if ( clngth > 40 ) clngth = 40

      !prompt for string; display default value C
      cha: do
         str: DO
            WRITE (OUNIT,20) CPRMPT(1:len_trim(CPRMPT)), C(1:len_trim(C))
            READ (IUNIT,35, iostat = err_string) STRING
            if (err_string == 0) exit
         END DO str

         !accept default value C if STRING is empty
         IF (len_trim(STRING) == 0) THEN
            CHARAC=C
         ELSE
            READ (STRING,35, iostat = err_charac) CHARAC
         END IF
         if (err_charac == 0) exit
      end do cha

      !find the true length of the input; verify that it is not too long
      do while (len_trim(charac) > clngth)
         cha2: do
            str2: do
               write(OUNIT, 60) clngth
               read (IUNIT, 35, iostat = err_string) string
               if (err_string == 0) exit
            end do str2

            if ( len_trim(string) == 0 ) then
               charac = c
            else
               read (string, 35, iostat = err_charac) charac
            end if
            if (err_charac == 0) exit
         end do cha2
      end do

20    format (1x, A, 1X, '[', A, ']')
35    format (A40)
60    format (' Try again: string is too long, maximum lenght = ', I2)
   end function

   integer function yesno(binary, prompt)
      !obtains YESNO from the screen; value is 0 for no, 1 for yes
      ! Global variables:
      use io_all
      implicit none
      ! Input parameters:
      character(len=*) :: prompt    !prompt
      integer :: binary             !default value
      ! Local variables:
      character(len=3) :: string    !internal unit
      ! Functions (replace by len_trim)
      ! integer :: lentru
      integer :: err_string

      yon:do
         do
            ! write prompt and display default values
            IF (BINARY == 1) WRITE(OUNIT,10) PROMPT(1:len_trim(PROMPT))
            IF (BINARY == 0) WRITE(OUNIT,11) PROMPT(1:len_trim(PROMPT))
            !
            READ (IUNIT, 20, iostat = err_string) STRING
            if (err_string == 0) exit
         end do
         !
         ! accept default value; check that input is 'y' or 'n'
         IF (len_trim(STRING) == 0) THEN
            YESNO = BINARY
            exit
         ELSE IF (STRING(1:1) == 'y' .OR. STRING(1:1) == 'Y') THEN
            YESNO = 1
            exit
         ELSE IF (STRING(1:1) == 'n' .OR. STRING(1:1) == 'N') THEN
            YESNO = 0
            exit
         ELSE
            WRITE (OUNIT,200)
         END IF
      end do yon
      !
10    FORMAT (1X, A, 1X, '[yes]')
11    FORMAT (1X, A, 1X, '[no]' )
20    FORMAT (A)
200   FORMAT (' Try again, answer must be yes or no')
   end function

   logical function logcvt(IJK)
      !converts 1 to true and anything else to false
      implicit none
      INTEGER IJK !input
      IF (IJK == 1) THEN
         LOGCVT = .TRUE.
      ELSE
         LOGCVT = .FALSE.
      END IF
   end function
end module menu_all
