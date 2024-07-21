#TREES_DB = "trees_db_ghidra_flt"
#TREES_DB = "trees_db_ghidra_viz"
#TREES_DB = "trees_db_test"

TREES_DB = "trees_db_ghidra_arch_flt"
#TREES_DB = "trees_db_ghidra_arch_viz"
CODE_GRAPH_COLLECTION = "code_graph"
MONGO_CLIENT = "mongodb://localhost:27017/"


code_path = "/Spring_2024/Project_Files/ghidra_scripts/"
src_path = "/Spring_2024/Project_Files/ghidra_scripts/src/"
binary_path = "/Spring_2024/Project_Files/ghidra_scripts/obj/"
trs_src_path = "/Spring_2024/Project_Files/ghidra_scripts/trs_src/"
trs_binary_path = "/Spring_2024/Project_Files/ghidra_scripts/trs_obj/"

musl_inc = (
                f"-std=c99 -nostdinc -ffreestanding -fexcess-precision=standard -frounding-math -D_XOPEN_SOURCE=700 "
                f"-I/Spring_2024/musl-1.2.2/arch/x86_64 " # powerpc " #aarch64 " # 
                f"-I/Spring_2024/musl-1.2.2/arch/generic "
                f"-I/Spring_2024/musl-1.2.2/obj/src/internal "
                f"-I/Spring_2024/musl-1.2.2/src/include "
                f"-I/Spring_2024/musl-1.2.2/src/internal "
                f"-I/Spring_2024/musl-1.2.2/obj/include "
                f"-I/Spring_2024/musl-1.2.2/include "
                f"-I/Spring_2024/musl-1.2.2/src/malloc/mallocng "
                f"-I/Spring_2024/musl-1.2.2/src/process "
                f"-I/Spring_2024/musl-1.2.2/src/dirent "
                f"-I/Spring_2024/musl-1.2.2/src/crypt "
                f"-I/Spring_2024/musl-1.2.2/src/math "
                f"-I/Spring_2024/musl-1.2.2/src/ctype "
                f"-I/Spring_2024/musl-1.2.2/src/errno "
                f"-I/Spring_2024/musl-1.2.2/src/ipc "
                f"-I/Spring_2024/musl-1.2.2/src/locale "
                f"-I/Spring_2024/musl-1.2.2/src/multibyte "
                f"-I/Spring_2024/musl-1.2.2/src/network "
                f"-I/Spring_2024/musl-1.2.2/src/passwd "
                f"-I/Spring_2024/musl-1.2.2/src/prng "
                f"-I/Spring_2024/musl-1.2.2/src/regex "
                f"-I/Spring_2024/musl-1.2.2/src/search "
                f"-I/Spring_2024/musl-1.2.2/src/stdio "
                f"-D__uint128_t=int "
           )

openssl_inc = (
			f"-I/Spring_2024/openssl-master/include "
			f"-I/Spring_2024/openssl-master/ssl "
			f"-I/Spring_2024/openssl-master/crypto "
			f"-I/Spring_2024/openssl-master/crypto/aes "
			f"-I/Spring_2024/openssl-master/crypto/ocsp "
			f"-I/Spring_2024/openssl-master/crypto/rsa "
			f"-I/Spring_2024/openssl-master/crypto/asn1 "
			f"-I/Spring_2024/openssl-master/crypto/async "
			f"-I/Spring_2024/openssl-master/crypto/bio "
			f"-I/Spring_2024/openssl-master/crypto/rc5 "
			f"-I/Spring_2024/openssl-master/crypto/des "
			f"-I/Spring_2024/openssl-master/crypto/hmac "
			f"-I/Spring_2024/openssl-master/crypto/sha "
			f"-I/Spring_2024/openssl-master/crypto/property "
			f"-I/Spring_2024/openssl-master/crypto/encode_decode "
			f"-I/Spring_2024/openssl-master/crypto/objects "
			f"-I/Spring_2024/openssl-master/crypto/bn "
			f"-I/Spring_2024/openssl-master/crypto/dh "
			f"-I/Spring_2024/openssl-master/providers/implementations/ciphers "
			f"-I/Spring_2024/openssl-master/providers/implementations/include "
			f"-I/Spring_2024/openssl-master/providers/common/include "
			f"-I/Spring_2024/openssl-master/crypto/x509 "
			f"-I/Spring_2024/openssl-master/crypto/pkcs7 "
			f"-I/Spring_2024/openssl-master/crypto/bf "
			f"-I/Spring_2024/openssl-master/crypto/camellia "
			f"-I/Spring_2024/openssl-master/crypto/cast "
			f"-I/Spring_2024/openssl-master/crypto/cmp "
			f"-I/Spring_2024/openssl-master/crypto/cms "
			f"-I/Spring_2024/openssl-master/crypto/comp "
			f"-I/Spring_2024/openssl-master/crypto/conf "
			f"-I/Spring_2024/openssl-master/crypto/crmf "
			f"-I/Spring_2024/openssl-master/crypto/ct "
			f"-I/Spring_2024/openssl-master/crypto/dsa "
			f"-I/Spring_2024/openssl-master/crypto/dso "
			f"-I/Spring_2024/openssl-master/crypto/ec "
			f"-I/Spring_2024/openssl-master/crypto/evp "
			f"-I/Spring_2024/openssl-master/crypto/engine "
			f"-I/Spring_2024/openssl-master/crypto/err "
			f"-I/Spring_2024/openssl-master/crypto/idea "
			f"-I/Spring_2024/openssl-master/crypto/lhash "
			f"-I/Spring_2024/openssl-master/crypto/md4 "
			f"-I/Spring_2024/openssl-master/crypto/md5 "
			f"-I/Spring_2024/openssl-master/crypto/objects "
			f"-I/Spring_2024/openssl-master/crypto/pem "
			f"-I/Spring_2024/openssl-master/crypto/pkcs7 "
			f"-I/Spring_2024/openssl-master/crypto/pkcs12 "
			f"-I/Spring_2024/openssl-master/crypto/property "
			f"-I/Spring_2024/openssl-master/crypto/rand "
			f"-I/Spring_2024/openssl-master/crypto/rc2 "
			f"-I/Spring_2024/openssl-master/crypto/rc4 "
			f"-I/Spring_2024/openssl-master/crypto/ripemd "
			f"-I/Spring_2024/openssl-master/crypto/seed "
			f"-I/Spring_2024/openssl-master/crypto/sm3 "
			f"-I/Spring_2024/openssl-master/crypto/store "
			f"-I/Spring_2024/openssl-master/crypto/ts "
			f"-I/Spring_2024/openssl-master/crypto/ui "
			f"-I/Spring_2024/openssl-master/crypto/whrlpool "
			f"-I/Spring_2024/openssl-master/crypto/x509 "
			f"-I/Spring_2024/openssl-master/ssl/quic "
			f"-I/Spring_2024/openssl-master/ssl/record "
			f"-I/Spring_2024/openssl-master/ssl/statem "
			f"-D_Atomic=\"\" "
              )

transformation_cmd = "--Transform=Flatten" #"--Transform=Virtualize" #

# Platform information

architecture     = "arm" #"riscv64" #"mips" #"powerpc" #"aarch64" #"x86_64" #"i386" #"mips64" # #
library          = "openssl" #"musl" #  #
compiler         = "gcc"
compiler_version = "11.4.0"
cpu              = "13th Gen Intel(R) Core(TM) i9-13900HX"
os_type          = "Linux ubuntu"
os_version       = "22.04.3 LTS"
transformation   = "Flatten" #"Virtualize" #
compiler_flags   = "-c"

