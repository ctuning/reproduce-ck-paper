#ifdef USE_OMP
#include <omp.h>
#endif

#include "filter.h"

void filter_codelet(int *matrix_ptr1, int *matrix_ptr2)
{
  int  i;
  int temp1;
  int v1;

  v1 = *matrix_ptr1++;

#ifdef USE_OMP
#pragma omp parallel for 
#endif
  for (i = 0; i < N * N; i++) {
    temp1 = abs(v1);
    *matrix_ptr2++ = (temp1 > T) ? 255 : 0;
    v1 = *matrix_ptr1++;
  }
}

