! Example 10: Calculate of the averages
! Descrição: magnetization(mag), energy(U),
!susceptibility(xi) and specific heat(chi).

! Criado por: Matheus Roos
! Data: 28/12/2023
module Examp_10mod
   implicit none
   integer, parameter :: db = 8
   real, parameter :: pi = 4*atan(1.)
   character(len=4) :: ext = '.dat'
   character(len=8) :: path = './Plots/'
   integer, parameter :: n = 4
   integer, parameter :: nSpins = n*n
   integer :: seed = 987654321
   integer, parameter :: B = 0      !Campo mag. externo
   real(kind=db), parameter :: delta = 1.d0     !tamanho do passo.
   real(kind=db), parameter :: J = 1            !Termo de troca (J>0 ferro)
   integer, parameter :: ngroup = 10 !n médias que tomaremos outra média
   integer, parameter :: sweep = 1, group = 2, total = 3
   integer, parameter :: value = 1, square = 2, sigsq = 3
   integer, parameter :: freq = 10
contains
   subroutine config_inicial(show, S)
      !Gera a rede de spins com uma onfiguração inicial aleatória.
      implicit none
      ! I/O variables:
      character(len=*), intent(in) :: show
      integer, dimension(n,n), intent(out) :: S !variável de spin
      ! Local variables:
      integer :: Nx, Ny

      S = 1

      do Nx = 1, n
         do Ny = 1, n
            if ( ran(seed) < 0.5 ) S(Nx, Ny) = -1
         end do
      end do

      if (upperCase(show) == 'S') call picture(S)
   end subroutine

   subroutine first_step(x, y)
      !Dá o primeiro passo aleatório na rede.
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

   subroutine hamiltonian(ratio, T)
      ! Calcula as contribuições enérgicas dos n primeiros vizinhos a temperatura T.
      implicit none
      ! I/O variables:
      real(kind=db), dimension(-4:4, -1:1), intent(out) :: ratio
      real(kind=db) :: T
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
      !é de suma importância, pois este é um grande gargalo na performance
      !nas simulções de Monte Carlo, os cálculos das exponenciais da função peso.
      do i = -4, 4, 2
         ratio(i, 1) = exp(-2*beta*(J*i + B))    !Spin up
         ratio(i, -1) = 1.d0 / ratio(i, -1)      !Spin down
      end do
   end subroutine

   integer function Ccontour(index, max)
      !Impõem as condições peródicas de contorno.
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
      !Soma as contribuições nos n primeiros vizinhos.
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
      !Executa uma caminhada aleatória a um sítio de deslocamento.
      implicit none
      ! I/O variables:
      integer, intent(inout) :: x, y
      ! Local variables:
      real(kind=8) :: r

      r = ran(seed)

      !nint faz a conversão de forma adequada. nint(0.6) = 1
      x = x + int(delta*nint(cos(r*2*pi)))
      y = y + int(delta*nint(sin(r*2*pi)))

      !Condições de contorno:
      x = Ccontour(x, n)
      y = Ccontour(y, n)
   end subroutine

   subroutine metropolis(Sx, Sy, S, ratio, accept)
      !Executa 1 passo metropolis.
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

   !Procedure optional
   function upperCase(word)
      !Converte letra minúscula em maiúscula
      implicit none
      character(len=3) :: upperCase
      character(len=*) :: word
      integer :: lenght, i

      lenght = len_trim(word)

      do i = 1, lenght
         if ( iachar(word(i:i)) > 90) then
            word(i:i) = achar(iachar(word(i:i)) - 32)
         end if
      end do

      upperCase = word
   end function


   subroutine picture(A)
      !Exibe a rede de spins no terminal.
      implicit none
      ! Input variable:
      integer, dimension(n,n), intent(in) :: A
      ! Local variables:
      integer :: k, l
      character(len=1), dimension(n,n) :: A_char = ' '

      do k = 1, n
         do l = 1, n
            if ( A(k, l) > 0 ) A_char(k,l) = 'X'
         end do
      end do

      !Header picture
      write(*,*) '--------------------'

      do k = 1, n
         write(*,10) (A_char(k,l), l=1, n)
      end do
