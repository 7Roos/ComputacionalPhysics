! O problema básico é encontrar para cada inteiro n, o valor da energia para o qual a Eq. (7) é satisfeita.
module param_e1
   implicit none
   REAL, parameter :: PI = 4*atan(1.) !pi=3.15159
   REAL :: POTMIN       !x value at equilibrium
   REAL :: GAMMA        !=sqrtB*mass*length**2*potential/hbar**2)
   REAL :: ETOL         !tolerance for energy search
   REAL :: XTOL         !tolerance for turning point search
   INTEGER :: NPTS      !number of integration points
   INTEGER :: NLEVEL    !total number of bounds states (depends on gamma)
   !
   INTEGER :: NGRF      !number of points for graphics output
   INTEGER, parameter :: MAXGRF = 1000      !maximum number of graphing points
   INTEGER, parameter :: MAXLVL = 100       !maximum number of quantum levels
end module param_e1

module map_e1
   implicit none
   integer, parameter :: igamma = 13
   integer, parameter :: ietol = 38
   integer, parameter :: ixtol = 39
   integer, parameter :: inpts = 40
   integer, parameter :: ingrf = 87
end module map_e1

program Exam1
   implicit none

   call init()    !Exibe a tela do cabeçalho e os parâmetros de configuração

   
   do
      call param()   !get input from screen
      
      call archon()  !search for bound states
   end do

end program Exam1

subroutine init()
   ! Inicializa de constantes e exibir tela de cabeçalho.
   ! Inicializa menu arrays para input dos parâmetros.
   !  No lugar do "INCLUDE 'IO.ALL'", trocamos por módulo, que é mais moderno e apropriado para Modern Fortran.
   ! Global variables
   use io_all
   use menu_all
   use param_e1
   implicit none
   !Local parameters:
   character(len=80), dimension(20) :: descrp   ! Descrição do programa.
   integer :: nhead, ntext, ngraph              ! Número de linhas para cada descritor.

   ! Obter parâmetros de ambiente.
   Call setup()

   ! Exibir tela de cabeçalho.
   descrp(1) = 'Example 1'
   descrp(2) = 'Bohr-Sommerfeld quantization for bound state'
   descrp(3) = 'energies of the 6-12 potential'
   nhead = 3

   ! Descrição da saída de texto.
   descrp(4) = 'energy and classical turning points for each state'
   ntext = 1

   ! Descri��ão da saída gráfica.
   descrp(5) = 'phase space (wavenumber vs. position) portrait'
   descrp(6) = 'of classical trajectories'
   ngraph = 2

   call header(descrp, nhead, ntext, ngraph)

   ! calculate constants
   !pi = 4*atan(1.)  ! Defined in module io_all

   ! Example 1:
   !POTMIN = 2**(1.D0/6.D0)

   !Exercise 1.7: Pot parabolic
   POTMIN = 0.D0
   

   !setup menu arrays, beginning with constant part
   call menu()

   MTYPE(13) = FLOAT
   MPRMPT(13) = 'Enter gamma=sqrtB*m*a**2*V/hbar**2) (dimensionless)'
   MTAG(13) = 'Gamma (dimensionless)'
   MLOLIM(13) = 1.
   MHILIM(13) = 500.
   MREALS(13) = 50.

   MTYPE(14) = SKIP
   MREALS(14) = 35.

   MTYPE(38) = FLOAT
   MPRMPT(38) = 'Enter tolerance for energy search (scaled units)'
   MTAG(38) = 'Energy search tolerance (scaled units)'
   MLOLIM(38) = 0.00001
   MHILIM(38) = 0.01
   MREALS(38) = 0.0005

   MTYPE(39) = FLOAT
   MPRMPT(39) = 'Enter tolerance for turning point search (scaled units)'
   MTAG(39) = 'Turn point search tolerance (scaled units)'
   MLOLIM(39) = 0.00001
   MHILIM(39) = 0.01
   MREALS(39) = 0.0005

   MTYPE(40) = NUM
   MPRMPT(40) = 'Enter number of points for action integral'
   MTAG(40) = 'Number of quadrature points for action integral'
   MLOLIM(40) = 20.
   MHILIM(40) = 5000.
   MINTS(40) = 100

   MTYPE(41) = SKIP
   MREALS(41) = 60.

   MSTRNG(MINTS(75)) = 'exmpll.txt'

   MTYPE(76) = SKIP
   MREALS(76) = 80.

   MSTRNG(MINTS(86)) = 'exmpll.grf'

   MTYPE(87) = NUM
   MPRMPT(87) = 'Enter number of points to be used in graphing'
   MTAG(87) = 'Number of graphing points'
   MLOLIM(87) = 10.
   MHILIM(87) = MAXGRF - 2
   MINTS(87) = 80

   MTYPE(88) = SKIP
   MREALS(88) = 90.
