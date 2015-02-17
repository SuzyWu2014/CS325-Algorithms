CC = gcc
CFLAGS = -Wall -std=c99 -O3 -g -I.
LDFLAGS =
#replace this if you want to change the output name
TARGET = alg1
TARGET2 = alg2
TARGET3 = alg3
TARGET4 = alg4

#any headers go here
INCLUDES =

#any .c or .cpp files go here
SOURCE = alg1.c
SOURCE2 = alg2.c
SOURCE3 = alg3.c
SOURCE4 = alg4.c

#default is to compile
default:	alg1 alg2 alg3 alg4

#depends on all of you source and header files
alg1: ${SOURCE} ${INCLUDES}
#this assumes you actually are linking all of the source files together
	${CC} ${CFLAGS} ${SOURCE} -o ${TARGET} ${LDFLAGS}

#depends on all of you source and header files
alg2: ${SOURCE2} ${INCLUDES}
#this assumes you actually are linking all of the source files together
	${CC} ${CFLAGS} ${SOURCE2} -o ${TARGET2} ${LDFLAGS}

#depends on all of you source and header files
alg3: ${SOURCE3} ${INCLUDES}
#this assumes you actually are linking all of the source files together
	${CC} ${CFLAGS} ${SOURCE3} -o ${TARGET3} ${LDFLAGS}

#depends on all of you source and header files
alg4: ${SOURCE4} ${INCLUDES}
#this assumes you actually are linking all of the source files together
	${CC} ${CFLAGS} ${SOURCE4} -o ${TARGET4} ${LDFLAGS}