10    format('|', 20(A1), '|')

      !Bottom picture
      write(*,*) '--------------------'
   end subroutine

   subroutine thermalization(show, nThermal, S, ratio)
      ! Executa n passos para termalizar o sistema na temperatura T.
      implicit none
      ! I/O variables:
      character(len=*), intent(in) :: show
      integer, intent(in) :: nThermal !Sweeps for thermalization
      integer, dimension(n,n) :: S !spins configuration
      real(kind=db), dimension(-4:4,-1:1), intent(in) :: ratio
      ! Local variables:
      integer :: accept, sucess, iter
      integer :: ix, iy !indices horizontal and vertical
      real :: sucess_ratio !Razão de passos aceitos

      if ( upperCase(show) == 'S' ) then
         open(unit=21, file=trim(path) // 'histo_equilibrium.dat')

         write(21,10)
         write(21,11) seed, n
         write(21,*)
10       format ('# Histograma de termalização')
11       format ('# seed:', I12, ', Size:', I5)
      end if

      call first_step(ix, iy)


      accept = 0; sucess = 0

      do iter = 1, nThermal
         call metropolis(ix, iy, S, ratio, accept)

         !Registrar em alguns intervalos a taxa de sucessos
         if ( upperCase(show) == 'S' .AND. mod(iter,freq) == 0 ) then
            sucess = sucess + accept

            write(21,15) iter, sucess

            sucess_ratio = sucess / 10.

            sucess = - accept

15          format (2(I5))
         end if
      end do


      if ( upperCase(show) == 'S' ) then
         close(21)

         write(*,*)
         write(*,12) trim(path)
         write(*,*)
12       format ('Histograma de equilíbrio em:', / , 3x,  A, 'histo_eq.dat')

         !Plot
         write(*,*)
         call system('gnuplot -p Templates/histrogram.gnu')
         write(*,13)
13       format ('Plot do histograma em:', / , 3x, './histogram.png')
      end if

      write(*,*)
      write(*,*) 'O sistema termalizou!'
      write(*,14) accept/float(nThermal)

14    format ('Taxa de sucesso:', F5.2, / )
   end subroutine

   subroutine groups(S, MC_steps, ngroups, ratio, mag)
      !Executa 10*n passos de Monte Carlo Metropolis p/calcular 10 médias indepenientes.
      implicit none
      ! I/O variables:
      integer, dimension(n,n) :: S
      integer, intent(in) :: MC_steps !Passsos MC para obter uma média
      integer, intent(in) :: nGroups !quantidade de bins(grupos formando n médias distintas).
      real(kind=db), dimension(-4:4, -1:1), intent(in) :: ratio
      real(kind=db), dimension(3,3), intent(out) :: mag
      ! Local variables:
      integer :: iter, iGroups, accept = 0
      integer :: ix, iy !index horizontal and vertical

      call first_step(ix, iy)

      mag(group, value) = 0.d0
      mag(group, square) = 0.d0

      do iGroups = 1, nGroups
         do iter = 1, MC_steps
            call metropolis(ix, iy, S, ratio, accept)
         end do
         ! Calcula a média percorrendo toda a rede, formando i grupos a cada iteração
         call sums(S, mag)
      end do
   end subroutine

   subroutine sums(S, mag)
      implicit none
      ! I/O variables
      real(kind=db), dimension(3,3), intent(out) :: mag
      integer, dimension(n, n), intent(in) :: S
      ! Local variables:
      integer :: ix, iy !index horizontal and vertical

      mag(sweep, value) = 0.d0
      do ix = 1, n
         do iy = 1, n
            mag(sweep, value) = mag(sweep, value) + S(ix, iy)
         end do
      end do

      !Calculamos o quadrado
      mag(sweep, square) = mag(sweep, value) ** 2

      !Agrupamos os resultados
      mag(group, value) = mag(group, value) + mag(sweep, value)
      mag(group, square) = mag(group, square) + mag(sweep, square)
   end subroutine

   subroutine averag(mag, ngroups, m, m_sig1, m_sig2)
      implicit none
      ! I/O variables:
      real(kind=db), dimension(3,3) :: mag
      integer, intent(in) :: ngroups
      real(kind=db), intent(out) :: m, m_sig1, m_sig2 !magnetização por sítio
      ! Local variables:
      integer :: iquant
      real(kind=db), dimension(3,3) :: chi

      do iquant = value, square
         mag(total, iquant) = 0
      end do

      !Normalizamos pelo número de spins.
      do iquant = value, square
         mag(group, iquant) = mag(group, iquant) / nSpins
      end do

      ! N*Delta mag = <m**2> - <m>**2 = N*\chi
      chi(group, value) = mag(group, square) - mag(group, value) ** 2

      mag(group, sigsq) = chi(group, value) / nSpins

      !Calculamos a média final da magnetização
      do iquant = value, sigsq
         mag(total, iquant) = mag(total, iquant) + mag(group, iquant)
      end do

      !Média por spin
      m = mag(total, value) / ngroups
      !flutuação no valor da magnetização
      m_sig1 = ( ( mag(total, square)/ngroups )  - m**2 ) / (ngroups*nSpins)
      m_sig1 = sqrt(m_sig1)
      !flutuação da flutuação
      m_sig2 = sqrt(mag(total, sigsq)) / ngroups
   end subroutine
end module Examp_10mod
PROGRAM Examp_10
   use Examp_10mod
   implicit none
   real(kind=db) :: Tmin, Tmax, Tstep, T
   integer :: iTemp
   integer :: nThermal, MC_steps, ngroups !n_step p/: termalizar, sweep, bins
   integer, dimension(n,n) :: S !Spins configurations
   character(len=1), dimension(2) :: show
   integer :: ix, iy !indixes spins configurations
   real(kind=db), dimension(-4:4, -1:1) :: ratio !Critério Metropolis
   real(kind=db), dimension(3,3) :: mag
   real(kind=db) :: m, m_sig1, m_sig2 !magnetização e flutuação por spin
   !test
   integer :: k, l, iter, accept
   real(kind=db) :: m_group
   m = 0.d0
   m_group = 0.d0

   call setup()

   !config. inicial
   call config_inicial(show(1), S)


   iTemp = 0
   varT: do
      T = Tmin + Tstep*iTemp
      if (T > Tmin) exit

      write(*,10) 'Temp:', T

      !Valores da hamiltoniana pra essa temperatura
      call hamiltonian(ratio, T)


      !Passos MC pra atingir o equilíbrio
      call thermalization(show(2), nThermal, S, ratio)


      !Caĺculo das médias.
      do k = 1, ngroups
         call first_step(ix, iy)
         do iter = 1, MC_steps
            call metropolis(ix, iy, S, ratio, accept)
         end do

         m = 0.d0
         iter = 0
         do ix = 1, n
            do iy = 1, n
               m = m + S(ix, iy)
            end do
         end do
         m_group = m_group + m
      end do

      print *, 'sistema termalizado:'

      print *, 'group:', m_group/dfloat(ngroups*nSpins)

      !write(*,*) 'Calcular as médias .... [Enter]'
      !read(*,*)

      !Criamos os grupos de médias (bins)
      !call groups(S, MC_steps, ngroups, ratio, mag)

      !Calculamos as médias
      !call averag(mag, ngroups, m, m_sig1, m_sig2)

      !write(20,11) T, m, m_sig1, m_sig2

      iTemp = iTemp + 1
   end do varT

   close(20)
   write(*,*) 'The end!'
10 FORMAT ( / , A, F5.2)
11 format (4(F10.5))
contains
   subroutine setup()
      implicit none
      character(len=20), parameter :: name = 'histerese_'
      character(len=10), parameter :: cols = 'T-m-mSig'

      !Criamos a pasta caso não exita
      call system('mkdir -p ' // trim(path))

      open(unit=20, file=trim(path) // trim(name) &
      & // trim(cols) // ext)

      write(*,10)
      write(20,10)
10    format('Monte Carlo simulation of the d=2 Ising model')

      write(20,11) seed
11    format('seed:', I10)

      write(20,12) n
12    format('Lattice(dim):', I3)

      write(20,13) J
13    format('J:', F4.1)

      write(*,*) 'Defina Tmin, Tmax, Tstep:'
      read(*,*) Tmin, Tmax, Tstep

      !write(*,*) 'Sweeps to thermal? [1000]'
      !read(*,*) nThermal

      nThermal = 100
      MC_steps = 100
      ngroups = 10

      write(20,14) nThermal
14    format('nThermal:', I5)

      !write(*,*) 'Visualizar config. inicial? [s/n]'
      !read(*,*) show(1)
      show(1) = 'N'

      write(*,*) 'Visualizar termalização? [s/n]'
      read(*,*) show(2)
   end subroutine
END PROGRAM Examp_10
