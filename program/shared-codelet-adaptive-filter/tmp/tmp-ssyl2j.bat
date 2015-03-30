call D:\Work1\CK\ck-repos\fgg-local-win\env\0a8da1441d8b0bbc\env.bat


echo %CK_CC% %CK_FLAGS_CREATE_OBJ% %CK_COMPILER_FLAGS_OBLIGATORY% %CK_FLAGS_DYNAMIC_BIN% %CK_FLAG_PREFIX_INCLUDE%..\  ..\filter.c  %CK_FLAGS_OUTPUT%filter.o
%CK_CC% %CK_FLAGS_CREATE_OBJ% %CK_COMPILER_FLAGS_OBLIGATORY% %CK_FLAGS_DYNAMIC_BIN% %CK_FLAG_PREFIX_INCLUDE%..\  ..\filter.c  %CK_FLAGS_OUTPUT%filter.o
if %errorlevel% neq 0 exit /b %errorlevel%

echo %CK_CC% %CK_FLAGS_CREATE_OBJ% %CK_COMPILER_FLAGS_OBLIGATORY% %CK_FLAGS_DYNAMIC_BIN% %CK_FLAG_PREFIX_INCLUDE%..\  ..\filter_codelet_day.c  %CK_FLAGS_OUTPUT%filter_codelet_day.o
%CK_CC% %CK_FLAGS_CREATE_OBJ% %CK_COMPILER_FLAGS_OBLIGATORY% %CK_FLAGS_DYNAMIC_BIN% %CK_FLAG_PREFIX_INCLUDE%..\  ..\filter_codelet_day.c  %CK_FLAGS_OUTPUT%filter_codelet_day.o
if %errorlevel% neq 0 exit /b %errorlevel%

echo %CK_CC% %CK_FLAGS_CREATE_OBJ% %CK_COMPILER_FLAGS_OBLIGATORY% %CK_FLAGS_DYNAMIC_BIN% %CK_FLAG_PREFIX_INCLUDE%..\  ..\filter_codelet_night.c  %CK_FLAGS_OUTPUT%filter_codelet_night.o
%CK_CC% %CK_FLAGS_CREATE_OBJ% %CK_COMPILER_FLAGS_OBLIGATORY% %CK_FLAGS_DYNAMIC_BIN% %CK_FLAG_PREFIX_INCLUDE%..\  ..\filter_codelet_night.c  %CK_FLAGS_OUTPUT%filter_codelet_night.o
if %errorlevel% neq 0 exit /b %errorlevel%

echo %CK_CC% %CK_COMPILER_FLAGS_OBLIGATORY%  %CK_FLAGS_DYNAMIC_BIN% filter.o filter_codelet_day.o filter_codelet_night.o  %CK_FLAGS_OUTPUT%a.exe %CK_LD_FLAGS_MISC% %CK_LD_FLAGS_EXTRA% %CK_EXTRA_LIB_M%
%CK_CC% %CK_COMPILER_FLAGS_OBLIGATORY%  %CK_FLAGS_DYNAMIC_BIN% filter.o filter_codelet_day.o filter_codelet_night.o  %CK_FLAGS_OUTPUT%a.exe %CK_LD_FLAGS_MISC% %CK_LD_FLAGS_EXTRA% %CK_EXTRA_LIB_M%
if %errorlevel% neq 0 exit /b %errorlevel%
