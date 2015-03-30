call D:\Work1\CK\ck-repos\ck-auto-tuning\env\compiler-gcc-local-mingw-64\env.bat


echo %CK_CC% %CK_FLAGS_CREATE_OBJ% %CK_COMPILER_FLAGS_OBLIGATORY% %CK_FLAGS_DYNAMIC_BIN% %CK_FLAG_PREFIX_INCLUDE%..\ -O3 -fno-if-conversion ..\filter.c  %CK_FLAGS_OUTPUT%filter.o
%CK_CC% %CK_FLAGS_CREATE_OBJ% %CK_COMPILER_FLAGS_OBLIGATORY% %CK_FLAGS_DYNAMIC_BIN% %CK_FLAG_PREFIX_INCLUDE%..\ -O3 -fno-if-conversion ..\filter.c  %CK_FLAGS_OUTPUT%filter.o
if %errorlevel% neq 0 exit /b %errorlevel%

echo %CK_CC% %CK_FLAGS_CREATE_OBJ% %CK_COMPILER_FLAGS_OBLIGATORY% %CK_FLAGS_DYNAMIC_BIN% %CK_FLAG_PREFIX_INCLUDE%..\ -O3 -fno-if-conversion ..\filter_codelet.c  %CK_FLAGS_OUTPUT%filter_codelet.o
%CK_CC% %CK_FLAGS_CREATE_OBJ% %CK_COMPILER_FLAGS_OBLIGATORY% %CK_FLAGS_DYNAMIC_BIN% %CK_FLAG_PREFIX_INCLUDE%..\ -O3 -fno-if-conversion ..\filter_codelet.c  %CK_FLAGS_OUTPUT%filter_codelet.o
if %errorlevel% neq 0 exit /b %errorlevel%

echo %CK_CC% %CK_COMPILER_FLAGS_OBLIGATORY%  %CK_FLAGS_DYNAMIC_BIN% filter.o filter_codelet.o  %CK_FLAGS_OUTPUT%a.exe %CK_LD_FLAGS_MISC% %CK_LD_FLAGS_EXTRA% %CK_EXTRA_LIB_M%
%CK_CC% %CK_COMPILER_FLAGS_OBLIGATORY%  %CK_FLAGS_DYNAMIC_BIN% filter.o filter_codelet.o  %CK_FLAGS_OUTPUT%a.exe %CK_LD_FLAGS_MISC% %CK_LD_FLAGS_EXTRA% %CK_EXTRA_LIB_M%
if %errorlevel% neq 0 exit /b %errorlevel%
