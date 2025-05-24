!! Formula 2 pts derivative
!! M. Roos, 26/03/2025

program form2Pts
   implicit none
   real(8) :: x, h, f_prime, f
   integer :: i

   f(x) = cos(x)

   ! Inputs
   write (*, *) 'Enter: x'
   read (*, *) x

   do i = 1, 8
      h = 10.d0**(-i)
      
      ! Cálculo da derivada
      f_prime = (f(x + h) - f(x))/h

      ! Impressão do resultado
      write (*, 10) h, f_prime
   end do
   10 format (2E13.4)
end program form2Pts
