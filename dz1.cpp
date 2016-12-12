#include "stdio.h"
#include "limits.h"

void main() {
	long long int a[200] = { 0 }; //сами числа
	int b[200] = { 0 }; //количество делителей
	for (long long int i = 100; i < 1000000000000000001; i++) {
		
		int j = 0; //обнуляем счетчик делителей
		long long int k = i; //работа над числом в проверке делителей
		
		while (k % 7 == 0) {
			j++;
			k = k / 7;
		}
		while (k % 5 == 0) {
			j++;
			k = k / 5;
		}
		while (k % 3 == 0) {
			j++;
			k = k / 3;
		}
		while (k % 2 == 0) {
			j++;
			k = k / 2;
		}

		if (b[199] < j) {
			for (int n = 199; n > -1; n--) {
				if (b[n] > j) {
					for (int l = 199; l < n+1; l--) {
						b[l] = b[l - 1];
						a[l] = a[l - 1];
					}
					b[n + 1] = j;
					a[n + 1] = i;
					break;
				}
			}
		}
	}; 


	for (int g = 0; g < 200; g++) {
		printf("%llu ", a[g]);
		printf("%d ", b[g]);
		
	}
	


	scanf_s("%s");
}
