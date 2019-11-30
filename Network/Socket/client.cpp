#pragma comment(lib, "Ws2_32.lib")
 
#include <bits/stdc++.h>
#include <WinSock2.h>

#define MAXN 1000
#define IP "127.0.0.1"
using namespace std;

int main(int argc, char* argv[]){	

	freopen("got.txt","w",stdout);
	
	string confirm;
	char message[MAXN];
 
	//Winsocket-DLL 設定
	WSAData wsaData;
	WORD DLLVSERION;
	DLLVSERION = MAKEWORD(2,1);
	WSAStartup(DLLVSERION, &wsaData);

	SOCKADDR_IN addr;
	int addlen = sizeof(addr);
	addr.sin_addr.s_addr = inet_addr(IP);
	addr.sin_family = AF_INET;
	addr.sin_port = htons(8080);
	
	//設定 socket
	SOCKET sConnect;
	sConnect = socket(AF_INET, SOCK_STREAM, 0);
	connect(sConnect, (SOCKADDR*)&addr, sizeof(addr));

	//接收 server 端的訊息
	ZeroMemory(message, MAXN);
	recv(sConnect, message, sizeof(message), 0);
	cout << message << endl;

	//關閉socket
	BOOL bDontLinger = FALSE;
	setsockopt(sConnect,SOL_SOCKET,SO_DONTLINGER,(const char*)&bDontLinger,sizeof(BOOL));
	closesocket(sConnect);
	
	return 0;

}