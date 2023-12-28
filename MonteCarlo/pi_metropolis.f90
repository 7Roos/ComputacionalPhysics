! Example 5: Metropolis algorith for estimative the value of pi.
! Descrição: criamos este exemplo para brincar com o algoritmo 
!Metropolis no cálculo de pi como feito nos exemplos anteriores.

! Criado por: Matheus Roos
! Data: 25/12/2023

program pi_metropolis
   implicit none
   integer :: seed = 3274927
   real, parameter :: exact = 4*atan(1.)
   real, parameter :: raio_max = 1
   integer, parameter :: n = 5000
   integer :: icount, ix
   real :: x, y, pi4, sigma, delta
   logical :: count

   !variable initialization
   icount = 0
   delta = raio_max*ran(seed)

   x = ran(seed)
   y = ran(seed)

   open(unit = 20, file='pi_x-y.dat')

   do ix = 1, n
      call metropolis(x, y, delta, count)
      

      if ( count .EQV. .TRUE. ) then
         icount = icount + 1
         write(20,*) x, y
      end if
   end do

   close(20)

   pi4 = real(icount)/n            !pi/4
   sigma = sqrt(pi4*(1 - pi4)/n)   !error

   print *, 'pi = ', 4*pi4, '+/-', 4*sigma, 'error = ', abs(exact - 4*pi4)
contains
   real function weight(x, y)
      implicit none
      real, intent(in) :: x, y
      weight = exp(1 - x**2 - y**2)
   end function

   subroutine metropolis(x, y, delta, count)
      implicit none
      real :: x, y, delta
      logical :: count
      !local variables:
      real :: new_x, new_y, ratio

      !take a trial step in square about (x,y)
      new_x = x + delta*(2*ran(seed) - 1)
      new_y = y + delta*(2*ran(seed) - 1)

      ratio = weight(new_x, new_y) / weight(x, y)

      count = .FALSE.

      if ( ratio > ran(seed) ) then !algorithm
         if ( new_x > 0 .AND. new_y > 0 ) then !first quadrant
            if ( (x**2 + y**2) <= 1. ) then !inside the circle
               x = new_x
               y = new_y

               count = .TRUE.
            end if
         end if
      end if
   end subroutine
end program pi_metropolis
