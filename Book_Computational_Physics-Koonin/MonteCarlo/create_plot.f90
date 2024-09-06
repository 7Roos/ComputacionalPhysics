program plot
   implicit none
   real(kind=8), parameter :: step = 10.d0**(-5)
   real(kind=8), parameter :: x_min = 0.d0, x_max = 1.d0
   real(kind=8) :: x
   integer :: iter = 0

   open(unit=20, file="data_x-y.dat")
   do
      x = x_min + iter*step
      if (x > x_max) exit

      write(20,*) x, fun()

      iter = iter + 1
   end do
   close(20)
contains
   real(kind=8) function fun()
      implicit none
      fun = 1.d0/(1.d0 + x**2)
   end function
end program plot
