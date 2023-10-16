# Compilador Fortran
FC = ifort

# Opções de compilação
#FLAGS = -O -warn all

# Arquivo fonte: (módulos)
COMMON_SOURCES = SETUP.f90 UTIL.f90 grfdat.f90

# Nome do executável (opcional)
EXECUTABLE = programa.out

# Lista de arquivos objeto
OBJECTS = $(COMMON_SOURCES:.f90=.o) $(SOURCE:.f90=.o)

# Comando para compilar
#compile:
#	$(FC) $(COMMON_SOURCES) $(SOURCE).f90 $(FLAGS) -o $(EXECUTABLE)
# Comando para compilar
compile: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(FC) $^ -o $@

# Regra para criar arquivos objeto
%.o: %.f90
	$(FC) -c $< -o $@

# Comando para limpar (opcional)
clean:
	rm -f $(EXECUTABLE) $(OBJECTS)

# Digite no terminal: make SOURCE=Example_file
