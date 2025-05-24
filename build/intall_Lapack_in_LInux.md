# Installation of the Lapack library on Linux distributions

<a>
  <img src="build/assets/lapackRobot.jpg" alt="Lapack robot ilustrate" width="400">
</a>

**Author:** M. Roos
**Date:** 28/03/2025
**Youtube:** [7Roos](https://www.youtube.com/@7roos198)

## Index

1.  [Introduction](#intro)
2.  [Installation](#installation)
    * [Ubuntu (Debian)](#ubuntu-debian)
    * [Fedora (RHEL)](#fedora-rhel)
    * [Arch Linux](#arch-linux)
3.  [Check installation](#check-installation)
4.  [Lapack documentation](#lapack-documentation)
5.  [Automated installation](#automated-installation)
6.  [Example Code (Fortran)](#example-code)
7.  [Compilillation and running](#compile-run)

## Introduction <a name="intro"></a>

This tutorial guides you in the installation and use of the Lapack library on various Linux distributions. Lapack is a high-performance linear algebra library, essential for scientific and engineering calculations.

## Installation <a name="installlation"></a>

### Ubuntu (Debian) <a name="ubuntu-debian"></a>
```bash
sudo apt update && sudo apt install -y libblas-dev liblapack-dev
```

### Fedora (RHEL) <a name="fedora-rhel"></a>
```bash
sudo dnf update && sudo yum install -y lapack lapack-devel blas blas-devel
```

### Arch Linux <a name="arch-linux"></a>
```bash
sudo pacman -Syu --noconfirm
sudo pacman -Syu blas lapack
```

## Check installation <a name="check-installation"></a>
```bash
ldconfig -p | grep blas
 ```

## Lapack documentation <a name="lapack-documentation"></a>
- [Official documentation of LAPACK](http://www.netlib.org/lapack/lug/lapack_lug.html)
- [Source code](https://www.netlib.org/lapack/explore-html-3.6.1/d2/d8a/group__double_s_yeigen_ga442c43fca5493590f8f26cf42fed4044.html)

## Automated installation <a name="automated-installation"></a>
- [myLinux](https://github.com/7Roos/myLinux)

## Example code (Fortran) <a name="example-code"></a>
```fortran
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
   call eigen(N, 1.d0*Sz, lambda, v)

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
```

## Pauli matrices
<a>
  <img src="build/assets/sigmaPauli.png" alt="Lapack robot ilustrate" width="400">
</a>

## Compilillation and running <a name="compile-run"></a>
```bash
ifx pauli.f90 -lblas -llapack
```
```bash
./a.out
```