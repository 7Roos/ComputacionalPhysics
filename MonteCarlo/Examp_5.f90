! Example 5: integration 2-D via Monte Carlo.
! Descrição: Neste exemplo de integral de Monte Carlo 2D
!estimamos o valor de pi ao calcular a área de um semi-círculo.

! Criado por: Matheus Roos
!(adaptado do livro do Steven R. Koonin)
! Data: 25/12/2023

program Ex5
   implicit none
   character(len=22), parameter :: name = './Plots/pi/pi_x-y-Erro'
   real, parameter :: exact = 4*atan(1.)
   integer :: seed = 3274927 !seed for random number generator
   integer :: n, icount, ix
   real :: x, y, pi4, sigma
   character(len=5) :: StrN


   do
      print *, 'Enter number of points (0 to stop)'
      read *, n
      if ( n == 0 ) stop

      write(StrN, '(I5)') n
      open(unit = 20, file=trim(name) // '_N(' // trim(adjustl(StrN)) // ').dat')

      icount = 0          !zero count

      do ix = 1, n        !loop over samples
         x = ran(seed)
         y = ran(seed)

         ! Se o valor satisfizer a condição imposta de validade,
         !aceitamos o sorteio como verdadeiro.
         ! Se não houvesse essa restrição, estaríamos calculando a área de um quadrado unitário,
         ! assim restringimos que ele esteja dentro do arco do semicírculo.
         if ( (x**2 + y**2) <= 1. ) icount = icount + 1

         if ( mod(ix, 100) == 0 ) then
            !A cada 100 valores calcula a média
            pi4 = real(icount)/ix            !pi/4
            write(20,*) x, y, exact - 4*pi4
         end if
      end do

      close(20)

      pi4 = real(icount)/n            !pi/4
      sigma = sqrt(pi4*(1 - pi4)/n)   !error

      print *, 'pi = ', 4*pi4, '+/-', 4*sigma, 'error = ', abs(exact - 4*pi4)
   end do
end program Ex5
