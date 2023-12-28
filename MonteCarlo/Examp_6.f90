! Example 6: Random walk 1-D
! Descrição: O segundo passo em simulações de Monte Carlo
!é definir o caminhante aleatório. Que pode dar passinhos da vovó
!passos curtos, como de um em um, ou grandes passos, saltando para
!uma posição aleatória da rede.

! Vamos antes considerar o caso unidimensinal, e ao impor as
!condições periódicas de contorno (o caminhante não pode ir pro infinito)
!definimos o caminho por um círculo fechado por onde nosso caminhante
!andará.

! Criado por: Matheus Roos
! Data: 25/12/2023

PROGRAM Examp_6
   implicit none
   integer, parameter :: db = 8
   integer, parameter :: n = 4
   integer :: seed = 987654321
   real(kind=db) :: r       !random number
   real(kind=db) :: sweep   !sorteio/varredura do próximo passo
   real(kind=db) :: delta   !tamanho do passo.
   integer :: x             !posição
   integer :: step          !próximo passo do caminhante

   delta = 1

   !Iniciamos a caminhada: sorteamos uma fração do espaço disponível 0 < x < n.
   do  
      x = int(N*ran(seed))
      if (x > 0) exit !não pode ser nulo
   end do
   print *, x

   do
      !sorteamos um número 0 < r < 1
      r = ran(seed)
      sweep = (2*r - 1)

      !Normalizamos para o tamanho do passo e pegamos a direção do passo
      step = int(sign(delta, sweep))

      x = x + step

      !Condições periódicas de contorno.
      if ( x >  n ) then
         !passou da borda superior, deve retornar pro início
         x = x - n
      end if
      if (x < 1 ) then
         !passou da borda inferior.
         x = x + n
      end if

      print *, x

      read(*,*)
   end do
END PROGRAM Examp_6
