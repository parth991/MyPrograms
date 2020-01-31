OBJS = Helloworld.o
CC = gcc
CFLAGS = -Wall --save-temps
INCLUDE = 
LIBS = 

.PHONY: all clean

all: hello

hello : $(OBJS)
	$(CC) $(CFLAGS) $(INCLUDES) -o $@ $(OBJS) $(LIBS)

clean:
	-rm -f *.o core *.core *.i *.s hello
    
.c.o:
	$(CC) $(CFLAGS) $(INCLUDES) -c $<  
