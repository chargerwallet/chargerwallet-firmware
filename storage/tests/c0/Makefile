CC=cc
CFLAGS=-Wall -fPIC
LIBS=
OBJ=storage.o norcow.o flash.o
OUT=libtrezor-storage0.com

$(OUT): $(OBJ)
	$(CC) $(CFLAGS) $(LIBS) $(OBJ) -shared -o $(OUT)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OUT) $(OBJ)
