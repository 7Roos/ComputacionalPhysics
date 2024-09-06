!
! Example 8: Monte Carlo simulation of the two-dimensional Ising Model.
!
!by Steven E. Koonin and Dawn C. Meredith, 1989.

module param_e8
   implicit none
   !REAL, parameter :: PI = 4*atan(1.) !pi=3.15159
   REAL :: B               !magnetic field strenght
   REAL :: J               !INTERACTION STRENGHT
   integer :: NX, NY
   REAL(KIND=8) :: DSEED   !random number seed
   INTEGER :: NTHERM       !number of thermalization sweeps
   INTEGER :: NFREQ        !freq of sweeps to avoid correlations
   INTEGER :: NSIZE        !size of groups
   integer :: NGROUP
   INTEGER :: XCNTR, YCNTR !data for centering display
   logical :: XSKIP, YSKIP ! data for centering display
   REAL, dimension(-4:4,-1:1) :: RATIO    !acceptance ratio matrix
   integer :: NSPIN !total number of spins
   logical :: terse !terse output
   !maximum horiz and vert dimensions
   !these are set assumin that you
   !have no graphics and the lenght of
   !your terminal=24
   integer, parameter :: MAXX = 79, MAXY = 20
end module param_e8

program Exam8
   implicit none

   call init()    !Exibe a tela do cabeçalho e os parâmetros de configuração

   do
      call param()   !get input from screen

      call archon()  !calculate the thermodynamic quantities
   end do

end program Exam8

!Pronta
subroutine init()
   ! Inicializa de constantes e exibi a tela de cabeçalho.
   ! Inicializa menu arrays para input dos parâmetros.
   !  No lugar do "INCLUDE 'IO.ALL'", trocamos por módulo, que é mais moderno e apropriado para Modern Fortran.
   !
   ! Global variables:
   use io_all
   use menu_all
   use param_e8
   implicit none
   !Local parameters:
   character(len=80), dimension(20) :: descrp   ! Descrição do programa.
   integer :: nhead, ntext, ngraph              ! Número de linhas para cada descritor.

   ! Obter parâmetros de ambiente.
   Call setup()

   ! Exibir tela de cabeçalho.
   descrp(1) = 'Example 8'
   descrp(2) = 'Monte Carlo simulation of the 2-D Ising Model'
   descrp(3) = 'using the Metropolis algorithm'
   nhead = 3

   ! Descrição da saída de texto.
   descrp(4) = 'acceptance rate, energy, magnetization, specific heat'
   descrp(5) = 'and susceptibility (all are values per spin)'
   ntext = 2

   ! Descrição da saída gráfica.
   descrp(6) = 'spin configuration (blank=-1; x=+1)'
   ngraph = 1

   call header(descrp, nhead, ntext, ngraph)

   !setup menu arrays, beginning with constant part
   call menu()

   MTYPE(13) = FLOAT
   MPRMPT(13) = 'Enter value for magnetic field (units of kT)'
   MTAG(13) = 'Magnetic field (units of kT)'
   MLOLIM(13) = -20.
   MHILIM(13) = 20.
   MREALS(13) = 0.

   MTYPE(14) = FLOAT
   MPRMPT(14) = 'Enter value for interactions strenght (units of kT)'
   MTAG(14) = 'interaction strength (units of kT)'
   MLOLIM(14) = -20.
   MHILIM(14) = 20.
   MREALS(14) = .3

   MTYPE(15) = SKIP
   MREALS(15) = 35.

   MTYPE(38) = NUM
   MPRMPT(38) = 'Enter number of x lattice points'
   MTAG(38) = 'Number of X lattice points'
   MLOLIM(38) = 2
   MHILIM(38) = MAXX
   MINTS(38) = 20

   MTYPE(39) = NUM
   MPRMPT(39) = 'Enter number of Y lattice points'
   MTAG(39) = 'Number of Y lattice points'
   MLOLIM(39) = 2
   MHILIM(39) = MAXY
   MINTS(39) = 20

   MTYPE(40) = NUM
   MPRMPT(40) = 'Integer random number seed for init fluctuations'
   MTAG(40) = 'Random number seed'
   MLOLIM(40) = 1000
   MHILIM(40) = 99999
   MINTS(40) = 54767

   MTYPE(41) = NUM
   MPRMPT(41) = 'Number of thermalization sweeps'
   MTAG(41) = 'Thermalization sweeps'
   MLOLIM(41) = 0
   MHILIM(41) = 1000
   MINTS(41) = 20

   MTYPE(42) = NUM
   MPRMPT(42) = 'Enter sampling frequency (to avoid correlations)'
   MTAG(42) = 'Sampling frequency'
   MLOLIM(42) = 1
   MHILIM(42) = 100
   MINTS(42) = 5

   MTYPE(43) = NUM
   MPRMPT(43) = 'Number of samples in a group'
   MTAG(43) = 'Group size'
   MLOLIM(43) = 1
   MHILIM(43) = 1000
   MINTS(43) = 10

   MTYPE(44) = NUM
   MPRMPT(44) = 'Enter number of groups'
   MTAG(44) = 'Number of groups'
   MLOLIM(44) = 1
   MHILIM(44) = 1000
   MINTS(44) = 10

   MTYPE(45) = SKIP
   MREALS(45) = 60.

   MSTRNG(MINTS(75)) = 'exmpl8.txt'

   MTYPE(76) = BOOLEN
   MPRMPT(76) = 'Do you want the short version of the output?'
   MTAG(76) = 'Short version of output'
   MINTS(76) = 0

   MTYPE(77) = SKIP
   MREALS(77) = 80.

   MSTRNG(MINTS(86)) = 'exmpl8.grf'

   MTYPE(87) = SKIP
   MREALS(87) = 90.
