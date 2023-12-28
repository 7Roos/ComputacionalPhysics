! Examplo 7: Random walk in 2-D lattice
! Descrição: Estendemos nosso caminhante aleatório para uma rede bidimensional com
!configurações aleatória (criada em um exemplo anterior).
! Agora há n formas de definir o caminhante. O mais comum são duas formas:
!-pular para a casa de acima, abaixo, à esq. ou então à direita;
!ou, pular para algum casa qualquer da rede.
! Poderíamos ainda imaginar outras formas mais exóticas, e.g.,
!o movimento "L" do cavalo do jogo de xadeez.
! Por simplicidade, vamos considerar o primeiro caso para testar a
!consistência das condições de contorno impostas.

! Criado por: Matheus Roos
! Data: 26/12/2023

PROGRAM Examp_7
   implicit none
   integer, parameter :: db = 8
   integer, parameter :: n = 4
   integer :: seed = 987654321
   real(kind=db) :: delta       !tamanho do passo.
   integer :: x, y                 !posição
   integer, dimension(n,n) :: S !variável de spin

   !Carrega a config. inicial
   call base(seed, n, S)

   delta = 1

   do
      !Iniamos a caminha num ponto qualquer da rede.
      x = int(n*ran(seed))
      y = int(n*ran(seed))

      !impedindo uma coord. nula
      if (x > 0 .AND. y > 0) exit
   end do

   ! Devemos escolher uma das duas formas para fazer a caminhada:

   !Passo do rei, em todas as direções, por uma casa apenas.
   call king_walk(seed, n, delta, x, y)

   !Pula para um ponto aleatórios da rede.
   call crazy_walk(seed, n, x, y)
END PROGRAM Examp_7

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

   r = ran(seed)

   !nint faz a conversão de forma adequada. nint(0.6) = 1
   x = x + int(delta*nint(cos(r*pi)))
   y = y + int(delta*nint(sin(r*pi)))

   !Condições de contorno:
   if ( x > n ) x = x - n
   if ( x < 1 ) x = x + n
   if ( y > n ) y = y - n
   if ( y < 1 ) y = y + n
end subroutine

subroutine crazy_walk(seed, size_lattice, x, y)
   implicit none
   ! I/O variables:
   integer :: seed
   integer, intent(in) :: size_lattice
   integer, intent(inout) :: x, y

   do
      x = int( size_lattice*ran(seed) )
      y = int( size_lattice*ran(seed) )

      !Coord. nula não está definida.
      if (x > 0 .AND. y > 0) return
   end do
end subroutine
