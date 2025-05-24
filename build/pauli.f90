!! Pauli matrices
!! M. Roos, 28/03/2025

program pauli
   implicit none
   !! Inputs
   integer, parameter :: N = 2
   integer, dimension(N, N) :: I, Sx, Sz
   !! Outputs
   real(8), dimension(N) :: lambda
   real(8), dimension(N, N) :: v

   ! Identidade.
   I = reshape([1, 0, 0, 1], [2, 2])

   ! Sigma x.
   Sx = reshape([0, 1, 1, 0], [2, 2])

   ! Sigma z.
   Sz = reshape([1, 0, 0, -1], [2, 2])

   ! Return eigenvalues and eigenvector
   call eigen(N, 1.d0*Sx, lambda, v)

   write(*,*) 'eigenvalues are:', lambda
   write(*,*) 'eigenvectors are:', v
end program pauli

!! Calculation of eigenvalues via LAPACK library
subroutine eigen(dim, A, eigenvalues, eigenvectors)
   implicit none
   integer, parameter :: db = kind(1.d0)
   integer, intent(in) :: dim
   real(KIND=db), dimension(dim, dim), intent(in) :: A
   real(KIND=db), dimension(dim), intent(out) :: eigenvalues
   real(KIND=db), dimension(dim, dim), intent(out) :: eigenvectors
   !!!! Standard Dsyev subroutine !!!!!
   character(len=1) :: JOBZ, UPLO
   integer :: N, LDA, INFO, lwork
   integer, parameter :: LWMAX = 1000
   real(KIND=db), dimension(dim) :: W
   real(kind=db), dimension(LWMAX) :: WORK
   real(KIND=db), dimension(dim, dim) :: P

   P = A

   JOBZ = 'V'; UPLO = 'U'
   N = dim; LDA = dim; lwork = -1

   call dsyev(JOBZ, UPLO, N, P, LDA, W, WORK, LWORK, INFO)

   LWORK = MIN(LWMAX, INT(WORK(1)))

   !Solve eigenproblem.
   call dsyev(JOBZ, UPLO, N, P, LDA, W, WORK, LWORK, INFO)

   !Check for convergence.
   if (info > 0) then
      write (*, *) 'The algorithm failed to find the eigenvalues'
      stop
   end if

   eigenvalues = w
   eigenvectors = P
end subroutine
