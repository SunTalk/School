#pragma comment(lib, "Ws2_32.lib")
 
#include <WinSock2.h>
#include <iostream>
 
using namespace std;
 
int main(){

	int r;
	char message[200];
	WSAData wsaData;
	WORD DLLVSERION;
	DLLVSERION = MAKEWORD(2,1);//Winsocket-DLL 版本
 
	//用 WSAStartup 開始 Winsocket-DLL
	r = WSAStartup(DLLVSERION, &wsaData);
 
	//宣告 socket 位址資訊(不同的通訊,有不同的位址資訊,所以會有不同的資料結構存放這些位址資訊)
	SOCKADDR_IN addr;
	int addrlen = sizeof(addr);
 
	//建立 socket
	SOCKET sListen; //listening for an incoming connection
	SOCKET sConnect; //operating if a connection was found
 
	//AF_INET：表示建立的 socket 屬於 internet family
	//SOCK_STREAM：表示建立的 socket 是 connection-oriented socket 
	sConnect = socket(AF_INET, SOCK_STREAM, 0);
 
	//設定位址資訊的資料
	addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	addr.sin_family = AF_INET;
	addr.sin_port = htons(1234);
 
	//設定 Listen
	sListen = socket(AF_INET, SOCK_STREAM, 0);
	bind(sListen, (SOCKADDR*)&addr, sizeof(addr));
	listen(sListen, SOMAXCONN);//SOMAXCONN: listening without any limit
 
	//等待連線
	SOCKADDR_IN clinetAddr;
	while(true)
	{
		cout << "waiting..." << endl;
 
		if(sConnect = accept(sListen, (SOCKADDR*)&clinetAddr, &addrlen))
		{
			cout << "a connection was found" << endl;
			printf("server: got connection from %s\n", inet_ntoa(addr.sin_addr));
 
			//傳送訊息給 client 端
			char sendbuf[] = "Give me a word:";
			send(sConnect, sendbuf, (int)strlen(sendbuf), 0);
			
			ZeroMemory(message, 200);
			r = recv(sConnect, message, sizeof(message), 0);
			cout << message << endl;
			cout << "End Message\n";

		}
		else{
			cout << "Failed\n";
		}
	}
	
	return 0;
	
}