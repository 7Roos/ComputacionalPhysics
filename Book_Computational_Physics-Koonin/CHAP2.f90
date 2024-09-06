! Ordinary Differential Equations
! dy/dx = f(x,y)

module chap2
   implicit none
contains
   real function func(x, y)
      implicit none
      real, intent(in) :: x, y
      func = -x*y                   !dy / dx
   end function

   real function dfx(x, y)
      implicit none
      real, intent(in) :: x, y
      dfx = -y                   !dy / dx
   end function

   real function dfy(x, y)
      implicit none
      real, intent(in) :: x, y
      dfy = -x                   !dy / dx
   end function

   subroutine euler(Y0, Ymax)
      ! Eq. 2.6: método de euler
      ! Yn+1 = Yn + hf(x,y) + O(h**2)
      implicit none
      real, intent(in) :: Y0, Ymax
      integer :: nstep, ix
      real :: h, y, x, diff

      print *, 'Método de Euler'
      do
         print *, 'Enter step size (.LE. 0 to stop)'
         read (*,*) h
         if (h <= 0) exit

         nstep = int(Ymax / h)    !number of steps to rach Ymax
         y = Y0                   !y(0)

         !loop over steps
         do ix = 0, nstep - 1
            x = ix*h                            !last x value
            y = y + h*func(x, y)                !new y value from Eq. 2.6
            diff = exp(-0.5*(x + h)**2) - y    !compare with exact value
            print *, ix, x + h, y, diff
         end do
      end do
   end subroutine

   subroutine taylor(Y0, Ymax)
      ! Eq. 2.6: método de euler
      ! Yn+1 = Yn + hf(x,y) + O(h**2)
      implicit none
      real, intent(in) :: Y0, Ymax
      integer :: nstep, ix
      real :: h, y, x, diff

      print *, 'Método de Taylor'
      do
         print *, 'Enter step size (.LE. 0 to stop)'
         read (*,*) h
         if (h <= 0) exit

         nstep = int(Ymax / h)    !number of steps to rach Ymax
         y = Y0                   !y(0)

         !loop over steps
         do ix = 0, nstep - 1
            x = ix*h                            !last x value
            y = y + h*func(x, y) + 0.5*(dfx(x, y) + func(x,y)*dfy(x, y))*h**2                !new y value from Eq. 2.6
            diff = exp(-0.5*(x + h)**2) - y    !compare with exact value
            print *, ix, x + h, y, diff
         end do
      end do
   end subroutine

end module chap2