end subroutine

subroutine param()
   !C gets parameters from screen
   ! ends program on request
   ! closes old files
   ! maps menu variables to program variables
   ! opens new files
   ! calculates all derivative parameters
   ! performs checks on parameters
   !
   ! Global variables:
   use menu_all
   use io_all
   use param_e1
   use map_e1
   implicit none
   ! Local variables:
   real :: S         !current value of action
   real :: E1        !current value of energy
   real :: X1, X2    !current turning points
   ! Function:
   !logical :: logcvt !converts 1 and 0 to true and false

   !get input from terminal
   call clear()
   call ask(1, istop)

   !stop program if requested
   IF (MREALS(IMAIN) == STOP) CALL FINISH()

   !close files if necessary
   IF (TNAME /= MSTRNG(MINTS(ITNAME))) CALL FLCLOS(TNAME,TUNIT)
   IF (GNAME /= MSTRNG(MINTS(IGNAME))) CALL FLCLOS(GNAME,GUNIT)

   !physical and numerical parameters
   GAMMA = MREALS(IGAMMA)
   ETOL = MREALS(IETOL)
   XTOL = MREALS(IXTOL)
   NPTS = MINTS(INPTS)

   !text output parameters
   TTERM = LOGCVT(MINTS(ITTERM))
   TFILE = LOGCVT(MINTS(ITFILE))
   TNAME = MSTRNG(MINTS(ITNAME))(1:12)

   !graphics output parameters
   GTERM = LOGCVT(MINTS(IGTERM))
   GHRDCP = LOGCVT(MINTS(IGHRD))
   GFILE = LOGCVT(MINTS(IGFILE))
   GNAME=  MSTRNG(MINTS(IGNAME))(1:12)
   NGRF = MINTS(INGRF)

   !open files
   IF (TFILE) CALL FLOPEN(TNAME,TUNIT)
   IF (GFILE) CALL FLOPEN(GNAME,GUNIT)
   !files may have been renamed
   MSTRNG(MINTS(ITNAME)) = TNAME
   MSTRNG(MINTS(IGNAME)) = GNAME

   !calculate total number of levels
   E1 = -ETOL
   CALL ACTION(E1,X1,X2,S)

   NLEVEL = INT(S/PI - .5) + 1

   !check value of GAMMA
   CALL PCHECK()
   call clear()
end subroutine

subroutine action(E, X1, X2, S)
   !calculates the (action integral)/2 (S) and the classical turning
   ! points (Xl,X2) for a given energy (E)
   !
   ! Global variables:
   use param_e1
   implicit none
   ! Input/output variables:
   real :: E         !energy (input)
   real :: S         !action (output)
   real :: X1, X2    !turning points (output)
   ! Local variables:
   real :: dx        !increment in turning point search
   real :: h         !quadrature step size
   real :: sum       !sum for integral
   integer :: ifac   !coefficient for Simpson's rule
   integer :: ix     !index on X
   real :: x         !current X value in sum
   real :: pot       !potential as a function of X (function)

   !find inner turning point; begin search at the well bottom
   x1 = POTMIN
   dx = .1

   do while(dx > XTOL)
      x1 = x1 - dx      !use simple search, going inward
      
      if ( pot(x1) >= E ) then
         
         x1 = x1 + dx
         dx = dx/2.
      end if
   end do

   !find the outer turning point; begin search at the well bottom
   x2 = POTMIN
   dx = .1
   do while(dx > XTOL)
      x2 = x2 + dx      !use aimpla aaarch going outward
      if ( pot(x2) >= E ) then
         x2 = x2 - dx
         dx = dx / 2.
      end if
   end do

   !Simpson's rula from X1+H to X2-H
   if ( mod(npts,2) == 1 ) NPTS = NPTS + 1   !NPTS must ba avan
   h = (x2 - x1) / NPTS
   sum = sqrt(e - pot(x1 + h))
   ifac = 2
   do ix = 2, NPTS-2
      x = x1 + ix*h
      if ( ifac == 2 ) then
         ifac = 4
      else
         ifac = 2
      end if
      sum = sum + ifac*sqrt(E - pot(x))
   end do

   sum = sum + sqrt(E - POT(x2 - H))
   SUM = sum*h / 3.

   !spacial hancLLing for »qrt bahavior of first and laat intarvals
   sum = sum + sqrt(E - pot(X1 + h))*2*h/3.
   sum = sum + sqrt(E - pot(x2 - h))*2*h/3.
   s = sum*gamma
