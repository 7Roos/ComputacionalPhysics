program trig
   implicit none
   real(8), parameter :: pi = 4*atan(1.d0)
   real(8) :: x0, x, step
   integer :: i

   open (unit=20, file='cos.dat')

   x0 = 0
   i = 0
   step = 0.001d0

   do
      x = x0 + i*step
      if (x > pi / 2.d0) exit
      write (20, 10) x, cos(x)
      i = i + 1
   end do

   close (20)

10 format(2(F10.5))
end program trig
