! Examp_13: Ising model 2-D: averages and histere curve
! Descrição: um simples programa que calcula a magnetização média
!e que podemos obter uma curva de histerese ao final.

! Matheus Roos, 05/02/2024

module Examp_13mod
   implicit none
   integer, parameter :: db = 8
   integer, parameter :: L = 30         !Size lattice
   integer, parameter :: nSpins = L*L  !n spins on the lattice
   integer :: seed = 987654321         !Seed random number
   integer, parameter :: B = 0      !Magnetic field
   real(db), parameter :: Jint = 1  !Exchange interaction, j>0 ferro
   integer, parameter :: sweep = 1, group = 2, total = 3
   integer, parameter :: value = 1, square = 2, var = 3
contains
   subroutine base(S)
      !Create and mount the Ising lattice.
      implicit none
      ! Output variables:
      integer, dimension(L, L) :: S
      ! Local variables:
      integer :: ix, iy !index spins

      S = 1

      do ix = 1, L
         do iy = 1, L
            if ( ran(seed) < 0.5 ) S(ix, iy) = -1
         end do
      end do
   end subroutine

   subroutine picture(A)
      !Print matrix/lattice
      implicit none
      ! I/O variables:
      integer, dimension(L, L), intent(in) :: A
      ! Local variables:
      integer :: ix, iy
      character(len=1) :: plus = 'x', minus = ' '
      character(len=1), dimension(0:L+1, 0:L+1) :: A_copy

      !Transform matrix integer to string
      do ix = 0, L+1
         do iy = 0, L+1
            !Botton and top
            if ( ix == 0 .OR. ix == (L+1) ) then
               A_copy(ix, iy) = "-"
               cycle
            end if

            !Side left and right
            if ( iy == 0 .OR. iy == (L+1) ) then
               A_copy(ix,iy) = "|"
               cycle
            end if
            A_copy(ix, iy)  = minus
            if ( A(ix, iy) > 0 ) A_copy(ix, iy)  = plus
         end do
      end do

      !print matrix
      do ix = 0, L+1
         write(*,*) (A_copy(ix, iy), iy = 0, L+1)
      end do
   end subroutine

   subroutine metropolis(S, steps, ratio)
      !Passo metropolis
      implicit none
      ! I/O variables:
      integer, dimension(L, L), intent(inout) :: S    !Matrix spins lattice
      integer, intent(in) :: steps                    !Passos de MC
      real(db), dimension(-4:4, -1:1), intent(in) :: ratio  !Energias do sistema
      ! Local variables:
      integer :: NN_sum, ix, iy, iter

      iter = 0

      do ix = 1, L
         do iy = 1, L
            iter = iter + 1
            if (iter > steps) exit
            !Pegamos a contribuições dos primeiros vizinhos para selecionar a energia correspondente.
            call sum_neighbors(S, ix, iy, NN_sum)

            if ( ran(seed) < ratio(NN_sum, S(ix, iy)) ) then
               !Flip the spin
               S(ix, iy) = -S(ix, iy)
            end if
         end do
      end do
   end subroutine


   subroutine hamiltonian(T, ratio)
      ! Cálculo das exponenciais e^{-beta H}.
      !O caćlulo do peso probabilístico contituiu-se num gargalo de desempnheo em MC,
      !por isso fazemos esse calculo de antemão
      implicit none
      ! I/O variables:
      real(db), intent(in) :: T
      real(db), dimension(-4:4, -1:1), intent(out) :: ratio
      ! Local variables:
      real(db) :: beta
      integer :: I

      beta = 1.d0/T

      !Esta expressão é única para o número de interações consideradas, ou seja,
      !depende da hamiltoniana. Neste caso o spin pode assumir +/- 1, e temos 4 spins interagindo.
      !Então podemos ter os 4 up ou down (+/-4), apenas um antialinhado (+/-2) e metade antilianha (0).
      !Dessa forma, só poderemos ter 5 valores (+/-4, +/-2 e 0) para o spin central +/-1.
      do I = -4, 4, 2
         ratio(i, -1) = exp(beta*(Jint*i - B)) !Spin down(o negatico do spin central rebate o sinal neg.)
         ratio(i, 1) = 1.d0 / ratio(i, -1)      !Spin up
      end do
   end subroutine

   subroutine sum_neighbors(S, ix, iy, NN_sum)
      implicit none
      ! I/O variables:
      integer, dimension(L, L), intent(in) :: S    !spins lattice
      integer, intent(in) :: ix, iy    !Index spins on the lattice
      integer, intent(out) :: NN_sum   !sum interactions spins
      ! Local variables:
      integer, parameter :: neighbors = 4 !num neighbors
      integer, parameter :: coord = 2     !var dimensional
      integer :: i, j, x, y
      integer, dimension(neighbors, coord) :: NN !location s neighbors

      NN_sum = 0

      !!!!!!!!!!!!!!!!!!
      !O spin interage com quatro vizinho. Os elementos estão organizados na vertical
      !(comp. x primeira coluna). Dessa forma, para o spins central S(0,0):
      ! S(-1,0), S(1,0), S(0, -1), S(0, 1).
      !!!!!!!!!!!!!!!!!!

      NN = reshape([ix,ix + 1,ix -1, ix,iy + 1,iy, iy, iy - 1], [4,2])

      !Pegamos o termo à esq. e à dir.:
      do i = 1, neighbors
         !Contour periodic conditions:
         x = Ccontour(NN(i, 1))
         Y = Ccontour(NN(i, 2))

         NN_sum = NN_sum + S(x, y)
      end do
   end subroutine

   integer function Ccontour(index)
      !Aplica as condições periódicas de contorno
      implicit none
      ! I/O variables:
      integer, intent(inout) :: index

      if ( index > L ) then
         index = Index - L
      else if ( index < 1 ) then
         index = Index + L
      end if

      Ccontour = index
   end function

   subroutine sum(S, ratio, sweeps, mag, mag2)
      implicit none
      ! I/O variables:
      integer, dimension(L, L), intent(inout) :: S
      real(8), dimension(-4:4, -1:1), intent(in) :: ratio
      integer, intent(in) :: sweeps
      integer, intent(out) :: mag, mag2
      ! Local variables:
      integer :: ix, iy

      mag = 0
      mag2 = 0

      !Executamos sweeps passos de Monte Carlo
      call metropolis(S, sweeps, ratio)

      !Apartir daí calculamos as médias
      do ix = 1, L
         do iy = 1, L
            mag = mag + S(ix, iy)
            mag2 = mag2 + S(ix, iy)**2
         end do
      end do
   end subroutine

   subroutine average(S, ratio, sweeps, mag, chi, mSigma)
      implicit none
      ! I/O variables:
      integer, dimension(L, L), intent(inout) :: S
      real(8), dimension(-4:4, -1:1), intent(in) :: ratio
      integer, intent(in) :: sweeps
      real(8), dimension(3, 3), intent(inout) :: mag, chi
      real(8) :: mSigma
      ! Local variables:
      integer :: bin, nbins, mag_sum, mag2_sum, iquant

      do iquant = value, var
         mag(group, iquant) = 0
         chi(group, iquant) = 0
      end do

      nbins = 10

      do bin = 1, nbins
         call sum(S, ratio, sweeps, mag_sum, mag2_sum)
         ! Calculate averages
         mag(sweep, value) = mag_sum / nSpins
         mag(sweep, square) = mag2_sum / nSpins

         ! Calculamos a variância
         mag(sweep, var) = mag(sweep, square) - mag(sweep, value)**2
         mag(sweep, var)  = mag(sweep, var)

         !Formamos os nBins (grupos)
         mag(group, value) = mag(group, value) + mag(sweep, value)
         mag(group, square) = mag(group, square) + mag(sweep, square)
         mag(group, var) = mag(group, var) + mag(sweep, var)

         !A suscetibilidade magnética é a própria flutuação da magnetização.
         chi(group, value) = chi(group, value) + mag(sweep, var)

      end do

      !Total é o grupo dividio pelo número de bins (frequency)
      mag(total, value) = mag(group, value) / nBins
      mag(total, square) = mag(group, square) / nBins
      mag(total, var) = (mag(total, square) - mag(total, value)**2) / nbins
      chi(total, value) = chi(group, value) / nBins
   end subroutine

end module Examp_13mod

PROGRAM Examp_13
   use Examp_13mod
   implicit none
   integer, dimension(L, L) :: S
   real(db) :: T
   real(db), dimension(-4:4, -1:1) :: ratio
   integer :: sweeps
   real(8), dimension(3, 3) :: mag, chi
   real(8) :: mSigma

   !Config. inicial
   call base(S)

   write(*,*) 'Quantos passos p/termalizar?'
   read(*,*) sweeps

   write(*,*) 'Config. inicial'
   call picture(S)

   do
      write(*,*) 'Entre com a temperatura'
      read(*,*) T
      if (T == 0) stop "too cool!"

      call hamiltonian(T, ratio)

      !Thermalization
      call metropolis(S, sweeps, ratio)

      write(*,*) 'Config após termalizar'
      call picture(S)

      call average(S, ratio, sweeps, mag, chi, mSigma)
      write(*,*) 'Mag:', mag(total, value), '+/-', sqrt(mag(total, var))
      write(*,*) 'Chi:', chi(total, value)

      call picture(S)
   end do
END PROGRAM Examp_13
