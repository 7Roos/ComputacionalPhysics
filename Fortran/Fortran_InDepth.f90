program Fortran_inDepth
   implicit none
   
   ! Chama a subrotina de boas-vindas
   call welcome_message()
   
   ! Chama novamente para demonstrar reuso
   print *, 'Chamando a subrotina novamente:'
   call welcome_message()

end program Fortran_inDepth

! Subrotina que imprime a mensagem de boas-vindas
subroutine welcome_message()
   implicit none
   
   ! Print a nicely formatted message
   print '(/, 10x, a)', '*************************************'
   print '(10x, a)', '*                                   *'
   print '(10x, a)', '*           Hello World!           *'
   print '(10x, a)', '*                                   *'
   print '(10x, a, /)', '*************************************'
   
   ! Alternative format using write
   write (*, '(/, 10x, a)') '*************************************'
   write (*, '(10x, a)') '*                                   *'
   write (*, '(10x, a)') '*           Hello World!           *'
   write (*, '(10x, a)') '*                                   *'
   write (*, '(10x, a, /)') '*************************************'
   
end subroutine welcome_message
