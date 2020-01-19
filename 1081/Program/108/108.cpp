#include <bits/stdc++.h>

using namespace std;

#define USE_CPPIO() ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 100
#define INF 0x3f3f3f3f
#define DEVIATION 0.00000005

int main(int argc, char const *argv[])
{

	int matrix[MAXN+5][MAXN+5];
	int num;

	while( ~scanf("%d",&num) ){

		memset(matrix, 0, sizeof(matrix));
		for(int i = 1 ; i <= num ; i++ ){
			for(int j = 1 ; j <= num ; j++ ){
				scanf("%d",&matrix[i][j]);
				matrix[i][j] += (matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1]);
			}
		}

		int ans = INT_MIN;
		for(int i = 0 ; i <= num ; i++ )
			for(int j = 0 ; j <= num ; j++ )
				for(int m = i+1 ; m <= num ; m++ )
					for(int n = j+1 ; n <= num ; n++ )
						ans = max(ans,(matrix[m][n]-matrix[m][j]-matrix[i][n]+matrix[i][j]));
	
		printf("%d\n",ans);
		
	}


	return 0;
}