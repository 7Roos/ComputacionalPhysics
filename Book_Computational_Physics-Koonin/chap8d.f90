program random_distribution
   implicit none
   real :: x 

   do  
    call logdst(x) 

   print *, x
   read(*,*)
   end do
end program random_distribution

subroutine logdst(x)
   implicit none
   real, intent(out) :: x 
   integer :: seed = 98347927

   x = log(1. - ran(seed))
end subroutine
