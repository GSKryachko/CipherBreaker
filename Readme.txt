This program will try to decrypt text, encrypted with substitution cipher.

Usage:
To decode you will need language model. To build it you will need several txt files
with texts on preferable language. Put them in directory, then run program as follows:

>main.py analyze Texts/ Stats/ language

language should be either EN or RU

Then use

>main.py get_key Texts/ masks Stats/ key lang

Key will be saved in key file.

To decrypt:

>main.py decrypt source destination key lang

Also for testing purposes you can encrypt file using random key as follows:

>main.py encrypt source destination lang

Decrypting method:
We can build mask for every word as follows:
apple -> abbcd
test -> abcd
bonobo -> abcbab
Such mask is invariant to any letter substitution.
On analyzing stage, we save most interesting words (words from one and two letters,
longest words, words with several occurrences of same letter) with their masks.
Using these masks, we can get key if input texts has enough size.