end subroutine

!Pronta
subroutine param()
   ! gets parameters from screen
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
   use param_e8
   implicit none
   ! Local variables:
   integer :: if_spins !possible values for sum of neighb. spins
   ! map between menu indices and parameters
   integer, parameter :: IB = 13, IJ = 14
   integer, parameter :: INX = 38, INY = 39
   integer, parameter :: IDSEED = 40, INTHRM = 41, INFREQ = 42, INSIZE = 43, INGRP = 44, ITERSE = 76

   !get input from terminal
   call clear()
   call ask(1, istop)

   !stop program if requested
   IF (MREALS(IMAIN) == STOP) CALL FINISH()

   !close files if necessary
   IF (TNAME /= MSTRNG(MINTS(ITNAME))) CALL FLCLOS(TNAME,TUNIT)
   IF (GNAME /= MSTRNG(MINTS(IGNAME))) CALL FLCLOS(GNAME,GUNIT)

   !set new parameter values
   !physical and numerical
   B = MREALS(IB)
   J = MREALS(IJ)
   NX = MINTS(INX)
   NY = MINTS(INY)
   DSEED = dble(MINTS(IDSEED))
   NTHERM = MINTS(INTHRM)
   NFREQ = MINTS(INFREQ)
   NSIZE = MINTS(INSIZE)
   NGROUP = MINTS(INGRP)

   !text output
   TTERM = LOGCVT(MINTS(ITTERM))
   TFILE = LOGCVT(MINTS(ITFILE))
   TNAME = MSTRNG(MINTS(ITNAME))(1:12)
   terse = logcvt(MINTS(ITERSE))

   !graphics output parameters
   GTERM = LOGCVT(MINTS(IGTERM))
   GHRDCP = LOGCVT(MINTS(IGHRD))
   GFILE = LOGCVT(MINTS(IGFILE))
   GNAME=  MSTRNG(MINTS(IGNAME))(1:12)

   !open files
   IF (TFILE) CALL FLOPEN(TNAME,TUNIT)
   IF (GFILE) CALL FLOPEN(GNAME,GUNIT)
   !files may have been renamed
   MSTRNG(MINTS(ITNAME)) = TNAME
   MSTRNG(MINTS(IGNAME)) = GNAME

   call clear()

   ! Calculate derivative parameters
   NSPIN = NX*NY

   do if_spins=-4,4,2
      !ratio of prob.; not all matrix elem are used
      ratio(if_spins, -1) = exp(2*(j*if_spins + B))
      ratio(if_spins, 1) = 1. / ratio(if_spins, -1)
   end do

   ! Calculate parameters for best looking text display
   if ( 2*NX <= TRMWID ) then
      XSKIP = .TRUE.                !skip spaces in x
      XCNTR = (TRMWID - 2*NX) / 2   !how to center display
   else
      XSKIP = .FALSE.
      XCNTR = (TRMWID - NX) / 2
   end if

   if ( XCNTR < 1 ) XCNTR = 1

   if ( 2*NY <= (TRMLIN - 5) ) then
      YSKIP = .TRUE.                   !skip spaces in y
      YCNTR = (TRMLIN - 2*NY) / 2 - 3  !how to center display
   else
      YSKIP = .FALSE.
      YCNTR = (TRMLIN - NY) / 2 - 3
   end if

   if ( YCNTR < 0 ) YCNTR = 0
