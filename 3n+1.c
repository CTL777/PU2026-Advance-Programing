#include <stdio.h>

int main() {
	int num, x;
	scanf("%d", &num);
	while (num >= 1){
	    printf("%d ", num);
	    if (num == 1){
	        break;
	    }
	    x = num % 2;
	    if (x == 0){
	        num = num/2;
	    }
	    else{
	        num = (num*3) + 1;
	    }
	}

}
