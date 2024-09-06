module Chap1
   ! NUmerical calculu of the Chapter 1
   implicit none
   real, parameter :: h_bar = 1.
   real, parameter :: pi = 4*atan(1.)
   integer, parameter :: maxlvl = 100    ! Máximo de níveis de energia
   real, parameter :: etol = 0.0005, xtol = 0.0005 ! Tolerance energia e x
   real, parameter :: potmin = 2.**(1./6.)   !Menor potencial
   real, parameter :: gamma = 50.   ! Parâmetro físico
   real, parameter :: nPOINTS = 16  ! N pontos da integral
   ! TODO: Correct the value of maxgrf
   integer :: maxgrf = 10
contains
   real function derivative(f, x)
      implicit none
      real, external :: f
      real, intent(in) :: x
      !local variable
      real, parameter :: h = 1E-2

      derivative = (f(x +h) - f(x-h)) / (2*h)
   end function

   real function integral(f, a, b)
      implicit none
      real, external :: f
      real, intent(in) :: a, b
      !local variable
      real :: h, sum, x
      integer :: fac, i, n

      n = nPOINTS

      if ( mod(n,2) /= 0 ) then
         n = n + 1
      end if

      h = (b-a) / n

      sum = f(a)

      fac = 2
      do i = 2, n-2
         if ( fac == 2 ) then
            fac = 4
         else
            fac = 2
         end if

         x = i*h
         sum = sum + fac*f(x)
      end do
      sum = sum + f(b)
      integral = sum*h/3.
   end function

   real function newton(f, guess)
      implicit none
      real, external :: f
      real, intent(in) :: guess
      ! local variable: newton algorithm
      real :: tol, x, x0, error

      tol = 1E-6
      x0 = guess

      do
         x = x0 - (f(x0) / derivative(f, x0))

         error = abs(x - x0)

         if ( error < tol ) exit

         x0 = x
      end do

      newton = x
   end function
end module Chap1