end subroutine

!Pronta
subroutine archon()
   ! Calculates the thermodynamic quantities: energy, magnetization
   ! susceptibility, and specific heat at constant field and interaction
   ! strength
   !
   ! Global variables
   use io_all
   use param_e8
   USE menu_all ! Para poder utilizar a sub-rotina pause.
   implicit none
   ! Local variables:
   integer, dimension(MAXX, MAXY) :: spin !spin configuration
   ! All of the thermodynamic quant have 2 indices
   !(not all array elements are used, e.g. CHI(sweep, value)
   !first index is the level: sweep, group, or total
   !second index is the level: quantity, quant**2, or sigma**2
   real, dimension(3,3) :: mag      !magnetization
   real, dimension(3,3) :: energy   !energy
   real, dimension(3,3) :: CB       !specifc heat
   real, dimension(3,3) :: CHI      !suscepitility
   integer :: ITHERM                !thermalization index
   integer :: iter                  !iteraction index
   real :: accept                    !acceptance ratio
   integer :: IX, IY                !horiz and vert indices
   integer :: NLINES                !number of lines printed to terminal
   integer :: more, igrp            !how many more groups, group index
   integer :: isweep                !sweep index
   integer :: sweep, group, total   !which level of calculation
   integer :: value, square, sigsq  !which quantity
   ! Functions:
   !real :: getflt    !get floating point number from screen
   !integer :: getint !get integer data from screen
   real :: rannos    !generate a random number

   ! Inicializa variables:
   sweep = 1; group = 2; total = 3
   value = 1; square = 2; sigsq = 3

   ! output summary of parameters
   if (TTERM) call PRMOUT(OUNIT, NLINES) !terminal
   if (TFILE) call PRMOUT(TUNIT, NLINES) !datafile
   if (GFILE) call PRMOUT(GUNIT, NLINES) !graphic

   ! Random initial spin confiuration.
   ! Percorre a rede inicializando de forma aleatória as configurações de spin da rede.
   !Para isso, gera-se um número aleatório, se este for maior
   !que 1/2 temos SPIN UP, caso contrário, SPIN DOWN.
   do IX = 1, NX
      do IY = 1, NY
         if ( rannos(DSEED) > .5 ) then
            spin(IX, IY) = 1
         else
            spin(IX, IY) = -1
         end if
      end do
   end do

   ! Thermalize init config
   do ITHERM = 1, NTHERM
      call METROP(spin, accept)
      if (TTERM) write (OUNIT, 7) ITHERM, accept
      if (TFILE) write(TUNIT, 7) ITHERM, accept
   end do

7  format (5x, 'Thermalization sweep ', I4, ', acceptance ratio =', F6.3)

   if (TTERM) call pause(' to begin summing...', 1)

   ! Zero total averages
   call zero(total, mag, energy, chi, cb)
   more = NGROUP

   ! Allow for more grounps
   do
      ! Loop over groups
      do igrp = NGROUP - MORE + 1, NGROUP
         ! Zero group averages
         call zero(group, mag, energy, chi, cb)

         if ((TTERM) .AND. (.NOT. GTERM) .AND. (.NOT. TERSE)) call TITLES(OUNIT, NLINES)

         if ((TFILE) .AND. (.NOT. TERSE)) call titles(TUNIT, NLINES)

         do iter = 1, NFREQ*NSIZE
            ! Make a sweep of the lattice
            call METROP(spin, accept)

            ! Include in averages
            if ( mod(iter, NFREQ) == 0 ) then
               !which sweep is it
               isweep = iter/NFREQ 

               ! Zero sweep averages
               call zero(sweep, mag, energy, chi, cb)

               !sweep totals, add to group
               call sum(spin, mag, energy)

               !dislay data
               if ( GTERM ) then
                  call display(OUNIT, spin, mag, energy, accept, igrp, isweep)
               else if ((TTERM) .AND. (.NOT. terse)) then
                  call SWPOUT(OUNIT, mag, energy, accept, igrp, isweep, NLINES)
               end if

               if ((TFILE) .AND. (.NOT. terse)) call swpout(OUNIT, mag, energy, accept, igrp, isweep, NLINES)

               if ((GFILE) .OR. (GHRDCP)) call display(GUNIT, spin, mag, energy, accept, igrp, isweep)
            end if
         end do

         !calc total averages
         call averag(mag, energy, chi, cb, igrp)
      end do

      more = getint(10, 0, 1000, 'How many more groups?')

      if ( more > 0 ) then
         NGROUP = NGROUP + more
         NLINES = 0
         if ((TTERM) .AND. (.NOT. terse)) call clear
         cycle
      else
         exit
      end if
   end do
end subroutine

!Pronta
subroutine METROP(spin, accept)
   ! Make one sweep of the lattice using the Metropolis algorithm
   !to generate a new configuration.
   ! Global variables:
   use param_e8
   implicit none
   ! Input/Output:
   integer, dimension(MAXX, MAXY) :: spin    !spin configuration (I/O)
   real, intent(out) :: accept             !acceptance ratio
   ! Local variables:
   integer :: ix, iy                   !horizontal and vertical indices
   integer :: IXM1, IXP1, IYM1, IYP1   !indices of nearest neighbors
   integer :: NNSUM                    !sum of nearest neighbors
   ! Function:
   real :: rannos

   !zero acceptance ratio
   accept  = 0.

   do ix = 1, NX
      !nearest neighbors
      IXP1 = ix + 1

      !with periodic b.c
      if (ix == nx) IXP1 = 1

      IXM1 = ix - 1
      if (ix == 1) IXM1 = NX

      do iy = 1, NY
         !nearest neighbors
         IYP1 = iy + 1

         !with periodic b.c
         if (iy == ny) IYP1 = 1

         IYM1 = iy - 1
         if (iy == 1) IYM1 = NY

         !term to weight new configuration
         !S_{i+1, j} + S_{i-1,j} + S_{i, j+1} + S_{i, j-1}
         NNSUM = spin(ix, IYP1) + spin(ix, IYM1) + spin(IXP1, iy) + spin(IXM1, iy)

         if ( rannos(DSEED) < RATIO(NNSUM, spin(ix, iy)) ) then
            !Flip the spin
            spin(ix, iy) = -spin(ix, iy)

            !update accept count
            accept = accept + 1
         end if
      end do
   end do

   !make it a ratio
   accept = accept / NSPIN
end subroutine

!Pronta
subroutine sum(spin, mag, energy)
   ! Calculate magnetization and energy for this sweep
   !add these values to the group averages
   ! Global variables:
   use param_e8
   implicit none
   ! Input/output variables:
   integer, dimension(MAXX, MAXY), intent(in) :: spin !spin configuration
   ! All of the thermodynamic quantities have 2 indices
   !(not all array elements are used, e.g. CHI(sweep, value))
   !first index is the level: sweep, group, or total
   !second index is the quantity: value, square, or sigma**2
   real, dimension(3,3) :: mag      !magnetization
   real, dimension(3,3) :: energy   !energy
   ! Local variables:
   integer :: pairs                 !interaction sum
   integer :: sweep, group, total   !which level of calculation
   integer :: value, square, sigsq  !which quantity
   integer :: ix, iy                !horizontal and vertical indices
   integer :: IXM1, IYM1            !neighbor indices

   sweep = 1; group = 2; total = 3
   value = 1; square = 2; sigsq = 3

   !zero pair sum
   pairs = 0


   do iy = 1, NY
      !neighbor just below
      IYM1 = iy - 1
      !period b.c.
      if (iy == 1) IYM1 = ny
      do ix = 1, NX
         !neighbor to the left
         if (ix == 1) IXM1 = nx

         ! This method of summing pairs does not count twice
         !PAIRS = PAIRS + SPIN(IX, IY)*(SPIN(IX, IYM1) + SPIN(IXM1,IY))
         !magnetization is the sum of the spins

         mag(sweep,value) = mag(sweep, value) + spin(ix, iy)
      end do
   end do

   mag(sweep, square) = mag(sweep, value)**2
   energy(sweep, value) = -J*pairs - B*mag(sweep, value)
   energy(sweep, square) = energy(sweep, value)**2

   ! Add sweep contributions to group sums
   mag(group, value) = mag(group, value) + mag(sweep, value)
   mag(group, square) = mag(group, square) + mag(sweep, square)

   energy(group, value) = energy(group, value) + energy(sweep, value)
   energy(group, square) = energy(group, square) + energy(sweep, square)
end subroutine

!Pronta
subroutine averag(mag, energy, chi, cb, igroup)
   ! Find group averages from group sums and add these to total averages;
   !calculate uncertainties and display results
   ! Global variables:
   use param_e8
   use io_all
   implicit none
   ! Input/Outut variables:
   ! All of the thermodynamic quantities have 2 indices
   !(not all array elements are used, e.g. CHI(sweep, value))
   !first index is the level: sweep, group, or total
   !second index is the value: quantity, quant**2, or sigma**2
   real, dimension(3,3) :: mag      !magnetization
   real, dimension(3,3) :: energy   !energy
   real, dimension(3,3) :: cb       !specific heat
   real, dimension(3,3) :: chi      !susceptibility
   integer, intent(in) :: igroup    !group index
   ! Local variables:
   real :: m, msig1, msig2 !magnetization and uncertainties
   real :: e, esig1, esig2 !energy and uncertainties
   real :: sus, sussig !susceptibility and uncertainty
   real :: c, csig !specific heat and uncertainty
   integer :: iquant !index the quantity
   integer :: sweep, group, total !which level of calculation
   integer :: value, square, sigsq !which quantity

   sweep = 1; group = 2; total = 3
   value = 1; square = 2; sigsq = 3

   ! Calculate group averages and uncertainties from group sums
   do iquant = value, square
      mag(group, iquant) = mag(group, iquant) / NSIZE
      energy(group, iquant) = energy(group, iquant) / NSIZE
   end do

   chi(group, value) = mag(group, square) - mag(group, value)**2

   mag(group, sigsq) = chi(group, value) / NSIZE
   if (mag(group, sigsq) < 0.) mag(group, sigsq) = 0.

   cb(group, value) = energy(group, square) - energy(group, value)**2

   energy(group, sigsq) = cb(group, value) / NSIZE
   if (energy(group, sigsq) < 0.) energy(group, sigsq) = 0.

   chi(group, square) = chi(group, value)**2
   cb(group, square) = cb(group, value)**2

   ! Add group to total sums
   do iquant = value, sigsq
      mag(total, iquant) = mag(total, iquant) + mag(group, iquant)
      energy(total, iquant) = energy(total, iquant) + energy(group, iquant)
      chi(total, iquant) = chi(total, iquant) + chi(group, iquant)
      cb(total, iquant) = cb(total, iquant) + cb(group, iquant)
   end do

   ! Find total averages using total sums accumulated so far
   m = mag(total, value) / igroup
   msig1 = (mag(total, square) / igroup - m**2) / igroup / NSIZE
   if (msig1 < 0) msig1 = 0.
   msig1 = sqrt(msig1)
   msig2 = sqrt(mag(total, sigsq)) / igroup

   E = energy(total, value) / igroup
   esig1 = (energy(total, square) / igroup - E**2) / igroup / NSIZE
   if (esig1 < 0) esig1 = 0.
   esig1 = sqrt(esig1)
   esig2 = sqrt(energy(total, sigsq)) / igroup

   sus = chi(total, value) / igroup
   sussig = (chi(total, square) / igroup - sus**2) / igroup
   if (sussig < 0.) sussig = 0.
   sussig = sqrt(sussig)

   c = cb(total, value) / igroup
   csig = (cb(total, square) / igroup - c**2) / igroup
   if (csig < 0) csig = 0.
   csig = sqrt(csig)

   ! Write out summary
   if (TTERM) call TXTOUT(mag, energy, cb, chi, E, esig1, esig2, M, msig1, msig2, sus, sussig, c, csig, igroup, OUNIT)

   if (TFILE) call TXTOUT(mag, energy, cb, chi, E, esig1, esig2, M, msig1, msig2, sus, sussig, c, csig, igroup, TUNIT)
end subroutine

!Pronta
subroutine zero(ilevel, mag, energy, chi, cb)
   ! Zero for ILEVEL thermodynamic values
   implicit none
   ! Input/Output variabels:
   integer, intent(in) :: ilevel !which level to zero
   ! All of the thermodynamic quantities have 2 indices
   !(not all array elements are used, e.g. CHI(sweep, value))
   !first index is the level: sweep, group, or total
   !second index is the value: quantity, quant**2, or sigma**2
   real, dimension(3,3), intent(out) :: mag !magnetization
   real, dimension(3,3), intent(out) :: energy  !energy
   real, dimension(3,3), intent(out) :: cb !specific heat
   real, dimension(3,3), intent(out) :: chi !susceptibility
   ! Local variables:
   integer :: iquant

   do iquant = 1, 3
      mag(ilevel, iquant) = 0.
      energy(ilevel, iquant) = 0.
      chi(ilevel, iquant) = 0.
      cb(ilevel, iquant) = 0.
   end do
end subroutine

!Pronta
subroutine PRMOUT(munit, NLINES)
   ! Write out parameter summary to munit
   ! Global variables:
   use io_all
   use param_e8
   USE menu_all ! Para poder utilizar a sub-rotina pause.
   implicit none
   ! Input/output variables:
   integer :: munit     !Fortran unit number
   integer :: nlines    !number of lines sent to terminal

   if ( munit == OUNIT ) call clear()

   WRITE (MUNIT,5)
   WRITE (MUNIT,6)
   WRITE (MUNIT,7) B
   WRITE (MUNIT,8) J
   WRITE (MUNIT,10) NX, NY
   WRITE (MUNIT,15) NTHERM
   WRITE (MUNIT,20) NFREQ, NSIZE
   write(munit, *) ' '

   NLINES = 7

5  format (' Output from example 8:')
6  format (' Monte Carlo Simulation of the', &
   & '2-D Ising Model using the Metropolis Algorithm')
7  format (' Magnetic field (unit of kT) =', 1PE12.5)
8  format (' Interaction strenght (units of kT) =', 1PE12.5)
10 format (' NX =', I3, 5X, ' NY =', I3)
15 format (' numer of thermalization sweeps =', I4)
20 format (' sweep frequency =', I4, ' group size =', I4)
end subroutine

!Pronta
subroutine display(munit, spin, mag, energy, accept, igroup, isweep)
   ! Display spin configuration (spin = -1 is a blank, spin 1 is an X)
   !and write out data for this sweep
   ! Global variables:
   use param_e8
   use io_all
   use menu_all !para usar pause
   implicit none
   ! Input variabels:
   integer, dimension(MAXX, MAXY) :: spin !spin configuration
   ! All of the thermodynamic quantities have 2 indices
   !(not all array elements are used, e.g. CHI(sweep, value))
   !first index is the level: sweep, group, or total
   !second index is the value: quantity, quant**2, or sigma**2
   real, dimension(3,3) :: mag      !magnetization
   real, dimension(3,3) :: energy   !energy
   real :: accept                   !acceptance ratio
   integer :: munit                 !unit we're writing to
   integer :: isweep, igroup        !sweep and group index
   ! Local variables
   integer :: sweep, group, total               !which level of calculation
   integer :: value, square, sigsq              !which quantity
   integer :: ix, iy                            !lattice indices
   character(len=1), dimension(MAXX) :: cspin   !spin as character data
   character(len=80) :: blnk                    ! blanks for centering in x

   !Initialization
   blnk = ' '
   sweep = 1; group = 2; total = 3
   value = 1; square = 2; sigsq = 3

   if ( munit == OUNIT ) then
      call clear()
      !center output
      do iy = 1, YCNTR
         write(OUNIT, *) ' '
      end do
   end if

   write(munit, 11) igroup, isweep, NSIZE, accept, &
   & energy(sweep, value)/NSPIN, mag(sweep, value)/NSPIN
11 format (' Group', I3, ', sweep', I3, ' out of', I3, 5X &
   & ' accept =', F6.3, ' Energy =', F7.3, ' Mag =', F6.3)

   !change +-1 to X and blanck
   do iy = NY, 1, -1
      do ix = 1, NX
         if ( spin(ix, iy) == 1 ) then
            cspin(ix) = 'X'
         else
            cspin(ix) = ' '
         end if
      end do
   end do

   ! Write out a line at a time (no centering done for TUNIT)
   if ( munit == TUNIT ) then
      ! Loop do implicit
      write(TUNIT, 16) (cspin(ix), ix = 1, nx)
   else
      if ( XSKIP ) then
         write(munit, 10) blnk(1:XCNTR), (cspin(ix), ix = 1, NX)
      else
         write(munit, 15) blnk(1:XCNTR), (cspin(ix), ix = 1, NX)
      end if
      if (YSKIP) write(munit, *) ' '
   end if
10 format (1x, A, 100(A1, 1X))
15 format (1x, A, 100(A1))
16 format (1x, 100(A1))

   if (munit == OUNIT) call pause(' to continue...', 0)
end subroutine

!Pronta
subroutine SWPOUT(munit, mag, energy, accept, igroup, isweep, nlines)
   ! And write out date for this sweep
   ! Global variables:
   use param_e8
   use io_all
   implicit none
   !Input parameters:
   ! All of the thermodynamic quantities have 2 indices
   !(not all array elements are used, e.g. CHI(sweep, value))
   !first index is the level: sweep, group, or total
   !second index is the value: quantity, quant**2, or sigma**2
   real, dimension(3,3) :: mag !magnetization
   real, dimension(3,3) :: energy !energy
   real :: accept !acceptance ratio
   integer :: munit !unit we're writing to
   integer :: isweep, igroup !sweep and group index
   integer :: nlines ! lines writen to terminal
   ! Local variables:
   integer :: sweep, group, total !which level of calculation
   integer :: value, square, sigsq !which quantity

   sweep = 1; group = 2; total = 3
   value = 1; square = 2; sigsq = 3

   write(munit, 11) igroup, isweep, NSIZE, accept, &
   & energy(sweep, value)/NSPIN, mag(sweep, value)/NSPIN
11 format (7x, I3, 7X, I3, '/', I3, 7X, F6.3, 7X, F9.5, 7X, F9.3)

   IF (munit == OUNIT) nlines = nlines + 1
end subroutine

!Pronta
SUBROUTINE TXTOUT(mag, energy, cb, chi, e, esig1, esig2, m,msig1, msig2, sus, sussig, &
& c, csig, igroup, munit)
   ! Write out averages and uncertainties to munit
   ! Global variables:
   use param_e8
   use io_all
   use menu_all !para usar pause
   !use menu_all
   implicit none
   ! Input variables:
   ! All of the thermodynamic quantities have 2 indices
   !(not all array elements are used, e.g. CHI(sweep, value))
   !first index is the level: sweep, group, or total
   !second index is the value: quantity, quant**2, or sigma**2
   real, dimension(3,3) :: mag      !magnetization
   real, dimension(3,3) :: energy   !energy
   real, dimension(3,3) :: cb       !specific heat
   real, dimension(3,3) :: chi      !susceptibility
   integer :: igroup                !group index
   real :: m, msig1, msig2          !magnetization and uncertainties
   real :: e, esig1, esig2          !energy nd uncertainties
   real :: sus, sussig              !susceptibility and uncertainty
   real :: c, csig                  !specific heat and and uncertainty
   INTEGER :: MUNIT                 !which unit number
   ! Local variable:
   integer :: sweep, group, total !which level of calculation
   integer :: value, square, sigsq !which quantity

   sweep = 1; group = 2; total = 3
   value = 1; square = 2; sigsq = 3

   write(MUNIT, 30) igroup, NGROUP
   write(MUNIT, 32)
   write(MUNIT, 33)
   write(MUNIT, 35) energy(group, value)/NSPIN, sqrt((energy(group, sigsq)))/NSPIN, &
      mag(group, value)/NSPIN, sqrt((mag(group, sigsq)))/NSPIN, &
      chi(group, value)/NSPIN, sqrt((chi(group, sigsq)))/NSPIN

   write(MUNIT, 40) e/NSPIN, esig1/NSPIN, esig2/NSPIN, m/NSPIN,  &
   & msig1/NSPIN, msig2/NSPIN, sus/NSPIN, sussig/NSPIN, c/NSPIN, csig/NSPIN

   write(MUNIT, *) ' '

   if ((MUNIT == OUNIT) .AND. (.NOT. TERSE)) call pause('to continue...', 1)

30 format (' Group', I3, ' (out of ', I4, ') averages')
32 format (14X, 'Energy', 13X, 'Magnetization', 5X, 'Susceptibility', 2x, 'Specific Heat')
33 format (14X, '------', 13X, '-------------', 5X, '--------------', 2X, '-------------')
35 format (' group', 2(1x, F7.3, ' +/-', F6.3, 6X), 2(2X, F6.3, 7X))
40 format (' total', 2(1x, F7.3, ' +/-', F6.3, ' /', F6.3), 2(1X, F6.3, '+/-', F6.3))
end subroutine

!Pronta
subroutine titles(munit, nlines)
   ! Write out text data title
   !  Global variables:
   use io_all
   implicit none
   ! Input/output variables:
   integer, intent(in) :: munit
   integer :: nlines

   if (munit == OUNIT) call clear()

   write(munit, 10)
   write(munit, 11)

10 format (6x, 'Group', 3X, 'Sweep/out of', 5X, 'Accept', 9X, 'Energy', 6X, 'Magnetization')
11 format (6X, '-----', 3X, '------------', 5X, '-----', 9X, '------', 6X, '-------------')

   if (munit == OUNIT) nlines = nlines + 2
end subroutine

real(kind=8) function RANNOS(DSEED)
   ! Return a uniformly distributed random number between 0 and 1
   implicit none 
   real(kind=8) :: DSEED
   real(kind=8) :: D2P31M, D2P31

   D2P31M = 2147483647.D0
   D2P31 = 2147483711.D0

   DSEED = MOD(16807.D0*DSEED, D2P31M)
   RANNOS = DSEED / D2P31
end function
