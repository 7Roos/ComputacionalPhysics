! Example 2: integration via Monte Carlo with weight w.
! Descrição: modificamos o exemplo anterior para adicionar um peso 
!w e assim melhorar a estimativa da integral.

! Criado por: Matheus Roos
!(adaptado do livro do Steven R. Koonin)
! Data: 25/12/2023

module Ex2_mod
contains
   real function fun(x)
      implicit none
      real, intent(in) :: x
      fun = 1./(1. + x**2)
   end function

   real function weight(x)
      implicit none
      real, intent(in) :: x
      weight = (4. - 2*x)/3.
   end function

   real function xx(y)
      !x as a function of y
      implicit none
      real, intent(in) :: y
      xx = 2. - sqrt(4. - 3*y)
   end function
end module Ex2_mod

program Ex2
    use Ex2_mod
   implicit none
   integer :: seed = 987654321 !seed for random number generator
   real, parameter :: exact = .78540      !exact answer
   integer :: N, iX
   real :: sumF, sumF2, fX, f_ave, f2_ave, sigma
   ! Adicionando um peso à distribuição
   real :: x, y

   do
      print *, 'Enter number of points (0 to stop)'
      read *, N
      if ( N == 0 ) STOP

      sumF = 0.   !zero sums
      sumF2 = 0.

      do iX = 1, n    !loop over samples
         y = ran(seed)
         x = xx(y)
         fx = fun(x) / weight(x) !integrand

         sumF = sumF + fX
         sumF2 = sumF2 + fX**2
      end do

      !averages
      f_ave = sumF/N
      f2_ave = sumF2/N

      sigma = sqrt((f2_ave - f_ave**2) / N)   !error

      print *, 'integral =', f_ave, '+/-', sigma, 'error =', exact - f_ave
   end do
end program Ex2
