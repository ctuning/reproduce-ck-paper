#!/bin/sh

rm -rf ./a.out
rm -rf *.o

export CC=${CK_CC}
export CXX=${CK_CXX}
export CFLAGS="${CK_PROG_COMPILER_VARS} ${CK_PROG_COMPILER_FLAGS} -DXOPENME"
export LDFLAGS="${CK_PROG_LINKER_LIBS} ${CK_EXTRA_LIB_M}"
export LIBS="${CK_PROG_LINKER_LIBS} ${CK_EXTRA_LIB_M}"

echo ""
echo "${CC} -c ${CFLAGS} ../filter_codelet.c"
${CC} -c ${CFLAGS} ../filter_codelet.c
${CC} -S ${CFLAGS} ../filter_codelet.c

echo ""
echo "${CC} -O3 -DXOPENME ../filter.c ../ctuning.c filter_codelet.o"
${CC} -O3 -DXOPENME ../filter.c ../ctuning.c filter_codelet.o
