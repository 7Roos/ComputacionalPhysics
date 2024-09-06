! Example 7: Create base spin (table).
! Descrição: A primeira etapa do método de Monte Carlo (MC)
!é gerar as configurações de n spins de forma aleatória  e
!uniformemente distribuída.
! Geramos um número aleatóio r, se r> o.5, então a variável de spin S>0, caso contrário
!S<0. No final criamos um plot dessa tabela.

! Criado por: Matheus Roos
! Data: 25/12/2023

PROGRAM Examp_7
   implicit none
   integer, parameter :: N = 20 !Size lattice
   character(len=8), parameter :: path = './Plots/'
   character(len=10), parameter :: name = 'Base.dat'
   character(len=1) :: visual, source
   integer :: seed = 987654321
   integer :: Nx, Ny !indices horizontal and vertical lattice
   integer, dimension(N,N) :: S = 1 !spin variable
   real :: r !storage random number

   do Nx = 1, N
      do Ny = 1, N
         r = ran(seed)
         if ( r < 0.5 ) S(Nx, Ny) = -1
      end do
   end do

   write(*,*) 'Base gerada. Deseja visualizar?[s/n]'
   read(*,*) visual
   if ( visual == 's' .OR. visual == 'S' ) then
      write(*,*) 'Ver no terminal ou no gráfico?[t/g]'
      read(*,*) source
      if ( source == 't') then
         call print_matrix(N, S)
      else
         call graph()
         write(*,*) 'Salvo como "Base.png"'
      end if
   end if

contains
   subroutine print_matrix(dim, A)
      implicit none
      ! I/O variables:
      integer, intent(in) :: dim
      integer, dimension(dim, dim), intent(in) :: A
      ! Local variables:
      integer :: i,j
      do i = 1, dim
         write(*,10) (A(i,j), j=1, dim)
      end do
10    format (20(I2))
   end subroutine

   subroutine graph()
      implicit none
      integer :: i,j

      call system('mkdir -p ' // trim(path))

      open(unit=20, file=trim(path) // trim(name))

      do i = 1, N
         write(20,11) (S(i,j), j=1, N)
      end do

11    format (20(I3))
      close(20)

      call system('gnuplot -p Templates/Base.gnu')
   end subroutine
END PROGRAM Examp_7


