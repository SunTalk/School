@echo off

cls
echo COMPILING...

g++ %1\%1.cpp -o %1\%1.exe

if %ERRORLEVEL% EQU 0 (
	echo START
	%1\%1.exe < %1\%1.in > %1\%1.out
)

echo FINISH

