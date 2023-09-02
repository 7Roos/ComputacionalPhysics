module grfdat_all
    ! Apend. D4, pág. 632
    ! FILE GRAPHIT.HI and GRAPH.LO.
    implicit none
    INTEGER :: NPOINT          !number of points to graph
    INTEGER :: ILINE           !code for line type
    INTEGER :: ISYM            !code for symbol type
    INTEGER :: IFREQ           !symbol frequency
    INTEGER :: NPLOT           !total number of plots on page
    INTEGER :: IPLOT           !number of current plot
    INTEGER :: NXTICK,NYTICK   !number of tick marks
 
    CHARACTER(len=60) :: LABEL(2)    !xaxis and yaxis labels
    CHARACTER(len=60) :: TITLE       !title for graphics page
    CHARACTER(len=60) :: INFO        !informational message
 
    REAL :: XMIN,XMAX !limits on independent variable
    REAL :: YMIN,YMAX !limits on dependent variable
    REAL :: XOVAL     !y value along x axis
    REAL :: YOVAL     !x value along y axis
 contains
    subroutine LNLNAX()
       !draws linear-linear axes
       implicit none
       !Global variables
       real :: xsize, ysize    !size of axes in inches
       ! Local variables:
       real :: xstp, ystp      !length between ticks in user units
       real :: vsize, hsize    !XSIZE and YSIZE
 
       !write title
       IF (IPLOT == 1) CALL BANNER(TITLE)
       !set subplot area
       call SUBPLT(IPLOT, NPLOT, XSIZE, ysize)
       !label axes
       call labels(label)
       ! write informational message
       hsize = xsize
       vsize = ysize
       call legend()
       !draw linear-linear axes
       xstp = (XMAX - XMIN)/NXTICK
       ystp = (YMAX - YMIN)/NYTICK
       !! VAX (Obsolete)
       !call GRAF(XMIN, XSTP, XMAX, YMIN, YSTP, YMAX)
       !!
    end subroutine
 
    subroutine LGLNAX()
       implicit none
       print *, 'preencher'
    end subroutine
 
    subroutine LGLGAX()
       implicit none
       print *, 'preencher'
    end subroutine
 
    subroutine LEGEND()
       !write information at the top left of the plot
       implicit none
       ! Passed variables:
       !real :: xsize, ysize
       ! Local variables:
       integer :: len!, lentru    !length of char string
       !real :: vsize, hsize       !XSIZE and YSIZE
 
       ! Inicialized variables:
       info = ' '
 
       !prints message at top of plotting area
       len = len_trim(info)
       if ( len > 0 ) then
          !! VAX (Obsolete)
          !call messag(info(1:len), len, hsize*.05, vsize*1.03)
          !!
       end if
    end subroutine
 
    subroutine XYPLOT(x, y)
       !plots xy data
       implicit none
       ! Global variables:
       real, dimension(NPOINT) :: x !independent variable data array
       real, dimension(NPOINT) :: y !dependent variable data array
 
       !set line type
       !! VAX (Obsolete)
       !IF (ILINE == 2) CALL DOT
       !IF (ILINE == 3) CALL DASH
       !IF (ILINE == 4) CALL CHNDSH
       !IF (ILINE == 5) IFREQ = -IFREQ   !no line at all
       !!
 
       !set symbol type
       !! VAX (Obsolete)
       !IF (ISYM == 1) CALL MARKER(16)   !circle
       !IF (ISYM == 2) CALL MARKER(2)    !triangle
       !IF (ISYM == 3) CALL MARKER(0)    !square
       !IF (ISYM == 4) CALL MARKER(4)    !cross
       !F (ISYM == 5) THEN              !point
       !   CALL SCLPIC(.3)
       !   CALL MARKER(15)
       !END IF
       !!
 
       !plot
       !! VAX (Obsolete)
       !CALL CURVE(X,Y,NPOINT,IFREQ)
       !!
 
       !reset line type and frequency
       !! VAX (Obsolete)
       !IF (ILINE == 2) CALL RESET('DOT')
       !IF (ILINE == 3) CALL RESET('DASH')
       !IF (ILINE == 4) CALL RESET('CHNDSH')
       !IF (ILINE == 5) IFREQ = -IFREQ
       !!
    end subroutine
 
    subroutine CONTOR()
       implicit none
       print *, 'preencher'
    end subroutine
 
    subroutine GTDEV(device)
       !sets device for graphics output to DEVICE
       !
       ! Global variables:
       use io_all
       implicit none
       ! Passed variables:
       integer :: device !device flag
       integer :: screen !send to terminal
       integer :: paper  !make a hardcopy
       integer :: file   !send to a file
 
       ! Inicialized variables:
       screen = 1; paper = 2; file =3
 
       !reset output device
       !! VAX provable
       !CALL IOMGR(0,-102)
       !!
       !4014 tektronix screen at 9600 baud
 
       !! Subroutines TEKALLDO and PSCRPT obsolete.
       !IF (DEVICE == SCREEN) CALL TEKALLD0(4014,960,0,0,0)
       !postscript Printer with default values
       !IF (DEVICE == PAPER) CALL PSCRPT(0,0,0)
       !!
    end subroutine
 
    subroutine GPAGE(DEVICE)
       !end graphics page
       use io_all ! subroutine clear
       implicit none
       integer :: device !which device is it?
 
       !! VAX (Obsolete)
       !CALL ENDPL(0)
       !!
       CALL CLEAR()
       !! VAX (Obsolete)
       !CALL DONEPL()
       !!
    end subroutine
 
    subroutine BANNER(TITLE)
       !prints title to top of graphics page
       implicit none
       !Global variables:
       character(len=60) :: title    !title to be printed
       ! Functions(replaced by len_trim):
       !integer :: lentru            !returns string length
       ! Local variables:
       integer :: lenttl             !length of title
 
       !treat title as a graph by itself so that it is centered
       !! VAX !!
       !call area2D(7.5, 9.) !'AREA2D' SETS 2D PLOT SIZE;
       !call height(.14)
       !!
       lenttl = len_trim(title)
 
       !! VAX !!
       !call headin(title(1:lenttl), lenttl, 1., 1)
       !call endgr()
       !!
    end subroutine
 
    subroutine LABELS(label)
       ! labels both x and y axes
       implicit none
       !Global variables:
       character(len=60), dimension(2) :: label     !!x and y labels
       ! Functions:(replaced by len_trim)
       !integer :: lentru
       ! Local variables:
       integer :: lenx, leny                        !length of labels
 
       lenx = len_trim(label(1))
       leny = len_trim(label(2))
       !! VAX (Obsolete)
       !call xname(label(1)(1:lenx), lenx)
       !call yname(label(1)(1:leny), leny)
       !!
    end subroutine
 
    subroutine SUBPLT(IPLOT, NPLOT, XSIZE, YSIZE)
       !defines subplotting area
       !The choice of subplot size and placement is dependent on the
       ! device and graphics package; those given here are for an 8.5 X 11
       ! inch page using DISSPLA
       implicit none
       ! Passed variables:
       integer :: NPLOT        !total number of plots on page
       integer :: IPLOT        !number of current plot
       real :: xsize, ysize    !size of plotting area in inches
       ! Local variables:
       real :: xorig, yorig    !location of lower left corner (inches)
 
       !finish last plot (sets DISSPLA back to level 1)
       !! VAX (Obsoleted)
       !IF (IPLOT .NE. 1) CALL ENDGR(0)
       !!
       !define subplotting area (in inches); whole page is 8.5 x 11
       if ( NPLOT == 1 ) then
          xsize = 7.5
          ysize = 9.
          !! Vax (Obsoleted)
          !call height(.14)
          !!
       else if (NPLOT == 2) then
          ysize = 4.25
          xsize = 6.5
          xorig = 1.
          if ( IPLOT == 1 ) yorig = 5.75
          if (IPLOT == 2) yorig = .75
          !! Vax (Obsoleted)
          !call height(.125)
          !!
       else if (NPLOT == 3) then
          ysize = 2.80
          xsize = 6.5
          xorig = 1.
          if ( IPLOT == 1 ) yorig = 7.2
          if (IPLOT == 2 ) yorig = 3.9
          if (IPLOT == 3 ) yorig = .6
          !! Vax (Obsoleted)
          !call height(.11)
          !!
       else if (NPLOT == 4) then
          xsize = 3.25
          ysize = 4.25
          !! Vax (Obsoleted)
          !call height(.11)
          !!
          if ( IPLOT == 1 ) then
             xorig = .5
             yorig = 5.75
          else if (IPLOT == 2 ) then
             xorig = 4.75
             yorig = 5.75
          else if (IPLOT == 3 ) then
             xorig = .5
             yorig = .5
          else if (IPLOT == 4 ) then
             xorig = 4.75
             yorig = .5
          end if
       end if
 
       !use default origin if there is only one plot
       !! Vax (Obsoleted)
       !IF (NPLOT /= 1) CALL PHYSOR(XORIG,YORIG)
       !!
    end subroutine
    ! File GRAPH.LO
 end module grfdat_all