end subroutine

real function pot(x)
   !evaluates the Lennard-Jones potential at X
   implicit none
   ! Passed variable:
   real :: x

   !If you change the potential, normalize to a minimum of -1
   ! and change the value of POTMIN in subroutine INIT to the
   ! new equilibrium position (i.e. the X value at which the force is zero)
   ! Lannard-Jonas potantlal in scaled variables

   ! Example 1:
   !pot = 4*(x**(-12) - x**(-6))

   ! Exercise 1.7: V(r) = r**2
   pot = -1.D0 + x**2
end function

subroutine PCHECK()
   !ensure that the number of states is not greater than the size of
   ! the data arrays; if so prompt for smaller GAMMA
   !
   ! Global parameters:
   use param_e1
   use menu_all
   use io_all
   use map_e1
   implicit none
   ! Local parameters:
   real :: s         !action
   real :: e         !small negative energy
   real :: x1, x2    !classical turning points
   ! Function (Procedure of module.)
   !real :: getflt    !returns a floating point variable

   do while((NLEVEL - 1) > MAXLVL)
      write(OUNIT, 15) NLEVEL, MAXLVL
      MHILIM(igamma) = gamma
      MREALS(igamma) = getflt(MREALS(igamma)/2, MLOLIM(igamma), MHILIM(igamma), 'Enter a smaller gamma')
      gamma = MREALS(igamma)

      E = -ETOL
      call action(E, X1, X2, S)
      NLEVEL = int(s/pi + .5) + 1
   end do
15 format ('Total number of levels (=', I5, &
   & ') is larger than maximum allowable (=', I3, ')')
end subroutine

subroutine archon()
   !finds the bound states of the Lennard-Jones potential
   ! from the Bohr-Sommerfeld quantization rule
   !
   ! Global variables
   use io_all
   use param_e1
   USE menu_all ! Para poder utilizar a sub-rotina pause.
   implicit none
   ! Local variables:
   REAL :: S !current value of action
   REAL :: E1 !current value of energy
   REAL :: X1,X2 !current turning points
   REAL :: F1 !f=action/2 - pi/2 -ilevel*pi
   INTEGER :: ILEVEL !current level
   REAL :: ENERGY(0:MAXLVL) !energy of bound state
   REAL :: XIN(0:MAXLVL) !inner turning point
   REAL :: XOUT(0:MAXLVL) !outer turning point
   INTEGER :: NLINES !number of lines printed to terminal
   INTEGER :: SCREEN !send to terminal
   INTEGER :: PAPER !make a hardcopy
   INTEGER :: FILE !send to a file

   ! Inicializa variables:
   SCREEN = 1; PAPER = 2; file = 3

   !output summary of parameters
   IF (TTERM) CALL PRMOUT(OUNIT,NLINES)
   IF (TFILE) CALL PRMOUT(TUNIT,NLINES)
   IF (GFILE) CALL PRMOUT(GUNIT,NLINES)

   !search for bound states
   E1 = -1. !begin at the well bottom
   F1 = -PI/2. !the action ls zero there
   
   !find the NLEVEL bound states
   do ILEVEL = 0, NLEVEL - 1
      CALL SEARCH(ILEVEL, E1, F1, X1, X2) !search for eigenvalue
      ENERGY(ILEVEL) = E1                 !store values for this state
      XIN(ILEVEL) = X1
      XOUT(ILEVEL) = X2

      !text output
      IF (TTERM) CALL TXTOUT(OUNIT, ILEVEL, E1, X1, X2, NLINES)
      IF (TFILE) CALL TXTOUT(TUNIT, ILEVEL, E1, X1, X2, NLINES)

      F1 = F1-PI !guess to begin search for next level
   end do

   

   IF (TTERM) CALL PAUSE(' to continue...',1)
   IF (TTERM) CALL CLEAR
   !graphics output
   ! CONTINUAR A PARTIR DAQUI
