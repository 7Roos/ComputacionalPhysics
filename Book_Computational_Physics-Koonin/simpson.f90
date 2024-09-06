module calc
   implicit none
   real, parameter :: pi = 4*atan(1.)
   real, parameter :: alpha = 1.
   real, parameter :: infinity = 1E2
contains
   real function fun(x)
      implicit none
      real, intent(in) :: x

      !fun = exp(-alpha * (x**2))
      fun = 1. / (1.  + x**2)
   end function

   real function fun2D(x, y)
      implicit none
      real, intent(in) :: x, y

      !fun2D = exp(y - x)
      fun2D = x + y
   end function

   subroutine int_simpson(a, b, result)
      implicit none
      real, intent(in) :: a, b              !Limites de integração
      real, intent(out) :: result           !Resultado da integral
      integer :: nPoints = 10    !Número de pontos
      real :: h, sum, x
      integer :: fac, i


      do
         h = (b - a) / nPoints

         if (h < 1E-1) exit
         nPoints = nPoints + 100
      end do

      if (mod(nPoints, 2) /= 0) nPoints = nPoints + 1 !Para garantir que seja possível dividir em partes iguais

      sum = fun(a)  !contribuição do ponto inicial

      fac = 2       !Fator da regra de Simpson
      do i = 1, nPoints - 1
         if ( fac == 2 ) then
            fac = 4
         else
            fac = 2
         end if
         x = i*h
         sum = sum + fac*fun(x)
      end do
      sum = sum + fun(b)    !contribuição do ponto final

      result = sum*h/3.
   end subroutine

   subroutine trapezio2D(x0, xn, y0, yn, result)
      implicit none
      real, intent(in) :: x0, xn, y0, yn              !Limites de integração
      real, intent(out) :: result           !Resultado da integral
      integer :: n = 2    !Número de pontos
      real :: hx, hy, sum, x, y, fac, fac2
      integer :: i, j

      hx = (xn - x0) / n
      hy = (yn - y0) / n

      do j = 0, n
         x = x0 + j*hx
         if ( j == 0 .OR. j == n ) then
            fac2 = 1
         else
            fac2 = 2
         end if

         do i = 0, n
            y = y0 + i * hy
            if ( i == 0 .OR. i == n ) then
               fac = 1
            else
               fac = 2
            end if

            sum = sum + fac2*fac*fun2D(x, y)
         end do
      end do

      result = sum*hx*hy / 4.
   end subroutine


   subroutine int_simpson2D(x0, xn, y0, yn, result)
      implicit none
      real, intent(in) :: x0, xn, y0, yn              !Limites de integração
      real, intent(out) :: result           !Resultado da integral
      integer :: nPoints = 200    !Número de pontos
      real :: hx, hy, sum, x, y
      integer :: fac, fac2, i, j

      do
         hx = (xn - x0) / nPoints
         hy = (yn - y0) / nPoints

         if ( MAX(hx, hy) < 1E-1) exit
         nPoints = nPoints + 100
      end do

      if (mod(nPoints, 2) /= 0) nPoints = nPoints + 1 !Para garantir que seja possível dividir em partes iguais

      hx = (xn - x0) / nPoints
      hy = (yn - y0) / nPoints

      !contribuição do ponto inicial, fixamos y e varremos x.
      sum = 0.

      do j = 0, nPoints
         y = y0 + j*hy

         if ( j == 0 .OR. j == nPoints ) then
            !Ponto inicial e final
            fac2 = 1
         else if (fac2 == 1) then
            ! Primeira alternância de fatores
            fac2 = 4
         else if (fac2 == 4) then
            fac2 = 2
         else if (fac2 == 2) then
            fac2 = 4
         end if

         do i = 0, nPoints
            x = x0 + i*hx

            if ( i == 0 .OR. i == nPoints ) then
               !Ponto inicial e final
               fac = 1
            else if (fac == 1) then
               ! Primeira alternância de fatores
               fac = 4
            else if (fac == 4) then
               fac = 2
            else if (fac == 2) then
               fac = 4
            end if

            sum = sum + fac2*fac*fun2D(x, y)
         end do
      end do

      result = sum*hx*hy/9.
   end subroutine

end module calc
program simpson
   use calc
   implicit none
   integer :: N
   real :: exact, error, numerical

   do
      write(*,*) 'Entre com a dimensão (0 stop)'
      read(*,*) N
      if ( N == 0 ) STOP

      exact = (sqrt(pi/alpha))**N

      if ( N == 1 ) then


         ! Como a função gaussiana é par, integramos apenas metade do intervalo e multiplicamos por 2.
         call int_simpson(0., infinity, numerical)
         numerical = 2*numerical

         error = abs(exact - numerical)

         print *, 'Resultado exato-numerico:', exact, '-', numerical
         print *, 'Erro:', error

      else if( N == 2 ) then
         exact = 1.
         !call trapezio2D(0., 1., 0., 1.,numerical)
         call int_simpson2D(0., 1., 0., 1., numerical)

         error = abs(exact - numerical)

         print *, 'Resultado exato-numerico:', exact, '-', numerical
         print *, 'Erro:', error
      end if
   end do

end program simpson



