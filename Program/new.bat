@echo off

mkdir %1

type template > %1\%1.cpp
echo.> %1\%1.in
echo.> %1\%1.out
echo %1 Created
