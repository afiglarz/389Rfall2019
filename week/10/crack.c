#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <openssl/rand.h>

#include "crypto.h"
#include "common.h"

#define LEDGER_FILE "ledger.bin"
#define PERMISSIONS (S_IRUSR | S_IWUSR)

// Used similar code from crypto.c
// and how to use the MD5 hash function

int cracker(unsigned char key[]) {
  int a;
  int b;
  int c;

  unsigned char gen_hash[4];
  unsigned char* t;
  unsigned char* final_hash;

  // Bruteforce check of every number combination for 3 bytes
  for (a = 0; a < 256; a++) {
    for (b = 0; b < 256; b++) {
      for (c = 0; c < 256; c++) {

	// Setting values to the generated hash need a nullbyte so that
	// Its treated as a legit string
	gen_hash[0] = a;
	gen_hash[1] = b;
	gen_hash[2] = c;
	gen_hash[3] = '\0';

	// Hashing, first time
	t = md5_hash(gen_hash, 3);

	// Take the first two bytes, zero the rest
	memset(t + 2, 0, 14);

	// Hash again, this time only with the first 
	final_hash = md5_hash(t, 2);

	// Compare if the Hashes are the same
	if (memcmp(final_hash, key, 16) == 0) {
	  printf("%s", gen_hash);
	  return 1;
	  
	}
      }
    }
  }
  return 1;
}


int main(int argc, char **argv) {
  int fd;
  unsigned char first_bytes[16];
  
  // Read from the ledger and grab the first 16 bytes
  // Grabbed this directly from crypto.c
  fd = open(LEDGER_FILE, O_RDONLY, PERMISSIONS);
  read(fd, first_bytes, 16);
  close(fd);

  // Run the crack on those first 16 bytes
  cracker(first_bytes);
  
  return 1;
}
