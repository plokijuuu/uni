#include <stdio.h>
#include <string.h>
int my_atoi(const char *number);
int main(void) 
{
	printf("%d",my_atoi("-456- -5.4ola"));
    return 0;
}
int my_atoi(const char *number)
{
	int i=0,sum=0,temp=1;
	int size=strlen(number);
	for(i=size-1;i>=0;i--)
	{
		if(number[i]>='0' && number[i]<='9')
		{
			sum+=((number[i]-'0')*temp);
			temp=temp*10;
		}
		else if(number[i]=='-' && sum!=0)
		{
			if(i==0) sum*=-1;
			else if(number[i-1]==' ')
			{
				if(number[i+1]>='0' && number[i+1]<='9') sum*=-1;
				else
				{
					sum=0;
					temp=1;
				}
			}
			else
			{
				sum=0;
				temp=1;
			}
		}
		else if(number[i]==' ') sum+=0;
		else
		{
			sum=0;
			temp=1;
			
		}
	}
	return sum;
}
