! This a comment line in Fortran, which is 
! ignored by the compiler.
! The exclamation mark is reserved symbol for 
! comments in Fortran.
program arithmeticOperations
   print *, "|| Arithmetic Operations with Integers in Fortran ||"
   print *, " - Addition: 2 + 3 =       ", 2 + 3
   print *, " - Subtraction: 5 - 2 =    ", 5 - 2
   print *, " - Multiplication: 4 * 3 = ", 4 * 3
   print *, " - Division: 10 / 2 =      ", 10 / 2
   print *, " - Exponentiation: 2 ** 3 =", 2 ** 3

   !print *, " | Special cases: |"
   !print *, " This a continuation line in 'Fortran' &
   !& which is used to split long lines."
   !print 10, "Exp negative base: -2 ** 2 =", -2 ** 2
   !print 10, "Exp negative base: (-2) ** 2 =", (-2) ** 2
   !print 11, "Denominator > numerator: 3 / 4 =", 3 / 4, &
   !& ', rest =', mod(3, 4)
   !print 11, "Denominator = numerator: 4 / 4 =", 4 / 4, &
   !& ', rest =', mod(4, 4)
   !print 11, "Denominator < numerator(not multiple): 5 / 4 =", 5 / 4, &
   !& ', rest =', mod(5, 4)
   !print 11, "Denominator < numerator(multiple): 8 / 4 =", 8 / 4, &
   !& ', rest =', mod(8, 4)

   print *, " | Error cases: |"
   !print *, " - Division by zero: 10 / 0 = ", 10 / 0
   !print *, " - Multiplication: 4 * -3 = ", 4 * -3
   print *, " - Undefined variable: 2 + j =", 2 + j
!10 format ('->', A47, I3)
!11 format ('->', A47, I3, A8, I3)
end program arithmeticOperations