end subroutine

subroutine PRMOUT(munit, NLINES)
   !outputs parameter summary to the specified unit
   ! Global variables:
   use io_all
   use param_e1
   USE menu_all ! Para poder utilizar a sub-rotina pause.
   implicit none
   ! Input/output variables:
   integer :: munit     !unit number for output (input)
   integer :: nlines    !number of lines written so far (output)

   if ( munit == OUNIT ) call clear()

   WRITE (MUNIT,2)
   WRITE (MUNIT,4)
   WRITE (MUNIT,6) ETOL,XTOL
   WRITE (MUNIT,8) NPTS
   WRITE (MUNIT,10) GAMMA,NLEVEL
   WRITE (MUNIT,12)
   WRITE (MUNIT,2)
   IF (MUNIT /= GUNIT) THEN
      WRITE (MUNIT,20)
      WRITE (MUNIT,25)
   END IF

   NLINES = 7

2  format (' ')
4  format (' Output from example 1: Bohr Sommerfeld Quantization')
6  format (' Energy tolerance =', E12.5, &
   & '   position tolerance =', E12.5)
8  format (' number of quadrature points =', I4)
10 format (' For gamma =', F8.2, ' there are', I4, ' levels:')
12 format (' (all quantities are expressed in scaled units)')
20 format (8x, 'Level', 8x, 'Energy', 12x, 'Xmin', 12x, 'xmax')
25 format (8X, '-----', 8X, '------', 12X, '----', 12X ,'----')
end subroutine

subroutine search(N, E1, F1, X1, X2)
   !finds the N'th bound state
   ! El is passed in as initial guess for the bound state energy
   ! and returned as the true bound state energy with turning points
   ! X1 and X2
   ! F1 is the function which goes to zero at a bound state
   ! F1 = action/2-(n+1/2)*pi
   !
   ! Global variables:
   use param_e1
   implicit none
   ! Input/Outuput variables:
   INTEGER :: N      !current level (input)
   REAL :: E1, E2     !trial energies (I/O)
   REAL :: F1, F2     !f=action/2-pi*(n+l/2) (I/O)
   REAL :: S         !action (output)
   REAL :: X1, X2     !turning points (output)
   ! Local variables:
   REAL :: DE        !increment in energy search

   !guess the next energy in order to begin search
   E2 = E1 + ABS(E1)/4.
   DE = 2*ETOL

   ! use secant search to find the bound state
   do while (abs(de) > etol)
      CALL ACTION(E2, X1, X2, S) !S at new energy
      F2 = S - (N + .5)*PI       !F at new energy
      IF (F1 /= F2) THEN         !calculate new DE
         DE = -F2*(E2 - E1)/(F2 - F1)
      ELSE
         DE = 0.
      END IF

      E1 = E2                       !roll values
      F1 = F2
      E2 = E1 + DE                  !increment energy
      if (E2 >= 0) E2 = - ETOL      !keep energy negative
   end do
end subroutine

SUBROUTINE TXTOUT(munit, ilevel, e, x1, x2, nlines)
   !writes results for one state to the requested unit
   !
   ! Global variables:
   use io_all
   use menu_all
   implicit none
   ! Input variables:
   INTEGER :: MUNIT !output unit specifier
   INTEGER :: ILEVEL !current level
   REAL :: E !eigen energy
   REAL :: X1,X2 !classical turning points
   INTEGER :: NLINES !number of lines printed so far

   !if screen is full, clear screen and retype headings

   if ( mod(NLINES, TRMLIN - 6) == 0 .AND. (MUNIT == OUNIT)) then
      call pause(' to continue...', 1)
      call clear()
      write(MUNIT, 20)
      write(MUNIT, 25)
   end if

   WRITE (MUNIT,30) ILEVEL, E, X1, X2

   ! keep track of printed lines only for terminal output
   IF (MUNIT == OUNIT) NLINES = NLINES+1
20 FORMAT (8X, 'Level', 8X, 'Energy', 12X, 'Xmin', 12X, 'Xmax')
25 FORMAT (8X, '-----', 8X, '------', 12X, '----', 12X ,'----')
30 format (8X, I4, 3(8X, F8.5))
end subroutine

