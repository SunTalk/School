@echo off

g++ server.cpp -o server.exe -lws2_32
g++ client.cpp -o client.exe -lws2_32
g++ client_2.cpp -o client_2.exe -lws2_32