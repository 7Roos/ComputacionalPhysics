! Example 3: integration 2-D via Monte Carlo.
! Descrição: Neste exemplo de integral de Monte Carlo 2D
!estimamos o valor de pi ao calcular a área de um semi-círculo.

! Criado por: Matheus Roos
! Data: 25/12/2023

PROGRAM Examp_3
   implicit none
   integer :: seed = 3274927 !seed for random number generator
   real, parameter :: exact = 4*atan(1.)
   integer :: n, icount, ix
   real :: x, y, pi4, sigma

   do  
    print *, 'Enter number of points (0 to stop)'
    read *, n 
    if (n == 0) stop 

    icount = 0 !zero count
    do ix = 1, n !loop for samples
        x = ran(seed)
        y = ran(seed)

        if ( (x**2 + y**2 <= 1.) ) icount = icount + 1
    end do

    pi4 = real(icount) / n !pi/4
    sigma = sqrt(pi4*(1. - pi4)) !error

    print *, 'pi = ', 4*pi4, '+/-', 4*sigma, 'error = ', exact - 4*pi4
   end do
END PROGRAM Examp_3