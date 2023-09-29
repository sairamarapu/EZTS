#include<stdio.h>
struct a{
	char x;
	double y;
	int z;
};
int main(){
	struct a yes;
	yes.z=10;
	yes.y=10;
	printf("%d\n%d\n",yes.z,yes.y);
	printf("%d",sizeof(yes));
	return 0;
}
