! Examp_12: Statistic
! Descrição: Sendo as simulações de Monte Carlo um processo
!estocástico, para obtermos os resultados das simulaçãoes devemos
!realizar um trabalho estatístico. Esta tarefa possui muitos detalhes importantes
!e para evitar um desenolvimento demorado do próximo passo que é
!calcular quantidades termodinâmicas como a magnetização e a energia interna.

! Matheus Roos, 27/02/2024

PROGRAM Examp_12
   implicit none
   !Parameters:
   integer, parameter :: L = 4
   integer, parameter :: n = L*L
   integer, parameter :: sweep = 1, group = 2, sigSq = 3
   integer, parameter :: value = 1, square = 2, total = 3
   !Arrays:
   integer, dimension(L, L) :: S
   !Variables:
   integer :: i,j, bin, nBins, iquant
   real, dimension(3,3) :: mag, chi

   s = reshape([-1, -1, 1, 1, 1, 1 ,1 ,1, -1, 1, 1, 1, -1, -1, 1, -1], [4,4])

   nBins = 4

   do iquant = value, sigSq
    mag(group, iquant) = 0
    chi(group, iquant) = 0
   end do

   do bin = 1, nBins
    do iquant = value, square
        mag(sweep, iquant) = 0
    end do

      do i = 1, L
         do j = 1, L
            mag(sweep, value) = mag(sweep, value) + S(i,j)
            mag(sweep, square) = mag(sweep, square) + S(i,j)**2
         end do
      end do

      !mag de uma varredura
      mag(sweep, value) = mag(sweep, value) / n
      mag(sweep, square) = mag(sweep, square) / n

      !calculamos a flutuação
      mag(sweep, sigSq) = mag(sweep, square) - mag(sweep, value)**2

      !Formamos os nBins grupos
      mag(group, value) = mag(group, value) + mag(sweep, value)
      mag(group, square) = mag(group, square) + mag(sweep, square)
      mag(group, sigSq) = mag(group, sigSq) + mag(sweep, sigSq)

      !A suscetibilidade magnética é a própria flutuação da magnetização.
      chi(group, value) = chi(group, value) + mag(sweep, sigSq)

      write(*,*) 'mag, mag**2, deltaMag:', mag(sweep, value), mag(sweep, square), sqrt(mag(sweep, sigSq))

      S(bin,bin) = - S(bin,bin) !Apenas damos uma flutuação totalmente fictícia
   end do

   !Total é o grupo dividio pelo número de bins (frequency)
   mag(total, value) = mag(group, value) / nBins
   mag(total, square) = mag(group, square) / nBins
   mag(total, sigSq) = mag(group, sigSq) / nBins
   chi(total, value) = chi(group, value) / nBins

   write(*,*) 'final'
   write(*,*) 'mag, mag**2, deltaMag:', mag(total, value), mag(total, square), sqrt(mag(total, sigSq))
   write(*,*) 'Sigma2:', sqrt(mag(total, square) - mag(total, value)**2)
   write(*,*) 'chi:', chi(group, value)
END PROGRAM Examp_12
