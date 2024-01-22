! Example 10: Metropolis algorithm for Ising 2-D
! Descrição: utilizamos o algoritmo Metropolis para uma rede
!de Ising 2D c/interações de primeiros vizinhos apenas, e podendo
!ter um campo externo H.

! Criado por: Matheus Roos
! Data: 26/12/2023

PROGRAM Examp_10
   implicit none
   integer, parameter :: db = 8
   integer, parameter :: n = 20
   integer :: seed = 987654321
   integer, parameter :: B = 0      !Campo mag. externo
   integer, parameter :: sweep = 10000  !Varreduras
   real(kind=db), parameter :: delta = 1.d0     !tamanho do passo.
   real(kind=db), parameter :: T = 1.d0         !temperatura
   real(kind=db), parameter :: J = 1            !Termo de troca
   integer, dimension(n,n) :: S !variável de spin
   integer :: x, y              !posição
   integer :: i                 !indice das varreduras
   integer :: NN_sum            !soma dos primeiros vizinhos: Si-1,j +...+Sij+1.
   real(kind=db), dimension(-4:4, -1:1) :: ratio !razão entre o estado exp. e o antigo
   integer :: accept   !Passos aceitos

   !Carrega a config. inicial.
   call base(seed, n, S)

   !Visitando o primeiro estado
   call first_step(seed, n, x, y)

   !Definimos a hamiltoniana do modelo e a razão r=w(S')/w(S)
   call hamiltonian(J, B, T, ratio)

   accept = 0

   do i = 1, sweep
      !Realizamos um passo experimental
      call king_walk(seed, n,delta, x, y)

      !Somamos as contribuições dos primeiros vizinhos:
      !nn_sum = Si-1j + Si+1j + Sij-1 + Sij+1
      call sum_neighbors(n, S, x, y, NN_sum)

      !Algoritmo Metropolis
      call metropolis(seed, NN_sum, ratio, S(x,y), accept)
   end do

   call export()
contains
   subroutine export()
      implicit none
      character(len=8), parameter :: path = './Plots/'
      character(len=24), parameter :: name = 'Metropolis_L(20)T(1).dat'
      character(len=1) :: visual, source
      integer :: k, l

      write(*,*) 'Fim do passeio. Deseja visualizar?[s/n]'
      read(*,*) visual
      if ( visual == 's' .OR. visual == 'S' ) then
         write(*,*) 'Ver no terminal ou no gráfico?[t/g]'
         read(*,*) source

         if ( source == 't') then
            do k = 1, n
               write(*,10) (S(k,l), l=1, n)
            end do

         else
            call system('mkdir -p ' // trim(path))

            open(unit=20, file=trim(name))

            do k = 1, N
               write(20,10) (S(k,l), l=1, N)
            end do

            close(20)

            write(*,*) 'Salvo em:' // trim(path) // trim(name)
         end if
      end if

10    format (20(I2))
   end subroutine
END PROGRAM Examp_10

subroutine base(seed, size, S)
   implicit none
   ! I/O variabls:
   integer :: seed
   integer, intent(in) :: size           !semente e dimensão da rede
   integer, dimension(size,size), intent(out) :: S !variável de spin
   ! Local variables:
   integer :: Nx, Ny

   S = 1

   do Nx = 1, size
      do Ny = 1, size
         if ( ran(seed) < 0.5 ) S(Nx, Ny) = -1
      end do
   end do
end subroutine

subroutine first_step(seed, size_lattice, x, y)
   implicit none
   ! I/O variabls:
   integer :: seed
   integer, intent(in) :: size_lattice
   integer, intent(out) :: x, y

   do
      !Iniamos a caminha num ponto qualquer da rede.
      x = int( size_lattice*ran( seed ) )
      y = int( size_lattice*ran( seed ) )

      !A coord. nula não está definida.
      if (x > 0 .AND. y > 0) exit
   end do
end subroutine

subroutine king_walk(seed, N, delta, x, y)
   implicit none
   ! I/O variables:
   integer :: seed
   integer, intent(in) :: n
   real(kind=8), intent(in) :: delta
   integer, intent(inout) :: x, y
   ! Local variables:
   real, parameter :: pi = 4*atan(1.)
   real(kind=8) :: r
   integer, external :: Ccontour

   r = ran(seed)

   !nint faz a conversão de forma adequada. nint(0.6) = 1
   x = x + int(delta*nint(cos(r*pi)))
   y = y + int(delta*nint(sin(r*pi)))

   !Condições de contorno:
   x = Ccontour(x, n)
   y = Ccontour(y, n)
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

subroutine hamiltonian(J, B, T, ratio)
   implicit none
   integer, parameter :: db = 8
   ! I/O variables:
   real(kind=db), intent(in) :: J, T
   integer, intent(in) :: B
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
      ratio(i, -1) = exp(2*beta*(J*i - B))    !Spin down
      ratio(i, +1) = 1.d0 / ratio(i, -1)      !Spin up
   end do
end subroutine

subroutine sum_neighbors(size_lattice, S, Sx, Sy, NN_sum)
   implicit none
   ! I/O variables:
   integer, intent(in) :: size_lattice !Dimensão da rede
   integer, intent(in) :: Sx, Sy !Indice horizontal e vertical do sítio visitado
   integer, dimension(size_lattice, size_lattice), intent(in) :: S
   integer, intent(out) :: NN_sum
   ! Local variables:
   integer :: i, j !indice
   integer :: x, y !indice dos primeiros vizinhos
   integer, external :: Ccontour

   NN_sum = 0

   do i = -1, 1, 2
      do j = -1, 1, 2
         x = Sx + i
         y = Sy + j

         !Condições de contorno
         x = Ccontour(x , size_lattice)
         y = Ccontour(y , size_lattice)

         NN_sum = NN_sum + s(x,y)
      end do
   end do
end subroutine

subroutine metropolis(seed, NN_sum, ratio, spin, accept)
   implicit none
   integer, parameter :: db = 8
   ! I/O variables:
   integer :: seed
   integer, intent(in) :: nn_sum
   real(kind=db), dimension(-4:4,-1:1), intent(in) :: ratio
   integer :: spin
   integer :: accept

   ! Através da variável nn_sum acessamos o valor da exponencial para
   !o spin = S(x,y).
   if ( ran(seed) < ratio(nn_sum, spin) ) then
      !Flip the spin
      spin = -spin

      !update accept count
      accept = accept + 1
   end if
end subroutine
