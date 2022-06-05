# RSA-encrypt-logic
##  __1. Asymmetric Key Encryption__ 
&nbsp;&nbsp; Asymmetric encryption involves a mechanism called Public Key and Private Key.  Everyone in the network can access the public key but the private key is anonymous. The user generates a private key using a function.
### &nbsp;&nbsp; _1.1 Logic_
&nbsp;&nbsp; To encrypt a message, one can use the public key.
Send the message over a channel. The private key is then generated on the receiver side.
The private key is used to decrypt the encrypted message.

### &nbsp;&nbsp; _1.2 RSA is asymmetric!_
&nbsp;&nbsp; The Rivest-Shamir-Adleman(RSA) Algorithm is a public-key crypto algorithm based on the principle that prime factorization of a large composite number is tough.  Only the private key of the receiver can decrypt the cipher message. RSA is a key pair generator.

## __2. The RSA algorithm:__

### &nbsp;&nbsp; _2.1 Key-pair generation_ 
&nbsp;&nbsp;  Generate a random private key and public key (the size is 1024-4096 bits).

### &nbsp;&nbsp; _2.2 Encryption_ 
&nbsp;&nbsp; It encrypts a secret message (integer in the range [0…key_length]) using the public key and decrypts it back using the secret key.

### &nbsp;&nbsp; _2.3 Digital signature_
&nbsp;&nbsp; Sign messages (using the private key) and verify message signature (using the public key).

### &nbsp;&nbsp; _2.4 Key exchange_
&nbsp;&nbsp; It securely transports a secret key used for encrypted communication.


## __3. STEPS OF RSA__

    1. Generate two large prime numbers (I chose size of 8 bits for this example) : "p", "q" 

    2. Compute "n" : n = p * q

    3. Compute "totient" : totient = (p-1)*(q-1)

    4. Choose an "e" : 1 < e < totient(n) and (e, totient) are coprimes

    5. Compute "d" :  d * e (mod (totient)) = 1. In this example I expanded the range for "d" by augmenting the number  of iterations to satify the presented equation. Must also be coprimes. 

    6. Define pub_key and pv_key as [n, e] and [d, n] respectively

    7. Create Encryption and Decryption functions:
        coded = msg **(e) mod n
        de_coded = coded **(d) mod n

    8. Visualize

### &nbsp;&nbsp; ___3.1 How to work___
&nbsp;&nbsp; ***_
My rsa object has a _generate_keys()_ method to build the parameters and keys for the RSA algorithm. For encryption is necessary the use of the _cipher()_ method. As for decrypting, make use of _de_cipher()_ method. Note that it's needed a _key__ for the encrypting/dec. methods, this logic is applied because this specification is fundamental for security purposes.
_***





## Generate Large prime numbers

### Logic
> * Random number generation by calling nBitRandom(bitsize) 

> * Basic division test by calling get_lowLevelPrime(prime_candidate)

> * Rabin Miller Test by calling rabin_passed(prime_candidate)
