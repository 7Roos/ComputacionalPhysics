! Example 4: Metropolis algorith.
! Descrição: script do algoritmo Metropolis, podemos adaprá-lo
!para estimar o valor de pi e comparar com o resultado do
!exemplo anterior (daí o peso w = exp(1 - x**2 - y**2)).
! O peso w vai depender da natureza do problema.

! Criado por: Matheus Roos
!(adaptado do livro do Steven R. Koonin)
! Data: 25/12/2023

module Ex4
   implicit none
   integer :: seed = 39249187
contains
   real function weight(x, y)
      implicit none
      real, intent(in) :: x, y
      weight = exp(1 - x**2 - y**2)
   end function

   subroutine metropolis(x, y, delta)
      implicit none
      real :: x, y, delta
      !local variables:
      real :: new_x, new_y, ratio

      !take a trial step in square about (x,y)
      new_x = x + delta*(2*ran(seed) - 1)
      new_y = y + delta*(2*ran(seed) - 1)

      ratio = weight(new_x, new_y) / weight(x, y)

      if ( ratio > ran(seed) ) then
         x = new_x
         y = new_y
      end if
   end subroutine
end module Ex4
