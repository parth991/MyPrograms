.PHONY = all clean

CC = gcc
CFLAGS = -Wall
INCLUDE = 
LIBS = 
OBJS = main.o
OBJS += Functions.o

all: factorial

factorial: $(OBJS)
	$(CC) $(CFLAGS) $(INCLUDES) -o $@ $(OBJS) $(LIBS)
	
clean:
	-rm -f *.o core *.core *.i *.s factorial
    
.c.o:
	$(CC) $(CFLAGS) $(INCLUDES) -c $<  
