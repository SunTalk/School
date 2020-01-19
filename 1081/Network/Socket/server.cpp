#pragma comment(lib, "Ws2_32.lib")

#include <bits/stdc++.h>
#include <WinSock2.h>

#define MAXN 1000
using namespace std;
 
int main(int argc, char* argv[]){

	char message[MAXN];
	//Winsocket-DLL 設定
	WSAData wsaData;
	WORD DLLVSERION;
	DLLVSERION = MAKEWORD(2,1);
	WSAStartup(DLLVSERION, &wsaData);
 
	SOCKADDR_IN addr;
	int addrlen = sizeof(addr);
	addr.sin_addr.s_addr = INADDR_ANY;
	addr.sin_family = AF_INET;
	addr.sin_port = htons(8080);

	//建立 socket
	SOCKET sListen;
	SOCKET sConnect;
	// windows的socket中 AF_INET 跟 PF_INET 是一樣的可以混用
	sConnect = socket(AF_INET, SOCK_STREAM, 0);
	sListen = socket(AF_INET, SOCK_STREAM, 0);
	bind(sListen, (SOCKADDR*)&addr, sizeof(addr));//將addr的資訊綁到socket上
	listen(sListen, 3);

	SOCKADDR_IN clinetAddr;
	while(true)
	{
		cout << "Waiting..." << endl;
		if(sConnect = accept(sListen, (SOCKADDR*)&clinetAddr, &addrlen))
		{
			cout<< "got connect" << inet_ntoa(clinetAddr.sin_addr) << endl;

			//傳送訊息給 client 端
			FILE *fp = fopen("send.txt","r");
			char sendbuf[MAXN],str;
			int len = 0;
			while( ~(str = fgetc(fp)) )
				sendbuf[len++] = str;
			sendbuf[len++] = '\0';
			send(sConnect, sendbuf, (int)strlen(sendbuf), 0);
			
		}

	}
	
	return 0;
	
}