! Examp_4: Evolution of the error in estimating the value of pi
! Descrição: Modificamos o exemplo 3 para avaliar a evolução do
!erro nao estimar pi, esse valor deve tender para  1/\sqrt{\pi}

! Criado por: Matheus Roos
! Data: 06/01/2024

PROGRAM Examp_4
   implicit none
   character(len=22), parameter :: name = './Plots/pi_N-error.dat'
   real, parameter :: exact = 4*atan(1.)
   integer :: seed = 3274927
   integer :: ix, N, iter
   integer :: icount
   real :: x, y, pi4, error

   N = 10**9
   icount = 0
   iter = 1

   open(unit = 20, file = name)

   do ix = 1, N
      x = ran(seed)
      y = ran(seed)

      if ( (x**2 + y**2 <= 1.)) icount = icount + 1

      if ( mod(ix, 10**iter) == 0 ) then
         pi4 = 4*real(icount)/ix
         error = pi4 - exact

         write(20,*) ix, error

         write(*,*) 'Trocar iter?', N, iter, ix
         read(*,*) iter
      end if
   end do

   close(20)
END PROGRAM Examp_4