subroutine grfout(device, energy, xin, XOUT)
   !outputs phase space portraits of the bound states to the terminal
   ! and/or a file
   !
   ! Global variables:
   use io_all
   use param_e1
   use grfdat_all
   implicit none
   !Input variables:
   INTEGER :: DEVICE          !which device is being used?
   REAL :: ENERGY(0:MAXLVL)   !energy of bound state
   REAL :: XIN(0:MAXLVL)      !inner turning point
   REAL :: XOUT(0:MAXLVL)     !outer turning point
   !Local parameters:
   INTEGER :: ILEVEL             !level index
   REAL :: H                     !step size for x
   INTEGER :: IX                 !x index
   REAL :: E                     !current energy
   REAL :: K(MAXGRF)             !current wavenumber
   REAL :: X(MAXGRF)             !current position
   CHARACTER(LEN=9) :: CGAMMA,CN !Gamma,nlevel as a character string
   REAL :: POT                   !potential (function)
   INTEGER :: LEN,NLEN           !length of character data
   INTEGER :: SCREEN             !send to terminal
   INTEGER :: PAPER              !make a hardcopy
   INTEGER :: FILE               !send to a file

   ! Inicialization variables:
   SCREEN = 1; paper = 2; FILE = 3

   !messages for the impatient
   IF (DEVICE /= SCREEN) WRITE (OUNIT,100)

   !calculate parameters for graphing

   if ( DEVICE /= file ) then
      NPLOT = 1 !how many plots
      IPLOT = 1

      YMAX = GAMMA*SQRT(1. + ENERGY(NLEVEL - 1)) !limits on data points
      YMIN = -YMAX
      XMIN = XIN(NLEVEL - 1)
      XMAX = XOUT(NLEVEL - 1)
      YOVAL = XMIN
      XOVAL = 0.

      IF (MOD(NGRF,2) == 0) NGRF = NGRF + 1

      NPOINT = NGRF  !keep number of points odd

      ILINE = 1      !line and symbol styles
      ISYM = 1
      IFREQ = 0
      NXTICK = 5
      NYTICK = 5

      CALL CONVRT(GAMMA, CGAMMA, LEN) !titles and labels
      CALL ICNVRT(NLEVEL, CN, NLEN)

      INFO=' NLEVEL = ' // CN(1:NLEN)
      TITLE = 'Semiclassically Quantized Trajectories, Gamma = ' // CGAMMA
      LABEL(1) = 'scaled position'
      LABEL(2) = 'scaled wave number'

      CALL GTDEV(DEVICE)                      !device nomination
      IF (DEVICE == SCREEN) CALL GMODE        !change to graphics mode
      CALL LNLNAX()                           !draw axes
   end if

   ! calculate classical phase space trajectory for each bound state
   ! by finding the scaled wavenumber as a function of X and Energy
   do ILEVEL = 0, NLEVEL - 1
      E = ENERGY(ILEVEL)
      H = (XOUT(ILEVEL) - XIN(ILEVEL))/((NGRF - 1)/2) !step size
      X(1) = XIN(ILEVEL)
      K(1) = 0.

      do IX = 1, (NGRF - 1)/2
         X(IX + 1) = XIN(ILEVEL) + (IX)*H
         K(IX + 1) = (E - POT(X(IX + 1))) !scaled wave number
         IF (K(IX) <= 0) THEN
            K(IX) = 0.
         ELSE
            K(IX) = GAMMA*SQRT(K(IX))
         END IF
      end do

      do IX = (NGRF + 1)/2, NGRF - 1 !graph is symmetric about x-axis
         X(IX + 1) = X(NGRF-IX)
         K(IX + 1) = -K(NGRF-IX)
      end do

      !output results
      if ( DEVICE == FILE ) then
         WRITE (GUNIT,75) E
         WRITE (GUNIT,70) (X(IX), K(IX), IX = 1, NGRF)
      else
         CALL XYPLOT(X,K)
      end if
   end do

   !end graphing session
   IF (DEVICE /= FILE) CALL GPAGE(DEVICE) !close graphing package
   IF (DEVICE == SCREEN) CALL TMODE       !switch to text mode

70 format (2(5X, E11.3))
75 format ( /, ' Position vs. wave number for Energy =', 1PE11.3)
100 format ( /,' Patience, please; output going to a file.')
contains
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
end subroutine
!Pág. 264
