! Example 11: Thermalization of the simulation
! Descrição: Existem diversos critérios para auxiliar na determinação
!de uma simulação de Monte Carlo.
! Vamos olhar aqui para o comportamento da magnetização
!a cada varredura(sweep).

! Criado por: Matheus Roos
! Data: 28/12/2023

module Examp_11mod
   implicit none
   integer, parameter :: db = 8
   integer, parameter :: n = 20
   integer, parameter :: nSpins = n*n
   integer :: seed = 987654321
   integer, parameter :: B = 0      !Campo mag. externo
   integer, parameter :: sweep = 10000  !Varreduras
   real(kind=db), parameter :: delta = 1.d0     !tamanho do passo.
   real(kind=db), parameter :: T = 3.d0         !temperatura
   real(kind=db), parameter :: J = 1            !Termo de troca
   real, parameter :: pi = 4*atan(1.)
contains
   subroutine base(S)
      implicit none
      ! Output variable:
      integer, dimension(n,n), intent(out) :: S !variável de spin
      ! Local variables:
      integer :: Nx, Ny

      S = 1

      do Nx = 1, n
         do Ny = 1, n
            if ( ran(seed) < 0.5 ) S(Nx, Ny) = -1
         end do
      end do
   end subroutine

   subroutine first_step(x, y)
      implicit none
      ! Output variable:
      integer, intent(out) :: x, y

      do
         !Iniamos a caminha num ponto qualquer da rede.
         x = int( n*ran( seed ) )
         y = int( n*ran( seed ) )

         !A coord. nula não está definida.
         if (x > 0 .AND. y > 0) exit
      end do
   end subroutine

   subroutine hamiltonian(ratio)
      implicit none
      ! I/O variables:
      real(kind=db), dimension(-4:4, -1:1), intent(out) :: ratio
      ! Local variables:
      real(kind=db) :: beta
      integer :: i

      beta = 1.d0 / T

      ! A razão 'ratio' neste caso pode assumir apenas os valores:
      !0, +/-2 e +/- 4. Podemos então construir uma matriz que apesar de
      !ter sido definida como 9 x 3, vamos preencher e utilizar apenas 5 linhas,
      !que são os 5 valores possíveis, e 2 colunas, que são o spin central up e o down.
      ! Dessa forma dica fácil acessar o peso probabilístico armazenado, informando
      !dois parâmetros: a soma dos primeiros vizinhos (linha) e o valor atual do
      !spin (coluna).

      ! Fazer esta soma antecipadamente para cada valor de temperatura
      !é de suma importância, pois este �� um grande gargalo na performance
      !nas simulções de Monte Carlo, os cálculos das exponenciais da função peso.
      do i = -4, 4, 2
         ratio(i, -1) = exp(2*beta*(J*i + B))    !Spin down
         ratio(i, +1) = 1.d0 / ratio(i, -1)      !Spin up
      end do
   end subroutine

   integer function Ccontour(index, max)
      implicit none
      integer, intent(in) :: max
      integer, intent(inout) :: index

      if ( index > max ) then
         index = index - max
      end if

      if ( index < 1 ) then
         index = index + max
      end if

      Ccontour = index
   end function

   subroutine sum_neighbors(S, Sx, Sy, NN_sum)
      implicit none
      ! I/O variables:
      integer, intent(in) :: Sx, Sy !Indice horizontal e vertical do sítio visitado
      integer, dimension(n, n), intent(in) :: S
      integer, intent(out) :: NN_sum
      ! Local variables:
      integer :: i, k !indice
      integer :: x, y !indice dos primeiros vizinhos

      NN_sum = 0

      do i = -1, 1, 2
         do k = -1, 1, 2
            x = Sx + i
            y = Sy + k

            !Condições de contorno
            x = Ccontour(x , n)
            y = Ccontour(y , n)

            NN_sum = NN_sum + s(x,y)
         end do
      end do
   end subroutine

   subroutine king_walk(x, y)
      implicit none
      ! I/O variables:
      integer, intent(inout) :: x, y
      ! Local variables:
      real(kind=8) :: r

      r = ran(seed)

      !nint faz a conversão de forma adequada. nint(0.6) = 1
      x = x + int(delta*nint(cos(r*pi)))
      y = y + int(delta*nint(sin(r*pi)))

      !Condições de contorno:
      x = Ccontour(x, n)
      y = Ccontour(y, n)
   end subroutine

   subroutine metropolis(Sx, Sy, S, ratio, accept)
      implicit none
      ! I/O variables:
      real(kind=db), dimension(-4:4,-1:1), intent(in) :: ratio !critério Metropolis
      integer, dimension(n,n) :: S !Variáveis dos n X n spins da rede
      integer :: accept !num. de sucessos
      integer :: Sx, Sy !Indíce horiz. e vert. do spin visitado
      ! Local variables
      integer :: nn_sum !Soma da contribuição dos n primeiros vizinhos

      !Realizamos um passo experimental
      call king_walk(Sx, Sy)

      !Somamos as contribuições dos primeiros vizinhos:
      !nn_sum = Si-1j + Si+1j + Sij-1 + Sij+1
      call sum_neighbors(S, Sx, Sy, NN_sum)

      ! Através da variável nn_sum acessamos o valor da exponencial
      if ( ran(seed) < ratio(nn_sum, S(Sx, Sy)) ) then
         !Flip the spin
         S(Sx, Sy) = -S(Sx, Sy)

         !update accept count
         accept = accept + 1
      end if
   end subroutine
end module Examp_11mod

PROGRAM Examp_11
   use Examp_11mod
   implicit none
   character(len=8), parameter :: path = "./Plots/"
   character(len=20), parameter :: name = "conv_freq-mag-U.dat"
   integer, dimension(n,n) :: S !variável de spin
   integer :: x, y              !posição
   integer :: i                 !indice das varreduras
   real(kind=db), dimension(-4:4, -1:1) :: ratio !razão entre o estado exp. e o antigo
   integer :: accept       !Passos aceitos
   real(kind=db) :: mag, U !thermodynamic quantities
   character(len=4) :: StrT
   !Carrega a config. inicial.
   call base(S)

   !Visitando o primeiro estado
   call first_step(x, y)

   !Definimos a hamiltoniana do modelo e a razão r=w(S')/w(S)
   call hamiltonian(ratio)

   accept = 0

   write(StrT,'(F4.1)') T

   open(unit=20, file=trim(path) // 'T(' // trim(adjustl(StrT)) &
   & // ')' //  trim(name))
   do i = 1, sweep
      call metropolis(x, y, S, ratio, accept)

      call average(S, mag, U)
      write(20,10) i, mag, U
   end do

   close(20)
10 format (I6, 2(F10.5))
END PROGRAM Examp_11

subroutine average(S, mag, U)
   use Examp_11mod
   implicit none
   ! I/O variables:
   integer, dimension(n,n), intent(in) :: S
   !Todas as quantidades por sítio:
   real(kind=db), intent(out) :: mag   !magnetização
   real(kind=db), intent(out) :: U     !energia interna
   ! Local variables:
   integer :: ix, iy, x, y
   integer :: pairs !pares de vizinhos

   pairs = 0
   mag = 0.d0
   U = 0.d0

   !Magnetização de todos os spins da rede
   do ix = 1, n
      x = ix
      do iy = 1, n
         y = iy

         mag = mag + S(ix, iy)

         x = Ccontour(x, n)
         y = Ccontour(y, n)

         pairs = pairs + S(x, y)
      end do
   end do

   !Energia interna por sítio
   U = (J*pairs - B*mag) / nSpins

   !Magnetização por sítio
   mag = mag / nSpins
end subroutine
