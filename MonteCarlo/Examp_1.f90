! Example 1: integration via Monte Carlo.
! Descrição: Integramos um função qualquer unidimensional
!através do método de Monte Carlo.

! Criado por: Matheus Roos 
!(adaptado do livro do Steven R. Koonin)
! Data: 25/12/2023

program Ex1
   implicit none
   integer :: seed = 987654321 !seed for random number generator
   real, parameter :: exact = .78540      !exact answer
   integer :: N, iX
   real :: sumF, sumF2, fx
   real :: f_ave, f2_ave, sigma, x
   character(len=10) :: strPoints

   do
      print *, 'Enter number of points (0 to stop)'
      read *, N
      if ( N == 0 ) STOP

      write(strPoints, '(I5)') N

      open(unit=20, file="MC_" // trim(adjustl(strPoints)) // ".dat")

      sumF = 0.   !zero sums
      sumF2 = 0.

      do iX = 1, n    !loop over samples
         ! Geramos um número aleatório entre 0<ran<1, ou seja, dentro do limite de integração.
         ! Repetimos este procedimento n vezes, pegando então n pontos nesse intervalo.
         ! Então ao final tomamos a média e calculamos o desvio da média.
         x = ran(seed)
         fx = fun(x) !integrand

         !add contributions to sums
         sumF = sumF + fX
         sumF2 = sumF2 + fX**2

         write(20,*) x, fx
      end do

      !averages
      f_ave = sumF/N
      f2_ave = sumF2/N

      sigma = sqrt((f2_ave - f_ave**2) / N)   !error

      print *, 'integral =', f_ave, '+/-', sigma, 'error =', exact - f_ave

      close(20)
   end do

contains
   real function fun(x)
      !function to integrate
      implicit none
      real, intent(in) :: x
      fun = 1./(1. + x**2)
   end function
end program Ex1
